import module
from flask import Flask, render_template
from bs4 import BeautifulSoup


app = Flask(__name__)


@app.route('/')
def root():
    # a module will get all the json information form the site API and then it will be imported from a file
    # module.open_and_read
    return render_template(
        'index.html',
        poster = test_data["results"][0]["poster_path"],
    )


# html_content = module.portal_getter('')

if __name__ == "__main__":
    app.run(debug=True)
