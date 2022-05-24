import zipfile
import rarfile
import os
import sys
from threading import Thread
import argparse
from itertools import product
import time

parser = argparse.ArgumentParser(description='Compressedcrack',epilog='Use the -h for help')
parser.add_argument('-i','--input', help='Insert the file path of compressed file',required=True)
parser.add_argument('rules',nargs='*',help='‹min> <max› <character>')
#Const Character
CHARACTER="abedefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789! @#$%^&*()-_+=~`[]{}\|/;:'?.,"

class Check:
    def __init__(self,Arg):
        self.typen= None
        self.rules = False
        self.startLength = None
        self.maxLength = None
        self.character = None
        #Check rules
        if len(Arg)>= 4:
            self.getData(Arg)
            self.rules = True
        elif len(Arg) == 0 or len(Arg) > 2:
            parser.print_help()
            parser.exit()
        #Check


