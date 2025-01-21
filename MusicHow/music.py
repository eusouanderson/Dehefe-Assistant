import yt_dlp
import os
import time

# Caminho absoluto do diretório onde o script está sendo executado
path = os.path.abspath(os.path.dirname(__file__))
print(f"Caminho atual: {path}")

def buscar_e_tocar_musica(musica):
    # Configurações do yt-dlp para baixar o áudio
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioquality': 1,
        'outtmpl': os.path.join(path, 'temp_audio.%(ext)s'),  # Salva o arquivo no diretório atual
        'quiet': False
    }

    # Realiza a busca no YouTube com yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_url = f"ytsearch:{musica}"
        info_dict = ydl.extract_info(search_url, download=True)
        video_url = info_dict['entries'][0]['url']

    # O nome do arquivo baixado (considerando a extensão correta)
    audio_file = os.path.join(path, 'temp_audio.webm')  # Caminho absoluto do arquivo baixado

    # Tenta abrir o arquivo de áudio no app Filmes e TV
    os.system(f"powershell Start-Process 'ms-windows-store://pdp/?PFN=Microsoft.ZuneMusic_8wekyb3d8bbwe'")

    # Aguardar um pouco para garantir que o app seja aberto
    time.sleep(2)

    # Usar o app Filmes e TV para reproduzir o áudio
    os.system(f"start microsoft.microsoftmusic:{audio_file}")

    # Limpa o arquivo temporário após reprodução
    os.remove(audio_file)

    print("Música tocando...")

# Exemplo de uso
musica = "Shape of You Ed Sheeran"
buscar_e_tocar_musica(musica)
