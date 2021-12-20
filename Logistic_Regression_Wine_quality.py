# -*- coding: utf-8 -*-
"""CS2202 CS Mini-Project Logistic Regression on Wine-Dataset to predict quality of wine .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wDG18v2L2IdIzsZPNVuH9clZQaugcb82

# ***Computational Statistics Mini-Project***

------------------------------------------------------------

Name: Shashank Bhosagi

Roll No. : CS2202

S.Y.Btech Division-B

----------------------------

### ***DATASET***

Dataset was downloaded for UCI Machine Learning Repository 

Link to Dataset : https://archive.ics.uci.edu/ml/datasets/Wine+Quality

There are two datasets on this website RED wine and WHITE wine but in this project we will use White wine

Problem Statement: Predict the quality of White-Wine using a classification method called ***Logistic Regression***

--------------------------------------------

### **1. Uploading the DataSet in Colab**
"""

from google.colab import files

uploaded = files.upload()

"""-----------------------------------------------------------

### *2. Load the file in a dataframe using Pandas*
"""

import pandas as pd

wine = pd.read_csv("/content/winequality-white.csv")

"""-----------------------------------------------------------------------------------------------------------------------------------------------

### **3. Describing the Data**
"""

wine.head()

"""Our data has 12 columns. And all columns seems to be in numeric form so its good for us.

1 - fixed acidity

2 - volatile acidity

3 - citric acid

4 - residual sugar

5 - chlorides

6 - free sulfur dioxide

7 - total sulfur dioxide

8 - density

9 - pH

10 - sulphates

11 - alcohol

12 - quality (score between 0 and 10)

Where 12th Data **'quality'** is ***output variable***
"""

wine.info()

"""All the values are in float or int so its great for us and no type conversions required.
No. of rows = 4898
Hence shape of the data is  **4838x12**
"""

wine.describe()

"""-------------------------------------------------------------------------------------------------------------------

###**4. Let's check for missing data if any**
"""

wine.isnull().sum()

"""Zeros indicate that there is no null values in our Data-set!!

### **5. Converting the "quality" column from scores b/w 1-10 to 0's and 1's**

As the objective is to predict wine as good or bad we need to convert in result column  1 or 0

Where,

1 indicates good quality

0 indicates bad quality
"""

import matplotlib.pyplot as plt
wine.hist(column = 'quality', figsize=(10,10))

plt.show()

"""From this histogram we can take the mid-point approx at 6.5
so we will set condition as 

if 3 to 6.5 (3 is lowest point) = 0

if 6.5 or greater = 1
"""

bins = (1, 6.5, 9)
classes = ['bad','good']
wine['quality'] = pd.cut(wine['quality'], bins = bins, labels = classes)

"""Let's check if the 'quality' column changed or not :)"""

wine.head()

"""It changed to the labels 'bad' or 'good' but we wanted 0 or 1 so here we can use LabelEncoder which is present in Skit-learn.preprocessing"""

from sklearn.preprocessing import LabelEncoder
label_quality = LabelEncoder()
wine['quality'] = label_quality.fit_transform(wine['quality'])

wine.head()

wine['quality'].value_counts()

"""Now we have converted the 'quality' column in a 0 or 1 format

### **6. Preparing the data for classification**

Now we will split the dataset into training data and testing data with 70% data as training and remaining as testing.
"""

from sklearn.model_selection import train_test_split

train,test= train_test_split(wine,test_size=0.30,random_state=565,stratify=wine['quality'])# stratify the outcome

train_X=train[train.columns[:11]]
test_X=test[test.columns[:11]]
train_Y=train['quality']
test_Y=test['quality']

"""### **7. Normalization of data using StandardScaler**"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

train_X = sc.fit_transform(train_X)
test_X = sc.fit_transform(test_X)

from sklearn.linear_model import LogisticRegression
from sklearn import metrics

import warnings
warnings.filterwarnings('ignore')
m = LogisticRegression()
m.fit(train_X,train_Y)
p = m.predict(test_X)

print('The accuracy Score is:\n',metrics.accuracy_score(p,test_Y))

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

print("Classification Report:")
print(classification_report(test_Y,p ))

from sklearn.metrics import roc_auc_score,confusion_matrix
roc_auc_score(test_Y,p)



conf = confusion_matrix(test_Y,p)
conf

import seaborn as sns
label = ["0","1"]
sns.heatmap(conf, annot=True, xticklabels=label, yticklabels=label)
