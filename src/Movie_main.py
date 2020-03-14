#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 12:16:32 2020

@author: yanni
"""

from util_intent_slots_detection import *


from pymysql import *

conn = connect(host='localhost', port=3306, database='Movie', user='root', password='sabrina930101', charset='utf8')
cs1 = conn.cursor()


def main(req):
    
    predicted_Intent, predicted_Slots = Intent_Slots_Detection(req)
    
    movieName = ''
    
    if predicted_Intent[0] == 'recom_keyword':
        print('Keyword Recommendation: ', predicted_Slots)
    elif predicted_Intent[0] == 'recom_upcoming':
        print('Upcoming Recommendation: ', predicted_Slots)
    elif predicted_Intent[0] == 'aspect_analysis':
        print('Aspect Analysis:', predicted_Slots)
    elif predicted_Intent[0]:
        print('Basic Info: ', predicted_Intent[0])
        for slot in predicted_Slots:
            if slot[0] == 'movieName':
                movieName = slot[1]
        search_command = "SELECT " + predicted_Intent[0]+ " FROM movie_all where title = '" + movieName + "'"
        cs1.execute(search_command)
        myresult = cs1.fetchall()
        result = myresult[0][0]
    else:
        result = "Sorry, I don't understand"
    return result

req = 'what is the genre of Radioactive?'

result = main(req)
print(result)