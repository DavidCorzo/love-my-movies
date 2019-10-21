import requests
import ast
import json
import redis
import flask


def json_retrieve(url_portal):
    failiure = True
    while failiure:
        try:
            html_content = requests.get(url_portal).text
            failiure = False
        except:
            print(f"unable to get {url_portal}")
            html_content = None
            failiure = True

    with open(filename, mode='w+') as f:
        pass
    
    return html_content


# https: // www.themoviedb.org/documentation/api


url = 'https://api.themoviedb.org/3/discover/movie?api_key=4cddaca15876165c4395177ea57cc102&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1'

info = json_retrieve(url)
# print(info)


class OpenAndProcessAFile():
    def __init__(self, filename):
        self.filename = filename

    def open_and_categorize_json(self):
        try:
            r = redis.StrictRedis(host="localhost", port=6379,
                                  db=0, charset="utf-8", decode_responses=True)
            with open(self.filename, mode='r', encoding="utf8") as data_file:
                test_data = json.load(data_file)
                r.set(self.filename, test_data)
        except Exception as e:
            print(f'An error occurred {e}')


Class = OpenAndProcessAFile('discover_movies.json')
print(Class.open_and_categorize_json())
