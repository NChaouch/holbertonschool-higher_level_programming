#!/usr/bin/python3

"""
define prototypes and import
"""


import requests
import csv


def fetch_and_print_posts():

    """
    code
    """


# get posts from API
    url = 'https://jsonplaceholder.typicode.com/posts'
    resp = requests.get(url)  # send HTTP requests to API
    print(f'Status Code:', resp.status_code)
    if resp.status_code == 200:
        posts = resp.json()
        for post in posts:
            print(post.get('title'))


# get same posts and save in file csv
def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    resp = requests.get(url)
    if resp.status_code == 200:
        posts = resp.json()
        data_post = []
        for post in posts:
            data_post.append({
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            })

        with open('posts.csv', 'w', newline='') as f:
            # csv.DictWriter for write recovered data to a CSV file
            w = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            w.writeheader()
            w.writerows(data_post)
