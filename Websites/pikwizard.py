# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:35:43 2020

@author: dralioz
"""

# Libraries and modules
import requests
from bs4 import BeautifulSoup
from Websites.Helper.help import check_from_csv

# edit links
def edit_link(link,web_url):
    edit=link[-32:]
    link=web_url+"/photos/"+edit+"-l.jpg"
    return link

# get links 
def get_links(n_img, url, agent, web_url):
    img_links=[]
    r=requests.get(url, headers=agent).text
    soup=BeautifulSoup(r,"lxml")
    results=soup.find_all("div",attrs={"class":"row-container"})
    results=soup.find_all("div",attrs={"class":"photo-container"})
    results=soup.find_all("div",attrs={"class":"photo-overlay"})
    results=soup.find_all("a",attrs={"class":"photo-details-link"},limit=n_img)
    for result in results:
        link=result.get("href")
        link=edit_link(link,web_url)
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
    links=get_links(n_img,url,agent,web_url)
    length=len(links)
    while(length<n_img):
        l2=length
        url=web_url+"/?q="+data+"&page={}".format(i)
        new_links=get_links(n_img,url,agent,web_url)
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
    print("Got {} {} links from pikwizard".format(len(links),data))
    return links










