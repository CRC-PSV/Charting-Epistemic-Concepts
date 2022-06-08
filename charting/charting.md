Charting
========


The 3 scripts correspond to the 3 main steps described in the methods section of the article, as presented in the diagram below. 

![diagram](charting_diagram.jpg)

To generate the results, first open the config file (`charting_config.py`) and follow the instruction to update the required values.
The scripts can then be run in order, execution details will be printed in a terminal window.

#### Note on reproducibility

Some minor corrections were made to the text extraction process late in the project (we found out some non-text content -mostly urls- had skimmed though).
This had no effect on the results, but did have a slight impact on the text length of some of the documents. 
After the correction, a handful of documents (a few dozens) ended up being slightly (most by 10 words or less) below the 150 words abstract / 2000 words text threshold.

The code used to compute the docterm matrix was refactored before publishing.
This had no impact on the values themselves, but changed the order of the rows and columns within the resulting docterm matrix.
In order to get the same output from the LDA topic modeling, a manual reordering based on the original disposition is required.

If the value of `LEGACY` in `charting_config.py` is set to `True` (it is by default), these changes will be taken into account in order to reproduce exact results found in the publication.
If set to `False`, everything will be run from scratch, so the results will differ slightly (the overall picture and conclusions remain the same)
