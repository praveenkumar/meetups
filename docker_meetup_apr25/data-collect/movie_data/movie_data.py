#!/usr/bin/env python
'''Flask Application for Movie data'''

from flask import Flask
from flask import request, render_template, flash
from movielib import get_movie_data, write_movie_data
APP = Flask(__name__)
APP.config.update(dict(SECRET_KEY='development',
                       DOWNLOAD_LOCATION='/data/html'))
APP.config.from_envvar('MOVIE_SETTINGS', silent=True)


@APP.route('/')
def hello_world():
    return render_template('submit_movie_data.html')


@APP.route('/add_movie', methods=['POST', 'GET'])
def add_movie():
    if request.method == 'POST':
        movie_data = get_movie_data(request.form['title'],
                                    request.form['plot'],
                                    'http://www.omdbapi.com')
        write_movie_data(request.form['title'],
                         movie_data, APP.config['DOWNLOAD_LOCATION'])
    flash('New entry successfully added')
    return hello_world()


if __name__ == '__main__':
    APP.run(host='0.0.0.0', debug=True)
