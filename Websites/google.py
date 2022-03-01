# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:48:57 2020

@author: dralioz
"""

# Libraries
from urllib.parse import quote
import requests
import urllib.request as ureq
from Websites.Helper.help import check_from_csv

# edit link
def edit_link(link):
    index=link.find(".jpg" or ".png")
    if index==-1:
        index=link.find(".jpeg")
        link=link[:index+5]
        return link
    else:
        link=link[:index+4]
        return link

# editting
def edit_links(rdata,n_img):
    end_object=-1
    extensions={".jpg",".png",".jpeg"}
    google_image_seen=False
    img_links=[]
    for i in range(n_img):
        while (True):
            try:
                new_line=rdata.find('"https://',end_object + 1)
                end_object=rdata.find('"',new_line + 1)
                buffor=rdata.find("\\",new_line + 1,end_object)
                if buffor!=-1:
                    img_link=(rdata[new_line + 1 :buffor])
                else:
                    img_link=(rdata[new_line + 1:end_object])
                
                if any(extension in img_link for extension in extensions):
                    break
            except Exception:
                break
        img_link=edit_link(img_link)
        statu=check_from_csv(img_link)
        if statu!=0 or img_link in img_links:
            i-=1
            continue
        else:
            img_links.append(img_link)
    return img_links

# get links
def get_all_links(data,n_img,url,web_url,agent):
    req=ureq.Request(url,headers=agent)
    r=ureq.urlopen(req)
    rData=str(r.read())
    img_links=edit_links(rData,n_img)
    print("Got {} {} links form google".format(len(img_links),data))
    return img_links




