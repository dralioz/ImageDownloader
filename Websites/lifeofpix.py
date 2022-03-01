# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:57:04 2020

@author: dralioz
"""

import requests
from bs4 import BeautifulSoup
from Websites.Helper.help import check_from_csv

# edit link
def edit_link(link,agent):
    r=requests.get(link,headers=agent).text
    soup=BeautifulSoup(r,"lxml")
    result=soup.find("div",attrs={"class":"node"})
    result=soup.find("img",attrs={"id":"pic","class":"img-low-to-high"})
    link=result.get("data-src")
    return link

# get links
def get_links(n_img,url,agent):
    img_links=[]
    r=requests.get(url,headers=agent).text
    soup=BeautifulSoup(r,"lxml")
    results=soup.find_all("div",attrs={"class":"page"})
    results=soup.find_all("div",attrs={"class":"container"})
    results=soup.find_all("div",attrs={"class":"img-grid"})
    results=soup.find_all("div",attrs={"class":"node show reveal"})
    results=soup.find_all("a",attrs={"class":"clickarea"},limit=n_img)
    for result in results:
        link=result.get("href")
        link=edit_link(link,agent)
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
    while (length<n_img):
        l2=length
        url=web_url+"search/"+data+"/{}/?".format(i)
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
    print("Got {} {} links from lifeofpix".format(len(links),data))
    return links









        