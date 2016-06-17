import os
import json
from collections import Counter
import pandas as pd
from instagram.client import InstagramAPI

INSTAGRAM_ACCESS_TOKEN = ''
INSTAGRAM_CLIENT_ID = '85ab786c3c8d4334983c385cc92b9854'
INSTAGRAM_CLIENT_SECRET = '7690377ad88943caa99e98241874285a'

api = InstagramAPI(access_token=INSTAGRAM_ACCESS_TOKEN, client_id=INSTAGRAM_CLIENT_ID,client_secret=INSTAGRAM_CLIENT_SECRET)

def getNbLikes(listMedia):
    likes =0
    count =0
    for media in listMedia:
        likes = likes + media.like_count
        count = count + 1
    if count > 0:
        return likes/count
    else:
        return 0

def getTags(listMedia):
    tags = []
    for media in listMedia:
        for mediaTag in media.tags:
            tags.append(mediaTag.name)
    return Counter(tags)

def getMedia(locationId):
    medias =  api.location_recent_media(location_id=locationId)
    return medias[0]


bestLocations = [];
latD=48.858844
lonD=2.294351

for x in range(-10, 10):
    for z in range(-10,10):
        print(x,z)
        locations = api.location_search(lat=48.858844+x*0.001, lng=2.294351+z*0.001)
        for location in locations:
            likes = 0
            if not any(d['name'] == location.name for d in bestLocations):
                images = getMedia(location.id)
                likes = getNbLikes(images)
                tags = getTags(images)
                if len(images)>0 :
                    bestLocations.append(dict(name=location.name,latitude=location.point.latitude,longitude=location.point.longitude,likes=likes,tags=tags,id=location.id,nbrImages=len(images)))

finalData = pd.DataFrame.from_dict(bestLocations)
finalData.to_csv('instadata.csv', sep='\t', encoding='utf-8')
