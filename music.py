#!./env/Scripts/python
import argparse
from typing import Tuple
import yt_dlp as youtube_dl
from gooey import Gooey

@Gooey
def main():
    parser = argparse.ArgumentParser(description="Video/Audio downloader")
    parser.add_argument("link", help="link of the video/audio u want to download")
    parser.add_argument("--format", "-f", help="format of the video/audio u want to download", choices=["mp3", "mp4"])
    args = parser.parse_args()
    if args.format:
        downmusic(args.link, args.format)
    else:
        downmusic(args.link)

def downmusic(link, format="mp3"):
    if format == "mp3":
        format2 = "bestaudio/best"
        postprocessors = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ]
    elif format == "mp4":
        format2 = "best"
        postprocessors = [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",
            }
        ]
    ydl_opts = {
        "noplaylist": True,
        "format": format2,
        "outtmpl": "C:/Music/%(title)s.%(ext)s",
        "postprocessors": postprocessors,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])




if __name__ == "__main__":
    main()
