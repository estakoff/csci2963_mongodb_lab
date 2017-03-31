from pymongo import MongoClient
import random
import time
client = MongoClient()


def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    db = client.csci2963.definitions
    allWords = db.find()
   # randPost = random.randint(0, len(allWords))
    i = 0
    for post in allWords:
        i+=1
    randPost = random.randint(0, i)
    i = 0
    foundPost = db.find_one()
    allWords = db.find()
    for post in allWords:
        if i == randPost:
           print "yay"
           foundPost = post
           break 
        i+=1
   
    return foundPost


if __name__ == '__main__':
    a = random_word_requester()
    print a
    t = time.time()
    db.update(a, "dates": t)
    print a
