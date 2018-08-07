import os
from subprocess import call
import sys

# iterate through all files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for filename in files:
    # print the file name, so we can see the artist and song names
    print("\n"+filename)
    # get the user input for Title and Artist
    title = input("\nTitle: ")
    artist = input("\nArtist: ")
    # use eyeD3 tool to change the title and the artist of the current song
    call(['eyeD3', filename, '-a', artist, '-t', title])
    # new_fn will get the "new" file name, since we changed the metadata with the previous command
    new_fn = artist + " - " + title + ".mp3"
    # change the file name
    call(['mv', filename, new_fn])
    # move the song to a new directory. In this script, we're moving the files to 'songs/', which is outside the current directory
    call(['mv', new_fn, '../songs/'])

