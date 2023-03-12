from lib.docmodel import DocModel
from lib.utils.generators import generate_all_docmodels
from lib.utils.io_utils import save_json
from charting.charting_config import DOCMODELS_PATH, DATA_PATH, CORPUS_PATH, CHARTING_PATH, RESULTS_PATH

import pathlib, shutil, random
import pandas as pd

def export_doc_refs_json(save_path):
    """Saves corpus metadata as a json file. See DocModel.__repr__ for details"""

    docs = {}
    for dm in generate_all_docmodels(DOCMODELS_PATH):
        docs[dm.id] = repr(dm)

    save_json(save_path, docs)


def make_sub_corpus(dest_path, target_path, n_docs):

    files = [f for f in dest_path.iterdir()]
    for f in random.sample(files, n_docs):
        shutil.copy(f, target_path / f.name)


def print_docterm():
    print(pd.read_pickle(RESULTS_PATH / 'abstracts_docterm_df.p'))


if __name__ == '__main__':
    # export_doc_refs_json(DATA_PATH / 'corpus_metadata.json')
    # make_sub_corpus(CORPUS_PATH, pathlib.Path('D:/charting/testcorpus'), 5000)
    print_docterm()
