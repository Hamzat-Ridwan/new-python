import numpy as np
# import urllib.request

climate_data = np.genfromtxt('DailyDelhiClimateTest.csv', delimiter=',', skip_header=1)
# climate_data = np.genfromtxt('Climate_data.xlsx', delimiter='', skip_header=1)

mul = climate_data @ np.array([1,1,1,1])
temp = climate_data[:, 0]
cat = np.concatenate((climate_data, mul.reshape(114, 1)), axis=1)
print(temp.min())
print(cat)

np.savetxt('Climate_results.csv', cat,delimiter=',' , fmt='%.2f', header='meantemp,humidity,wind_speed,meanpressure,yields', comments='')