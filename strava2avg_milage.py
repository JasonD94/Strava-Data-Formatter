import pandas as pd
import sys
from datetime import datetime

"""
    This script will calculate the average milage for a given strava "activities.csv" export
    The average milage will be per week, over the last 8 weeks
"""

fields = ["Activity Date", "Distance"]

filePth = None

try:
    filePth = sys.argv[1]
except:
    print("No cmd args found! Running with default activities.csv file instead.\n")

# activities.csv is the default export name for LinkedIn Messages
activitiesDF = None

try:
    if filePth:
        print(filePth)
        activitiesDF = pd.read_csv(filePth, usecols=fields)
    else:
        activitiesDF = pd.read_csv("csv/activities.csv", usecols=fields)
except:
    print("\n\n!!!Error: you need to provide me with a activities.csv file from LinkedIn for me to parse!!\n\n")

    # Ye this is apparently not recommended but it doesn't quit the Idle shell on my Windows box so...
    raise SystemExit

# Collect distances within the last 8 weeks


for index, row in activitiesDF.iterrows():

    dateStr = str(row["Activity Date"])
    distance = float(row["Distance"]) / 1.609
    distanceFm = "{:.2f}". format(distance)

    print("%s: %s miles" % (dateStr, distanceFm))

    

    datetimeObj = datetime.strptime(dateStr, '%b %d, %Y, %I:%M:%S %p')
    print(datetimeObj)
