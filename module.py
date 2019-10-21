import requests
import ast
import json
import redis
import flask


def json_retrieve(url_portal):
    failiure = True
    while failiure:
        try:
            content = requests.get(url_portal).text
            failiure = False
        except:
            print(f"unable to get {url_portal}")
            content = None
            failiure = True

    return content


# https: // www.themoviedb.org/documentation/api


class OpenAndProcessAFile():
    def __init__(self):
        pass

    def open_and_categorize_json(self, filename):
        try:
            # r = redis.StrictRedis(host="localhost", port=0000,  # 6379
            #                       db=0, charset="utf-8", decode_responses=True)
            # with open(filename, mode='r', encoding="utf8") as data_file:
            #     test_data = json.load(data_file)
            #     r.set(filename, test_data)
            with open(filename, mode='r', encoding='utf8') as f:
                Master_Dict = json.load(f)
                return Master_Dict

        except Exception as e:
            print(f'An error occurred {e}')

    def send_html_relevant_info(self, Master_Dict):
        '''This method must be envoqued only if what will be proccessed in it is a dictionary'''
        for key, value in Master_Dict.items():
            # I MUST SEARCH FOR THE KEY CALLED "RESULTS"
            if str(key) == 'results':
                current_list = value
        return current_list

# Class = OpenAndProcessAFile()
# master = Class.open_and_categorize_json('discover_movies.json')
# Class.send_html_relevant_info(master)





# <div class="col-md-4">
    #     <h2>
    #       {{ two_title }}
    #     </h2>
    #     <img class="image_basic" src="{{ two_img }}" alt="">
    #     <button type="button" class="collapsible">About</button>
    #     <div class="content">
    #       <p>{{ two_about }} </p>
    #     </div>
    #     <i onclick="myFunction(this)" class="fa fa-thumbs-up"></i>
    #     voted: {{ two_vote }}
    #   </div>



    #   <div class="col-md-4">
    #     <h2>
    #       {{ three_title }}
    #     </h2>
    #     <img class="image_basic" src="{{ three_img }}" alt="">
    #     <button type="button" class="collapsible">About</button>
    #     <div class="content">
    #       <p>{{ three_about }} </p>
    #     </div>
    #     <i onclick="myFunction(this)" class="fa fa-thumbs-up"></i>
    #     voted: {{ three_vote }}
    #   </div>
    # </div>

    # <div class="row big-row">
    #   <div class="col-md-4">
    #     <h2>
    #       {{ four_title }}
    #     </h2>
    #     <img class="image_basic" src="{{ four_img }}" alt="">
    #     <button type="button" class="collapsible">About</button>
    #     <div class="content">
    #       <p>{{ four_about }} </p>
    #     </div>
    #     <i onclick="myFunction(this)" class="fa fa-thumbs-up"></i>
    #     voted: {{ four_vote }}
    #   </div>


    #   <div class="col-md-4">
    #     <h2>
    #       {{ five_title }}
    #     </h2>
    #     <img class="image_basic" src="{{ five_img }}" alt="">
    #     <button type="button" class="collapsible">About</button>
    #     <div class="content">
    #       <p>{{ five_about }} </p>
    #     </div>
    #     <i onclick="myFunction(this)" class="fa fa-thumbs-up"></i>
    #     voted: {{ five_vote }}
    #   </div>


    #   <div class="col-md-4">
    #   </div>
