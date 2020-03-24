#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 12:16:32 2020

@author: yanni
"""

from src.util_intent_slots_detection import *
from src.Aspect_Mining.Aspect_Sentiment import *
from MYSQL import *

# database_name = 'MovieAssistant'
# table_name = 'movie_all_new'
# user_name = 'root'
# password_info = 'PLPgroup11'
#
# conn = connect(host='localhost', port=3306, database= database_name, user= user_name, password= password_info, charset='utf8')
# cs1 = conn.cursor()

last_intent = ''
suggest_lst = []
def main(req,mysql):
    global last_intent, suggest_lst
    if last_intent:
        predicted_Intent = last_intent
        if req == '1'or  req =='2' or req =='3':
            print('yes')
            predicted_Slots = [['movieName', suggest_lst[int(req)]]]
        else:
            predicted_Slots = [['movieName', req]]

    else:
        predicted_Intent, predicted_Slots = Intent_Slots_Detection(req)
        print(predicted_Intent)
        movieName = ''
    
    if predicted_Intent[0] == 'recom_keyword':
        print('Keyword Recommendation: ', predicted_Slots)
    elif predicted_Intent[0] == 'recom_upcoming':
        print('Upcoming Recommendation: ')
    elif predicted_Intent[0] == 'aspect_analysis':
        if predicted_Slots[0][0] == 'aspect':
            movieName = predicted_Slots[1][1]
            aspect = predicted_Slots[0][1]
        elif predicted_Slots[1][0] == 'aspect':
            movieName = predicted_Slots[0][1]
            aspect = predicted_Slots[1][1]
        
        if aspect in ['acting', 'direction', 'screenplay', 'sound', 'story', 'visual']:
            print('OK')
            search_command = "SELECT * FROM aspect_sentiment" + " where title = '" + movieName + "'"
            myresult = mysql.ExecQuery(search_command)
            if myresult:
                result = aspect_score(aspect,myresult)
            else:
                result = "Sorry, I don't have the information about this movie"
        else:
            result = "Sorry, I don't have the information about this movie"
        
        print('Aspect Analysis:', predicted_Slots)
    elif predicted_Intent[0] == 'reviews_summary':
        print('Summary:', predicted_Slots)
    elif predicted_Intent[0] == 'recom_similarity':
        print('Similarity Recommendation:', predicted_Slots)
    elif predicted_Intent[0]:
        print('Basic Info: ', predicted_Intent[0])
        if not predicted_Slots:
            result = "Sorry, I don't understand"
        else:
            for slot in predicted_Slots:
                if slot[0] == 'movieName':
                    movieName = slot[1]
                    print(movieName)
            search_command = "SELECT " + predicted_Intent[0] + " FROM movie_all_new" + " where title = '" + movieName + "'"
            myresult = mysql.ExecQuery(search_command)
            if last_intent and myresult == ():
                last_intent = ''
                suggest_lst = []
                result = "Sorry, I don't have the information about this movie"
            
            elif myresult == ():
                search_command = "SELECT title FROM movie_all_new" + " where title like '" + '%' + movieName.replace(" ", "% %") + '%' + "'" + " order by users_rating desc"
                myresult = mysql.ExecQuery(search_command)
                if myresult == ():
                    result = "Sorry, I don't have the information about this movie"
                else:
                    last_intent = predicted_Intent
                    suggest_lst = [myresult[0][0],myresult[1][0], myresult[2][0]]
                    result = "Which movie are you referring to? \n1: " + myresult[0][0] + ' \n2: '+ myresult[1][0] + '\n3: ' + myresult[2][0] + '\nEnter the selected number or retype the movie name'
            else:
                last_intent = ''
                suggest_lst = []
                result = 'The ' + predicted_Intent[0] + ' of ' + movieName + ' is ' + myresult[0][0]
    else:
        result = "Sorry, I don't understand"
    print(result)
    return result

req = 'What do people say about the actor of Burden?'

mysql = MYSQL()
result = main(req, mysql)
print(result)