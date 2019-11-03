import requests
import redis
from flask import Flask, render_template
import json
import ast

####################################################### separate #######################################################
####################################################### separate #######################################################

class CompleteManipulationOfData():
    def __init__(self):
        pass

    def json_retrieve(self,url_portal):
        '''This function retrieves the json response from the API url
        It will return none if the response is unsuccesful
        !! RETURNS 1(RESULTS KEY) AND 2(PAGE NUMBER)'''
        try:
            content = requests.get(url_portal).text
            failure = False
            content = json.loads(content)
            page = content["page"]
            content = content["results"]
            return content, page
        except:
            failure = True
        
        return content,page

