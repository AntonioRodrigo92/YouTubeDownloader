import time

from moviepy.editor import *
from pytube import YouTube


def convert_files(input_dir, output_dir):
    for entry in os.scandir(input_dir.name):
        if (entry.path.endswith(".mp4")) and entry.is_file():
            print("Converting")
            mp4_to_mp3(entry.path, output_dir)
            print("Converting: Success")


def download_music(links, output_dir):
    for link in links:
        if is_valid_youtube_url(link):
            download_audio(link, output_dir)


def is_valid_path(path):
    return os.path.exists(path)


def download_audio(link, output_dir):
    yt = YouTube(link)
    try:
        audio = yt.streams.get_audio_only()
        print("Downloading " + audio.title)
        audio.download(output_dir.name)
        print("Success")
    except:
        print("ERRO na musica " + yt.title)


def mp4_to_mp3(input_audio_path, output_directory):
    input_audio = AudioFileClip(input_audio_path)
    output_name = get_output_file_name(input_audio.filename)
    input_audio.write_audiofile(output_directory + "\\" + output_name, verbose=False, logger=None)
    input_audio.close()


def get_output_file_name(file_name):
    name = os.path.basename(file_name).split('.')[0]
    return name + ".mp3"


def is_valid_youtube_url(url):
    return url.startswith("https://www.youtube.com/watch?v=")


class Downloader:
    def __init__(self, links, temp_dir, dest_dir, download_text, download_path_label):
        self.links = links
        self.temp_dir = temp_dir
        self.dest_dir = dest_dir
        self.download_text = download_text
        self.download_path_label = download_path_label

    def download(self):
        if is_valid_path(self.dest_dir):
            self.download_text.set("Downloading . . .")
            download_music(self.links, self.temp_dir)
            self.download_text.set("Converting Files . . .")
            convert_files(self.temp_dir, self.dest_dir)
            self.temp_dir.cleanup()
            print("FIM!")
        else:
            self.download_path_label.config(text="Select a valid path")
        self.download_text.set("Download")
