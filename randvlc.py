# RANDVLC
# Utilitaire de lancement de vidéos aléatoire depuis un répertoire et via VLC
# Par Kaemyll - dec 2021

import os, random, subprocess

vidPath = str(input('Indiquez le chemin vers votre répertoire vidéo => (Windows = \\) '))
nbVideo = int(input('Combien de vidéos voulez-vous visionner ? '))

def rndmp():
   randomfile = random.choice(os.listdir(vidPath))
   file = vidPath + randomfile
   # todo - rendre modifiable le chemin de VLC, ainsi que la durée de start et run
   subprocess.call(['C:\\Program Files (x86)\\VideoLAN\VLC\\vlc.exe ', file, f'--start-time={random.randint(15,60)}', f':run-time={random.randint(30,120)}', '--play-and-exit', '--fullscreen'])

for iter in range(0, nbVideo):
   rndmp()
