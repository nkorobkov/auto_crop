__author__ = 'Insolia'

from os import listdir, mkdir
from conf import *
from os.path import isfile, join
from PIL import Image
import glymur

loadpath = LOADPATH
savepath = SAVEPATH

try:
    mkdir(savepath)
except(OSError):
    pass

raw_photo_names = [f for f in listdir(loadpath) if isfile(join(loadpath, f)) and f[0] != '.' and f[-3:] == 'jp2']

for f in raw_photo_names:
    ph = glymur.Jp2k(join(loadpath, f))

    im = Image.fromarray(ph[:])

    new_p = im.crop((LF, UP, RG, LO))

    new_p.save(join(savepath, f[:-3]+'png'))
    #im.show()

    print 'succes at ' + join(savepath, f)
