from pathlib import Path
from shutil import which
import yt_dlp

BASE_DIR = Path(__file__).resolve().parent
VIDEO_DIR = BASE_DIR / "video"

FFMPEG_PATH = which("ffmpeg")

def proximo_nome_video():
    VIDEO_DIR.mkdir(exist_ok=True)

    numeros = []
    for arquivo in VIDEO_DIR.glob("*.mp4"):
        if arquivo.stem.isdigit():
            numeros.append(int(arquivo.stem))

    return max(numeros) + 1 if numeros else 1

def baixar_video(url):
    numero = proximo_nome_video()
    caminho_saida = VIDEO_DIR / f"{numero}.%(ext)s"

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": str(caminho_saida),
        "noplaylist": True,
    }

    if FFMPEG_PATH:
        ydl_opts["ffmpeg_location"] = FFMPEG_PATH

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"Vídeo baixado com sucesso: {VIDEO_DIR / f'{numero}.mp4'}")

    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")

if __name__ == "__main__":
    url = input("Cole a URL do vídeo do YouTube: ").strip()
    baixar_video(url)