library(dplyr)
library(ncdf4)
setwd("C:\\Users\\a_colleague\\Desktop\\basin_prcp_scripts\\data")

#Go to this website and download the pr_ files first: https://www.northwestknowledge.net/metdata/data/

pfiles <- list.files(pattern = "*.nc")

for(i in 1:42){
  year <- i + 1978
  nc_file <- nc_open(pfiles[i])
  #I figured out that these cells cover our basin
  prcp_3d <- ncvar_get(nc_file, varid = 'precipitation_amount', start = c(155, 229, 1),
                       count = c(10,15, -1))
  prcp_avg <- apply(prcp_3d, MARGIN = 3, FUN = mean)
  write.csv(file = paste('basin_prcp_', year, '.csv', sep = ''), x = prcp_avg)
}
