#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Add the picture name wiht "@ 2 x" ,put the pictures of the two images into a three times.

import sys, getopt
import os
from PIL import Image
import re
import shutil

def main(argv):
       inputDir = ''
       try:
          opts, args = getopt.getopt(argv,"hi:",["ifile="])
       except getopt.GetoptError:
          print ('test.py -i <inputDir>')
          sys.exit(2)
       for opt, arg in opts:
          if opt == '-h':
             print ('test.py -i <inputDir>')
             sys.exit()
          elif opt in ("-i", "--ifile"):
             inputDir = arg
             if not os.path.isdir(inputDir):
                    print ('文件夹不存在')
                    sys.exit()
             return os.path.abspath(inputDir)

def add3xImage(path):
    for maindir, subdir, file_name_list in os.walk(path):
        for name in file_name_list:
            filePath = os.path.join(maindir,name)
            if os.path.isfile(filePath) and filePath.endswith('.png'):
                if '@2x.png' not in filePath and '@3x.png' not in filePath:
                    nameList = filePath.split('.png')
                    print(nameList[0]+'@2x.png')
                    os.renames(filePath, nameList[0]+'@2x.png')

    for maindir, subdir, file_name_list in os.walk(path):
        for name in file_name_list:
            filePath = os.path.join(maindir,name)
            if os.path.isfile(filePath) and filePath.endswith('.png'):

                dirName =os.path.basename(name)
                filename = os.path.splitext(name)[0]

                nameList = filePath.split('@')[0]
                image2xpath = nameList+'@2x.png'
                image3xpath = nameList+'@3x.png'
                # print(image2xpath)
                if os.path.exists(image2xpath) and os.path.exists(image3xpath) == False:
                    print(filePath + '只有2倍图')
                    im = Image.open(image2xpath)
                    w, h = im.size
                    out = im.resize((w*150//100, h*150//100),Image.ANTIALIAS)
                    strinfo = re.compile('2x')
                    b = strinfo.sub('3x',image2xpath)
                    out.save(b, 'png')
                    # print(name)
                if os.path.exists(image2xpath) == False and os.path.exists(image3xpath) == True:
                    print(filePath+ '只有3倍图')
                    im = Image.open(image3xpath)
                    w, h = im.size
                    out = im.resize((w*100//150, h*100//150),Image.ANTIALIAS)
                    strinfo = re.compile('3x')
                    b = strinfo.sub('2x',image3xpath)
                    out.save(b, 'png')
                # else:
                #     print(filePath)

if __name__ == "__main__":
        path = main(sys.argv[1:])
        # print(path)
        # for name in [x for x in os.listdir(os.chdir(path)) if os.path.isdir(x) and os.path.splitext(x)[1]=='.imageset']:
        #     print(name)
        # add3xImage(path)

        for maindir, subdir, file_name_list in os.walk(path):
            if os.path.isdir(maindir) and maindir.endswith('.imageset'):
                dirName =os.path.basename(maindir)
                filename = os.path.splitext(dirName)[0]

                image2xpath = os.path.join(maindir, filename+'@2x.png')
                if os.path.exists(image2xpath):
                    # print(apath+'存在')
                    toPath =  os.path.join(os.path.dirname(maindir), filename+'@2x.png')
                    shutil.copyfile(image2xpath, toPath)
                else:
                     print(image2xpath+'不存在')

                image3xpath= os.path.join(maindir, filename+'@3x.png')
                if os.path.exists(image3xpath):
                    toPath =  os.path.join(os.path.dirname(maindir), filename+'@3x.png')
                    shutil.copyfile(image3xpath, toPath)
                else:
                     print(image3xpath+'不存在')

                #
                # for file_name in file_name_list:
                #     if file_name.endswith('.png'):
                #         apath = os.path.join(maindir, file_name)
                #          # 获取文件夹名
                #         fapath =os.path.basename(maindir)
                #
                #         print(os.path.basename(maindir))
                #         print(apath)#每个文件的文本存到list中

        print('完成')
