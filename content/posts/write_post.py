#!/usr/bin/python3.7

from datetime import date
import string

satisfied = False

def quote(string):
    return '"' + string + '"'

def create_boilerplate(title, date):
    lower_dash_title = title.lower().replace(' ', '-')
    lines = ['---\n',
             'title: ' + quote(title) + '\n',
             'date: ' + quote(date) + '\n',
             'template: "post"\ndraft: true\n',
             'slug: "/posts/' + lower_dash_title + '"\n',
             'category: \ntags: \n' + (' - \n' * 3),
             'description: \n---\n']
    boilerplate = ''
    for line in lines:
        boilerplate += line
    return boilerplate

while not satisfied:
    title = input("Create a post title: (Eg. 'Why you should stop using Chrome NOW')\n")
    WORDS = [word.capitalize() for word in title.split() if not word in string.punctuation]
    FORMATTED = '-'.join(WORDS)
    filename = str(date.today()) + '---' + FORMATTED + '.md'
    cfm = input("A new file, " + filename +" will be created. (Y/n)")
    if cfm.upper() != 'N':
        boilerplate = create_boilerplate(title, str(date.today()))
        with open(filename, 'w') as post:
            post.write(boilerplate)
        satisfied = True
        break

