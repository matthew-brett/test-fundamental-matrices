# Test fundamental matrix calculations

The home of the Adelaide RMF datasets is
<https://www.ai4space.group/research/adelaidermf> — but the links there are
broken (I've emailed the first contact listed on that page).

In the meantime, I found what appear to be the data files at `data/AdelaideRMF` in
<https://github.com/trungtpham/RCMSA>.  Commit `0d5f3e3` of that repository is
the source of the `AdelaideRMF` directory here.

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
