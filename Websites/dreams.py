# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:25:33 2020

@author: dralioz
"""

import requests
from bs4 import BeautifulSoup
from Websites.Helper.help import check_from_csv

# edit link
def edit_link(link):
    control_1="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
    control_2="//googleads.g.doubleclick.net/pagead/viewthroughconversion/1008246980/?value=0&guid=ON&script=0"
    if (control_1 in link or control_2 in link):
        return None
    else:
        return link

# get links
def get_links(n_img,url,agent):
    img_links=[]
    r=requests.get(url,headers=agent).text
    soup=BeautifulSoup(r,"lxml")
    results=soup.find_all("div",attrs={"class":"item-slide"})
    results=soup.find_all("a")
    results=soup.find_all("img",attrs={"class":"dt-image"},limit=n_img)
    for result in results:
        link=result.get("data-src")
        link=edit_link(link)
        if link==None:
            continue
        else:
            statu=check_from_csv(link)
            if statu!=0 or link in img_links:
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
        part_1="search.php?srh_field="
        part_2="&s_all=y&s_ph=y&s_il=y&s_video=y&s_audio=y&s_st=new&s_sm"
        part_3="=all&s_rsf=0&s_rst=7&s_mrg=1&s_sl0=y&s_sl1=y&s_sl2"
        part_4="=y&s_sl3=y&s_sl4=y&s_sl5=y&s_clc=y&s_clm=y&s_orp=y&s_ors="
        part_5="y&s_orl=y&s_orw=y&s_mrc1=y&s_mrc2=y&s_mrc3=y&s_mrc4=y&s_mrc5"
        part_6="=y&s_exc=&pg={}".format(i)
        url=web_url+part_1+data+part_2+part_3+part_4+part_5+part_6
        new_links=get_links(n_img, url, agent)
        for link in new_links:
            links.append(link)
        length=len(links)
        i+=1
        if l2==length:
            count+=1
        if count==1:
            break
    if (length>n_img):
        n=length-n_img
        del links[-n:]
    print("Got {} {} links from dreamstime".format(len(links),data))
    return links













