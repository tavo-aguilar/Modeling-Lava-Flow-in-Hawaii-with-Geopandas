import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cartopy.crs as ccrs
from cartopy.feature import NaturalEarthFeature, LAND, COASTLINE, OCEAN, LAKES, BORDERS
from cartopy import feature as cfeature
import geoplot.crs as gcrs

import geopandas as gpd
import geoplot as gplt

import matplotlib.tri as tri

# Dataset download can be found in this link: https://drive.google.com/drive/folders/1qlt1otxXMTUnnoVofBgBoEKjgdw9Qd86?usp=share_link

# read in the data as a geopandas dataframe
hawaii=gpd.read_file('/Users/gustavoaguilar/Downloads/Datasets for Python Earth/Coastline.shp')

#Select only the data from island called "Hawaii".
bigIsland=hawaii[(hawaii.isle=='Hawaii')]
fig, ax = plt.subplots(figsize=(8,6)) # make fig and ax objects
#Set the ocean to blue.
ax.set_facecolor('lightblue')
# plot the polygons from the geometry column
bigIsland.plot(ax=ax,edgecolor='black',linewidth=1,facecolor='lightgreen')
plt.title("Island of Hawaii")

fig, ax = plt.subplots(figsize=(8,6))
# read in the elevation data as a Pandas DatFrame.
bigIslandElev=pd.read_csv('/Users/gustavoaguilar/Downloads/Datasets for Python Earth/BigIslandElev.csv')
# plot longitude as x, latitude as y and elevation as z:
x=bigIslandElev.lon.values
y=bigIslandElev.lat.values
z=bigIslandElev.elevation.values
plt.title("Elevation")
ax.tricontourf(x,y,z)

fig, ax = plt.subplots(figsize=(8,6))
#Setting the ocean to blue.
ax.set_facecolor('lightblue')
bigIsland.plot(ax=ax,edgecolor='black',linewidth=1,facecolor='lightgreen')
plt.title("Contour plot of Hawaii")
ax.tricontour(x,y,z,colors='k',linewidths=1,levels=np.arange(-5000,5000,1000));

#Set Conversion Strings
UTM4='+proj=utm +zone=4 +ellps=GRS80 +datum=NAD83 +units=m'
WGS84='+proj=longlat +ellps=WGS84 +datum=WGS84'

#Get Big Island Flows in UTM
bigIslandFlows=gpd.read_file('/Users/gustavoaguilar/Downloads/Datasets for Python Earth/BigIslandData.shp',crs=UTM4)

#Converting between coordinate systems 
bigIslandFlows=gpd.read_file('/Users/gustavoaguilar/Downloads/Datasets for Python Earth/BigIslandData.shp',crs=UTM4).to_crs(WGS84)  # convert to WGS84

fig, ax = plt.subplots(figsize=(8,6))
#Setting the ocean to blue.
ax.set_facecolor('lightblue')
bigIsland.plot(ax=ax,edgecolor='black',linewidth=1,facecolor='lightgreen')

ax.tricontour(x,y,z,colors='k',linewidths=1,levels=np.arange(-5000,5000,500))

# now the flow polygons:
bigIslandFlows.plot(ax=ax,column='Ages',cmap='magma',legend=True,legend_kwds={'label':'Date of Eruption (A.D.)'})
plt.xlim(-156.2,-154.8)
plt.title("Lava Flows in Hawaii")
plt.show()
