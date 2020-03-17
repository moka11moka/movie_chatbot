#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 16:43:30 2020

@author: yanni
"""
import json
import codecs
import pandas as pd
import numpy as np
import random

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn import metrics


import pandas as pd
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import numpy as np

import re

import io
import json
import codecs
from itertools import chain
import nltk
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelBinarizer
import sklearn
import pandas as pd

#pip install python-crfsuite

import pycrfsuite
import spacy
import en_core_web_sm


import en_core_web_sm
nlp = en_core_web_sm.load()

from snips_nlu import SnipsNLUEngine
import pickle

path = '/Users/yanni/PycharmProjects/chatbot/src/'
# train Intent Detection Model
    
df = pd.read_excel(path + 'Training Phrases.xlsx') 
df = df.dropna()
X = df['Phrase']
y = df['Label']

X_train = X
Y_train = y

bigram_vectorizer = TfidfVectorizer(ngram_range=(1, 2),token_pattern=r'\b\w+\b', min_df=1)
train_bigram_vectors = bigram_vectorizer.fit_transform(X_train)

bigram_vectorizer_filename = path + 'Intent_Detection_bigram_vectorizer.sav'
pickle.dump(bigram_vectorizer, open(bigram_vectorizer_filename, 'wb'))

ch21 = SelectKBest(chi2, k='all')
train_bigram_Kbest = ch21.fit_transform(train_bigram_vectors, Y_train)

ch21_filename = path + 'Intent_Detection_ch21.sav'
pickle.dump(ch21, open(ch21_filename, 'wb'))


model_svm = SVC(C=5000.0, gamma="auto", kernel='rbf')
clr_svm = model_svm.fit(train_bigram_Kbest, Y_train)

crlsvm_filename = path + 'Intent_Detection_Model.sav'
pickle.dump(clr_svm, open(crlsvm_filename, 'wb'))

