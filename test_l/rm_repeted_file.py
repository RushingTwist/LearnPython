# -*- coding: UTF-8 -*-

# 视频文件下载重复了, 重复文件为(1).mp4结尾, 将该特征文件全部移除

import os

def rm_repeted_file(path):

    for file in os.listdir(path):
        fullPath  = path + '/' + file
        print(file)
        if os.path.isdir(fullPath):
            rm_repeted_file(fullPath)
        else:
            if file == '.DS_Store':
                continue

            if "(1).mp4" in file:
                os.remove(fullPath)

if __name__ == '__main__':
    rm_repeted_file(r"/Volumes/WIN_ZZZ/216.编程必备基础-音视频小白系统入门课")
