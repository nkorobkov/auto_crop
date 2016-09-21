__author__ = 'Insolia'

from os import listdir, mkdir
from conf import *
from os.path import isfile, join
from PIL import Image


loadpath = LOADPATH
savepath = SAVEPATH

try:
    mkdir(savepath)
except(OSError):
    pass

raw_photo_names = [f for f in listdir(loadpath) if isfile(join(loadpath, f)) and f[0] != '.']

for f in raw_photo_names:
    ph = Image.open(join(loadpath, f))

    new_p = ph.crop((LF, UP, RG, LO))

    new_p.save(join(savepath, f))

    print 'succes at ' + join(savepath, f)