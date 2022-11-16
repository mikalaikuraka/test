import requests
import json


log = {}

def connection_check(url):

    url = url.strip()

    responce_get = requests.get(url)
    code_get = responce_get.status_code

    responce_post = requests.post(url)
    code_post = responce_post.status_code


    if code_get != 405:
        mtd = 'GET'
        opt = requests.options(url)
        answer = {'OPTIONS' : opt.status_code}
        status_code = {mtd : code_get}
        answer.update(status_code)
        status = {url : answer}
        log.update(status)
    else:
        pass

    if code_post != 405:
        mtd = 'POST'
        opt = requests.options(url)
        answer = {'OPTIONS' : opt.status_code}
        status_code = {mtd : code_post}
        answer.update(status_code)
        status = {url : answer}
        log.update(status)
    else:
        pass


urls = [
    'https://en.wikipedia.org/w/index.php',
    'http://www.google.com',
    'https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html', 
    'https://ru.hexlet.io/courses/python-setup-environment/lessons/start-with-poetry/theory_unit',
    'https://habr.com/ru/post/593529/', 'https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html'
    ]


for i in range(len(urls)):
    connection_check(urls[i])

