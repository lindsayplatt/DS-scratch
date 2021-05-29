
# subset nc files to our area of interest 
import xarray as xr 
import numpy as np 
import pandas as pd 

#Go to this website and download the pr_ files first: https://www.northwestknowledge.net/metdata/data/

lats, lons = [30, 31], [-88, -87] 

for year in range(1979, 2022):
    file = 'pr_%s.nc' % year
    file_out = 'basin_prcp_%s.csv' % year 

    nc = xr.open_dataset(local_dir + file) 

    data = nc['precipitation_amount']

    data = data.loc[dict(lon = slice(lons[0], lons[1]))]
    data = data.loc[dict(lat = slice(lats[1], lats[0]))]

    mean_precip = np.mean(data, axis = (1,2))

    out = pd.DataFrame({'day': mean_precip['day'].values, 'prcp': mean_precip.values})
    # np.savetxt(file_out, out, delimiter=',')
    out.to_csv(file_out, index = False) 
