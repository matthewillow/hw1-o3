#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:59:16 2019

@author: KiraMotiaOsia
"""
import json
import os
import matplotlib.pyplot as plt
from scipy.io import netcdf
import numpy as np

with netcdf.netcdf_file('MSR-2.nc', mmap=False) as netcdf_file:
    variables = netcdf_file.variables
    print(*variables, sep='\t' )
lat = 41.18
lon = 69.16
massivelon=variables['longitude'].data
massivelat=variables['latitude'].data
massivetime=variables['time'].data
gorodlon = np.searchsorted(massivelon, lon)
gorodlat = np.searchsorted(massivelat, lat)
#print(gorodlon,gorodlat)
massiveozon=variables['Average_O3_column'].data[:,gorodlat,gorodlon]
#print(massiveozon)

x = massivetime
y = massiveozon
fig = plt.figure()

plt.title('OZONE DENSITY IN TASHKENT')
plt.ylabel('Ozone density (Dobson units)')
plt.xlabel('Time (months)')

plt.plot(x, y,color='red',label='All data',alpha=0.4)
xja=x[0:5555:12]
yja=y[0:5555:12]
plt.plot(xja, yja,label='Janury data')
xju=x[5:5555:12]
yju=y[5:5555:12]
plt.plot(xju, yju,label='June data', color='green')
plt.savefig('ozon.png')
minall = min(y)
maxall = max(y)
avall = np.sum(y)/480
print(minall,maxall,avall)

minallja = min(yja)
maxallja = max(yja)
avallja = np.sum(yja)/40
print(minallja,maxallja,avallja)

minallju = min(yju)
maxallju = max(yju)
avallju = np.sum(yju)/40
print(minallju,maxallju,avallju)
M = {
  'city': 'Tashkent',
  'coordinates': [37.66, 55.77],
  'jan': {
    'min': 313.0,
    'max': 366.0,
    'mean': 340.1
  },
  'jul': {
    'min': 293.0,
    'max': 347.0,
    'mean': 313.8
  },
  'all': {
    'min': 267.0,
    'max': 388.0,
    'mean': 316.3
  }
}
with open('ozon.json', 'w') as f:
      json.dump(M,f)
      
#with open('happyness.json', 'r') as f:
#print(f.read())
#f.seek(0)
#p = json.load(f)
#rint(p['city'])
      






