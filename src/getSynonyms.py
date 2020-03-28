#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 19:14:51 2020

@author: yanni
"""

#!pip install wiktionaryparser

from wiktionaryparser import WiktionaryParser
parser = WiktionaryParser()
word = parser.fetch('actor')

### plural
word[0]['definitions'][0]['text'][0]


### synonym and related terms
word[0]['definitions'][0]['relatedWords']