Charting
========


The 3 scripts correspond to the 3 main steps described in the methods section of the article, as presented in the diagram below. 

![diagram](charting_diagram.jpg)

To generate the results, first open the config file (`charting_config.py`) and follow the instruction to update the required values.
The scripts can then be run in order, execution details will be printed in a terminal window.

#### Notes on reproducibility

Some minor corrections were made to the text extraction process late in the project (we found out some non-text content -mostly urls- had skimmed though).
After the correction, a handful of documents (a few dozens) ended up being slightly (most by 10 words or less) below the 150 words abstract / 2000 words text threshold.

The code used to compute the docterm matrix was refactored before publishing.
This had no impact on the values themselves, but reordered the rows and columns of the matrix.

In order to reproduce the exact same output from the LDA topic modeling, a manual reordering based on the original configuration is required.

If the value of `LEGACY` in `charting_config.py` is set to `True` (it is by default), these changes will be taken into account in order to reproduce exact results found in the publication.
If set to `False`, everything will be run from scratch, so the LDA results might differ slightly , although the overall picture and conclusions should not be affected.
