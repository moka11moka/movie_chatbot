#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 17:04:36 2020

@author: yanni
"""

import io
import json

from snips_nlu import SnipsNLUEngine

path = '/Users/yanni/PycharmProjects/chatbot/src/'
### train Slots Detection Model

#!snips-nlu generate-dataset en {path}/Movie_intent.yaml {path}/Movie_entity.yaml  > {path}/Movie_dataset.json
with io.open(path + 'Movie_dataset.json') as f:
    sample_dataset = json.load(f)
    
nlu_engine = SnipsNLUEngine()

nlu_engine.fit(sample_dataset)

nlu_engine.persist(path + 'Movie_Slots_Detection')

#!snips-nlu generate-dataset en {path}/Aspect_intent.yaml {path}/Aspect_entity.yaml  > {path}/Aspect_dataset.json
with io.open(path + 'Aspect_dataset.json') as f:
    aspect_dataset = json.load(f)
    
nlu_engine = SnipsNLUEngine()

nlu_engine.fit(aspect_dataset)

nlu_engine.persist(path + 'Aspect_Slots_Detection')