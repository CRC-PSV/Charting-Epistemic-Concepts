
def step_3_lda_clusters():
    # Load docterm
    # create LdaModel: params
    # save dfs
    # Cluster
    # Save results
    pass


def calc_cluster_coocs(cluster, vocab):
    # init a CoocModel: vocab, window
    # generator: filter doc on cluster, words on NVA
    # update
    # save df
    pass


def step_3_cluster_coocs():
    # load vocab
    # for each cluster, calc_cluster_coocs(cluster, vocab)

    pass


def step_3_main():
    step_3_lda_clusters()
    step_3_cluster_coocs()


if __name__ == '__main__':
    step_3_main()


