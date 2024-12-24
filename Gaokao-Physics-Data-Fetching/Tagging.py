# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:42:55 2021

@author: hp
"""

import os
import sys
import pickle
from knowledge_filter import *
from math import *
import json

k_to_ch={}
for root,dirs,files in os.walk(r".\\Doc_write"):
    dir_set=dirs
    break
Chapter_Dict={"第一章":"运动学",
              "第二章":"力学",
              "第三章":"",
              "第四章":"运动学",
              "第五章":"运动学",
              "第六章":"电学",
              "第七章":"电学",
              "第八章":"磁学",
              "第九章":"磁学",
              "第十章":"磁学",
              "第十一章":"热学",
              "第十二章":"光学",
              "第十三章":"运动学",
              "第十四章":"原子物理",
              "第十五章":"光学",
              "第十六章":"光学",
              "第十七章":"",
              "第十八章":"热学"}
def save_text(file_cnt,temp_st,tag):
    if(tag=='Null' or tag==''):
        return
    filename='./New_Dataset_5/'+str(file_cnt)+'.txt'
    temp_st=temp_st.replace('\n','')
    with open(filename,'w',encoding='utf-8') as f:
        f.write(temp_st)
        f.write('\n')
        f.write(tag)
        f.close()

def sigmoid_like(rate):
    rate=5.0-10.0*rate
    return 1/(1+e**(-rate))

def Tag_process(text_set):
    max_num=0
    max_tag=''
    for temp_tag in cfg:
        temp_num=0.0
        model_list=cfg[temp_tag]
        order=0
        total=10
        for word in model_list:
            cnt_num=text_set.count(word)
            temp_num+=cnt_num*sigmoid_like(order/total)
            order+=1
        if(temp_num>max_num):
            max_num=temp_num
            max_tag=temp_tag
    if(max_tag==''):
        return 'Null'
    return k_to_ch[max_tag]

with open('cfg.txt','r',encoding='utf-8') as f:
    js=f.read()
    cfg=json.loads(js)
    f.close()

for dir_0 in dir_set:
    for root,dirs,files in os.walk(r".\\Doc_write\\"+dir_0):
        for file in files:
            if (file.find('.txt')==-1):
                continue
            node_name=file.replace('.txt','')
            k_to_ch[node_name]=Chapter_Dict[dir_0]

for root,dirs,files in os.walk(r"./After_scrapy_data"):
    dir_set=dirs
    break

tfiwf=pickle.load(open("./model/tfiwf.pkl","rb"))
file_cnt=0
for root,dirs,files in os.walk(r"./New_Dataset_2"):
    for file in files:
        txt_file=os.path.join(root,file)
        with open(txt_file,'r',encoding='utf-8') as f1:
            text_set=f1.readlines()
            f1.close()
        # if(file_cnt==100):
        #     break
        if(file_cnt==4):
            file_cnt=file_cnt
        text_set=''.join(text_set)
        text_set=knowledge_filter(text_set)
        tag=Tag_process(text_set)
        file_cnt+=1
        if(file_cnt%1000==0):
            print(file_cnt)
        save_text(file_cnt,text_set,tag)
    break