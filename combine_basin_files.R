# restart computer
setwd("C:\\Users\\a_colleague\\Desktop\\basin_prcp_scripts\\data")

library(dplyr)
library(data.table)

pfiles <- list.files(pattern = 'basin')

pdata <- fread(pfiles[1])
colnames(pdata) <- c('day', 'prcp')
pdata <- round(pdata,2)
pdata$date <- as.numeric(pdata[,1][[1]])
pdata$date <- as.Date(pdata$date, origin = "1979-01-01")

for(i in 2:42){
  # i = 2
  year <- 1978 + i
  current <- fread(pfiles[i])

  colnames(current) <- c('day', 'prcp')
  current <- round(current,2)
  current$date <- as.numeric(current[,1][[1]])
  current$date <- as.Date(current$date, origin = paste(year, "-01-01", sep = ''))
  pdata <- rbind(pdata, current)
}

#plot annual total
pdata_annual <- group_by(pdata, year(date)) %>%
  summarize(total_prcp = sum(prcp))

plot(pdata_annual$`year(date)`, pdata_annual$total_prcp,
     xlab = 'Year', ylab = 'Annual precipitation, mm')
