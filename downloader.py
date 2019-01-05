import random
import urllib.request


print("what type of file that you want to download : ")
print("pls select as follows: 1 for audio, 2 for video, 3 for image")


user_input = int(input("pls select your option"))
url= str(input("pls paste the  url here"))


def video_downloader(url0):
    name = random.randrange(1, 100000)
    full_name = str(name) + ".mp4"
    urllib.request.urlretrieve(url0, full_name)

def audio_downloader(url0):
    name = random.randrange(1, 100000)
    full_name = str(name) + ".mp3"
    urllib.request.urlretrieve(url0, full_name)

def image_downloader(url0):
    name = random.randrange(1, 100000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url0, full_name)

if user_input == 1:
    audio_downloader(url)
elif user_input == 2:
    video_downloader(url)
elif user_input == 3:
    image_downloader(url)
else:
    print("you entered wrng option")







