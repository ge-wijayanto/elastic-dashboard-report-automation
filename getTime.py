import time
import datetime

## Example of URL Query
# Local Time -> 06:00:00.000 - 09:00:00.000 (UTC +7)
# URL -> https://<Elastic URL>?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:'2023-08-15T23:00:00.000Z',to:'2023-08-16T02:00:00.000Z'))
# UTC is used for URL Query

# UTC Time Grabber
def getTimeUTC():
    current_utc_time = time.gmtime()

    current_datetime_utc = datetime.datetime.fromtimestamp(time.mktime(current_utc_time))

    # Current UTC Time - 3 Hours (Hourly Interval)
    three_hours_before_utc = current_datetime_utc - datetime.timedelta(hours=3)

    old_utc_time = three_hours_before_utc.utctimetuple()

    return current_utc_time, old_utc_time

# Local Time Grabber
def getTimeLocal():
    current_local_time = time.localtime()

    current_datetime_local = datetime.datetime.fromtimestamp(time.mktime(current_local_time))

    # Current Local Time - 3 Hours (Interval)
    three_hours_before_local = current_datetime_local - datetime.timedelta(hours=3)

    old_local_time = three_hours_before_local.utctimetuple()

    return current_local_time, old_local_time