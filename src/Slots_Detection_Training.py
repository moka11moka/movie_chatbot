#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 17:04:36 2020

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


### train Slots Detection Model

#!snips-nlu generate-dataset en /Users/yanni/downloads/Movie_intent.yaml /Users/yanni/downloads/Movie_entity.yaml  > /Users/yanni/downloads/Movie_dataset.json
with io.open("/Users/yanni/downloads/Movie/Movie_dataset.json") as f:
    sample_dataset = json.load(f)
    
nlu_engine = SnipsNLUEngine()

nlu_engine.fit(sample_dataset)

nlu_engine.persist("/Users/yanni/downloads/Movie/Slots_Detection")
#jdata = []
#
#for train_phrase in X:
#    jdata.append(nlu_engine.parse(train_phrase.replace('?', '.')))
#
#
#def loadData(jdata):
#    data_List = []
#    
#    word_List = []
#    tag_List = []
#    for data in jdata:
#        
#        wordList=[]
#        tagList=[]
#        posList=[]
#        sentlist=[]
#        
#        tokenList = data['input'].replace('.', '').split()
#        if len(data['slots']) == 0:
#            print('Error', data['input'])
#            continue
#
#        for tok in tokenList:
#            wordList.append(tok)
#            slot_detail_lst = []
#            
#            hit_flag = False
#
#            for i in range(len(data['slots'])):
#                slot_detail_lst = data['slots'][i]['rawValue'].split()
#                for idx,slot_detail in enumerate(slot_detail_lst):
#                    if tok == slot_detail and idx:
#                        tagList.append('I-'+data['slots'][i]['entity'])
#                        hit_flag = True
#                        break
#                    elif tok == slot_detail:
#                        tagList.append('B-'+data['slots'][i]['entity'])
#                        hit_flag = True
#                        break
#                    elif i == len(data['slots']) -1 and idx ==len(slot_detail_lst)-1:
#                        tagList.append('O')
#                if hit_flag ==True:
#                    break
#        sent = ' '.join(wordList)
#        sent_nlp = nlp(sent)
#        for token in sent_nlp:
#            posList.append(token.tag_)
#        
#        for idx,word in enumerate(wordList):
#            sentlist.append((word,posList[idx],tagList[idx]))
#    
#        data_List.append(sentlist)
#        word_List.append(wordList)
#        tag_List.append(tagList)
#    return data_List
#
#train_list = loadData(jdata)
#
#####
################################################################
#def word2features(sent, i):
#    word = sent[i][0]
#    postag = sent[i][1]
#    features = [  # for all words
#        'bias',
#        'word.lower=' + word.lower(),
#        #'word[-3:]=' + word[-3:],
#        'word.isupper=%s' % word.isupper(),
#        'word.istitle=%s' % word.istitle(),
#        'word.isdigit=%s' % word.isdigit(),
#        'postag=' + postag,
#        'postag[:2]=' + postag[:2],
#    ]
#    if i > 0: # if not <S>
#        word1 = sent[i-1][0]
#        postag1 = sent[i-1][1]
#        features.extend([
#            '-1:word.lower=' + word1.lower(),
#            '-1:word.istitle=%s' % word1.istitle(),
#            '-1:word.isupper=%s' % word1.isupper(),
#            '-1:word.isdigit=%s' % word1.isdigit(),
#            '-1:postag=' + postag1,
#            '-1:postag[:2]=' + postag1[:2],
#        ])
#    else:
#        features.append('BOS')  # beginning of statement
#        
#    if i < len(sent)-1:  # if not <\S>
#        word1 = sent[i+1][0]
#        postag1 = sent[i+1][1]
#        features.extend([
#            '+1:word.lower=' + word1.lower(),
#            '+1:word.istitle=%s' % word1.istitle(),
#            '+1:word.isupper=%s' % word1.isupper(),
#            '+1:word.isdigit=%s' % word1.isdigit(),
#            '+1:postag=' + postag1,
#            '+1:postag[:2]=' + postag1[:2],
#        ])
#    else:
#        features.append('EOS')
#                
#    return features
#
#
#def sent2features(sent):
#    return [word2features(sent, i) for i in range(len(sent))]
#
#def sent2labels(sent):
#    return [label for token, postag, label in sent]
#
#def sent2tokens(sent):
#    return [token for token, postag, label in sent]
##################################################################
#
#df_1 = pd.DataFrame(train_list[1],columns=["Word","POS","Entity or Aspect Tag"])
## change to dataframe for easy printing.
#df_1
#
#features = sent2features(train_list[1])
#
#X_train = [sent2features(s) for s in train_list]
#y_train = [sent2labels(s) for s in train_list]
#
#trainer = pycrfsuite.Trainer(verbose=False)
#
#for xseq, yseq in zip(X_train, y_train):
#    trainer.append(xseq, yseq)
#
#trainer.set_params({
#    'c1': 1.0,   # coefficient for L1 penalty
#    'c2': 1e-3,  # coefficient for L2 penalty
#    'max_iterations': 50,  # stop earlier
#
#    # include transitions that are possible, but not observed
#    'feature.possible_transitions': True
#})
#    
#trainer.params()
#
#trainer.train('Movie.crfsuite')

#####

    #test_slots = nlu_engine.parse(test_phrase.replace('?', '.'))
    #test_data = loadData([test_slots])
    #X_test = sent2features(test_data[0])
    #example_sent = X_test
    #tagger = pycrfsuite.Tagger()
    #tagger.open('Movie.crfsuite')
    #predicted_Slots = tagger.tag(example_sent)