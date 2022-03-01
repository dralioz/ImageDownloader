# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 23:17:35 2020

@author: dralioz
"""

import requests
from bs4 import BeautifulSoup
from Websites.Helper.help import check_from_csv

# edit links
def edit_link(link):
    add="2048x2048"
    link=link.replace("?k=","?s=")
    index=link.find("?s=")+3
    link=link[:index]+add
    return link
    

# get links
def get_links(n_img,url,agent):
    img_links=[]
    r=requests.get(url,headers=agent).text
    soup=BeautifulSoup(r,"lxml")
    results=soup.find_all("div",attrs={"class":"search-content__gallery-assets"})
    results=soup.find_all("gi-asset",attrs={"class":"gallery-mosaic-asset"})
    results=soup.find_all("article",attrs={"class":"gallery-mosaic-asset__container"})
    results=soup.find_all("a",attrs={"class":"gallery-mosaic-asset__link"})
    results=soup.find_all("figure",attrs={"class":"gallery-mosaic-asset__figure"})
    results=soup.find_all("img",attrs={"ng-class":"thumbClassNames"},limit=n_img)
    for result in results:
        link=result.get("src")
        if link==None:
            continue
        else:
            link=edit_link(link)
            statu=check_from_csv(link)
            if statu!=0:
                continue
            else:
                img_links.append(link)
    return img_links

# get all links
def get_all_links(data,n_img,url,web_url,agent):
    i=2
    count=0
    links=get_links(n_img,url,agent)
    length=len(links)
    while(length<n_img):
        l2=length
        part2="/foto%C4%9Fraflar/{}?page={}&phrase={}&sort=best".format(data,i,data)
        url=web_url+part2
        new_links=get_links(n_img,url,agent)
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
    print("Got {} {} links from istock.tr".format(len(links),data))
    return links






