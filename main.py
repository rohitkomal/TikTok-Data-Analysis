from asyncio.windows_events import NULL
import pandas as pd
import numpy as np
from TikTokApi import TikTokApi


api = TikTokApi(custom_verify_fp="https://www.youtube.com/watch?v=-uCt1x8kINQ")
for trending_video in api.trending.videos(count=50):
    # Prints the author's username of the trending video.
    print(trending_video.author.username)
# Watch https://www.youtube.com/watch?v=-uCt1x8kINQ for a brief setup tutorial
def callAPI():
    for trending_video in api.trending.videos(count=50):
        # Prints the author's username of the trending video.
        print(trending_video.author.username)

print('Hello wok')

videos = api.trending.videos(count=50)
print(videos)
for v in videos:
    print(v)