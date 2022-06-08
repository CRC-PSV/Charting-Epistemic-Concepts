Charting
========


The 3 scripts correspond to the 3 main steps described in the methods section of the article. 
1. a
2. b
3. c

To generate the results, first open the config file (`charting_config.py`) and follow the instruction to update the required values.
The scripts can then be run in order, execution details will be printed in a terminal window.

#### Note on reproducibility

Some minor corrections were made to the text extraction late in the project when we found out some non-text content had skimmed though (mostly urls).
This does not affect the results, but affects the text length of some of the documents. 
After the correction, a handful of documents (a few dozens) thus end up being slightly (most by 10 words or less) below the 150 words abstract / 2000 words text threshold.

The code used to compute the docterm matrix was refactored before
This had no impact on the values themselves, but did change the order of the rows and columns within the docterm matrix.
Since this difference impacts the results of the topic modeling, a manual reordering based on the original disposition is required to obtain the same results.

If the value of `LEGACY` in `charting_config.py` is set to `True` (it is by default), these changes will be taken into account in order to reproduce exact results found in the publication.
If set to `False`, everything will be run from scratch, so the results will differ slightly (the overall picture and conclusions remain the same)
