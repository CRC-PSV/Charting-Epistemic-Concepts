# Some of the steps have been grouped or reordered compared to the diagram to speed up the process

from lib.utils.input_utils import read_y_n_input
import sys

from .charting_config import LEGACY_MODE, DOCMODELS_PATH, CORPUS_PATH
from lib.preprocess.extraction import extract_and_tag_docmodel_texts, create_docmodels_from_xml_corpus

CONFIG_NAME = 'charting_config.py'


def step_1_setup():
    """Prints step info and promps y/n to continue or exit"""

    print('Starting extraction and preprocessing (step 1)')
    print(f'Make sure file paths and other project settings in {CONFIG_NAME} are set correctly before proceeding.')
    print(f'') # confirm paths and check if empty
    if LEGACY_MODE:
        print(f'LEGACY_MODE is currently set to {LEGACY_MODE}, document filtering and docterm matrix will rely on loaded data. See dearme for details')
    else:
        print(f'LEGACY_MODE is currently set to {LEGACY_MODE}, document filtering and docterm matrix will be computed from scratch. See readme for details')

    if not read_y_n_input('Continue? (y/n): '):
        print('Cancelling...')
        sys.exit()


def step_1_extraction():
    print('Starting extraction step.')
    print('This will create and pickle DocModel objects from the source XML files.')
    create_docmodels_from_xml_corpus(CORPUS_PATH, DOCMODELS_PATH)


# TTagging
# loop over DMs, run TT
def step_1_tagging():
    print('Starting tagging step')
    print('This will read the previously created DocModels, extract the textual contents and generate tags')
    extract_and_tag_docmodel_texts(DOCMODELS_PATH)


# 150/2k Filtering
# If legacy, use list, else use len
def step_1_filtering(legacy: bool):
    print('Starting filtering step')
    if legacy:
        print('Using legacy mode, DocModels will be filtered using loaded data')
        legacy_ids = []  # TODO
        filter_fct = lambda x: x.id in legacy_ids
    else:
        print('NOT using legacy mode, DocModels will be filtered based on the 150/2000 abstract and text words')
        filter_fct = lambda x: x.abs_words >= 150 and x.text_words >= 2000
    print('Warning: Filtered DocModels will be deleted!')
    # TODO
    # Cycle and delete those filtered out


def step_1_docterm(legacy: bool):
    # Load matrix if legacy
    # Else make model and all
    pass


def step_1_main():
    step_1_setup()
    step_1_extraction()
    step_1_filtering(LEGACY_MODE)
    print('Done building the corpus done. Next step will be forming the docterm matrix from abstracts')

    step_1_docterm(LEGACY_MODE)
    print('Docterm matrix built and saved to results folder. Step 1 complete!')


if __name__ == '__main__':
    step_1_main()


