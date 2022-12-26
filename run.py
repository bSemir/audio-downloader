import os
from pytube import YouTube

try:
    # url input from user
    yt = YouTube(input("Enter the URL of the video that you want to download: \n>> "))

    # check if the video exists
    yt.check_availability()

    # only audio
    audio = yt.streams.filter(only_audio=True).first()

    # replace this with your own path
    destination = "/home/semirb/Music"

    # download the file
    out_file = audio.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)
except:
    print("Something went wrong. Please try again.\n")
else:
    print(
        yt.title + " has been successfully downloaded.\nCheck it out in: " + destination
    )
    # print("Thumbnail URL: " + yt.thumbnail_url)

# TODO: save the video thumbnail also
