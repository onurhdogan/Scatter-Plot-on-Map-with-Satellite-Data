# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stations = pd.read_excel('/home/onurhdogan/Desktop/van/Tr_stations.xlsx')

lat  = stations['lat'].values
lon = stations['lon'].values
Temperature = stations['value'].values

fig = plt.figure(figsize=(8,8))
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)

m = Basemap(resolution='i',projection='cyl',\
    llcrnrlon=26.0,llcrnrlat=35.8,\
    urcrnrlon=36.3,urcrnrlat=42.3)

m.arcgisimage(service="ESRI_Imagery_World_2D", xpixels = 3500, dpi=500, verbose= True)

m.drawcoastlines(color='black')
m.drawcountries(color='black')
m.drawstates(color='black')

m.scatter(lon, lat, latlon=True,
          c=Temperature,s=160,
          cmap='jet')

plt.colorbar().set_label(label='Temperature',size=17,weight='bold')
plt.title("Temperature Scatter Plot with High Res Satellite Data",fontsize = 21 )

lats = list(lat)
lons = list(lon)

x,y = m(lons, lats)
labels = stations['name']

for label, xpt, ypt in zip(labels, x, y):
    plt.text(xpt+0.03, ypt-0.015, label,fontsize=16, alpha=1,color="white")

fig.savefig("/home/onurhdogan/Desktop/van/Tr_temp.png", dpi=300)
