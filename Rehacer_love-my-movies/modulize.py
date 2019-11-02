import requests
import redis
from flask import Flask, render_template
import json
import ast


def json_retrieve(url_portal):
    '''This function retrieves the json response from the API url
        It will return none if the response is unsuccesful'''
    try:
        content = requests.get(url_portal).text
        failure = False
        content = json.loads(content)
        page = content["page"]
        content = content["results"]
        return content, page
    except:
        failure = True

####################################################### separate #######################################################
####################################################### separate #######################################################


urls = ['https://api.themoviedb.org/3/discover/movie?api_key=4cddaca15876165c4395177ea57cc102&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1',  # POPULAR MOVIES
        "https://api.themoviedb.org/3/trending/movie/week?api_key=4cddaca15876165c4395177ea57cc102",  # TRENDING MOVIES
        "https://api.themoviedb.org/3/movie/upcoming?api_key=4cddaca15876165c4395177ea57cc102&language=en-US&page=1"  # UPCOMING MOVIES
        ]

####################################################### separate #######################################################
####################################################### separate #######################################################


