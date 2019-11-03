import module
from ast import literal_eval
import json
from flask import Flask, render_template
from redis import Redis


app = Flask(__name__)


# /discover/movie/?certification_country=US&certification=R&sort_by=vote_average.desc
# /discover/movie?api_key=4cddaca15876165c4395177ea57cc102&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1


def get_workable_data_for_html(url):
    try:
        request_response = module.json_retrieve(url)
    except Exception as e:
        print(f"Unable to get the response {e}")
    # TURN STRING FROM REQUESTS IN TO DICTIONARY
    D = json.loads(request_response)
    Instance = module.OpenAndProcessAFile()
    D = Instance.send_html_relevant_info(D)
    return D


def topfive(master_l):
    top_five = []
    counter = 0
    for elements in master_l:
        if counter != 7:
            top_five.append(master_l[counter])
            counter += 1
        else:
            break
    return top_five


@app.route('/')
def root():
    '''a module will get all the json information form the site API and then it will be imported from a file
    module.open_and_read'''
    url_popularity = 'https://api.themoviedb.org/3/discover/movie?api_key=4cddaca15876165c4395177ea57cc102&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1'
    url_trending = "https://api.themoviedb.org/3/trending/movie/week?api_key=4cddaca15876165c4395177ea57cc102"
    url_upcoming = "https://api.themoviedb.org/3/movie/upcoming?api_key=4cddaca15876165c4395177ea57cc102&language=en-US&page=1"
    master_p = get_workable_data_for_html(url_popularity)
    master_t = get_workable_data_for_html(url_trending)
    master_u = get_workable_data_for_html(url_upcoming)

    return render_template(
        'index.html',
        one_title=master_p[0]["original_title"],
        one_about=master_p[0]["overview"],
        one_vote=master_p[0]["vote_count"],
        one_img=master_p[0]["poster_path"],

        two_title=master_p[1]["original_title"],
        two_about=master_p[1]["overview"],
        two_vote=master_p[1]["vote_count"],
        two_img=master_p[1]["poster_path"],

        three_title=master_p[2]["original_title"],
        three_about=master_p[2]["overview"],
        three_vote=master_p[2]["vote_count"],
        three_img=master_p[2]["poster_path"],

        four_title=master_p[3]["original_title"],
        four_about=master_p[3]["overview"],
        four_vote=master_p[3]["vote_count"],
        four_img=master_p[3]["poster_path"],

        five_title=master_p[4]["original_title"],
        five_about=master_p[4]["overview"],
        five_vote=master_p[4]["vote_count"],
        five_img=master_p[4]["poster_path"],

        six_title=master_p[5]["original_title"],
        six_about=master_p[5]["overview"],
        six_vote=master_p[5]["vote_count"],
        six_img=master_p[5]["poster_path"],

        seven_title=master_t[6]["original_title"],
        seven_about=master_t[6]["overview"],
        seven_vote=master_t[6]["vote_count"],
        seven_img=master_t[6]["poster_path"],

        eight_title=master_t[7]["original_title"],
        eight_about=master_t[7]["overview"],
        eight_vote=master_t[7]["vote_count"],
        eight_img=master_t[7]["poster_path"],


        nine_title=master_t[8]["original_title"],
        nine_about=master_t[8]["overview"],
        nine_vote=master_t[8]["vote_count"],
        nine_img=master_t[8]["poster_path"],


        ten_title=master_t[9]["original_title"],
        ten_about=master_t[9]["overview"],
        ten_vote=master_t[9]["vote_count"],
        ten_img=master_t[9]["poster_path"],


        eleven_title=master_t[10]["original_title"],
        eleven_about=master_t[10]["overview"],
        eleven_vote=master_t[10]["vote_count"],
        eleven_img=master_t[10]["poster_path"],


        twelve_title=master_u[11]["original_title"],
        twelve_about=master_u[11]["overview"],
        twelve_vote=master_u[11]["vote_count"],
        twelve_img=master_u[11]["poster_path"],


        thireteen_title=master_u[12]["original_title"],
        thireteen_about=master_u[12]["overview"],
        thireteen_vote=master_u[12]["vote_count"],
        thireteen_img=master_u[12]["poster_path"],


        fourteen_title=master_u[13]["original_title"],
        fourteen_about=master_u[13]["overview"],
        fourteen_vote=master_u[13]["vote_count"],
        fourteen_img=master_u[13]["poster_path"],

        fifteen_title=master_u[14]["original_title"],
        fifteen_about=master_u[14]["overview"],
        fifteen_vote=master_u[14]["vote_count"],
        fifteen_img=master_u[14]["poster_path"],


        sixteen_title=master_u[15]["original_title"],
        sixteen_about=master_u[15]["overview"],
        sixteen_vote=master_u[15]["vote_count"],
        sixteen_img=master_u[15]["poster_path"],


        seventeen_title=master_u[16]["original_title"],
        seventeen_about=master_u[16]["overview"],
        seventeen_vote=master_u[16]["vote_count"],
        seventeen_img=master_u[16]["poster_path"]

    )


if __name__ == "__main__":
    app.run(debug=True)
