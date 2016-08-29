# -*-coding:utf-8 -*-

import jieba
from globe_info import *
import os

def split_to_word(content, name, dir_path):

    seg_list = jieba.cut(content, cut_all=True)
    path = dir_path+"\\"+str(name)+'.txt'
    a = open(path, 'w')
    a.truncate()
    a.close()
    for i in seg_list:
        a = open(path, 'a')
        a.write('%s ' % (i.encode('utf-8')))
        a.close()









