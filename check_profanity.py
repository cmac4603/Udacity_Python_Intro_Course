import urllib

def read_text():
    quotes = open("/Users/colinmacrae/Documents/Programming/1. Udacity Programming Foundations with Python/movie_quotes.txt")
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Motherfucker just swore!")
    elif "false" in output:
        print("This document is clean!")
    else:
        print("Something went wrong...")

read_text()
