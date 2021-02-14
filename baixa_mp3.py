from pytube import YouTube
import re
import os
import pytube
from pytube.extract import playability_status



# link = input("Cole o link aqui: ")
# # path = input("onde deseja salvar o video? ")
# path = "C:/Users/Pichau/Desktop/_garbage/musica"
# yt = YouTube(link)

# print("começando...")
# # ys = yt.streams.filter(only_audio=True).first().download(path)
# ys = yt.streams.filter(only_audio=True).first().download(path)
# print('Download concluído')
# print('Sucesso!')

def carregaUnico():
    
    link = input("Cole o link aqui: ")
    # path = input("onde deseja salvar o video? ")
    path = "C:/Users/Pichau/Desktop/_garbage/musica"
    yt = YouTube(link)

    print("começando...")
    ys = yt.streams.filter(only_audio=True).first().download(path)
    print('Download concluído')
    print('Sucesso!')

def baixaUm():
  
    link = input("Cole o link aqui: ")
    # path = input("onde deseja salvar o video? ")
    path = "C:/Users/Pichau/Desktop/_garbage/musica"
    yt = YouTube(link)

    print("começando...")
    # ys = yt.streams.filter(only_audio=True).first().download(path)
    ys = yt.streams.filter(only_audio=False).first().download(path)
    ys = yt.streams.first().download(path)
    print('Download concluído')
    print('Sucesso!')


def main():
    carregaUnico()
    # baixaUm()

if __name__ == "__main__":
    main()