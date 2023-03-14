from pathlib import Path


# Test block, TODO remove
TEST_MODE = False

if TEST_MODE:
    LEGACY_MODE = False
    CORPUS_PATH = Path('D:/charting_test/testcorpus')
    DOCMODELS_PATH = Path('D:/charting_test/docmodels')
    RESULTS_PATH = Path('D:/charting_test/results')

else:
    LEGACY_MODE = True
    CORPUS_PATH = Path('D:/articles')
    DOCMODELS_PATH = Path('D:/charting/docmodels')
    RESULTS_PATH = Path('D:/charting/results')


# Project path settings

# If everythin is located in the same base directory, paths can me set relative to a common BASE_DATA_PATH to keep things neat
# BASE_DATA_PATH = Path()
# Raw corpus (bmc xml files) directory. Should contain corpus files ONLY to avoid problem.
#CORPUS_PATH = Path('D:/articles')
# DocModels will be saved in / loaded from DOCMODELS_PATH. Directory should initially be empty and contain ONLY dataframes to avoid problems.
#DOCMODELS_PATH = Path('D:/charting/docmodels')
# Various results (mostly pickled dataframes and json files) will be saved to / loaded from RESULTS_PATH
#RESULTS_PATH = Path('D:/charting/results')

# General project paths, should be left as is
CHARTING_PATH = Path(__file__).parent
DATA_PATH = CHARTING_PATH / 'data'
LEXICON_PATH = DATA_PATH / 'lexicon.csv'

# Set this to True to load the legacy working corpus instead of running step 1 from scratch, in order to ensure full reproducibility of the published results
# If using legacy mode, document ids and docterm labels lists should be accessible as json files (these files are ignored if legacy mode is disabled)
# See readme for details
#LEGACY_MODE = True
LEGACY_IDS_PATH = DATA_PATH / 'legacy/legacy_ids.json'
LEGACY_DOCTERM_LABELS = DATA_PATH / 'legacy/legacy_docterm_labels.json'


# Other settings

# Number of topics for LDA topic model
N_TOPICS = 7
# Random seed (set to 2112 to reproduce the original results)
RND_SEED = 2112
# List of words on which to compute cooccurrence references
# Set to None to compute on the whole lexicon (data might be quite heavy and should probably be split up)
COOC_REFS_TERMS = ['model', 'mechanism', 'prediction', 'understanding', 'explanation', 'theory']
