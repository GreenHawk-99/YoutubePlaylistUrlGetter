import os
import re

try:
    from pytube import Playlist
    from art import *
except ModuleNotFoundError:
    os.system('pip install pytube')
    os.system('pip install art')
tprint('Boki YTPUG', "alpha")
print('Boki Youtube Playlist Urls Getter')
print('Developed by GreenHawk with the help of this tutorial: https://www.youtube.com/watch?v=vuaApmJW6Yo')
print('------------------------------------------------')  # 48


# function to get urls from playlist
def get_playlist(playlists):
    url_list = []
    # get link one by one from playlist
    for playlist in playlists:
        playlist_urls = Playlist(playlist)
        # for each url add in the collection urls
        for url in playlist_urls:
            url_list.append(url)
    return url_list


regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)



url_input = input('Please enter a playlist url:\nIf you got multiple space them with a \'space\'\n')
# https://www.youtube.com/playlist?list=PLISIWpdFvjhMeuxvl3GAV3wgQFvaozzDZ https://www.youtube.com/playlist?list=OLAK5uy_karBuEpqUrxd6T2sMjgrt4AQVGUyezQho
# print(url_input)
url_given = url_input.split()
print(url_given)
print('------------------------')  # 24
# print(re.match(regex, "http://www.example.com") is not None)  # True
# print(re.match(regex, "example.com") is not None)  # False
# print(re.match(regex, "https://www.youtube.com/playlist?list=PLISIWpdFvjhMeuxvl3GAV3wgQFvaozzDZ") is not None)
# print(re.match(regex, "https://www.youtube.com/playlist?list=OLAK5uy_karBuEpqUrxd6T2sMjgrt4AQVGUyezQho") is not None)
# print(re.match(regex, "poop") is not None)

# playlist = ['https://www.youtube.com/playlist?list=PLISIWpdFvjhMeuxvl3GAV3wgQFvaozzDZ',
            #'https://www.youtube.com/playlist?list=OLAK5uy_karBuEpqUrxd6T2sMjgrt4AQVGUyezQho']
# pl_urls = get_playlist(playlist)


for url in url_given:
    if not re.match(regex, url):
        print('The input are not link')
    else:
        pl_urls = get_playlist(url_given)
        with open('YTPUG-MusicUrls.txt','w') as f:
            for url in pl_urls:
                f.write(url+'\n')
        print("File successfully created with the urls into "+os.getcwd())