#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 12:16:32 2020

@author: yanni
"""
from src.Keyword_Recommendation.Keyword_Recommendation import Genre_Recomm, Keyword_Recomm
from src.util_intent_slots_detection import *
from src.Aspect_Mining.Aspect_Sentiment import *
from MYSQL import MYSQL

result, last_intent = '', ''
suggest_lst = []

def main(req,mysql):
    global last_intent, suggest_lst, result
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
        print('Keyword Recommendation: ', predicted_Slots[0][1])
        index_str = Genre_Recomm(True,predicted_Slots[0][1])
        if index_str == "":
            index_str = Keyword_Recomm(True,predicted_Slots[0][1])
        if index_str == "":
            result = "Sorry, we don't have category " + predicted_Slots[0][1]
        else:
            cate_recomm = "SELECT title FROM movie_simple " + " where idx in (" + index_str[:-1] + ")"
            myresult = mysql.ExecQuery(cate_recomm)
            title_str = ""
            print(myresult)
            for title in myresult:
                title_str += title[0] + ","
            result = "Here are the recommendations: "+ title_str[:-1]
        return result

    elif predicted_Intent[0] == 'recom_upcoming':
        print('Upcoming Recommendation: ')
        index_str = Genre_Recomm(False,predicted_Slots[0][1])
        if index_str == "":
            index_str = Keyword_Recomm(False,predicted_Slots[0][1])
        if index_str == "":
            result = "Sorry, we dont' have category " + predicted_Slots[0][1]
        else:
            cate_recomm = "SELECT title FROM upcoming " + " where idx in (" + index_str[:-1] + ")"
            myresult = mysql.ExecQuery(cate_recomm)
            title_str = ""
            print(myresult)
            for title in myresult:
                title_str += title[0] + ","
            result = "Here are the recommendations: "+ title_str[:-1]
        return result
    elif predicted_Intent[0] == 'aspect_analysis':
        movieName = predicted_Slots[1][1]
        aspect = predicted_Slots[0][1]
        search_command = "SELECT * FROM aspect_sentiment" + " where title = '" + movieName + "'"
        myresult = mysql.ExecQuery(search_command)
        if myresult:
            result = aspect_score(aspect,myresult)
        else:
            result = "Sorry, I don't have the information about this movie"
        print('Aspect Analysis:', predicted_Slots)
    elif predicted_Intent[0] == 'reviews_summary':
        print('Summary:', predicted_Slots)
        movieName = predicted_Slots[0][1]
        search_command = "SELECT summary FROM movies" + " where title = '" + movieName + "'"
        result = mysql.ExecQuery(search_command)
        if not result:
            result = "Sorry, I don't have the information about this movie"
        else:
            result = result[0][0]
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
    return result

req = 'Recommend some happy to watch'
mysql = MYSQL()
result = main(req, mysql)
print(result)


