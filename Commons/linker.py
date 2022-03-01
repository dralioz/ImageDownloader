# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:25:28 2020

@author: dralioz
"""

# libraries and modules
import urllib
import random
import csv
from Websites.pikwizard import get_all_links as pik_gal
from Websites.istock import get_all_links as is_gal
from Websites.lifeofpix import get_all_links as life_gal
from Websites.dreams import get_all_links as dr_gal
from Websites.shutterstock import get_all_links as shut_gal
from Websites.bing import get_all_links as bing_gal
from Websites.google import get_all_links as google_gal

websites=["https://pikwizard.com",
          "https://www.istockphoto.com/tr",
          "https://www.lifeofpix.com/",
          "https://www.dreamstime.com/",
          "https://www.shutterstock.com/tr/",
          "https://www.bing.com/images/async?q=",
          "https://www.google.com/"]

uap=["/?q=","/foto%C4%9Fraflar/{}?phrase={}&sort=best",
     "search/{}?","search/"]

gg=["search?q=","&biw=1536&bih=674&tbm=","isch&sxsrf=ACYBGNSXXpS6Y",
    "mAKUiLKKBs6xWb4uUY5gA:","1581168823770&source=lnms&sa=X&ved=",
    "0ahUKEwioj8jwiMLnAhW9AhAIHbXTBMMQ_AUI3QUoAQ"]

uap2=["search.php?securitycheck=929029b445579eb7e1554e756dd89028&firstvalue=",
      "&lastsearchvalue=&srh_field=",
      "&s_all=y&s_ph=y&s_il=y&s_video=y&s_audio=y"]

pb=["&first","1","&count","&adlt","off","&aft"]

# url rewriter
def url_builder(data,i,*n_img):
    query=urllib.parse.quote_plus(data)
    n_img=str(n_img)
    urls=["{}".format(websites[0])+uap[0]+data,
          "{}".format(websites[1])+uap[1].format(data,data),
          "{}".format(websites[2])+uap[2].format(data),
          "{}".format(websites[3])+uap2[0]+data+uap2[1]+data+uap2[2],
          "{}".format(websites[4])+uap[3]+data,
          "{}".format(websites[5])+query+pb[0]+pb[1]+pb[2]+n_img+pb[3]+pb[4]+pb[5],
          "{}".format(websites[6])+gg[0]+query+gg[1]+gg[2]+gg[3]+gg[4]+gg[5]]
    return urls[i]

# shuffle links
def shuffle_and_get(links,n_img):
    random.shuffle(links)
    return links[:n_img]        

# collect links
def collect_all_links(data,n_img,agent):
    pik=pik_gal(data,n_img,url_builder(data,0),websites[0],agent)
    ist=is_gal(data, n_img, url_builder(data,1),websites[1],agent)
    life=life_gal(data,n_img,url_builder(data,2),websites[2],agent)
    dream=dr_gal(data,n_img,url_builder(data,3),websites[3],agent)
    shut=shut_gal(data,n_img,url_builder(data,4),websites[4],agent)
    bing=bing_gal(data,n_img,url_builder(data,5,n_img),websites[5],agent,pb)
    
    google=google_gal(data,n_img,url_builder(data,6),websites[6],agent)
    
    all_links=google+pik+ist+life+dream+shut+bing
    shuffled_links=shuffle_and_get(all_links,n_img)
    return shuffled_links














