import pytube
from pytube import Playlist

# link = input('Qual o link da playlist? ')
link = 'https://www.youtube.com/playlist?list=PLShWV96y1kqsu-7QEaalwGDkn-Jel1G5X'
p = Playlist(link)

caminho = "C:/Users/Pichau/Desktop/_garbage/musica/MarilhaMendonça/" + input('Qual albúm? ')

print(f'Baixando Playlist: {p.title}')
print(f'A Playlist contem: {len(p)} para baixar')

lista_videos = []
for video in p.videos:
    # Pega a melhor resolução que existe do vídeo
    # video.streams.get_highest_resolution().download(caminho)
    print(f'Baixando:  {video.title}')
    video.streams.first().download(caminho)
    lista_videos.append(video.title)

print(lista_videos)

