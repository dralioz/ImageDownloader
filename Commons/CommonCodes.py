# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:35:23 2020

@author: dralioz
"""

import os
import time
import requests
import urllib.request as ureq
import urllib
import imghdr

# Introduction 1
def wel2us():
    print("Welcome to the Image Downloader, Object Labeller - I.D.O.L!")
    time.sleep(2)
    print("To enter multiple data, just put a comma between each two data")
    time.sleep(3)

# countdown
def countdown(second):
    for i in range(second):
        print(str(second-i),end=" \r")
        time.sleep(1)

# save folder
def save_folder(save):
    if not os.path.exists(save):
        os.mkdir(save)

# userface 1
def usf_1(data):
    print("\nAll urls are rewritten for {}. It takes some time. Please wait".format(data))
    time.sleep(2)
    print("All links will be taken in ")
    countdown(10)
    print("0 . . . links are getting!")

# userface 2
def usf_2(path):
    print("Save folder is opening. Please wait.")
    time.sleep(2)
    save_folder(path)
    print("The folder is opened")

# userface 3
def usf_3():
    time.sleep(2)
    print("Downloading will be start in ")
    countdown(5)
    print("0 . . . Downloading is started!")

# download_img_1 (data, link ve gerekirse ek parametre alacak.)
def download_img_1(data,links,save_path,amount):
    count=0
    print("Beginning: {}".format(time.asctime()))
    for i, link in enumerate(links):
        img_name=save_path+"/"+data+"_{:06}.jpg".format(amount+i+1)
        try:
            ureq.urlretrieve(link,img_name)
        except urllib.error.HTTPError as exception:
            print(exception)
            pass
        except TypeError as exception:
            print(exception)
            pass
        print(i+1,end=" \r")
        count+=1
    print("{} images are downloaded".format(count))
    print("Done! ",time.asctime())

# downlaod_img_2
def download_img_2(data,links,save_path,amount):
    count=0
    print("Beginning: ",time.asctime())
    for i, link in enumerate(links):
        img_name=save_path+"/"+data+"_{:06}.jpg".format(amount+i+1)
        try:
            images=requests.get(link)
        except requests.exceptions.ConnectionError as exception:
            print(exception)
            pass
        except requests.exceptions.MissingSchema as exception:
            print(exception)
            pass
        with open(img_name,"wb") as writer:
            writer.write(images.content)
        print(i+1,end=" \r")
        count+=1
    print("{} images are downloaded".format(count))
    print("Done! ",time.asctime())

def download_img_3(data,links,save_path,amount,agent):
    count=0
    print("Beginning:",time.asctime())
    for i, link in enumerate(links):
        request=ureq.Request(link,None,agent)
        image=ureq.urlopen(request).read()
        img=save_path+"/"+data+"_{:06}.jpg".format(amount+i+1)
        if not imghdr.what(None,image):
            raise
        with open(img,"wb") as f_down:
            f_down.write(image)
        print(i+1,end=" \r")
        count+=1
    print("{} images are downloaded".format(count))
    print("Done!",time.asctime())
