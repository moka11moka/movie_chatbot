import json
import nltk

path_key = "D:\\Natural_Language_Processing\\CA\\movie_chatbot\\src\\Keyword_Recommendation\\"
def Keyword_Recomm(flag,slots):
    if flag:
        with open(path_key + 'keyword_cluster_15.json', 'rb') as f:
            keyword_dict = json.load(f)
        num_cate = 15
    else:
        with open(path_key + 'keyword_cluster_upcoming.json', 'rb') as f:
            keyword_dict = json.load(f)
        num_cate = 4
    i = 0
    while i < num_cate:
        if slots.lower() in keyword_dict[str(i)]:
            break
        i += 1
    if i >= num_cate:
        index_str = ""
    else:
        if flag:
            with open(path_key + 'movie_cate_dict.json', 'rb') as f:
                index_dict = json.load(f)
        else:
            with open(path_key + 'upcoming_cate_dict.json', 'rb') as f:
                index_dict = json.load(f)
        index = index_dict[str(i)][:3]
        index_str = ""
        for i in index:
            index_str += str(i) + ","

    return index_str


def Genre_Recomm(flag,slots):
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
    result = Keyword_Recomm(True,'happy')
    print(result)