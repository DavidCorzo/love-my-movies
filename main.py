import module
from ast import literal_eval
import json
from flask import Flask, render_template
from bs4 import BeautifulSoup
from redis import Redis


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


# r = Redis(host='redis', port=6379, db=0)


# r.set("one_title", master[0]["original_title"])
# r.set("one_about", master[0]["overview"])
# r.set("one_vote", master[0]["vote_count"])
# r.set("one_img", master[0]["poster_path"])

# r.set("two_title", master[1]["original_title"])
# r.set("two_about", master[1]["overview"])
# r.set("two_vote", master[1]["vote_count"])
# r.set("two_img", master[1]["poster_path"])

# r.set("three_title", master[2]["original_title"])
# r.set("three_about", master[2]["overview"])
# r.set("three_vote", master[2]["vote_count"])
# r.set("three_img", master[2]["poster_path"])

# r.set("four_title", master[3]["original_title"])
# r.set("four_about", master[3]["overview"])
# r.set("four_vote", master[3]["vote_count"])
# r.set("four_img", master[3]["poster_path"])

# r.set("five_title", master[4]["original_title"])
# r.set("five_about", master[4]["overview"])
# r.set("five_vote", master[4]["vote_count"])
# r.set("five_img", master[4]["poster_path"])

# r.set("six_title", master[5]["original_title"])
# r.set("six_about", master[5]["overview"])
# r.set("six_vote", master[5]["vote_count"])
# r.set("six_img", master[5]["poster_path"])

# r.set("seven_title", master[6]["original_title"])
# r.set("seven_about", master[6]["overview"])
# r.set("seven_vote", master[6]["vote_count"])
# r.set("seven_img", master[6]["poster_path"])

# r.set("eight_title", master[7]["original_title"])
# r.set("eight_about", master[7]["overview"])
# r.set("eight_vote", master[7]["vote_count"])
# r.set("eight_img", master[7]["poster_path"])


# r.set("nine_title", master[8]["original_title"])
# r.set("nine_about", master[8]["overview"])
# r.set("nine_vote", master[8]["vote_count"])
# r.set("nine_img", master[8]["poster_path"])


# r.set("ten_title", master[9]["original_title"])
# r.set("ten_about", master[9]["overview"])
# r.set("ten_vote", master[9]["vote_count"])
# r.set("ten_img", master[9]["poster_path"])


# r.set("eleven_title", master[10]["original_title"])
# r.set("eleven_about", master[10]["overview"])
# r.set("eleven_vote", master[10]["vote_count"])
# r.set("eleven_img", master[10]["poster_path"])


# r.set("twelve_title", master[11]["original_title"])
# r.set("twelve_about", master[11]["overview"])
# r.set("twelve_vote", master[11]["vote_count"])
# r.set("twelve_img", master[11]["poster_path"])


# r.set("thireteen_title", master[12]["original_title"])
# r.set("thireteen_about", master[12]["overview"])
# r.set("thireteen_vote", master[12]["vote_count"])
# r.set("thireteen_img", master[12]["poster_path"])


# r.set("fourteen_title", master[13]["original_title"])
# r.set("fourteen_about", master[13]["overview"])
# r.set("fourteen_vote", master[13]["vote_count"])
# r.set("fourteen_img", master[13]["poster_path"])

# r.set("fifteen_title", master[14]["original_title"])
# r.set("fifteen_about", master[14]["overview"])
# r.set("fifteen_vote", master[14]["vote_count"])
# r.set("fifteen_img", master[14]["poster_path"])


# r.set("sixteen_title", master[15]["original_title"])
# r.set("sixteen_about", master[15]["overview"])
# r.set("sixteen_vote", master[15]["vote_count"])
# r.set("sixteen_img", master[15]["poster_path"])


# r.set("seventeen_title", master[16]["original_title"])
# r.set("seventeen_about", master[16]["overview"])
# r.set("seventeen_vote", master[16]["vote_count"])
# r.set("seventeen_img", master[16]["poster_path"])


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

        # r.get("one_title")
        # r.set("one_about")
        # r.set("one_vote")
        # r.set("one_img")

        # r.get("two_title")
        # r.get("two_about")
        # r.get("two_vote")
        # r.get("two_img")

        # r.get("three_title")
        # r.get("three_about")
        # r.get("three_vote")
        # r.get("three_img")

        # r.get("four_title")
        # r.get("four_about")
        # r.get("four_vote")
        # r.get("four_img")

        # r.get("five_title")
        # r.get("five_about")
        # r.get("five_vote")
        # r.get("five_img")

        # r.get("six_title")
        # r.get("six_about")
        # r.get("six_vote")
        # r.get("six_img")

        # r.get("seven_title")
        # r.get("seven_about")
        # r.get("seven_vote")
        # r.get("seven_img")

        # r.get("eight_title")
        # r.get("eight_about")
        # r.get("eight_vote")
        # r.get("eight_img")


        # r.get("nine_title")
        # r.get("nine_about")
        # r.get("nine_vote")
        # r.get("nine_img")


        # r.get("ten_title")
        # r.get("ten_about")
        # r.get("ten_vote")
        # r.get("ten_img")


        # r.get("eleven_title")
        # r.get("eleven_about")
        # r.get("eleven_vote")
        # r.get("eleven_img")


        # r.get("twelve_title")
        # r.get("twelve_about")
        # r.get("twelve_vote")
        # r.get("twelve_img")


        # r.get("thireteen_title")
        # r.get("thireteen_about")
        # r.get("thireteen_vote")
        # r.get("thireteen_img")


        # r.get("fourteen_title")
        # r.get("fourteen_about")
        # r.get("fourteen_vote")
        # r.get("fourteen_img")

        # r.get("fifteen_title")
        # r.get("fifteen_about")
        # r.get("fifteen_vote")
        # r.get("fifteen_img")


        # r.get("sixteen_title")
        # r.get("sixteen_about")
        # r.get("sixteen_vote")
        # r.get("sixteen_img")


        # r.get("seventeen_title")
        # r.get("seventeen_about")
        # r.get("seventeen_vote")
        # r.get("seventeen_img")

    )


if __name__ == "__main__":
    app.run(debug=True)
