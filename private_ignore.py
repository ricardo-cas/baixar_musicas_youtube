from pytube import Playlist
from pytube.exceptions import VideoPrivate
from pytube import *
from pytube.extract import playability_status

path = "C:/Users/Pichau/Desktop/_garbage/musica/private_ignore"
playlist_url = 'https://www.youtube.com/playlist?list=PLShWV96y1kqsu-7QEaalwGDkn-Jel1G5X'
# yt = YouTube('https://www.youtube.com/watch?v=BPhvbIuq7uM&t=158s&ab_channel=DreamDevelopers')

my_playlist = Playlist(playlist_url)


# p = Playlist(playlist_url)

# Lista as urls da Playlist
# for url in p.video_urls:
#     print(url)


print(my_playlist)
for video in my_playlist.videos:
    try:
        # Download each video individually here, e.g. like this:
        video.streams.first().download(path)
        # or try follow the other examples in the documentation
    except VideoPrivate:  # skip private videos
        continue