import requests
from redis import Redis
from rq import Queue


def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())
    
q = Queue(connecion=Redis())

result = q.enqueue(count_words_at_url, 'http://nvie.com')
