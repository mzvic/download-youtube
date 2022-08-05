import pytube
import sys
#upgrade certifi

def mp4():
    yt = pytube.YouTube(url)
    print(f"Title: {yt.title}")
    print(f"Author: {yt.author}")
    stream = yt.streams.get_highest_resolution()
    print("Downloading...")
    stream.download()
    print("Download complete!")
    exit(0)
def mp3():
    yt = pytube.YouTube(url)
    print(f"Title: {yt.title}")
    print(f"Author: {yt.author}")
    stream = yt.streams.filter(only_audio=True).first()
    print("Downloading...")
    stream.download()
    print("Download complete!")
    exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <url> <mp4/mp3> ")
        exit(1)
    url = sys.argv[1]
    if sys.argv[2] == "mp4":
        mp4()
    elif sys.argv[2] == "mp3":
        mp3()
    else:
        print("Usage: python main.py <url> <mp4/mp3> ")
        exit(1)