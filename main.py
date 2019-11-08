from flask import Flask, render_template
import json
import requests
import modulize
import redis

app = Flask(__name__)


def get_relevant(urls):
    '''This function gets the votes calibrated on redis
    Aditionaly prepares all the data to be sent to the rendered index.html'''
    err = []

    Instance = modulize.CompleteManipulationOfData()
    trending = None
    popular = None
    upcoming = None

    counter = 0
    for url in urls:
        if counter == 0:
            try:
                popular = Instance.json_retrieve(url)[0]
            except:
                err.append(0.1)

        elif counter == 1:
            try:
                trending = Instance.json_retrieve(url)[0]
            except:
                err.append(0.2)

        elif counter == 2:
            try:
                upcoming = Instance.json_retrieve(url)[0]
            except:
                err.append(0.3)
        counter += 1

    return popular, trending, upcoming
    # Must create a redis server vote count
    # redis as cache
    r = redis.Redis(host='localhost', port=6379, db=0)
    try:
        # redis vote count
        for a in popular:
            for b in a.items():
                redis_popular = r.set(a['id'],a['vote_count'])
        for c in trending:
            for d in c.items():
                redis_trending = r.set(c['id'],c['vote_count'])
        for e in upcoming:
            for f in e.items():
                redis_upcoming = r.set(e['if'],e['vote_count'])
    except:
        print('Unable to get votes in to redis.')


r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def root():

    urls = ['https://api.themoviedb.org/3/discover/movie?api_key=4cddaca15876165c4395177ea57cc102&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1',  # POPULAR MOVIES
        "https://api.themoviedb.org/3/trending/movie/week?api_key=4cddaca15876165c4395177ea57cc102",  # TRENDING MOVIES
        "https://api.themoviedb.org/3/movie/upcoming?api_key=4cddaca15876165c4395177ea57cc102&language=en-US&page=1"  # UPCOMING MOVIES
        ]

    Master=get_relevant(urls)

    return render_template(
        'index.html',
        popular=Master[0],
        trending=Master[1],
        upcoming=Master[2]
        
    )






if __name__ == '__main__':
    app.run(debug=True)


