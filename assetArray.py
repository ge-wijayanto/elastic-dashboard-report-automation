import synonymLibrary as synonym
import getTime as getTime

current_utc_time, old_utc_time = getTime.getTimeUTC() # Get UTC Time for query ranges in the URL
current_local_time, old_local_time = getTime.getTimeLocal() # Get Local System Time

# Target Dashboard URL 
target_link = [
    # Target Dashboard 1 - Elastic
    f"https://<Elastic Dashboard URL>?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:'{getTime.time.strftime('%Y-%m-%dT%H:00:00.000Z', old_utc_time)}',to:'{getTime.time.strftime('%Y-%m-%dT%H:00:00.000Z', current_utc_time)}'))",
    # Target Dashboard 2 – Elastic
    f"https://<Elastic Dashboard URL>?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:'{getTime.time.strftime('%Y-%m-%dT%H:00:00.000Z', old_utc_time)}',to:'{getTime.time.strftime('%Y-%m-%dT%H:00:00.000Z', current_utc_time)}'))",
    # ...
    # Target Dashboard n - Elastic
    f"https://<Elastic Dashboard URL>?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:'{getTime.time.strftime('%Y-%m-%dT%H:00:00.000Z', old_utc_time)}',to:'{getTime.time.strftime('%Y-%m-%dT%H:00:00.000Z', current_utc_time)}'))"
]

# File Name for Each Retrieved Dashboards
image_paths = [
    # Target Dashboard 1
    "path/to/file/Report1.png",
    # Target Dashboard 2
    "path/to/file/Report2.png",
    # ...
    # Target Dashboard n
    "path/to/file/Reportn.png"
]

# Captions to be included in WhatsApp messages for reporting (Optional)
caption = [
    f"Report Title 1\n{synonym.synonym_of_day}, {synonym.date} {synonym.synonym_of_month} {synonym.year} {synonym.old_local_clock}:00 - {synonym.current_local_clock}:00 WIB",
    f"Report Title 2\n{synonym.synonym_of_day}, {synonym.date} {synonym.synonym_of_month} {synonym.year} {synonym.old_local_clock}:00 - {synonym.current_local_clock}:00 WIB",
    # ...
    f"Report Title n\n{synonym.synonym_of_day}, {synonym.date} {synonym.synonym_of_month} {synonym.year} {synonym.old_local_clock}:00 - {synonym.current_local_clock}:00 WIB"
]