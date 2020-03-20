#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 12:16:32 2020

@author: yanni
"""

from util_intent_slots_detection import *


from pymysql import *

database_name = 'Movie'
table_name = 'movie_all'
user_name = 'root'
password_info = 'sabrina930101'

conn = connect(host='localhost', port=3306, database= database_name, user= user_name, password= password_info, charset='utf8')
cs1 = conn.cursor()

last_intent = ''
suggest_lst = []
def main(req):
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
            if last_intent and myresult == ():
                last_intent = ''
                suggest_lst = []
                result = "Sorry, I don't have the information about this movie"
            
            elif myresult == ():
                search_command = "SELECT title FROM " + table_name + " where title like '" + '%' + movieName.replace(" ", "% %") + '%' + "'" + " order by users_rating desc"
                cs1.execute(search_command)
                myresult = cs1.fetchall()
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
    return result

req = 'what is the genre of First Co?'

result = main(req)
print(result)