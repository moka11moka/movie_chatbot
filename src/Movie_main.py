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
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

result, last_intent = '', ''
suggest_lst = []

def main(req,mysql):
    global last_intent, suggest_lst, result

    if last_intent:
        predicted_Intent = last_intent
        if req == '1'or  req =='2' or req =='3':
            predicted_Slots = [['movieName', suggest_lst[int(req)]]]
        else:
            predicted_Slots = [['movieName', req]]
    else:
        predicted_Intent, predicted_Slots = Intent_Slots_Detection(req)
        movieName = ''
    
    if predicted_Intent[0] == 'recom_keyword':
        index_str = Genre_Recomm(True,predicted_Slots[0][1])
        if index_str == "":
            index_str = Keyword_Recomm(True,predicted_Slots[0][1])
        if index_str == "":
            result = "Sorry, we don't have category " + predicted_Slots[0][1]
        else:
            cate_recomm = "SELECT title,rating FROM movie_simple " + " where idx in (" + index_str[:-1] + ")"
            myresult = mysql.ExecQuery(cate_recomm)
            title_str = ""
            tips = ""
            for movie in myresult:
                title_str += movie[0] + ","
                if movie[1]!="":
                    tips += movie[0] + " is " + movie[1] + " level movie. "
            result = "Here are the recommendations: "+ title_str[:-1] + ".\nTips:" + tips
        return result

    elif predicted_Intent[0] == 'recom_similarity':
        movieName = predicted_Slots[0][1]
        search_command = "SELECT recommends FROM movies" + " where title = '" + movieName + "'"
        result = mysql.ExecQuery(search_command)
        if not result:
            result = "Sorry, I don't have the information about this movie"
        else:
            result = result[0][0]

    elif predicted_Intent[0] == 'recom_upcoming':
        if predicted_Slots == []:
            index_str = "30,45,51," # index of top3
        else:
            slot = predicted_Slots[0][1]
            index_str = Genre_Recomm(False,slot)
        if index_str == "":
            index_str = Keyword_Recomm(False,slot)
        if index_str == "":
            result = "Sorry, we dont' have category " + slot
        else:
            cate_recomm = "SELECT title,rating FROM upcoming_simple " + " where idx in (" + index_str[:-1] + ")"
            myresult = mysql.ExecQuery(cate_recomm)
            title_str = ""
            tips = ""
            for movie in myresult:
                title_str += movie[0] + ","
                if movie[1] != "":
                    tips += movie[0] + " is " + movie[1] + " level movie. "
            result = "Here are the recommendations: " + title_str[:-1] + ".\nTips:" + tips
        return result

    elif predicted_Intent[0] == 'aspect_analysis':
        aspect = ''
        print(predicted_Slots)
        if predicted_Slots[0][0] == 'aspect':
            movieName = predicted_Slots[1][1]
            aspect = predicted_Slots[0][1]
        elif predicted_Slots[1][0] == 'aspect':
            movieName = predicted_Slots[0][1]
            aspect = predicted_Slots[1][1]
        
        if aspect in ['acting', 'direction', 'screenplay', 'sound', 'story', 'storyline','visual']:
            print('OK')
            search_command = "SELECT * FROM aspect_sentiment" + " where title = '" + movieName + "'"
            myresult = mysql.ExecQuery(search_command)
            if myresult:
                result = aspect_score(aspect,myresult)
            else:
                result = "Sorry, I don't have the information about this movie"
        else:
            result = "Sorry, I don't have the information about this movie"
    elif predicted_Intent[0] == 'reviews_summary':
        movieName = predicted_Slots[0][1]
        search_command = "SELECT summary FROM movies" + " where title = '" + movieName + "'"
        result = mysql.ExecQuery(search_command)
        if not result:
            result = "Sorry, I don't have the information about this movie"
        else:
            result = result[0][0]
    elif predicted_Intent[0]:
        if not predicted_Slots:
            result = "Sorry, I don't understand"
            chatbot = ChatBot('Norman')
            result = chatbot.get_response(req)
        else:
            for slot in predicted_Slots:
                if slot[0] == 'movieName':
                    movieName = slot[1]
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

chatbot = ChatBot("bot")
trainer = ListTrainer(chatbot)

req = 'Hi?'
mysql = MYSQL()
try:
    result = main(req, mysql)
except:
    chatbot = ChatBot('Norman')
    result = chatbot.get_response(req)
print(result)


