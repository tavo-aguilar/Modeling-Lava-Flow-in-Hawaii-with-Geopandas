# Modeling-Lava-Flow-in-Hawaii-with-Geopandas
Lava flow modeling in the state of Hawaii from the past


## Overview

- The island of Hawaii is a state with a number of active volacnos. To make this island habitable, the government has to plan accordingly where to make cities. Understanding lava flows and eruptions in the island helps filter places on areas to not build around. This project maps the island of Hawaii and models lava flow from a dataset provided by the website: https://www.navdat.org/NavdatSearch/Search.cfm . 

## Background

- To model the lava flow of Hawaii, we must take the data and load it into a geopandas dataframe. From there, we can generate figures to model the elavation levels of Hawaii. Once the elavation levels are modeled, we read in the flow polygons and convert them from UTM (Universal Transverse Mercator) to WGS84 (World Geodetic System 1984) to properly genrate figures for each flow. 

## Methods

- The code in this repository does utilize a number of packages to model the lava flow in Hawaii. The main ones will be numpy, pandas, matplotlib, geopandas, geoplot and cartropy. These packages are standard for most users wokring in Earth Science using python. The Earth can be filtered to a users liking to be able to study a particular region of interest (ROI), in which our case is Hawaii. We use geopandas to read in the datasets to first plot an outline for our ROI using the costline data.
  
- Next, a few figures of the elavation for our ROI will be useful to model lava flow. This is done by taking the elavation data and plotting it taking the elavation to be the z-coordinate. Another figure can be made by drawing contours instead of making one with color to represent higher elevations. We can use different commands to draw contours as close as we would want.
  
- The final step is to take the island data and use it to model lava flows on our generated figures. We must convert the UTM in the given data and convert it to WGS84 to be able to plot it on our figures. Once the data is converted, we are ready to plot and lava flows will show and are color coded by dates on the legend. 

## Results

- Now for the plots! The first one is a plot from the coastlines of Hawaii. The first plot generated should look like so:
  
  <img width="598" height="571" alt="Screenshot 2026-01-16 at 11 46 40 PM" src="https://github.com/user-attachments/assets/b14634e7-0c9f-43c1-ace2-b4591803f826" />

- The next plot is the elavation for our ROI, it is represented by having the darker colors at lower elevations and brighter colors at higher elevations. The following plot is generated:

  <img width="719" height="562" alt="Screenshot 2026-01-16 at 11 49 13 PM" src="https://github.com/user-attachments/assets/774077c9-67a3-4894-abce-7453cbe5aab9" />

- While having colors on the plot is nice to easier observe elevations for our ROI, contour plots are more useful when trying to display lava flows. The following figure is plotted from elavations of -5000 to 5000 in intervals of 1000:

  <img width="733" height="509" alt="Screenshot 2026-01-16 at 11 54 51 PM" src="https://github.com/user-attachments/assets/38c4cb7c-7b07-4195-b1f3-4ee152c0c83b" />

- The final plot is our lava flow model! After conversion of the data, we are now able to plot the lava flow in our ROI on our contour plot with intervals being set to 500 rather than 1000 like our other contour plot:

  <img width="659" height="559" alt="Screenshot 2026-01-16 at 11 58 56 PM" src="https://github.com/user-attachments/assets/a30b2292-196c-4096-85a8-fd875c1dd895" />

- The plots are consistant with what we would expect from lava flows in our ROI. Based on maps of Hawaii that already have lava flows shown, we have an accurate result from the data we plotted:

  ![HawaiiGuide-Big-Island-Map-2025-v1-alt-web](https://github.com/user-attachments/assets/803f70d8-624f-4ef8-b415-656215f4b07c)


## How to Run

1. Download all the data from the following folder in this drive: https://drive.google.com/drive/folders/1qlt1otxXMTUnnoVofBgBoEKjgdw9Qd86?usp=share_link . The .shp files proved difficult to upload, so I made a drive folder containing all the necessary data.

2. Make sure all required packages are installed: numpy, cartopy, geoplot, geopandas, matplotlib.pyplot, pandas. If any packages are missing, use the pip install [package] command into your IDE terminal to install required packages.

3. Once steps 1 and 2 are done, you can use the Hawaii.py file and run it. It is important to provide the right path to be given to the data to be able to properly load the data. Enjoy!

