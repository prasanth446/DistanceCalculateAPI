import csv
import schedule
import time

from math import radians, cos, sin, asin, sqrt

# Taking one coordinate input values as a base. If needed this can be fetched from any other source also
lon1 = 5.604358
lat1 = 51.673471
lon2 = 5.547473487
lat2 = 51.72756055

# Calculating the Distance between a pair of points by using REST API function
def restapifn(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2]) # convert decimal degrees to radians
    # calculating the radian distance of Longitude and latitude
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
    result = c * r
    result = '\n' + str(result)
    return result


# Job to write the write/append the results from each run into rows of a CSV file
def job():
    distance = restapifn(lon1, lat1, lon2, lat2)
    with open("outfile.csv", 'a') as f:
        f.write(distance)


# Scheduler to run the Job for every 10 minutes automatically
def scheduler():
    schedule.every(10).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    scheduler()
