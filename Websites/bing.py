# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:03:12 2020

@author: dralioz
"""

import urllib
import urllib.request as ureq
import re
import posixpath
from Websites.Helper.help import check_from_csv

# get links
def get_links(url,agent):
    img_links=[]
    request=ureq.Request(url,None,headers=agent)
    response=ureq.urlopen(request)
    html=response.read().decode("utf-8")
    results=re.findall("murl&quot;:&quot;(.*?)&quot;",html)
    for result in results:
        if ".jpg" or ".jpeg" or ".png" in result:
            statu=check_from_csv(result) # csv kontrolü
            # Liste Kontrolü
            if statu!=0 or result in img_links:
                continue
            else:
                img_links.append(result)
    return img_links

# get all links
def get_all_links(data,n_img,url,web_url,agent,bing):
    query=urllib.parse.quote_plus(data)
    i=2 # diğer koddaki p_c değişkeni
    count=0
    links=get_links(url,agent)
    length=len(links)
    while(length<n_img):
        l2=length
        url=web_url+query+bing[0]+str(i)+bing[2]+str(n_img)+bing[3]+bing[4]+bing[5]
        new_links=get_links(url,agent)
        for link in new_links:
            links.append(link)
        length=len(links)
        i+=1
        if l2==length:
            count+=1
        if count==5:
            break
    if (length>n_img):
        n=length-n_img
        del links[-n:]
    print("Got {} {} links form bing".format(len(links),data))
    return links

# edit links (Don't use)
def edit_links(links):
    img_links=[]
    for link in links:
        path=urllib.parse.urlsplit(link).path
        filename=posixpath.basename(path).split("?")[0]
        file_type=filename.split(".")[-1]
        if file_type.lower() not in ["jpe","jpeg","jfif","exif",
                                      "tiff","gif","bmp","png","webp","jpg"]:
            file_type="jpg"
        img_links.append(link)
    return file_type, img_links

















        