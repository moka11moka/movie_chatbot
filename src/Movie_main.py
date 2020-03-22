#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 12:16:32 2020

@author: yanni
"""

from src.util_intent_slots_detection import Intent_Slots_Detection
from pymysql import *

database_name = 'movie_all'
table_name = 'movie_all'
user_name = 'root'
password_info = '794463019'

conn = connect(host='localhost', port=3306, database=database_name, user= user_name, password= password_info, charset='utf8')
cs1 = conn.cursor()

def conversation(req):
    predicted_Intent, predicted_Slots = Intent_Slots_Detection(req)
    movieName = ''
    if predicted_Intent[0] == 'recom_keyword':
        print('Keyword Recommendation: ', predicted_Slots)
    elif predicted_Intent[0] == 'recom_upcoming':
        print('Upcoming Recommendation: ')
    elif predicted_Intent[0] == 'aspect_analysis':
        print('Aspect Analysis:', predicted_Slots)
    elif predicted_Intent[0] == 'reviews_summary':
        print('Summary:', predicted_Slots)
    elif predicted_Intent[0]:
        print('Basic Info: ', predicted_Intent[0])
        if not predicted_Slots:
            result = "Sorry, I don't understand"
        else:
            for slot in predicted_Slots:
                if slot[0] == 'movieName':
                    movieName = slot[1]
            search_command = "SELECT " + predicted_Intent[0] + " FROM " + table_name + " where title = '" + movieName + "'"
            cs1.execute(search_command)
            myresult = cs1.fetchall()
            result = myresult[0][0]
    else:
        result = "Sorry, I don't understand"
    return result

req = 'who is the directors of Burden?'

result = conversation(req)
# cs1.close()
# conn.close()

