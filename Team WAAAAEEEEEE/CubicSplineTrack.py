"""
This code is borrowed from Team Squeem
"""

#from IPython.core.display import display, HTML
#display(HTML("<style>.container { width:100% !important; }</style>")) # makes the notebook fill the whole window

#import matplotlib.pyplot as plt
import numpy as np
#import xarray as xr
import pandas as pd
import datetime
#import matplotlib as mpl
#import matplotlib.patches as patches
import datetime#, os, re, shutil

import pycubicspline

#from sklearn.preprocessing import MinMaxScaler

#from mpl_toolkits.basemap import Basemap

#import matplotlib.image as mpimg

#from glmtools.io.glm import GLMDataset

#from squeemtools.Graphing import MakeBigGraph

import warnings
warnings.filterwarnings("ignore")

def cubic_spline_trackfile(infile, outfile, minute_interval=10):
    '''Given a track file, calculate the cubic spline locations of the track file'''
    
    # Load the trackfile
    center = pd.read_csv(infile,header=None,names=["Year","Month","Day","Hour","Lat","Long","Min_Pressure","Max_Winds","Unused"],low_memory=False,sep='\t')
    center = center.drop("Unused",axis=1)
    
    # Prep the data for spline
    temp = center.copy()
    temp = temp.drop_duplicates(subset=['Lat', 'Long'], keep='first') # That way there aren't 2 points in the same location
    
    # Make tuples of the data
    myx, myy = temp['Long'],temp['Lat']
    real = center['Long'],center['Lat']
    coords = myx,myy
    
    # Create datetime from dataframe
    temp['Date'] = (temp['Year'].astype('string')+'-'+temp['Month'].astype('string')+'-'+temp['Day'].astype('string')+'-'+temp['Hour'].astype('string')).apply(pd.to_datetime,format="%Y-%m-%d-%H")
    temp.drop(['Year','Month','Day','Hour'],axis=1,inplace=True)
    temp = temp.sort_values('Date')
    
    # Create the new rows for every 10 minutes
    first_date = temp.iloc[0].Date
    last_date = temp.iloc[-1].Date
    
    # Get the number of samples
    total_minutes = (last_date - first_date).total_seconds() // 60
    samples = int(total_minutes / minute_interval) + 1
    
    # Calculate the cubic spline
    x,y,yaw,k,travel = pycubicspline.calc_2d_spline_interpolation(*coords,samples)
    
    # Plot the spline and the points
    """
    plt.figure(figsize=(20,20))
    plt.plot(x,y,lw=5,c='blue',label='cubic spline')
    plt.scatter(*real,s=100,c='red',zorder=3,label='actual points')
    plt.legend()
    plt.show()
    """
    
    # Create new list of dates
    dates = []
    for _ in range(len(x)):
        dates.append(first_date)
        first_date += datetime.timedelta(minutes = minute_interval)
    
    # Create the new dataframe
    sample = pd.DataFrame(np.array([dates,x,y]).T,columns=[['Date','Long','Lat']])
    sample.to_csv(outfile)
    return