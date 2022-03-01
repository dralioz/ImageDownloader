# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:17:51 2020

@author: dralioz
"""

import cv2
import os
import sys
import keyboard
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
from Commons import CommonCodes as cc
from show_label.key_open_save import write_xml as wx
from Commons.TurkishProcess import find_amount_folder as faf

# global constants
img = None
tl_list = []
br_list = []
object_list = []

# constants
image_folder = None
savedir = None
obj = None
img_save=None
img_label_save=None

cnt_save=None
cnt_label=None

def key_action():
    while True:
        if keyboard.is_pressed("c"):
            break
        elif keyboard.is_pressed("e"):
            sys.exit()


def line_select_callback(clk,rls):
    global tl_list
    global br_list
    tl_list.append((int(clk.xdata),int(clk.ydata)))
    br_list.append((int(rls.xdata),int(rls.ydata)))
    object_list.append(obj)

picture=None
iterator=0
it2=0
def onkeypress(event):
    global object_list
    global tl_list
    global br_list
    global img
    global picture
    global obj

    if event.key=="e":
        cv2.destroyAllWindows()
        plt.close()
        sys.exit()

    elif event.key=="k":
        global iterator
        global savedir
        global cnt_label
        cnt_label+=1
        path_name=img_label_save+"/"+obj+"_{}".format(cnt_label)
        cv2.imwrite("{}.jpg".format(path_name),picture)
        wx(img_label_save,obj,tl_list,br_list,savedir)
        plt.close()
        tl_list=[]
        br_list=[]
        object_list=[]
        img=None
        
    elif event.key=="c":
        global it2
        global cnt_save
        cnt_save+=1
        path_name=img_save+"/"+obj+"_{}".format(cnt_save)
        cv2.imwrite("{}.jpg".format(path_name),picture)
        tl_list=[]
        br_list=[]
        object_list=[]
        img=None
        plt.close()
        
    elif event.key=="n":
        tl_list=[]
        br_list=[]
        object_list=[]
        img=None
        plt.close()
    else:
        print("Invalid key. Please enter a valid key.")


def toggle_selector(event):
    toggle_selector.RS.set_active(True)

       
def object_label():
    for n, image_file in enumerate(os.scandir(image_folder)):
        img=image_file
        fig,ax=plt.subplots(1)
        mngr=plt.get_current_fig_manager()
        mngr.window.setGeometry(250,120,1080,720)
        image=cv2.imread(image_file.path)
        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        global picture
        picture=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        ax.imshow(image)
        toggle_selector.RS=RectangleSelector(
            ax,line_select_callback,
            drawtype="box",useblit=True,
            button=[1],minspanx=5,minspany=5,
            spancoords="pixels",interactive=True
        )
        bbox=plt.connect("key_press_event",toggle_selector)
        key=plt.connect("key_press_event",onkeypress)
        plt.show()


def get_all_values_and_run(img_path,img_save_path,img_label_path,ann_path,data):
    global image_folder
    global savedir
    global obj
    global img_save
    global img_label_save
    global cnt_save
    global cnt_label
    image_folder=img_path # downloaded img path
    img_save=img_save_path # selected img path
    img_label_save=img_label_path # labelled img path
    savedir=ann_path # lxml path
    cc.save_folder(img_save)
    cc.save_folder(img_label_save)
    cc.save_folder(savedir)
    cnt_save=faf(img_save)
    cnt_label=faf(img_label_save)
    obj=data
    object_label()
        
        
        
        
        

        
        
        
        
        
        
        
        