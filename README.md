# Test fundamental matrix calculations

The home of the Adelaide RMF datasets is
<https://www.ai4space.group/research/adelaidermf> — but the links there are
broken. The first contact listed on that page — Hoi Sim Wong - kindly emailed
me a Dropbox link to the data.  The data almost completely corresponds to
another copy I found at `data/AdelaideRMF` in
<https://github.com/trungtpham/RCMSA>, commit `0d5f3e3`, but the copies here
are the copies fro the Dropbox link from the main author.

In the home page above above, the format of the files is given as:

> Each Matlab .mat file contains:
>
> * img1 - left image
> * img2 - right image
> * data - keypoint correspondences (x1,y1,1,x2,y2,1) where (x1,y1) in img1
>          and (x2,y2) in img2
> * score - SIFT correspondences matching score
> * label - 0 indicates gross outliers and others (e.g., 1, 2, ...)
>         indicate the structure membership

For citation of these datasets, see the main page above.  In particular:

> If you use this dataset in a publication, please cite:
>
>     Hoi Sim Wong, Tat-Jun Chin, Jin Yu and David Suter, Dynamic and
>     Hierarchical Multi-Structure Geometric Model Fitting, International
>     Conference on Computer Vision (ICCV), Barcelona, Spain, 2011.
>
> ```bibtex
> @inproceedings{wong11,
>   author = {Hoi Sim Wong and Tat-Jun Chin and Jin Yu and David Suter},
>   booktitle = {International Conference on Computer Vision (ICCV)},
>   title = {Dynamic and hierarchical multi-structure geometric model fitting},
>   year = {2011}
> }
> ```

To run the version of scikit-image that I am using:

```
git clone https://github.com/matthew-brett/scikit-image
# Currently commit 8cd967682
git co refactor-fundamental
```

and then follow the [instructions to install a development
version](https://scikit-image.org/docs/stable/gitwash/index.html).
