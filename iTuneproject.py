from PySide.phonon import *
media = Phonon.MediaObject()
path = "bedroom audio - ใครคนนั้น.mp3"
media.setCurrentSource(Phonon.MediaSource(path))
media.play()

file = open("playlist.txt","a")
file.write(path)
file.close()

file = open("playlist.txt","r")

file.readline()
listpath = []
listpath.append(file)
