#restart computer 

import os 
import glob 
import pandas as pd 
from datetime import datetime

os.chdir("C:\\Users\\a_colleague\\Desktop\\basin_prcp_scripts\\data")

# get files from 1979-2021 

pfiles = glob.glob('basin*')

pdata = pd.read_csv(pfiles[1])
pdata['prcp'] = round(pdata['prcp'], 2)
pdata['day'] = pd.to_datetime(pdata['day'])

for i in range(1, 42):
    # i = 2
    year = 1978 + i 

    current = pd.read_csv(pfiles[i])
    current['prcp'] = round(current['prcp'], 2) 
    current['day'] = pd.to_datetime(current['day'])

    pdata = pdata.append(current)


pdata['year'] = pdata['day'].dt.year

# plot annual total 
pdata_annual = pdata.groupby(['year']).sum()

import matplotlib.pyplot as plt

plt.plot(pdata_annual.index, pdata_annual['prcp'], 'o', color = 'black')
plt.xlabel('Year')
plt.ylabel('Annual precipitation, mm')
