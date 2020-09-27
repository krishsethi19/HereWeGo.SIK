from datetime import datetime
from itertools import dropwhile, takewhile

import instaloader as insta 

L = insta.Instaloader()


posts=insta.Profile.from_username(L.context, "fabriziorom").get_posts()

SINCE = datetime(2020, 9, 25)
UNTIL = datetime(2020, 9, 27)
k=0
while (k<6) :
    for post in takewhile(lambda p: p.date < UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
       
        L.download_post(post, "instagram")
        k+=1
    SINCE=UNTIL
    UNTIL=datetime.datetime.now()



