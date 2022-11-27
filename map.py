import csv
import sys
import requests
import json
import os
import time
import numpy as np
import matplotlib.pyplot as plt

# download image via multithreading
# skip download process for N/A data need to make check



import math
import os
import sys
import PIL
from PIL import Image
import threading
import shapefile
raj_district = ["01 अजमेर",]

def hit_khasra_number_url(coord):
    url = "https://bhunaksha.raj.nic.in/WMS?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&FORMAT=image%2Fpng&TRANSPARENT=true&LAYERS=VILLAGE_MAP&transparent=true&state=08&gis_code=0100207450292011046001&overlay_codes=&CRS=EPSG%3A3857&STYLES=VILLAGE_MAP&FORMAT_OPTIONS=dpi%3A101&WIDTH=1749&HEIGHT=1231&BBOX=452952.6480322401%2C2921579.7708080965%2C456664.62121833896%2C2924191.7673840285"+str(coord[0])+"&y="+str(coord[1])
    response = requests.get(url).text
    response = json.loads(response)
    return response


def get_each_khasra_number():
    path  = r"C:\Users\didel\Downloads\python codefor data downloding\shapfile\कालाहेडी_Points.shp"
    shape = shapefile.Reader(path)
    #first feature of the shapefile
    resp_list = []
    for each_feature in shape.shapeRecords():
        time.sleep(2)
        data = each_feature.shape._geo_interface_
        print(data)
        resp  = hit_khasra_number_url(data['coordinates']) 
        data['khasra_no'] = resp['plotnumber']
        data['info'] = resp['info']
        resp_list.append(list(data.values()))
    print(resp_list)
    with open(r"C:\Users\didel\Downloads\python codefor data downloding\shapfile\output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(resp_list)

if _name=='main_':
    get_each_khasra_number()