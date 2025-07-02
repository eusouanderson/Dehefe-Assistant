import os

import playsound
import yt_dlp


class MusicPlayer:
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(__file__))
        self.temp_audio_filename = 'temp_audio.mp3'  # vamos forçar mp3
        print(f'Caminho atual: {self.path}')

    def buscar_e_tocar_musica(self, musica: str):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(self.path, 'temp_audio.%(ext)s'),
            'quiet': True,
            'postprocessors': [],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            search_url = f'ytsearch:{musica}'
            ydl.extract_info(search_url, download=True)

        audio_file = os.path.join(self.path, self.temp_audio_filename)

        try:
            playsound.playsound(audio_file)
        except Exception as e:
            print(f'Erro ao tocar áudio: {e}')

        # Remove arquivo temporário
        if os.path.exists(audio_file):
            os.remove(audio_file)

        print('Música tocando...')


if __name__ == '__main__':
    player = MusicPlayer()
    player.buscar_e_tocar_musica('Shape of You Ed Sheeran')
