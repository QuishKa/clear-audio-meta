import os
import sys
from tkinter import Tk
from tkinter import filedialog
from os import listdir
from os.path import isfile, join
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError

supported_extensions = ('.mp3', '.aac', '.wav', '.flac', '.ogg', '.mpeg', '.aiff', '.wma')
delkeys = ('album', 'title', 'artist', 'author', 'composer', 'performer', 'albumartist', 'discsubtitle', 'lyricist')

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
            audio = EasyID3(join(path, f))
            for k in audio.keys():
                if k in delkeys:
                    audio[k] = u""
            audio.save()
        except ID3NoHeaderError:
            print(f"File {f} doesn't have ID3 headers and haven't been cleared\n")
            continue
        except Exception as e:
            print(e) # todo process exceptions
            return

if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(sys.argv[0])) 
    root = Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    if path != '':
        files = read_files_from_dir(path)
        del_tags(path, files)
    print("Press Enter to close this window...")
    input()