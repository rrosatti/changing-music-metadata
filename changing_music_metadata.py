import os
from subprocess import call
import sys

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for filename in files:
    print("\n"+filename)
    title = input("\nTitle: ")
    artist = input("\nArtist: ")
    call(['eyeD3', filename, '-a', artist, '-t', title])
    new_fn = artist + " - " + title + ".mp3"
    call(['mv', filename, new_fn])
    call(['mv', new_fn, '../songs/'])

