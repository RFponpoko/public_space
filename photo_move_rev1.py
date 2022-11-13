import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS


TARGET_PATH = "/home/hiroakikato/Pictures/Wallpapers/"
 
def get_exif(img):
    exif = img._getexif()
    try:
        for id,val in exif.items():
            tg = TAGS.get(id,id)
            if tg == "DateTimeOriginal":
                return val
    except AttributeError:
        return None
 
    return None

def list_files(dir, func):
    for file in os.listdir(dir):
        try:
            img = Image.open(dir + file)
        except:
            continue
        datetimeinfo = func(img)
        img.close()
        
        datetimeinfo = datetimeinfo.replace(" ", "_")
        mydate = datetimeinfo.split("_")
        format_mydate = mydate[0].replace(":", "-")
        mkdir_for_data(dir, format_mydate, file)

def file_move(from_file : str, to_file : str):
    shutil.move(from_file, to_file)

def mkdir_for_data(mypath : str, folder_name : str, file_name : str):
    from_here = r'./' + file_name
    to_there = r'./' + folder_name + r'/' + file_name
    if os.path.isdir(mypath + folder_name) == False:
        print(f'name new folder {folder_name}')
        os.mkdir(folder_name)
        file_move(from_here, to_there)
        
    else:
        print(f'{folder_name} exits')
        file_move(from_here, to_there)

def main():
    try:
        for taginfo in list_files(TARGET_PATH, get_exif):
            pass
    except:
        print('no (more) picture data in this folder')
 
if __name__ == '__main__':
    main()
    