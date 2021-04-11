#!/usr/bin/python3

import sys
import os.path
from os import path
from colorExtract import *


def showHelp():
    print('\tUSE\n./app.py [<filename>/EXTRA PARAMETERS] <other options>\n\n\tEXTRA PARAMETERS')
    print('--v\t\tShow version')
    print('--h\t\tShow this help and exit')
    print('\n\n\n')
    print('\tOTHER OPTIONS')
    print('#1\t\t only RGB extraction')
    print('#2\t\t extract RG, GB, RB alongwith RGB')
    print("\n\n\nNOTE:\nONLY .JPG and .PNG files are supported as of now")


def showVersion():
    print('Channel extraction tool-----Version  1.0.1')


def isValidFile(filename):
    file_fs = ['.png', '.jpg']
    retVal = False
    cond = path.exists(filename)
    if(cond):
        for fileN in file_fs:
            if filename.endswith(fileN):
                retVal = True
                break
    return retVal


def showinvalidOption():
    print("Try again with a correct input")


param0 = sys.argv[1]

if(param0[0] == '-'):
    if(param0 in ['--h', '-h', '--HELP', '-HELP']):
        showHelp()
    elif(param0 in ['--v', '-v', '--VERSION', '-VERSION']):
        showVersion()
    else:
        showinvalidOption()

elif(isValidFile(param0)):
    t = 1
    if(len(sys.argv) == 3):
        if(sys.argv[2] == '#1'):
            t = 1
        elif(sys.argv[2] == '#2'):
            t = 2
        else:
            t = 0

    if(t != 0):
        extractColors(param0, t)
    else:
        showinvalidOption()
else:
    showinvalidOption()
