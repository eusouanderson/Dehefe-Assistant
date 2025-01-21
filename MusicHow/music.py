import os
from pytube import YouTube, Search
import pygame

def buscar_e_tocar_musica(musica):
    # Formata a música para pesquisa no YouTube
    musica_formatada = musica.replace(" ", "+")

    # Realiza a busca no YouTube e obtém os resultados
    search = Search(musica_formatada)
    video = search.results[0]  # Pega o primeiro vídeo da lista

    # Obtém a URL do primeiro vídeo
    video_url = video.watch_url

    # Baixa o áudio do vídeo
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    
    # Baixa o áudio para um arquivo temporário
    output_file = stream.download(filename='temp_audio.mp4')

    # Inicializa o pygame para reproduzir o áudio
    pygame.mixer.init()

    # Carrega o arquivo de áudio
    pygame.mixer.music.load(output_file)

    # Reproduz o áudio
    pygame.mixer.music.play()

    # Espera até a música terminar
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Remove o arquivo temporário após a reprodução
    os.remove(output_file)

# Exemplo de uso
musica = "Shape of You Ed Sheeran"
buscar_e_tocar_musica(musica)
