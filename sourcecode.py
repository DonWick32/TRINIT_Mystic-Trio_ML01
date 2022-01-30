import requests
import string
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup
import tensorflow as tf
import nltk
import json
import numpy as np
import pandas as pd

def chatbot(query, index=0):
    global final
    final = ''
    defo = 'Sorry, no response available.'

    try:
        Search = list(search(query, tld="co.in", num=10, stop=3, pause=1))

        page = requests.get(Search[index])

        #tree = html.fromstring(page.content)

        soup = BeautifulSoup(page.content, features="lxml")

        text = ''
        article = soup.findAll('p')
        for element in article:
            text += '\n' + ''.join(element.findAll(text = True))
        text = text.replace('\n', '')
        sen = text.split('.')
        sen = sen[0].split('?')[0]

        chars = sen.translate(
            { ord(c): None for c in string.whitespace }
        )

        if len(chars) > 0:
           final  = sen
        else:
            final = defo
        return final
    except:
        if len(final) == 0: 
            final = defo
        return final
satisfaction = 0
count = 0
print("Welcome to COVID - 19 chat bot.")
satisfaction = 0
while (satisfaction != 1 and count <10) :
    query=input("Enter your query: ")
    print(chatbot(query))
    resp = 0
    while (resp != 1) :
        response = input("Are you satisfied with the response (Y/N)? ")
        if response.upper() == 'Y' :
            qu = 0
            while (qu != 1) :
                ggwp = input("Any more query (Y/N)? ")
                if ggwp.upper() == 'N':
                    satisfaction = 1
                    resp = 1
                    qu = 1
                    break
                elif ggwp.upper() == 'Y':
                    satisfaction = 0
                    resp = 1
                    qu = 1
                    break
                else :
                    print("Invalid input.")
                    satisfaction = 0
                    resp = 1
                    qu = 0
        elif response.upper() == 'N' :
                if count == 9:
                  count +=1
                  break
                print("Please rephrase your query.")
                count += 1
                satisfaction = 0
                resp = 1
                break
        else :
            print("Invalid input.")
            satisfaction = 0
            resp = 0
if count == 10 :
  print("Please visit a doctor.")
print("Thank you for using COVID - 19 chat bot.\nHave a good day!\nStay safe.")
