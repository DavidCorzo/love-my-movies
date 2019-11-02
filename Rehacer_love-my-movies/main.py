from flask import Flask, render_template
import json
import ast
import requests


app = Flask(__name__)


@app.route('/')
def root():
    return render_template(
        'index.html'
    )
