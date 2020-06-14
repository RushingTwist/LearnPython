# -*- coding: UTF-8 -*-


import os

def file_rename(path):

    for file in os.listdir(path):
        old_name  = path + '/' + file

        if os.path.isdir(old_name):
            file_rename(old_name)
            pass

        if "【更多IT教程 微信352852792】" in file:
            new_filename = old_name.replace("【更多IT教程 微信352852792】", "")
            print(old_name)
            print('======================')
            print(new_filename)
            os.rename(old_name, new_filename)


if __name__ == '__main__':
    file_rename(r"/Volumes/WIN_ZZZ/152.跟着360架构师 学习Shell脚本编程")

