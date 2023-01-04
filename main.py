from pytube import YouTube
from sys import argv
input("THIS IS FOR EDUCATIONAL PURPOSES ONLY. I AM NOT RESPONSIBLE FOR WAHT YOU DO WITH THIS PROGRAM (press enter to continue)")
place = "Where do you want to save the file: "
choice = input("Do you want to download  (1. A single video or (2. Multiple videos: ")

if choice == '1':
  save = input(place)
  while True:
    URL = input("What is the link: ")
    yt = YouTube(URL)

    print("Author: ", yt.author)
    print("Published: ", yt.publish_date)
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    print("Description: ", yt.description)
    print("Length (seconds): ", yt.length)
    print("Rating: ", yt.rating)

    print("DOWNLOADING...")
    yd = yt.streams.get_highest_resolution()
    yd.download(save)
    print("DOWNLOAD COMPLETE")

elif choice == '2':
  save2 = input(place)
  file = input("What is the file containing the links: ")
  while True:
    link = open(file, 'r')
    for i in link:
      yt = YouTube(i)
      yd = yt.streams.get_highest_resolution()

      print("Author: ", yt.author)
      print("Title: ", yt.title)
      print("Views: ", yt.views)
      print("Description: ", yt.description)
      print("Length (Seconds)", yt.length)
      print("Published: ", yt.publish_date)
      print("Rating: ", yt.rating)
      print("DOWNLOADING...")
      yd.download(save2)
    print("FINISHED")
  