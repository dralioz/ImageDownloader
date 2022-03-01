# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:56:19 2020

@author: dralioz
"""

import pathlib
# 3- ilgili data klasöründe (en/tr) kaç dosya olduğunu bulan fonksiyon yaz.
# 4- bu modülü idlmv5'e entegre et.

data_dict={"airplane":"uçak","aircraft":"uçak",
           "ambulance":"ambulans","ball":"top",
           "belt":"kemer","bicycle":"bisiklet",
           "bird":"kuş","bus":"otobüs",
           "car":"araba","cat":"kedi",
           "dog":"köpek","dolphin":"yunus",
           "eagle":"kartal","elephant":"fil",
           "flag":"bayrak","turkish flag":"türk bayrağı",
           "horse":"At","human":"Insan",
           "laptop":"bilgisayar","motorcycle":"motorsiklet",
           "mouse":"fare","person":"insan",
           "auto":"araba","automobile":"araba",
           "rocket":"roket","stop sign":"dur tabelası",
           "taxi":"taksi","train":"tren",
           "watch":"kol saati","wheel":"tekerlek",
           "truck":"kamyon","no entry":"girilmez",
           "seat belt":"emniyet kemeri","volvo":"araba",
           "bmw":"araba","ford":"araba",
           "renault":"araba","mercedes":"araba",
           "audi":"araba","opel":"araba","aston martin":"araba",
           "bugatti":"araba","porsche":"araba","people":"insan",
           }

def find_amount_folder(data_folder):
    count=0
    for path in pathlib.Path(data_folder).iterdir():
        if path.is_file():
            count+=1
    return count
    print("data klasöründe kaç tane data olduğunu bul")
    print("indirme işlemlerinden sonra yapılan tüm isimlendirmeler için")
    print("Bulduğun değerin 1 fazlasını döndür")

def translate_data(data):
    data=data.lower()
    try:
        t_data=data_dict["{}".format(data)]
    except KeyError :
        return data
    return t_data





