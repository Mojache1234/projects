import pandas as pd
import numpy as np
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

df = pd.read_csv('master.csv')

df.columns

# Drop Duplicates
df.drop_duplicates(subset='userid', keep='first', inplace=True)

# Remove punctuation, use lowercase, and split each word

df['nps_reason_tokenized'] = df['NPS_reason'].str.replace('[{}]'.format(string.punctuation), '').str.lower()

# Tokenize words
stop_words = set(stopwords.words('english')) 
df.nps_reason_tokenized = [[w for w in word_tokenize(s) if not w in stop_words] for s in df.nps_reason_tokenized.replace(np.nan, '')]

# Segment into promoters and detractors
promoters = df.loc[df['NPS_group'] == 'Promoter']
detractors = df.loc[df['NPS_group'] == 'Demoter']

# Create counters
bow = Counter()
bow_promoters = Counter()
bow_detractors = Counter()

# Get word counts
for s in df.nps_reason_tokenized.dropna():
    for w in s:
        bow[w] += 1

for s in promoters.nps_reason_tokenized.dropna():
    for w in s:
        bow_promoters[w] += 1

for s in detractors.nps_reason_tokenized.dropna():
    for w in s:
        bow_detractors[w] += 1

# Get ratios
bow_pos_neg_ratios = Counter()

for word, cnt in bow.most_common():
    if bow[word] >= 10:
        bow_pos_neg_ratios[word] = bow_promoters[word] / float(bow_detractors[word] + 1)

# Normalize ratios
for word, ratio in bow_pos_neg_ratios.most_common():
    if(ratio > 1):
        bow_pos_neg_ratios[word] = np.log(ratio)
    else:
        bow_pos_neg_ratios[word] = -np.log(1 / (ratio + 0.01))

# Find positive words
bow_pos_neg_ratios.most_common(30)

# Community
mask = df.nps_reason_tokenized.apply(lambda x: ('community' in x) or ('social' in x) or ('connect' in x) or ('together' in x) or ('others' in x))
for comment, score in df[(mask) & (df['NPS_group'] == 'Promoter')][['NPS_reason', 'NPS_score']].values:
    print('-', comment, '-- Score: ', score)

# Learning
mask = df.nps_reason_tokenized.apply(lambda x: ('learn' in x) or ('knowledge' in x) or ('skills' in x))
for comment, score in df[(mask) & (df['NPS_group'] == 'Promoter')][['NPS_reason', 'NPS_score']].values:
    print('-', comment, '-- Score: ', score)

# Sharing
mask = df.nps_reason_tokenized.apply(lambda x: 'sharing' in x)
for comment, score in df[(mask) & (df['NPS_group'] == 'Promoter')][['NPS_reason', 'NPS_score']].values:
    print('-', comment, '-- Score: ', score)

# Tech
mask = df.nps_reason_tokenized.apply(lambda x: 'tech' in x)
for comment, score in df[(mask) & (df['NPS_group'] == 'Promoter')][['NPS_reason', 'NPS_score']].values:
    print('-', comment, '-- Score: ', score)

# For LATAM (Highest NPS)
for comment, score in df.loc[(df['region_name'] == 'LATAM') & (df['NPS_group'] == 'Promoter')][['NPS_reason', 'NPS_score']].dropna().values:
    print('-', comment, '-- Score: ', score)

# Find negative words
list(reversed(bow_pos_neg_ratios.most_common()))[:20]

# Activity
mask = df.nps_reason_tokenized.apply(lambda x: ('activities' in x) or ('activity' in x) or ('active' in x))
for comment, score in df[(mask) & (df['NPS_group'] == 'Demoter')][['NPS_reason', 'NPS_score']].values:
    print('-', comment, '-- Score: ', score)

# Events
mask = df.nps_reason_tokenized.apply(lambda x: ('events' in x) or ('event' in x))
for comment, score in df[(mask) & (df['NPS_group'] == 'Demoter')][['NPS_reason', 'NPS_score']].values:
    print('-', comment, '-- Score: ', score)

# MENA (Lowest NPS)
for comment, score in df.loc[(df['region_name'] == 'MENA') & (df['NPS_group'] == 'Demoter')][['NPS_reason', 'NPS_score']].dropna().values:
    print('-', comment, '-- Score: ', score)

# APAC (Lowest NPS)
for comment, score in df.loc[(df['region_name'] == 'APAC') & (df['NPS_group'] == 'Demoter')][['NPS_reason', 'NPS_score']].dropna().values:
    print('-', comment, '-- Score: ', score)