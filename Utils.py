from pytube import YouTube


def download_audio(link, output_dir):
    yt = YouTube(link)
    audio = yt.streams.get_audio_only()
    print("Downloading " + audio.title)
    audio.download(output_dir)
    print("Success")


def download_video(link, output_dir):
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()
    print("Downloading " + video.title)
    video.download(output_dir)
    print("Success")


def is_valid_youtube_url(url):
    return url.startswith("https://www.youtube.com/watch?v=")
