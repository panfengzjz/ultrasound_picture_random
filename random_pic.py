#coding: utf-8
import sys
import os
import shutil
import numpy as np

from random import shuffle

src_directory = "./src"
dst_directory = "./dst"

def remove_file(oldPath, newPath):
    fileList = os.listdir(oldPath)
    for file in fileList:
        if(file[-3:] == 'jpg'):
            src = os.path.join(oldPath, file)
            dst = os.path.join(newPath, file)
            shutil.move(src, dst)

def get_pic_list():
    if (not os.path.exists(src_directory)):
        os.makedirs(src_directory)
        remove_file("./", src_directory)
    return os.listdir(src_directory)

def copy_and_rename_file(orgFile, newFile):
    if (not os.path.exists(dst_directory)):
        os.makedirs(dst_directory)
    shutil.move(orgFile, newFile)

def do_encoding():
    file_dict = {}
    pic_list = get_pic_list()
    number = len(pic_list)
    random_list = []
    for i in range(number):
        random_list.append("%03d.jpg" %i)
    for i in pic_list:
        shuffle(random_list)
        file_dict[i] = random_list.pop()
        copy_and_rename_file(os.path.join(src_directory, i),
                             os.path.join(dst_directory, file_dict[i]))
    np.save('my_file.npy', file_dict) 

def do_decoding():
    file_dict = np.load('my_file.npy', allow_pickle=True).item()
    for key, value in file_dict.items():
        copy_and_rename_file(os.path.join(dst_directory, value),
                             os.path.join(src_directory, key))

if __name__ == "__main__":
    step = int(sys.argv[1])
    if (step == 1):
        do_encoding()
    elif (step == 2):
        do_decoding()
