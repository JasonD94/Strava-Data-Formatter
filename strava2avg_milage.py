import pandas as pd
import sys
from datetime import datetime
from datetime import timedelta

"""
    This script will calculate the average milage for a given strava "activities.csv" export
    The average milage will be per week, over the last 8 weeks

    TODO: make an input "weeks", then do the calculation based on that
    TODO: then figure out the average for various week periods, like 2 vs 4 vs 8 vs 20 weeks
"""

fields = ["Activity Date", "Distance", "Activity Type"]

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

# Collect distances within the last 8 weeks, so use a time obj that's set to a day
# 8 weeks ago for comparsion later
td = timedelta(days=56)
dtEight = datetime.today() - td
print(dtEight)

milageSum = 0

for index, row in activitiesDF.iterrows():

    dateStr = str(row["Activity Date"])
    distance = float(row["Distance"]) / 1.609
    distanceFm = "{:.2f}". format(distance)

    # DON'T FORGET TO FILTER OUT NON-RIDE ACTIVITIES!
    # Otherwise stuff like hiking/kayaking/walking/etc will get counted!
    activityType = str(row["Activity Type"])

    # Parse datetime
    datetimeObj = datetime.strptime(dateStr, '%b %d, %Y, %I:%M:%S %p')

    # If datetime is in the past 8 weeks range, and it's a ride type activity, sum up it's milage
    if datetimeObj > dtEight and activityType == "Ride":

        milageSum += float(distanceFm)

        # Debug prints
        print("%s: %s miles | milageSum = %.2f" % (dateStr, distanceFm, milageSum))
        print(datetimeObj)

# Moment of truth: divide by 8, get the average milage over the last 8 weeks!
avgMilage = milageSum / 8
print("Average milage over the last 8 weeks was: %.2f miles" % avgMilage)
