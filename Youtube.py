from pytube import YouTube
link = input ("Digite o link desejado aqui: ")
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()
print ("Downloading...")
ys.download("Dowloads\python")
print ("Download completed!")
