import json
from tqdm.auto import tqdm
from pymysql import *

def text_to_csv(file_name):
    conn = connect(host='localhost', port=3306, database='movie_all', user='root', password='*****', charset='utf8')
    cs1 = conn.cursor()
    with open(file_name, 'r', encoding="utf-8") as f:
        for jsonstr in tqdm(f.readlines()):
            try:
                jsonstr = json.loads(jsonstr.strip()[:-1])
            except:
                continue
            title = jsonstr['title'].replace('"',"'") if jsonstr['title'] else 'Nothing'
            rating = jsonstr['rating'].replace('"',"'") if jsonstr['rating'] else 'Nothing'
            year = jsonstr['year'] if jsonstr['year'] else 'Nothing'
            users_rating = jsonstr['users_rating'].replace('"',"'") if jsonstr['users_rating'] else 'Nothing'
            votes = jsonstr['votes'].replace('"',"'") if jsonstr['votes'] else 'Nothing'
            img_url = jsonstr['img_url'].replace('"',"'") if jsonstr['img_url'] else 'Nothing'
            countries = ''.join(jsonstr['countries']).replace('"',"'") if jsonstr['countries'] else 'Nothing'
            languages = ''.join(jsonstr['languages']).replace('"',"'") if jsonstr['languages'] else 'Nothing'
            actors = ''.join(jsonstr['actors']).replace('"',"'") if jsonstr['actors'] else 'Nothing'
            genre = ''.join(jsonstr['genre']).replace('"',"'") if jsonstr['genre'] else 'Nothing'
            tagline = jsonstr['tagline'].replace('"',"'") if jsonstr['tagline'] else 'Nothing'
            description = jsonstr['description'].replace('"',"'") if jsonstr['description'] else 'Nothing'
            directors = ''.join(jsonstr['directors']) if jsonstr['directors'] else 'Nothing'
            runtime = jsonstr['runtime'].replace('"',"'") if jsonstr['runtime'] else 'Nothing'
            imdb_url = jsonstr['imdb_url'].replace('"',"'") if jsonstr['imdb_url'] else 'Nothing'
            reviews = ''.join(jsonstr['reviews']).replace('"',"'") if jsonstr['reviews'] else 'Nothing'
            sql = 'insert into movie_all values ('+'"'+title+'"'+','+'"'+rating+'"'+','+'"'+year+'"'+','+'"'+users_rating+'"'+','+'"'+votes+'"'+','+'"'+img_url+'"'+','+'"'+countries+'"'+','+'"'+languages+'"'+','+'"'+actors+'"'+','+'"'+genre+'"'+','+'"'+tagline+'"'+','+'"'+description+'"'+','+'"'+directors+'"'+','+'"'+runtime+'"'+','+'"'+imdb_url+'"'+','+'"'+reviews+'"'+')'
            try:
                cs1.execute(sql)
            except:
                continue
    conn.commit()
    cs1.close()
    conn.close()
text_to_csv('./movie_all.json')