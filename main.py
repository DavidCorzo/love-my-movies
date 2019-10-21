import module
from ast import literal_eval
import json
from flask import Flask, render_template
from bs4 import BeautifulSoup


app = Flask(__name__)

url_list = ['https://api.themoviedb.org/3/discover/movie?api_key=4cddaca15876165c4395177ea57cc102&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1']
# /discover/movie/?certification_country=US&certification=R&sort_by=vote_average.desc
# /discover/movie?api_key=4cddaca15876165c4395177ea57cc102&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1


def get_workable_data_for_html(url_list):
    responses = []
    for url in url_list:
        request_response = module.json_retrieve(url)
        responses.append(request_response)

    # TURN STRING FROM REQUESTS IN TO DICTIONARY
    D = json.loads(request_response)
    Instance = module.OpenAndProcessAFile()
    D = Instance.send_html_relevant_info(D)
    return D


master = get_workable_data_for_html(url_list)


def topfive(master_l):
    top_five = []
    counter = 0
    for elements in master_l:
        if counter != 5:
            top_five.append(master_l[counter])
            counter += 1
        else:
            break
    return top_five


@app.route('/')
def root():
    '''a module will get all the json information form the site API and then it will be imported from a file
    module.open_and_read'''
    master = get_workable_data_for_html(url_list)
    return render_template(
        'index.html',
        one_title=master[0]["original_title"],
        one_about=master[0]["overview"],
        one_vote=master[0]["vote_count"],
        one_img=master[0]["poster_path"],

        two_title=master[1]["original_title"],
        two_about=master[1]["overview"],
        two_vote=master[1]["vote_count"],
        two_img=master[1]["poster_path"],

        three_title=master[2]["original_title"],
        three_about=master[2]["overview"],
        three_vote=master[2]["vote_count"],
        three_img=master[2]["poster_path"],

        four_title=master[3]["original_title"],
        four_about=master[3]["overview"],
        four_vote=master[3]["vote_count"],
        four_img=master[3]["poster_path"],

        five_title=master[4]["original_title"],
        five_about=master[4]["overview"],
        five_vote=master[4]["vote_count"],
        five_img=master[4]["poster_path"],

        six_title=master[5]["original_title"],
        six_about=master[5]["overview"],
        six_vote=master[5]["vote_count"],
        six_img=master[5]["poster_path"],

        seven_title=master[6]["original_title"],
        seven_about=master[6]["overview"],
        seven_vote=master[6]["vote_count"],
        seven_img=master[6]["poster_path"],

        eight_title=master[7]["original_title"],
        eight_about=master[7]["overview"],
        eight_vote=master[7]["vote_count"],
        eight_img=master[7]["poster_path"],


        nine_title=master[8]["original_title"],
        nine_about=master[8]["overview"],
        nine_vote=master[8]["vote_count"],
        nine_img=master[8]["poster_path"],


        ten_title=master[9]["original_title"],
        ten_about=master[9]["overview"],
        ten_vote=master[9]["vote_count"],
        ten_img=master[9]["poster_path"],


        eleven_title=master[10]["original_title"],
        eleven_about=master[10]["overview"],
        eleven_vote=master[10]["vote_count"],
        eleven_img=master[10]["poster_path"],


        twelve_title=master[11]["original_title"],
        twelve_about=master[11]["overview"],
        twelve_vote=master[11]["vote_count"],
        twelve_img=master[11]["poster_path"],


        thireteen_title=master[12]["original_title"],
        thireteen_about=master[12]["overview"],
        thireteen_vote=master[12]["vote_count"],
        thireteen_img=master[12]["poster_path"],


        fourteen_title=master[13]["original_title"],
        fourteen_about=master[13]["overview"],
        fourteen_vote=master[13]["vote_count"],
        fourteen_img=master[13]["poster_path"],

        fifteen_title=master[14]["original_title"],
        fifteen_about=master[14]["overview"],
        fifteen_vote=master[14]["vote_count"],
        fifteen_img=master[14]["poster_path"],


        sixteen_title=master[15]["original_title"],
        sixteen_about=master[15]["overview"],
        sixteen_vote=master[15]["vote_count"],
        sixteen_img=master[15]["poster_path"],


        seventeen_title=master[16]["original_title"],
        seventeen_about=master[16]["overview"],
        seventeen_vote=master[16]["vote_count"],
        seventeen_img=master[16]["poster_path"]

    )


if __name__ == "__main__":
    app.run(debug=True)
