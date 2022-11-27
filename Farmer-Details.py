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
    url = "http://bhunaksha.raj.nic.in/bhunaksha/ScalarDatahandler?OP=4&state=08&levels=01,002,0745,02920,11035,001,&base_x=0&base_y=0&x="+str(coord[0])+"&y="+str(coord[1])
    response = requests.get(url).text
    response = json.loads(response)
    return response
def get_each_khasra_number():
    path  = "D:\Agribazaar Cadastral Data work\Vectorization\अजमेर\मसूदा\किराप\कालाहेडी\कालाहेडी/कालाहेडी_Points.shp"
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
    with open("D:\Agribazaar Cadastral Data work\Vectorization\अजमेर\मसूदा\किराप\कालाहेडी\कालाहेडी/output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(resp_list)
if _name=='main_':
    get_each_khasra_number()