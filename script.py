#!/usr/bin/env python

# Yoeri Nijs
# April, 2014
# GPL 3.0

import nltk, random, csv, sys
from nltk.corpus import names
from nltk.tokenize import word_tokenize
from text.classifiers import NaiveBayesClassifier
from text.blob import TextBlob

def selectTweets(row):
    tweetWords = []
    words = row[0].split()
    for i in words:
        i = i.lower()
        i = i.strip('@#\'"?,.!')
        tweetWords.append(i)
    row[0] = tweetWords

    if counter <= 499:
        trainTweets.append(row)
    else:
        testTweets.append(row)

trainTweets = []
testTweets = []


print "Tweet Sentiment Analyzer by Yoeri Nijs"
print "*" * 30


while True:
    
    # Ask for filename
    filename =  str(raw_input("> Please enter a filename (.csv): "))
    
    #Check if filename ends with .csv
    if filename.endswith(".csv"):
        
        try:
            
            #Open file
            with open(filename, 'rb') as csvfile: 
                reader = csv.reader(csvfile, delimiter=';', quotechar='|')
                
                #Print succes message
                print "> File opened successfully!"
                
                counter = 0
                for row in reader:
                    selectTweets(row)
                    counter += 1
                    
                print "> Wait a sec for the results..."
                    
                cl = NaiveBayesClassifier(trainTweets)
                
                print("Accuracy of the classifier: {0}".format(cl.accuracy(testTweets)))
                cl.show_informative_features(10)
                
                while True:
                
                    tweetWords = []
                    tweet =  str(raw_input("Please enter the text of the tweet you want to analize: "))
                    words = tweet.split()
                    for i in words:
                        i = i.lower()
                        i = i.strip('@#\'"?,.!')
                        tweetWords.append(i)
                    tweet = ' '.join(tweetWords)
                    print "> Analyzing the tweet"
                    
                    # Classify some text
                    print "Sentiment of the tweet:", (cl.classify(tweet))
                    
                    while True:
                        print
                        repeat =  str(raw_input("> Do you want to check another tweet (y/n)? "))
                        
                        if repeat == "n":
                            print "Exit program"
                            sys.exit()
                        if repeat != "y":
                            print "Something went wrong"
                        if repeat == "y":
                            break         
                
        #If file does not exist, display this
        except IOError:
            print "File does not exist."
            
    #Else if file does not end with .csv, do this
    else:
        print "Please open a file that ends with .csv"
