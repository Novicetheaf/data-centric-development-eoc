import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/add_reviews')
def add_reviews():
    return render_template("add-reviews.html")


@app.route('/reviews')
def reviews():
    return render_template("reviews.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
