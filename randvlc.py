# RANDVLC
# Utilitaire de lancement de vidéos aléatoire depuis un répertoire et via VLC
# Par Kaemyll - dec 2021

import os, random, subprocess

vidPath = str(input('Indiquez le chemin vers votre répertoire vidéo => (Windows = \\) '))

def rndmp():
   randomfile = random.choice(os.listdir(vidPath))
   file = vidPath + randomfile
   # todo - rendre modifiable le chemin de VLC, ainsi que la durée de start et run
   subprocess.call(['C:\\Program Files (x86)\\VideoLAN\VLC\\vlc.exe ', file, '--start-time=30.0', ':run-time=60.0', '--play-and-exit', '--fullscreen'])
   
nbVideo = int(input('Combien de vidéos voulez-vous visionner ? '))

for iter in range(0, nbVideo):
   rndmp()
