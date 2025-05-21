import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)

print(air_quality.head())

#Plot of the entire DF
#air_quality.plot()


#air_quality.station_paris.plot()
air_quality["station_london_mg_per_cb"] = air_quality["station_london"] * 1.882
print(air_quality)