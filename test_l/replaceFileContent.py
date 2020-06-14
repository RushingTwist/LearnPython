import os

def replaceFileContent(path):

    for file in os.listdir(path):

        if os.path.isdir(path + '/' + file):
            replaceFileContent(path + '/' + file)
            # print('==========')
        else:

            # print(file)

            if file == '.DS_Store':
                continue

            newContent = ''

            # with open(path + '/' + file, "r+", encoding='utf-8') as f:
            #
            #     content = f.read()
            #
            #     if 'ViewModel' in content:
            #         newContent = content.replace("ViewModel", "ViewModel_NEW")
            #
            #     else:
            #         newContent = content
            #
            #     if 'ViewController' in newContent:
            #         newContent = newContent.replace("ViewController", "ViewController_NEW")
            #
            # with open(path+'/'+file, 'w', encoding='utf-8') as f:
            #     f.write(newContent)

            # if 'ViewModel' in file:
            #     newName = file.replace("ViewModel", "ViewModel_NEW")
            #     os.rename(os.path.join(path,file), os.path.join(path,newName))
            #
            #
            # if 'ViewController' in file:
            #     newName = file.replace("ViewController", "ViewController_NEW")
            #     os.rename(os.path.join(path,file), os.path.join(path,newName))

            if ".h" in file:
                vc = file.replace("ViewModel", "ViewController")
                print("@\"%s\" : @\"%s\"," %(file[0:-2], vc[0:-2]))


if __name__ == '__main__':
    replaceFileContent('/Users/lynn/Desktop/公文审批(新)')
