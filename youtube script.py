import pytube
link = "https://youtu.be/9URM1_2S0ho?si=01IUdjJyKaOF5z-Y"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()
