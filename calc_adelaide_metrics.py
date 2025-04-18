#!/usr/bin/env python3
""" Write metrics from fundamental matrix calculations

See main `README.md` for the source of the Adelaide RMF data.
"""

from pathlib import Path

import numpy as np
import scipy.io as sio
import pandas as pd

from skimage.transform import FundamentalMatrixTransform
from skimage.transform._geometric import _append_homogeneous_dim as _as_h

# pip install opencv-python-headless
import cv2


class FMTMRS(FundamentalMatrixTransform):
    """ Version of FundamentalMatrixTransform using MRS scaling

    MRS scaling corresponds to original Hartley algorithm.
    """

    scaling = 'mrs'


class CV28Point:
    """ Simulate skimage transform using OpenCV

    OpenCV 8-point algorithm (Hartley).
    """

    algorithm = cv2.FM_8POINT

    def __init__(self):
        self.params = np.eye(3)

    def estimate(self, src, dst):
        self.params, _ = cv2.findFundamentalMat(src, dst, self.algorithm)
        return True


class CV2LMedS(CV28Point):
    """ OpenCV LMedS algorithm
    """

    algorithm = cv2.FM_LMEDS


transforms = dict(rms=FundamentalMatrixTransform(),
                  mrs=FMTMRS(),
                  cv28=CV28Point(),
                  cvLMS=CV2LMedS())


def calc_distances(src, dst, F, metric='distance'):
    """ Distances between calculated epipolar lines and points

    Parameters
    ----------
    src : array shape (N, D)
        Points in first image.
    dst : array shape (N, D)
        Matching points in second image.
    F : array shape (3, 3)
        Fundamental matrix mapping `src` to epipolar lines in `dst`.
    metric : {'distance', 'epip-distances'}, optional
        Matrix for distance between actual points `dst` and epipolar lines
        generated from `F`.  'distance' is signed distance from [1]_.
        'epip-distances' is the squared sum of distances of points from epipolar
        lines in both images.  See [2]_, section 7.1.4.

    Notes
    -----
    See [Wikipedia on point-line
    distance](https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line#A_vector_projection_proof)
    for standard distance formula, and various proofs.

    References
    ----------
    .. [1] Zhang, Zhengyou. "Determining the epipolar geometry and its
           uncertainty: A review." International journal of computer vision 27
           (1998): 161-195.
    .. [2] Hartley, Richard I. "In defense of the eight-point algorithm."
           Pattern Analysis and Machine Intelligence, IEEE Transactions on 19.6
           (1997): 580-593.
    """
    src_h, dst_h = _as_h(src), _as_h(dst)
    Fu = F @ src_h.T
    uFu = np.sum(dst_h.T * Fu, axis=0)
    if metric == 'distance':
        # See Zhang, p163, and Notes above.
        return uFu / np.sqrt(np.sum(Fu[:-1]**2, axis=0))
    if metric == 'epip-distances':
        # Hartley, p 585, section 7.1.4
        Fu_dash = F.T @ dst_h.T
        scaler = (1 / np.sum(Fu[:-1]**2, axis=0) +
                  1 / np.sum(Fu_dash[:-1]**2, axis=0))
        return (uFu ** 2) * scaler
    raise ValueError(f'Invalid metric "{metric}"')


def get_good_points(pth):
    """ Fetch non-outlier points from AdelaideRMF dataset

    Parameters
    ----------
    pth : Path
        of AdelaideRMF ``.mat`` file.

    Returns
    -------
    points : array shape N, 4
        Corresponding points, first two columns are points in image 1, last two
        columns are corresponding points in image 2.
    """
    mf = sio.loadmat(pth)
    data = mf['data']
    assert np.all(data[[2, 5]] == 1)  # homogeneous coordinate.
    points = data[[0, 1, 3, 4]].T
    # 0 indicates a "gross outlier".
    return points[np.squeeze(mf['label']) != 0]


# Not-outlier point correspondence from Adelaide RMF datasets.
datasets = {}
for data_pth in Path('AdelaideRMF').glob('*/*.mat'):
    datasets[data_pth.stem] = get_good_points(data_pth)

pts2sd = lambda pts : np.split(pts, 2, axis=1)


def calc_mad_rmsd(src, dst, F):
    return (np.mean(np.abs(calc_distances(src, dst, F, 'distance'))),
            np.sqrt(np.mean(calc_distances(src, dst, F, 'epip-distances'))))

# Standard MRS and RMS calculations.
rows = []
for name, pts in datasets.items():
    row = {'dataset': name}
    src, dst = pts2sd(pts)
    for tn, tf in transforms.items():
        assert tf.estimate(src, dst)
        row[f'{tn}-mad'], row[f'{tn}-rmsd'] = calc_mad_rmsd(src,
                                                            dst,
                                                            tf.params)
    rows.append(row)

# Reorder columns.
col_names = ['dataset']
for metric_name in 'mad', 'rmsd':
    for tn in transforms:
        col_names.append(f'{tn}-{metric_name}')

df = pd.DataFrame(rows)[col_names].sort_values('dataset')
df.to_csv('adelaide_rmf_metrics.csv', index=None)


# Train test calculations.
rng = np.random.default_rng()
rows = []
for name, pts in datasets.items():
    row = {'dataset': name}
    n = len(pts)
    n2 = n // 2
    tt = rng.permuted(np.repeat(['train', 'test'], [n2, n - n2]))
    train_s, train_d = pts2sd(pts[tt == 'train'])
    test_s, test_d = pts2sd(pts[tt == 'test'])
    for tn, tf in transforms.items():
        assert tf.estimate(train_s, train_d)
        row[f'{tn}-mad'], row[f'{tn}-rmsd'] = calc_mad_rmsd(test_s,
                                                            test_d,
                                                            tf.params)
    rows.append(row)

df = pd.DataFrame(rows)[col_names].sort_values('dataset')
df.to_csv('adelaide_rmf_tt_metrics.csv', index=None)
