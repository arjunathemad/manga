#! python3
# shingeki.py - Download every single shingeki no kyojin comic

import requests, os, bs4, webbrowser
import pyinputplus as pyip

url = 'https://ww7.readsnk.com/chapter/shingeki-no-kyojin-chapter-'


def chapter_request():
    chapter = input("Please enter the chapter number you would like to read (ex: 001 = chapter 1): ")
    newUrl = url + chapter
    return newUrl

def get_chapter():
    while True:
        user_choice = pyip.inputYesNo(prompt='Would you like to download this manga?: ')
        if user_choice == 'yes':
            res = requests.get(chapter_request())
            res.raise_for_status()
            playfile = open('shingekinokyojin.jpg', 'wb')
        else:

            webbrowser.open(chapter_request())


chapter_request()
get_chapter()





















