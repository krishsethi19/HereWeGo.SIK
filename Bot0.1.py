from datetime import datetime
from itertools import dropwhile, takewhile
from instabot import Bot 
import os
import instaloader as insta
from post import PostRecent, getPhotoAndCaption,clear_folder


bot = Bot() 
bot.login(username ='HereWeGo.SIK',password = 'kis@164264') 

path = "/Users/Apple/Desktop/HereWeGo/instagram"

L = insta.Instaloader()


posts=insta.Profile.from_username(L.context, "fabriziorom").get_posts()

SINCE = datetime(2020, 9, 26)
UNTIL = datetime(2020, 9, 27)
k=0
while (k<50) :
    for post in takewhile(lambda p: p.date > SINCE, dropwhile(lambda p: p.date >UNTIL , posts)):
       
        L.download_post(post, "instagram")
        k+=1
    photo,caption=getPhotoAndCaption(path)
    PostRecent(photo,caption)
    clear_folder(path)
    
    SINCE=UNTIL
    UNTIL=datetime.datetime.now()



