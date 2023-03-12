"""Config file for Article 1"""
from pathlib import Path

# Random seed (set to 2112 to reproduce the original results)
RND_SEED = 2112


# Project path settings
CHARTING_PATH = Path(__file__).parent
DATA_PATH = CHARTING_PATH / 'data'
LEXICON_PATH = DATA_PATH / 'lexicon.csv'


# If everythin is located in the same base directory, paths can me set relative to a common BASE_DATA_PATH to keep things neat
# BASE_DATA_PATH = Path()
#CORPUS_PATH = Path('D:/articles')
CORPUS_PATH = Path('D:/charting/testcorpus')
DOCMODELS_PATH = Path('D:/charting/docmodels')
RESULTS_PATH = Path('D:/charting/results')


# Set this to True to load the legacy working corpus instead of running step 1 from scratch, in order to ensure full reproducibility of the published results
# See readme for details
LEGACY_MODE = False
LEGACY_IDS_PATH = DATA_PATH / 'legacy/legacy_ids.json'
LEGACY_DOCTERM_LABELS = DATA_PATH / 'legacy/legacy_docterm_labels.json'


# Other settings
RANDOM_SEED = 2112
N_TOPICS = 7