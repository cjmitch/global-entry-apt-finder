# global-entry-apt-finder - Global Entry Appointment Finder

This python script uses the global entry scheduler api to find open apts within the next 30 days based on specified location ids from Global Entry Scheduler site and sends an email to desired address to notify of an opening. 


# Files

global-entry.py - python script

## How to use

There are many implementations on how to run the script concurrently throughout the day. The two I used was CronTab on a Mac and Google Cloud Function with Cloud Scheduler either one works however your computer will need to be running for CronTab to execute where Google Cloud allows you to be notified when not using your computer. 

[CronTab on Mac](https://betterprogramming.pub/how-to-execute-a-cron-job-on-mac-with-crontab-b2decf2968eb)
[Google Cloud Functions](https://cloud.google.com/spanner/docs/samples/spanner-functions-quickstart?hl=en)

*For cronjob / scheduler I set the interval to every minute.  I included a 5 minute wait time if an interview is found as to not spam emails of openings which can be modified if need but found that interview slots are picked up fast enough that it never resent the same opening with this threshold

For your preferred locations you will need to edit the script with the `locationId` of the locations you wish to query for. I found the locationId from using Chrome's Dev Tools to check the network requests for each location when using the Global Entry Scheduler.

e.g. `https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=1&**locationId=5002**&minimum=1` - 5002 is locationId for San Diego, CA

As well, you will need to create an app password for the gmail sender account in order to use the SMTP.

[Creating App Password for GMail](https://support.google.com/accounts/answer/185833?hl=en)

Hope this helps!