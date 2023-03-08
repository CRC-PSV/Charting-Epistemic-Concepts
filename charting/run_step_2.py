""""""

from lib.utils.io_utils import read_y_n_input, load_json
from charting.charting_config import LEXICON_PATH, DOCMODELS_PATH, RESULTS_PATH, LEGACY_MODE, RND_SEED
from lib.nlp_params import TT_NVA_TAGS
from lib.utils.generators import generate_ids_text_tags_filtered
from lib.models.coocs import CoocsModel


# TODO
# Samples


def step_2_main():
    """Runs step 2. Pretty straight forward since everything is handled by the CoocsModel"""

    # Load lexicon, init and update CoocsModel
    lexicon = load_json(LEXICON_PATH)
    cm = CoocsModel(lexicon, window=5, tag_attr='lemma')
    for para_id, tags in generate_ids_text_tags_filtered(DOCMODELS_PATH, filter_fct=lambda x: x.pos in TT_NVA_TAGS, flatten=False):
        cm.update(para_id, tags)

    # Save model, export and save df
    cm.shuffle_refs(rnd_seed=RND_SEED)
    cm.to_pickle(RESULTS_PATH / 'cooc_models/coocs_model_corpus.p')
    cm_df = cm.as_df()
    cm_df.to_pickle(RESULTS_PATH / 'cooc_dfs/coocs_corpus_df.p')

    # Shuffle, select and save samples
    if LEGACY_MODE:
        pass
    else:
        pass


if __name__ == '__main__':
    step_2_main()

