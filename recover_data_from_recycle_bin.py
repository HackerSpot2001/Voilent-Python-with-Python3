#!/usr/bin/python3
import os

def returnDir():
    dirs = ['C:/Recycler/','C://Recycled/','C://$Recycle.Bin/']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            print(os.listdir(recycleDir))

    return None