# Some of the steps have been grouped or reordered compared to the diagram to speed up the process

import sys
import os

from lib.utils.io_utils import read_y_n_input, load_json
from charting.charting_config import LEGACY_MODE, DOCMODELS_PATH, CORPUS_PATH, RESULTS_PATH, LEGACY_IDS_PATH, LEGACY_DOCTERM_LABELS
from lib.preprocess.extraction import extract_and_tag_docmodel_texts, create_docmodels_from_xml_corpus
from lib.utils.generators import generate_all_docmodels, generate_ids_abs_tags
from lib.nlp_params import TT_NVA_TAGS, SPECIAL_CHARACTERS_BASE
from lib.models.tagcounts import TagCountsModel
from lib.models.docterm import DocTermModel


CONFIG_NAME = 'charting_config.py'

# TODO
# All done!?


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
        legacy_ids = load_json(LEGACY_IDS_PATH)
        filter_fct = lambda x: x.id in legacy_ids
    else:
        print('NOT using legacy mode, DocModels will be filtered based on the 150/2000 abstract and text words')
        filter_fct = lambda x: x.abs_words >= 150 and x.text_words >= 2000
    print('Warning: Filtered DocModels will be deleted!')
    print('Filtering docmodels...')
    files_to_delete = []
    for dm in generate_all_docmodels(DOCMODELS_PATH):
        if not filter_fct(dm):
            files_to_delete.append(dm.filename)
    print('Deleting filtered docmodels...')
    for f in files_to_delete:
        os.remove(DOCMODELS_PATH / f)
    print('Done building working corpus')
    print(f'Deleted {len(files_to_delete)} docmodels, {len(os.listdir(DOCMODELS_PATH))} were kept')


def step_1_docterm(legacy: bool):

    if legacy:
        # Load legacy vocab to reproduce results
        labels = load_json(LEGACY_DOCTERM_LABELS)
        vocab = labels['columns']
        dt = DocTermModel(update_filter_fct=lambda x: x.pos in TT_NVA_TAGS)
        for doc_id, tags in generate_ids_abs_tags(DOCMODELS_PATH):
            dt.update(doc_id, tags)

    else:
        tc = TagCountsModel(update_filter_fct=lambda x: x.pos in TT_NVA_TAGS)
        dt = DocTermModel(update_filter_fct=lambda x: x.pos in TT_NVA_TAGS)

        for doc_id, tags in generate_ids_abs_tags(DOCMODELS_PATH):
            tc.update(tags)
            dt.update(doc_id, tags)

        # Make word list
        tc.filter_values(lambda x: (len(x) >= 3) and (not any(char in SPECIAL_CHARACTERS_BASE for char in x)))
        tc_df = tc.as_df()  # cols: total_counts article_counts
        tc_df = tc_df[(tc_df['article_counts'] <= 0.3*len(tc_df)) & (tc_df['article_counts'] >= 50)]  # TODO check filters

        # Make vocab
        vocab = tc_df.index

        # Save TagCountsModel for future reference
        tc.to_pickle(RESULTS_PATH / 'abstracts_tagcounts_model.p')


    # Filter DocTermModel to only keep vocab words before building the dataframe
    dt.filter_words(lambda x: x in vocab)

    # Save DocTermModel for future reference
    dt.to_pickle(RESULTS_PATH / 'abstracts_docterm_model.p')

    # Build, normalize and save docterm matrix. If legacy, reorder labels to match original configuration
    dt_df = dt.as_df(log_norm=True)
    if legacy:
        dt_df = dt_df.reindex(index=labels['index'], columns=labels['columns'])

    dt_df.to_pickle(RESULTS_PATH / 'abstracts_docterm_df.p')


def step_1_main():
    step_1_setup()
    step_1_extraction()
    step_1_filtering(LEGACY_MODE)
    print('Done extracting the data and building the working corpus.')

    print('Building the docterm matrix from the abstracts')
    step_1_docterm(LEGACY_MODE)
    print('Docterm matrix built and saved to results folder. Step 1 complete!')


if __name__ == '__main__':
    print(load_json(LEGACY_IDS_PATH)[:5])
    print(load_json(LEGACY_DOCTERM_LABELS)['index'][:5])
    print(load_json(LEGACY_DOCTERM_LABELS)['columns'][:5])
    # step_1_main()

