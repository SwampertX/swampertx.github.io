#!/usr/bin/python3.7

from datetime import date

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
    formatted = '-'.join([word.capitalize() for word in title.split()])
    filename = str(date.today()) + '---' + formatted + '.md'
    cfm = input("A new file, " + filename +" will be created. (Y/n)")
    if cfm.upper() != 'N':
        boilerplate = create_boilerplate(title, str(date.today()))
        with open(filename, 'w') as post:
            post.write(boilerplate)
        satisfied = True
        break

