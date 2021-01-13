
## jukebox.py
## 
##
##

import praw
import os
import json
import requests
from secret import spotify_token,spotify_user_id


def search_music(tmp_title,tmp_artist):
    '''
        search for music using the artist and title
    '''

    foo = '%20'
    title = foo.join(tmp_title)
    artist = foo.join(tmp_artist)

    query = 'https://api.spotify.com/v1/search?q=track:'+title+'%20artist:'+artist+'&type=track'.format(
        title,
        artist
    )
    response = requests.get(
        query,
        headers={
            "content-type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        }
    )

    response_json = response.json()
    songs = response_json["tracks"]["items"]
    uri = songs[0]["uri"]
            
    return uri  

def add_to_queue(song_id):
    '''
        adds the songs to the queue
    '''
    query = 'https://api.spotify.com/v1/me/player/queue?uri='+song_id.format(song_id)
    response = requests.post(
        query,
        headers={
            "content-type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        }
    )


def main():
    '''
        This returns the titles of the music
    '''
    reddit = praw.Reddit(client_id='sVRGjVMPWmQPGg',
                        client_secret='l9A7fN0i_mHHisvz1qaEMZh-NTY',
                        user_agent='tiger king',
                        username='music_tastes_good',
                        password="All4fun!@#$%^&")
    
    title_list = []
    n = 1
    for submission in reddit.subreddit('listentothis').new(limit=20):
        print(str(n) +' '+submission.title)

        temp = submission.title.split()
        for i in temp:
            if '[' in i:
                num = temp.index(i)
        if '--' in temp:
            tmp_title = temp[temp.index('--')+1:num]
            tmp_artist = temp[:temp.index('--')]
        elif '—' in temp:
            tmp_title = temp[temp.index('—')+1:num]
            tmp_artist = temp[:temp.index('—')]
        elif '-' in temp:
            tmp_title = temp[temp.index('-')+1:num]
            tmp_artist = temp[:temp.index('-')]
        try:    
            uri = search_music(tmp_title,tmp_artist)
        except:
            continue

        title_list.append(uri)
        n += 1 

    for i in title_list:
        add_to_queue(i)


main()
