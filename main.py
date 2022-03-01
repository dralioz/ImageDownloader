# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 00:03:36 2020

@author: dralioz
"""

# Libraries and Modules

import Commons.CommonCodes as cc
import Introduction.Intro as get_builder
from Commons.linker import collect_all_links as picker
from Websites.Helper.help import write2csv as wtc
from Websites.Helper.help import data_control as dc
from show_label.Labelling import get_all_values_and_run as gavar
from show_label.Labelling import key_action
from Commons.TurkishProcess import translate_data
import sys

# Agent
usr_agent={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}

# main function
def main():
    cc.wel2us()
    datas,n_imgs=get_builder.get_data_infos()
    down_paths=get_builder.downloaded_path_builder(datas)
    for i in range(len(datas)):
        cc.usf_1(datas[i])
        prev_data_amount=dc(datas[i])
        links=picker(datas[i],n_imgs[i],usr_agent)
        wtc(datas[i],links)
        cc.usf_2(down_paths[i])
        cc.usf_3()
        cc.download_img_2(datas[i],links,down_paths[i],prev_data_amount)

        #print("To continue picking or labelling process press 'c' ")
        #print("To stop the program press 'e' ")
        #print("\rKey:",end="")
        #key_action()

        ## data=translate_data(datas[i])
        #data=datas[i] #lxml dosyasındaki ismi görmek için yaptım.
        #
        #print("\n",end="")
        #cc.countdown(3)
        #
        #print("\n All downloaded images will open with order")
        #print("Press 'c' to save\nPress 'e' to exit",
        #      "\nPress 'n' to pass next image")
        #print("If you want to label, just take object in box and press 'k' ")
        #save_path="Saved/Saved_images"+"/"+data
        #label_path="Saved/Labelling/images"+"/"+data
        #ann_path="Saved/Labelling/Annotations"+"/"+data
        #cc.countdown(5)
        #gavar(down_paths[i],save_path,label_path,ann_path,data)
    # print("exit()")
    sys.exit()

# runner
if __name__=="__main__":
    main()
