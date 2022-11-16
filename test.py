import requests
import json

from requests.exceptions import ConnectionError

def check(urls):

    log = {}

    def get(code_get_1,url):

        if code_get_1 != 405:
            mtd = 'GET'
            opt = requests.options(url)
            answer = {'OPTIONS' : opt.status_code}
            status_code = {mtd : code_get_1}
            answer.update(status_code)
            status = {url : answer}
            log.update(status)
        else:
            pass

    def post(code_post_1, url):

        if code_post_1 != 405:
            mtd = 'POST'
            opt = requests.options(url)
            answer = {'OPTIONS' : opt.status_code}
            status_code = {mtd : code_post_1}
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


        get(code_get, url)

        post(code_get, url)


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
    'https://habr.com/ru/post/593529/', 'https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html'
    ]

check(urls)