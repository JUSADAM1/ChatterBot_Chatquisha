# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 13:19:55 2019

@author: justy
"""
# importing textblob so the program and analyse
from textblob import TextBlob

#USER DIRECTION
print("HELLO USER!! Please  enter whatever you want so your text can be analyzed. ")
print("If polarity is greater than 0 then it is positive")
print("If polarity is less than 0 then it is negative")
print("if polarity is just 0 then it is neutral")
# User must input text to be analyse.
text_analyser = input("Please input text to be analyzed:")

#Here is where it prints what the user typed in
print(text_analyser)

# here is where textblob starts to analyse what the user entered
AI_analysis = TextBlob(text_analyser)

# Print Analysis of text
print(AI_analysis.sentiment)