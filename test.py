import requests
import json
from requests.exceptions import ConnectionError

log = {}

def requests1(code_request, url, mtd1):
    if code_request != 405:
        mtd = mtd1
        opt = requests.options(url)
        answer = {'OPTIONS' : opt.status_code}
        status_code = {mtd : code_request}
        answer.update(status_code)
        status = {url : answer}
        log.update(status)
    else:
        pass

def connection_check(url):

    url = url.strip()

    responce_get = requests.get(url)
    code_get = responce_get.status_code

    responce_post = requests.post(url)
    code_post = responce_post.status_code

    requests1(code_get, url, "GET")
    requests1(code_post, url, "POST")

def check(urls):
  
    for i in range(len(urls)):
        try:
            responce = requests.get(urls[i])
            responce.raise_for_status()
        except ConnectionError:
            print(f'{urls[i]} - не является ссылкой!')
        else: 
            connection_check(urls[i])

    with open('file.json', 'w') as f:
        json.dump(log, f)

    print(log)
    
urls = [
    'http://skfgvodsjnfgsonfdvsnfvolsnfvdsofv',
    'https://en.wikipedia.org/w/index.php',
    'http://www.google.com',
    'https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html', 
    'https://ru.hexlet.io/courses/python-setup-environment/lessons/start-with-poetry/theory_unit',
    'https://habr.com/ru/post/593529/'
    ]

check(urls)
