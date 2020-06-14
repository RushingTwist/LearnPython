# -*- coding: UTF-8 -*-


import os

def file_rename(path):

    for file in os.listdir(path):
        old_name  = path + '/' + file

        if os.path.isdir(old_name):
            file_rename(old_name)
        else:
            # if "【飞猫客 www.feimaoke.com】" in file:

            #     idx = old_name.index("【飞猫客 www.feimaoke.com】")
            #     new_name = old_name[:idx]
            #     os.rename(old_name, new_name)
            if ".mp4" not in file:
                new_name = old_name + ".mp4"
                os.rename(old_name, new_name)
                print(old_name) 
                print("-------------")
                print(new_name)

        # if "【更多IT教程 微信352852792】" in file:
        #     new_filename = old_name.replace("【更多IT教程 微信352852792】", "")
        #     print(old_name)
        #     print('======================')
        #     print(new_filename)
        #     os.rename(old_name, new_filename)

if __name__ == '__main__':
    file_rename(r"/Volumes/WIN_ZZZ/216.编程必备基础-音视频小白系统入门课")

