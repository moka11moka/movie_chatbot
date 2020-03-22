#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:26:14 2020

@author: yanni
"""

from snips_nlu import SnipsNLUEngine
import pickle


path = 'C:\\Users\\guoxi\\Desktop\\movie_chatbot\\src\\'
# load Intent Detection Model
#print(path / "nlu_engine.json")
bigram_vectorizer_filename = 'C:/Users/guoxi/Desktop/movie_chatbot/src/Intent_Detection_bigram_vectorizer.sav'
ch21_filename = 'C:/Users/guoxi/Desktop/movie_chatbot/src/Intent_Detection_ch21.sav'
crlsvm_filename = 'C:/Users/guoxi/Desktop/movie_chatbot/src/Intent_Detection_Model.sav'

loaded_bigram_vectorizer = pickle.load(open(bigram_vectorizer_filename, 'rb'))
loaded_ch21 = pickle.load(open(ch21_filename, 'rb'))
loaded_crlsvm = pickle.load(open(crlsvm_filename, 'rb'))

### load Slots Detection Model
# loaded_NLUEngine = SnipsNLUEngine.from_path('C:/Users/guoxi/Desktop/movie_chatbot/src/SlotsDetection')

import io
import json

import en_core_web_sm

nlp = en_core_web_sm.load()

from snips_nlu import SnipsNLUEngine

# path = 'C:/Users/guoxi/Desktop/movie_chatbot/src/'

### train Slots Detection Model

with io.open(path + 'Movie_dataset.json') as f:
    sample_dataset = json.load(f)

loaded_NLUEngine = SnipsNLUEngine()

loaded_NLUEngine.fit(sample_dataset)

def Intent_Slots_Detection(test_phrase):
    if test_phrase[-1] == '?':
        test_phrase = test_phrase.replace('?', '.')
    elif test_phrase[-1] != '.':
        test_phrase += '.'
    test_bigram_vectors = loaded_bigram_vectorizer.transform([test_phrase])
    test_bigram_Kbest = loaded_ch21.transform(test_bigram_vectors)
    predicted_Intent = loaded_crlsvm.predict(test_bigram_Kbest)

    test_data = loaded_NLUEngine.parse(test_phrase)
    predicted_Slots = []
    for slot in test_data['slots']:
        predicted_Slots.append([slot['slotName'], slot['value']['value']])
    return (predicted_Intent, predicted_Slots)


