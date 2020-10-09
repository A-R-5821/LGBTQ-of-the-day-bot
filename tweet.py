'''
tweet.py: post tweets to twitter.com
11 September 2020
Vicki Langer (@vicki_langer)
'''

import tweepy
import time
import random 

import os.path
from os import environ

from get_tweet import get_tweet
# from get_reply import get_reply


consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']


#Empty array, will contain image names to post
arr=[]

# def get_img_random():
#     no=0
#     while(True):
#         if(os.path.exists('post_'+str(no)+'.png')):
#             return 'post_'+str(no)+'.png'
#         else:
#             continue

def getlist_linear():
    for i in range(100):
        if(os.path.exists('post_'+str(i)+'.png')):
            #add filename{no} to array if exists
            arr.append('post_'+str(i)+'.png')
        if(os.path.exists('post_'+str(i)+'a.png')):
            #add filename{no+'a'} to array if exists
            arr.append('post_'+str(i)+'a.png')
        
def authenticate_api():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return tweepy.API(auth)
    except Exception as error:
        print(f"An error occurred when attempting to authenticate with the twitter API. reason: {error}")



def main():
    api = authenticate_api()
    #reply_with = get_reply()

    # print("finding a tweet...")
    # tweet = get_tweet()
    # print("chose tweet: " + tweet)

    #get_tweet() is now done by generateImagePost.py, so the above won't be required

    #chose a random image from the array of linearly scanned files
    img = random.choice(arr)

    #Image removed from the array to avoid tweeting the same image
    arr.remove(img)

    #To just upload the generated image:
    tweet = api.update_with_media(img)  # variable used later for reply to this tweet
    print('tweet has been tweeted')
    #api.update_status(status=reply_with, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
    #print('chose reply:' + reply_with)
    #print('reply has been tweeted')
    
def run():
    
    #initializes the arr array containing names of existing post images
    getlist_linear()
    if len(arr)==0:
        print(f'No postable image(s) found in the directory - {os.getcwd()}')
        print('Make sure image(s) with appropriate naming syntax exists!')
        return
        
    #posts all the images scanned
    for i in range(len(arr)):
        main()
        #sleep for an hr before posting next image
        time.sleep(3600)
        
    #Pre-program-end msg
    print('Used up all the images scanned. Generate more images and recall the function/program')

run()
