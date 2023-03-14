from pathlib import Path
import pandas as pd
from sys import exit

from charting.charting_config import RESULTS_PATH, COOC_REFS_TERMS, DOCMODELS_PATH, LEGACY_DOCTERM_LABELS
from lib.nlp_params import SPECIAL_CHARACTERS_BASE
from lib.docmodel import DocModel
from lib.utils.io_utils import load_json

# labels = load_json(LEGACY_DOCTERM_LABELS)
# print(labels['columns'][1290])

# DocTerm test

old_dt_df = pd.read_pickle(Path('C:/Users/Sanchez/Desktop/m4data/old_docterm_df.p')).astype('float32')
new_dt_df = pd.read_pickle(RESULTS_PATH / 'abstracts_docterm_df.p').astype('float32')

new_dt_df.fillna(0, inplace=True)

print('checking index for mismatch...')
for i in range(len(old_dt_df.index)):
    if old_dt_df.index[i] != new_dt_df.index[i]:
        print(f'{i} - {old_dt_df.index[i]} - {new_dt_df.index[i]}')

print('\nchecking columns for mismatch')
for i in range(len(old_dt_df.columns)):
    if old_dt_df.columns[i] != new_dt_df.columns[i]:
        print(f'{i} - {old_dt_df.columns[i]} - {new_dt_df.columns[i]}')

print(old_dt_df.iloc[:,1290].nlargest(30))
print(new_dt_df.iloc[:,1290].nlargest(30))


print(old_dt_df.isnull().values.any())
print(new_dt_df.isnull().values.any())


print(old_dt_df['mechanism'].nlargest(5))
print(new_dt_df['mechanism'].nlargest(5))

print(old_dt_df.index[:10])
print(new_dt_df.index[:10])

print(old_dt_df.columns[:10])
print(new_dt_df.columns[:10])

print(old_dt_df)
print(new_dt_df)

print(f'\nDfs are equal: {new_dt_df.equals(old_dt_df)}\n')

# print(old_dt_df.iloc[1,1] == new_dt_df.iloc[1,1])

pairs = [(0, 16), (1, 5), (2, 235), (3, 211)]
for i, j in pairs:
    print(old_dt_df.iloc[i,j])
    print(new_dt_df.iloc[i,j])
    print()

exit()
for i in range(len(new_dt_df.index)):
    for j in range(len(new_dt_df.columns)):
        if old_dt_df.iloc[i,j] != new_dt_df.iloc[i,j]:
            print(f'value mismatch: {i}, {j}')
exit()

# Coocs test
cc_df = pd.read_pickle(RESULTS_PATH / 'cooc_df_corpus.p')
for w in COOC_REFS_TERMS:
    print(cc_df[w].nlargest(20))

