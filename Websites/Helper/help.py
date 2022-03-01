# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:25:28 2020

@author: dralioz
"""

# libraries and modules
import pandas as pd
import csv
import time

# check from csv
def check_from_csv(link):
    df=pd.read_csv("Commons/links.csv")
    column=df.iloc[:,2:].values
    for row in column:
        row=str(row)
        length=len(row)
        row=row[2:length-2]
        if row==link:
            return 1
    return 0

# write to csv
def write2csv(data, links):
    for link in links:
        with open("Commons/links.csv","a",newline="") as csv_links:
            field=["date & time","data","links"]
            theWriter=csv.DictWriter(csv_links,fieldnames=field)
            theWriter.writerow({"date & time":"{}".format(time.asctime()),
                                "data":"{}".format(data),
                                "links":"{}".format(link)})
        csv_links.close()

# data counter
def data_control(data):
    df=pd.read_csv("Commons/links.csv")
    column=df.iloc[:,1:2].values
    count=0
    for row in column:
        row=str(row)
        length=len(row)
        row=row[2:length-2]
        if row==data:
            count+=1
        else:
            continue
    return count