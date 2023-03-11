from charting.charting_config import LEXICON_PATH, DOCMODELS_PATH, RESULTS_PATH, LEGACY_MODE, RND_SEED, LEGACY_IDS_PATH, LEGACY_DOCTERM_LABELS, N_TOPICS
from lib.models.lda import LdaModel
from lib.models.coocs import CoocsModel
from lib.utils.generators import generate_ids_tags
from sklearn.cluster import MiniBatchKMeans
import pandas as pd
from lib.nlp_params import TT_NVA_TAGS


def step_3_lda_clusters():
    # Load docterm
    dt_df = RESULTS_PATH / 'abstracts_docterm_df.p'

    # create LdaModel: params
    lda_model = LdaModel(
        'lda_model',
        dt_df,
        n_components=80,
        doc_topic_prior=0.2,  # alpha
        topic_word_prior=0.02,  # beta
        max_iter=100,
        learning_decay=0.9,
        random_state=RND_SEED,
        learning_method='batch',
    )

    lda_model.fit()
    lda_model.to_pickle(RESULTS_PATH / 'lda/lda_model.p')

    doc_topics_df = lda_model.get_doc_topics_df()
    topic_words_df = lda_model.get_topic_words_df()

    doc_topics_df.to_pickle(RESULTS_PATH / 'lda/doc_topics_df.p')
    topic_words_df.to_pickle(RESULTS_PATH / 'lda/topic_words_df.p')

    #csv = lda.get_word_weights_csv()
    #with open(LDA_PATH / 'topic_word_probs.csv', 'wb') as f:
    #   f.write(csv.encode('utf-8'))

    # Cluster
    k = MiniBatchKMeans(n_clusters=7, random_state=RND_SEED).fit(doc_topics_df)
    clusters = k.predict(doc_topics_df)

    doc_cluster_series = pd.Series(index=doc_topics_df.index, data=clusters)
    doc_cluster_series = doc_cluster_series.map(lambda x: f'cluster_{x}')
    doc_cluster_series.to_pickle(RESULTS_PATH / 'doc_cluster_series.p')


def calc_cluster_coocs(cluster_name, doc_ids, lexicon):

    cm = CoocsModel(lexicon, window=5, tag_attr='lemma')

    for para_id, tags in generate_ids_tags(DOCMODELS_PATH, 'get_text_tags', flatten=False,
                                           dms_filter_fct=lambda x: x.id in doc_ids,
                                           tags_filter_fct=lambda x: x.pos in TT_NVA_TAGS,):
        cm.update(para_id, tags)

    cm.to_pickle(RESULTS_PATH / f'cooc_models/cooc_model_{cluster_name}.p')
    cm_df = cm.as_df()
    cm_df.to_pickle(RESULTS_PATH / f'cooc_dfs/cooc_df_{cluster_name}.p')


def step_3_cluster_coocs():

    # load vocab
    lexicon = load_json(LEXICON_PATH)
    cluster_series = pd.read_pickle(RESULTS_PATH / 'doc_cluster_series.p')
    clusters = cluster_series.unique()

    for cluster in clusters:
        calc_cluster_coocs(cluster, list(cluster_series[cluster_series == cluster].index), lexicon)

    print('Done!')


def step_3_main():
    step_3_lda_clusters()
    step_3_cluster_coocs()


if __name__ == '__main__':
    step_3_main()


