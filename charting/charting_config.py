"""Config file for Article 1"""
from pathlib import Path

# Set this to True to load the legacy working corpus instead of running step 1 from scratch, in order to ensure full reproducibility of the published results
# See readme for details
LEGACY_MODE = False


# Data path settings
# If everythin is located in the same base directory, paths can me set relative to a common BASE_DATA_PATH to keep things neat
# BASE_DATA_PATH = Path()
CORPUS_PATH = Path()
DOCMODELS_PATH = Path()
RESULTS_PATH = ''

