__author__ = 'Insolia'

from os import listdir, mkdir
from conf import *
from os.path import isfile, isdir, join
from PIL import Image


def process_dir(loadpath):
    mirror_dir_for_save(loadpath)
    object_names_in_folder = listdir(loadpath)
    print "start processing folder " + loadpath + " need to crop " + str(
        len(object_names_in_folder)) + " pics or folders"
    for f in object_names_in_folder:
        local_object = join(loadpath, f)

        if isfile(local_object) and f[0] != '.':
            process_photo(join(loadpath, f))
            continue

        if isdir(join(loadpath, f)) and RECURSIVE:
            process_dir(join(loadpath, f))
            continue


def process_photo(photo):
    ph = Image.open(photo)
    new_p = ph.crop((LF, UP, RG, LO))
    save_url = photo.replace(LOADPATH, SAVEPATH)
    new_p.save(save_url)
    print 'success at ' + save_url


def mirror_dir_for_save(loadpath):
    try:
        mkdir(loadpath.replace(LOADPATH, SAVEPATH))
    except(OSError):
        pass

if __name__ == '__main__':
    process_dir(LOADPATH)



