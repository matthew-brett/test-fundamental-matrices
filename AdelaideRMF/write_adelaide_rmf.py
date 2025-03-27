#!/usr/bin/env python3
""" Write non-outlier corresponding points from Adelaide RMF datasets

The datasets appear to be based at
`https://www.ai4space.group/research/adelaidermf`_ - but the links there are
broken (I've emailed the first contact listed on that page).

In the meantime, I found what appear to be the data files at `data/AdelaideRMF` in
`https://github.com/trungtpham/RCMSA`_.

In the page above, the format of the files is given as::

    Each Matlab .mat file contains:

        img1 - left image

        img2 - right image

        data - keypoint correspondences (x1,y1,1,x2,y2,1) where (x1,y1) in img1
               and (x2,y2) in img2

        score - SIFT correspondences matching score

        label - 0 indicates gross outliers and others (e.g., 1, 2, ...)
                indicate the structure membership

Accordingly this script goes through each dataset, loads the `.mat` file,
fetches the `data` variable, strips out the columns of all 1, and drops rows
where `label == 0`, then saves the results out into an `npz` file.

::
    git clone https://github.com/trungtpham/RCMSA
    cd data/AdelaideRMF
    python write_adelaide_rmf.py
"""

from pathlib import Path

import numpy as np
import scipy.io as sio


def process_fn(fn):
    mf = sio.loadmat(fn)
    data = mf['data']
    assert np.all(data[[2, 5]] == 1)  # homegeneous coordinate.
    points = data[[0, 1, 3, 4]].T
    # 0 indicates a "gross outlier".
    return points[np.squeeze(mf['label']) != 0]


mats = {}
for dir in ('H', 'F'):
    for fn in Path(dir).glob('*.mat'):
        var = process_fn(fn)
        mats[fn.stem] = var


np.savez('adelaide_rmf.npz', **mats)
