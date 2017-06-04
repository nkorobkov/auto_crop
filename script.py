__author__ = 'Insolia'

from os import listdir, mkdir
from conf import *
from os.path import isfile, isdir, join
from PIL import Image

loadpath = LOADPATH
savepath = SAVEPATH

def process_dir(local_loadpath):
    try:
        mkdir(local_loadpath.replace(loadpath, savepath))
    except(OSError):
        pass

    object_names_in_folder = listdir(local_loadpath)
    print "start processing folder " + local_loadpath + " need to crop " + str(len(listdir(local_loadpath))) + " pics or folders"
    for f in object_names_in_folder:
        local_object = join(local_loadpath, f)
        if isfile(local_object) and f[0] != '.':
            process_photo(join(local_loadpath, f))
            continue

        if isdir(join(local_loadpath, f)) and RECURSIVE:
            process_dir(join(local_loadpath, f))
            continue


def process_photo(photo):
    ph = Image.open(photo)
    new_p = ph.crop((LF, UP, RG, LO))
    save_url = photo.replace(loadpath,savepath)
    new_p.save(save_url)
    print 'succes at ' + join(savepath, photo.replace(loadpath + "/",""))


if __name__ == '__main__':
    process_dir(loadpath)
