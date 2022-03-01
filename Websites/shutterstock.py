# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:35:12 2020

@author: dralioz
"""

import requests
from bs4 import BeautifulSoup
from Websites.Helper.help import check_from_csv

# edit link
def edit_link(link):
    try:
        edit=link.replace("260nw","600w")
    except AttributeError as exception:
        print(exception)
        pass
    return edit

# get links
def get_links(n_img,url,agent):
    img_links=[]
    r=requests.get(url,headers=agent).text
    soup=BeautifulSoup(r,"lxml")
    results=soup.find_all("div",attrs={"class":"z_g_d65b1"})
    results=soup.find_all("div",attrs={"class":"z_g_63ded"})
    results=soup.find_all("div",attrs={"class":"z_h_b900b"})
    results=soup.find_all("a",attrs={"class":"z_h_81637"})
    results=soup.find_all("img",attrs={"class":"z_h_9d80b"},limit=n_img)
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
        url=web_url+"search/"+data+"?page={}".format(i)
        new_links=get_links(n_img, url, agent)
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
    print("Got {} {} links from shutterstock".format(len(links),data))
    return links













            