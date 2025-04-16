import os
import sys
from tkinter import Tk
from tkinter import filedialog
from os import listdir
from os.path import isfile, join
import eyed3

supported_extensions = ('.mp3', '.aac', '.wav', '.flac', '.ogg', '.mpeg', '.aiff', '.wma')

def read_files_from_dir(path: str = None) -> list|None:
    if path != None:
        files = [f for f in listdir(path) if isfile(join(path, f))]
        files = filter(lambda x: x.endswith(supported_extensions), files)
        return list(files)
    return None

def del_tags(path: str = None, files: list = None):
    if files == None:
        return
    if path == None:
        return
    for f in files:
        try:
            audiofile = eyed3.load(join(path, f))
            audiofile.tag.artist = ""
            audiofile.tag.album = ""
            audiofile.tag.album_artist = ""
            audiofile.tag.title = ""
            audiofile.tag.track_num = 0
            audiofile.tag.save()
        except Exception as e:
            print(e) # todo process exceptions
            return

if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(sys.argv[0])) 
    root = Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    print(path)

    files = read_files_from_dir(path)
    del_tags(path, files)