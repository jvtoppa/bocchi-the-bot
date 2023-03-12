import time
import tweepy
import random
from pathlib import Path
import os

s1 = os.environ['OAuth1']
s2 = os.environ['OAuth2']
s3 = os.environ['OAuth3']
s4 = os.environ['OAuth4']

auth = tweepy.OAuth1UserHandler(
   s1, s2, s3, s4
)

api = tweepy.API(auth)

while True:
    #abre letras
    ep = random.randint(1,12)
    frame = random.randint(1, 137)

    path = Path("ep" + str(ep) + "\\frame (" + str(frame) + ")")
    while path.is_file() == False:
        
        ep = random.randint(1,12)
        frame = random.randint(1, 137)

        path = Path("ep" + str(ep) + "\\frame (" + str(frame) + ").jpg")

    

    media = api.media_upload(path)
    post_result = api.update_status(status='Bocchi the Rock! Episódio ' + str(ep) + ".", media_ids=[media.media_id])
    #espera uma hora (aparece no console)
    for i in reversed(range(1,3600)):

        print(f"{i}   ", end="\r", flush=True)
        time.sleep(1)

    
