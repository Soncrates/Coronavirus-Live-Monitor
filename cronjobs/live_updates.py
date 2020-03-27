"""
This file runs a basic cronjob every 10 minutes to send a request to a local Node.js server
which scrapes the WHO coronavirus site and gets a video URL of the latest virus press
release.

It then sends the scraped URL to a PHP server which writes that data to a JS file
for the site.
"""

import schedule
import requests
from datetime import date, datetime
from time import gmtime, strftime, sleep

# function to be run every 10 minutes
def update_current_cases():
    # send initial request to local Node.js server
    ret = "http://localhost:7001/"
    ret = requests.get(ret)
    if(ret.status_code != 200):
        print("ERROR: " + str(ret.status_code))
        return 1
    # send response (as GET variable) of that request to the PHP server
    finalRequest = requests.get("https://covid19.xtrp.io/server/get_live_updates.php?src=" + ret.text)
    if(finalRequest.status_code != 200):
        print("ERROR: " + str(finalRequest.status_code))
        return 1
    print("Success " + request.text)
    return 0
# run function
update_current_cases()

# run function every 10 minutes
schedule.every(10).minutes.do(update_current_cases)

while True:
    schedule.run_pending()
    sleep(30)
