# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:59:51 2020

@author: dralioz
"""

# Constants
datas=None
n_imgs=None
down_path=[]
save_path=[]
label_im_save_path=[]
annotations_path=[]

# get data informations
def get_data_infos():
    global datas
    global n_imgs
    datas=input("What are you looking for?\nDatas:")
    n_imgs=input("How many images do you need?\nNumbers:")
    datas=datas.split(",")
    n_imgs=n_imgs.split(",")
    for i, amount in enumerate(n_imgs):
        amount=int(amount)
        n_imgs[i]=amount
    return datas,n_imgs

# downloaded path builders
def downloaded_path_builder(datass):
    global down_path
    for data in datass:
        path="Downloaded_images"+"/"+data
        down_path.append(path)
    return down_path

# save path builder
def save_path_builder(datass):
    global save_path
    for data in datass:
        path="Saved/Saved_images"+"/"+data
        save_path.append(path)
    return save_path

# label image save path
def label_save_path(datass):
    global label_im_save_path
    for data in datass:
        path="Saved/Labelling/images"+"/"+data
        label_im_save_path.append(path)
    return label_im_save_path

# ann path builder
def ann_path(datass):
    global annotations_path
    for data in datass:
        path="Saved/Labelling/Annotations"+"/"+data
        annotations_path.append(path)
    return annotations_path
