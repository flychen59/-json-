# -*- coding:utf8 -*-
import json
from os import listdir
import os

path = '/home/flychen/frustum-pointnets-master/dataset/kitti/label/'

filelist = listdir(path)
# for i in  filelist:
# print(filelist[0].split(".")[0])
#   i.split()
fileIndex = []

# 文件名读入时并非按照我们常识中的按照文件名字顺序读入，
# 例如：1.json,2.json,3.json；程序可能会按 3,1,2 的顺序读入，
# 这对我们后面批量处理造成很大的不便，所以读入文件名后，
# 我们要手动地对文件名进行一次排序
# 以下就是排序操作
for i in range(0, len(filelist)):
    index = filelist[i].split(".")[0]
    fileIndex.append(int(index))
# new_filelist =[]
for j in range(1, len(fileIndex)):
    for k in range(0, len(fileIndex) - 1):
        if fileIndex[k] > fileIndex[k + 1]:
            preIndex = fileIndex[k]
            preFile = filelist[k]
            fileIndex[k] = fileIndex[k + 1]
            filelist[k] = filelist[k + 1]
            fileIndex[k + 1] = preIndex
            filelist[k + 1] = preFile

# 完成排序后，开始按照文件名顺序读取文件内容信息
data = []  # 记录每个文件最终信息的列表
labelpath = '/home/flychen/frustum-pointnets-master/dataset/kitti/label/'
for file in filelist:
    with open(labelpath + file, 'r') as txt:
        lines = txt.readlines()
        eachdata = []  # 记录单个文件信息的列表

        seq=0


        for each in range(6, len(lines)):
            word = lines[each].split('"')
            for i in range(0, len(word)):
                if word[i] == 'car':
                    eachdata.append('car 0.0 0.0 0.0 500')
                    eachdata.append(int(lines[each + 2].strip().strip(',').split(':')[1]))
                    eachdata.append(int(lines[each + 3].strip().strip(',').split(':')[1]) )
                    eachdata.append(int(lines[each + 4].strip().strip(',').split(':')[1]))
                    eachdata.append(
                        int(lines[each + 5].strip().strip(',').split(':')[1]))  # (xmin,ymin,xmax,ymax,'shoes')
                    eachdata.append('0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0')

                elif word[i] == 'truck':
                    eachdata.append('truck 0.0 0.0 0.0 500')
                    eachdata.append(int(lines[each + 2].strip().strip(',').split(':')[1]) )
                    eachdata.append(int(lines[each + 3].strip().strip(',').split(':')[1]) )
                    eachdata.append(int(lines[each + 4].strip().strip(',').split(':')[1]))
                    eachdata.append(
                        int(lines[each + 5].strip().strip(',').split(':')[1]) )  # (xmin,ymin,xmax,ymax,'shoes')
                    eachdata.append('0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0')

        txt.close()
        data.append(eachdata)

# 记录完成后，开始将数据写入txt文件
with open('data2.txt', 'w') as txt:
    for eachdata in data:
        line=''
        i = 0
        for i in range(len(eachdata)):
            if i % 5 == 0 and i > 1 and i != len(eachdata) - 1:
                s = str(eachdata[i]) + ' '
                line = line + s
            elif i == len(eachdata) - 1:
                line = line + str(eachdata[i])
            else:
                s = str(eachdata[i]) + ','
                line = line + s
        lines = line.replace('json', '') + '\n'

        txt.writelines(lines)
    txt.close()
print('finish')

#        line='json'
#        while line:
#           line = txt.readline()
#          word = line.split()
#         for i in range(0,len(word)):

