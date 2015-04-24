#!/usr/bin/env python
'''Get movie data from OMDB api and store it in html file'''

import argparse
import os
import requests
from json2html import json2html


def generate_html(json_data):
    '''Convert json to html'''
    generated_html = json2html.convert(json=json_data)
    return generated_html.encode('utf-8')


def get_movie_data(movie_name, plot, api_url):
    '''Pull movie data from OMDB API'''
    payloads = {'t': movie_name, 'plot': plot}
    try:
        r_response = requests.get(api_url, params=payloads)
    except requests.exceptions.ConnectionError as err:
        err.message = 'Not able to connect to API server'
        raise
    return generate_html(r_response.json())


def write_movie_data(movie_name, movie_data, path):
    '''Write html data to file with given title'''
    if not os.path.isdir(path):
        os.makedirs(path)
    with open('%s/%s.html' % (path, movie_name), 'w') as file_handler:
        file_handler.write(movie_data)


def main():
    '''main method'''
    parser = argparse.ArgumentParser(description='Process movie data')
    parser.add_argument('movie_name', help='Name of the movie')
    parser.add_argument('--plot', help='options:short, full', default='short')
    parser.add_argument('--api_url', help='API url to make requests',
                        default='http://www.omdbapi.com')
    parser.add_argument('--path', help='Path to write movie data html file',
                        default='/data/html')
    args = parser.parse_args()
    movie_data = get_movie_data(args.movie_name, args.plot, args.api_url)
    write_movie_data(args.movie_name, movie_data, args.path)

if __name__ == '__main__':
    main()
