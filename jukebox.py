
## jukebox.py
## 
##
##

import praw
import webbrowser
import os


def fetches_titles(reddit):
    '''
    This returns the titles of the music
    ## and the youtube is added to a LIST
    ## when the user requests it
    '''
    url_list = []
    n = 1
    for submission in reddit.subreddit('listentothis').new(limit=10):
        print(str(n) +' '+submission.title)
        url_list.append(submission.url)
        n += 1
    return url_list

def fetches_dic(reddit):
    '''
    this makes a dictionary
    of the song name as the key
    and the song url as the value
    through the first 10 post
    '''
    song_dic = dict() 
    n = 1
    for submission in reddit.subreddit('listentothis').new(limit=10):
        song_dic[n] = submission.url
        n += 1
    return song_dic

def play_music(url_list,song_dic):
    '''
    This loops through the url liust
    and starting with index 0 opens song link
    in google 
    the next song can be played on user input
    '''
    i = 0
    end_state = True
    print('-------------------------------------')
    while end_state:
        menu_start = input('choose a number to play a song:\n')
        if menu_start.isnumeric() == True:   
            webbrowser.open(song_dic[int(menu_start)])
        elif menu_start == 'stop':
            break
    
            
def main():
    reddit = praw.Reddit(client_id='sVRGjVMPWmQPGg',
                        client_secret='l9A7fN0i_mHHisvz1qaEMZh-NTY',
                        user_agent='tiger king',
                        username='music_tastes_good',
                        password="All4fun!@#$%^&")

    url_list = fetches_titles(reddit)
    song_dic = fetches_dic(reddit)
    print('-----------------------------------')
    print('NOW PLAYING:')
    play_music(url_list,song_dic)

main()