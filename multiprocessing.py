keywords1 = {}
def f(m):
    tr4w.analyze(movies[m], candidate_pos = ['NOUN', 'PROPN','ADJ','VERB'], window_size=5, lower=False,stopwords=stopwords)
    words = tr4w.get_keywords(10)
    #print((len(movies[m]),words))
    keywords1[m] = ",".join(words)



from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Executor
import multiprocessing
import time
from tqdm.auto import tqdm
tr4w = TextRank4Keyword()
stopwords = ['films','movies','film','movie','story','stories']
start = time.time()
titles = [m for m in movies]
cpu_cnt = multiprocessing.cpu_count()
pool = ThreadPoolExecutor(max_workers=cpu_cnt)
with tqdm(total=len(titles)) as t:
    for _ in pool.map(f,titles):
        t.update(1)
        pass
    pool.close()
    pool.join()