import json
import nltk

path_key = "D:\\Natural_Language_Processing\\CA\\movie_chatbot\\src\\Keyword_Recommendation\\"

def Keyword_Recomm(flag,slots):
    print("Keyword_Recomm  "+ slots)
    if slots.isdigit():
        if flag:
            with open(path_key + 'movie_cate_dict.json', 'rb') as f:
                index_dict = json.load(f)
        else:
            with open(path_key + 'upcoming_cate_dict.json', 'rb') as f:
                index_dict = json.load(f)
        index = index_dict[slots][:3]
        index_str = ""
        for i in index:
            index_str += str(i) + ","
    else:
        index_str = ""

    return index_str

def Genre_Recomm(flag,slots):
    print("Genre_Recomm " + slots)
    WNlemma = nltk.WordNetLemmatizer()
    genre = WNlemma.lemmatize(slots.lower())

    if flag:
        with open(path_key + 'movie_genre_dict.json', 'rb') as f:
            index_dict = json.load(f)
    else:
        with open(path_key + 'upcoming_genre_dict.json', 'rb') as f:
            index_dict = json.load(f)
    index_str = ""
    if genre in index_dict.keys():
        index = index_dict[genre][:3]
        for i in index:
            index_str += str(i) + ","

    return index_str


if __name__ == '__main__':
    result = Genre_Recomm(False,'happy')
    print(result)
