"""
retrieves air pollution data daily from https://www.londonair.org.uk/Londonair/API/
"""
import requests
import json
import os

from datetime import date, timedelta

from paths.get_root_path import root_path

def air_quality(retrieval_date: date):
    """ Retrieve hourly airquality data and dump to JSON """
    previous_date = retrieval_date - timedelta(days=1)

    baseurl = "https://api.erg.ic.ac.uk/AirQuality"
    url = f"{baseurl}/Data/Site/SiteCode=CT3/StartDate={previous_date}/EndDate={retrieval_date}/Json"
    response = requests.get(url)
    filename = f"CT3_aq_{str(previous_date)}.json"
    with open(f"{root_path()}/data/raw/air_quality/{filename}", "w") as file:
        json.dump(response.json(), file)



if __name__ == "__main__":
    todays_date = date.today()
    air_quality(todays_date)
