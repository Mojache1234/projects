import pandas as pd
import re
# import pickle as pkl
import time
import numpy as np
import StringIO
import requests
from sympy import sigmoid
from matplotlib import pyplot as plt
import urllib2
from bs4 import BeautifulSoup
from sklearn.preprocessing import LabelEncoder
import h5py as hf
from collections import Counter

# Source: https://www.analyticsvidhya.com/blog/2017/05/questions-python-for-data-science/

# 1. Count how many times But, um... was said

txt = '''450
 00:17:53,457 --> 00:17:56,175
 Okay, but, um,
 thanks for being with us.

451
 00:17:56,175 --> 00:17:58,616
 But, um, if there's any
 college kids watching,

452
 00:17:58,616 --> 00:18:01,610
 But, um, but, um, but, um,
 but, um, but, um,

453
 00:18:01,610 --> 00:18:03,656
 We have to drink, professor.
 454
 00:18:03,656 --> 00:18:07,507
 It's the rules.
 She said "But, um"

455
 00:18:09,788 --> 00:18:12,515
 But, um, but, um, but, um...
 god help us all.
 '''

print(len(re.findall(r'[Bb]ut, um', txt)))

# What number should be mentioned to index only the domains?

str = """
Email_Address,Nickname,Group_Status,Join_Year
aa@aaa.com,aa,Owner,2014
bb@bbb.com,bb,Member,2015
cc@ccc.com,cc,Member,2017
dd@ddd.com,dd,Member,2016
ee@eee.com,ee,Member,2020
"""

for i in re.finditer('([a-zA-z]+@([a-zA-Z]+).(com))', str):
    print(i.group(0))
    print(i.group(1))
    print(i.group(2))  # <-- Answer
    print(i.group(3))

# 3. Find all people with name ending with sound "Y"

str = """
Diego
Andy
Mandi
Sandy
Hollie
Molly
Dollie
"""

pattern = r'([a-zA-Z]+([i$|ie$]))'  # This wasn't one of the answers, but none of the answers worked for python 3...
# pattern = r'(i$|ie$)'
temp = []
for i in re.finditer(pattern, str):
    temp.append(i.group(1))

print(temp)

# 4. concatenate list
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]

print(a + b)
print(a.extend(b))

# 5. Using pickle, freeze learning model for use later
# pkl.dump(model, "file")
# Source: https://pythontips.com/2013/08/02/what-is-pickle-in-python/

# 6. Convert string in date-time value
date_format = '%d/%m/%Y'
str = '21/01/2017'
datetime_value = time.strptime(str, date_format)

# 7. Given identity matrix, how would I create in python?
np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
np.eye(3)
np.identity(3)

# 8. Check if two arrays occupy same space
e = np.array([1, 2, 3, 2, 3, 4, 4, 5, 6])
f = np.array([[1, 2, 3], [2, 3, 4], [4, 5, 6]])

# changing first 5 values of e also changes first 5 values of f
# Print flags of both arrays by e.flags and f.flags; check the flag "OWNDATA". If one is false, then both arrays have same space allocated
e.flags
f.flags

# 9. Join train and test data set (both are numpy arrays) into resulting array
train_set = np.array([1, 2, 3])
test_set = np.array([[0, 1, 2], [1, 2, 3]])

# Vertical Stack
resulting_set = np.vstack([train_set, test_set])

# Horizontal Stack
resulting_set = train_set.append(test_set)
resulting_set = np.concatenate([train_set, test_set])

# 10. Tuning hyperparameters of a random forest classifier for the Iris dataset. What would be the best value for random_state (seed value)?
np.random.seed(1)
np.random.seed(40)
np.random.seed(32)
# ...There is no best value for seed. It depends on the data

# 11. Automatically fill missing values of column with specific date (01/01/2010)

a = pd.DataFrame({
    'name': ['Andy', 'Mandy', 'Sandy', 'Brandy'],
    'age': [20, 30, 10, 40],
    'Date_of_Joining': ['01/02/2013', '01/05/2014', None, '01/10/2009'],
    'Total_experience': [1, 10, 0, 20]
})

a.Date_of_Joining = a.Date_of_Joining.fillna('01/01/2010')

# 12. How to import decision tree classifier in sklearn
# from sklearn.tree import DecisionTreeClassifier

# 13. Uploaded dataset in csv format on google spreadsheet and shared publicly. How do you access it in python?
link = 'https://docs.google.com/spreadsheets/d/...'
source = StringIO.StringIO(requests.get(link).content)
data = pd.read_csv(source)

# 14. Imagine you have a dataframe train file with 2 columns & 3 rows, which is loaded in pandas. What will be the output of train['features_t']?

train = pd.DataFrame({
    'id': [1, 2, 4],
    'features': [
        ["A", "B", "C"],
        ["A", "D", "E"],
        ["C", "D", "F"]
    ]
})

train['features_t'] = train['features'].apply(lambda x: " ".join(['_'.join(i.split(' ')) for i in x]))

# 15. In a multi-class classification problem for predicting quality of wine on the basis of its attributes, the quality column has values 1 to 10. We want to substitute this by a binary classification problem with a threshold for classification to 5.

wine = pd.DataFrame({
    'fixed_acidity': [7.4, 7.8, 7.8, 11.2, 7.4],
    'volatile_acidity': [0.70, 0.88, 0.76, 0.28, 0.70],
    'citric_acid': [0.00, 0.00, 0.04, 0.56, 0.00],
    'residual_sugar': [1.9, 2.6, 2.3, 1.9, 1.9],
    'free_sd': [11, 25, 15, 17, 11],
    'total_sd': [34, 67, 54, 60, 34],
    'density': [0.9978, 0.9968, 0.9970, 0.9980, 0.9978],
    'pH': [3.51, 3.20, 3.26, 3.16, 3.51],
    'sulphates': [0.56, 0.68, 0.65, 0.58, 0.56],
    'quality': np.random.randint(low=1, high=10, size=5)
})

wine['qual_bin'] = np.where(wine['quality'] >= 6, 1, 0)
# Source: https://stackoverflow.com/questions/19913659/pandas-conditional-creation-of-a-series-dataframe-column

Y = wine['quality'].values
Y = np.array([1 if y >= 6 else 0 for y in Y])

# 16. What is the difference between df['Name'] and df.loc[:, 'Name']
# The latter is a view of the original dataframe whereas the former is a copy of the original dataframe

# 17. Which of the following will be the output of the given print statement?


def fun(x):
    x[0] = 5
    return x


g = [10, 11, 12]
print(fun(g), g)
# [5, 11, 12], [5, 11, 12]

# 18. It is necessary to know how to find the derivatives of sigmoid, as it would be essential for back propagation. How do you find the derivative?
x = 5
Dv = sigmoid(x) * (1 - sigmoid(x))

# 19. Suppose you are given a monthly data and you have to convert it to daily data. How would you expand every month?
# new_df = pd.concat([df] * 30  , ignore_index=True)

# 20. Change column name to click_count
df = pd.DataFrame({
    'Click_Id': ['A', 'B', 'C', 'D', 'E'],
    'Count': [100, 200, 300, 400, 250]
})

df.rename(columns={'Count': 'Click_Count'})
print(df.columns)

# 21. Convert dataframe into a dictionary

df = pd.DataFrame({
    'Click_Id': ['A', 'B', 'C', 'D', 'E'],
    'Count': [100, 200, 300, 400, 250]
})

df.set_index('Click_Id')['Count'].to_dict()

# 22. df1 = df. Change count in df. Print result?
df1 = df
df.loc[df.Click_Id == 'A', 'Count'] += 100
print(df.Count.values)
print(df1.Count.values)

df1.loc[df.Click_Id == 'A', 'Count'] += 100
print(df.Count.values)
print(df1.Count.values)  # Passed by reference

# 23. Bookmarking tasks to check how much time has elapsed
time.sleep()
time.time()

# 24. Read using pandas by skipping first three lines
pd.read_table('file.xlsx', skiprows=3)

# 25. Given the data frame below, how to produce desired outcome?
df = pd.DataFrame({
    'EMPID': ['E001', 'E002', 'E003', 'E004', 'E005', 'E006', 'E007', 'E008', 'E009', 'E010'],
    'Gender': ['M', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'M', 'M'],
    'Age': [34, 40, 37, 30, 44, 36, 32, 26, 32, 36],
    'Sales': [123, 114, 135, 139, 117, 121, 133, 140, 133, 133],
    'BMI': ['Normal', 'Overweight', 'Obesity', 'Underweight', 'Underweight', 'Normal', 'Obesity', 'Normal', 'Normal', 'Underweight'],
    'Income': [350, 405, 169, 189, 183, 80, 166, 120, 75, 40]
})

var = df.groupby(['BMI', 'Gender']).Sales.sum()
var.unstack().plot(kind='bar', stacked=True, color=['red', 'blue'], grid=False)
plt.show()

# 26. Given two lists, check if one is in the other
City_A = [1, 2, 3, 4]
City_B = [2, 3, 4, 5]
[i for i in City_A if i not in City_B]

# 27. Encountered UnicodeEncodeError: 'ascii' codec can't encode character
pd.read_csv('file.csv', encoding='utf-8')

# 28. Given a tuple, how to change 2nd index?
# Trick question: You can't change any of the values of a tuple, fool!

# 29. Read url using urllib2
urllib2.urlopen('www.abcd.org')
requests.get('www.abcd.org')

# 30. Read webpage using BeautifulSoup and extract title tag
html_doc = """
 <!DOCTYPE html>
 <htmllang="en">
 <head>
 <metacharset="utf-8">
 <metaname="viewport" content="width=device-width">
 <title>udacity/deep-learning: Repo for the Deep Learning Nanodegree Foundations program.</title>
 <linkrel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
 <linkrel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
 <metaproperty="fb:app_id" content="1401488693436528">
 <linkrel="assets" href="https://assets-cdn.github.com/">
 ...
 """

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title.string)

# 31. Given DataFrame, apply label encoder
d = ['A', 'B', 'C', 'D', 'E', 'AA', 'AB']
le = LabelEncoder()
print(le.fit_transform(d))

# 32. Output?
df = pd.dataFrame({
    'Id': [1, 2, 3, 4],
    'val': [2, 5, np.nan, 6]
})
print(df.val == np.nan)  # np.nan is an object, not a value (therefore, this will always be false)

# 33. Stored in HDFS format, how to find structure of data?
hf.keys()

# 34.
reviews = [
    'movie is unwatchable no matter how decent the first half is  . ',
    'somewhat funny and well  paced action thriller that has jamie foxx as a hapless  fast  talking hoodlum who is chosen by an overly demanding',
    'morse is okay as the agent who comes up with the ingenious plan to get whoever did it at all cost .'
]

counts = Counter()
for i in range(len(reviews)):
    for word in reviews[i].split(' '):
        counts[word] += 1

# 35. How to set a line width in the plot given?
plt.plot([1, 2, 3, 4], lw=3)
plt.show()

# 36. How to reset the index of dataframe to given list?
new_index = ['Safari', 'Iceweasel', 'Comodo Dragon', 'IE10', 'Chrome']
df = pd.DataFrame({
    None: ['Firefox', 'Chrome', 'Safari', 'IE10', 'Konqueror'],
    'http_status': [200, 200, 404, 404, 301],
    'response_time': [0.04, 0.02, 0.07, 0.08, 1.00]
})

df.reset_index(new_index,)

# 37. Given a dataframe, create a cross tab of two Series from that dataframe
pd.crosstab('df_train[Pclass], df_train[Survived]')

# 38. Write generic code to calculate n-gram of text.

sentence = 'this is a sample text'


def generate_ngrams(text, n):
    words = text.split()
    output = []
    for i in range(len(words) - n + 1):
        output.append(words[i: i + n])
    return output


# 39. Which of the following code will export dataframe(df) in CSV encoded in UTF-8 after hiding index and header labels?
# df_1 = pd.DataFrame(np.random.randint(low=1, high=4, size=5))
df_1 = pd.DataFrame(np.random.random((4, 5)))
df_1.to_csv('test_file.csv', encoding='utf-8', index=False, header=False)

# 40. Which of the following is a correct implementation of mean squared error (MSE) metric?


def MSE(real_target, predicted_target):
    return np.mean((real_target - predicted_target)**2)


real_target = np.random.random(5)
predicted_target = np.random.random(5)

print('Random Numbers:', MSE(real_target, predicted_target))

real_target = np.array([1, 2, 3, 4, 5])
predicted_target = np.array([1, 2, 3, 4, 5])
print('Same list:', MSE(real_target, predicted_target))
