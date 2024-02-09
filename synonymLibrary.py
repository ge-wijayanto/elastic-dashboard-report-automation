import getTime as getTime

current_utc_time, old_utc_time = getTime.getTimeUTC()
current_local_time, old_local_time = getTime.getTimeLocal()

# [0 - 6], 0 = Monday
def getSynonymDay(day_name):
    synonyms = {
        0: "Monday", 
        1: "Tuesday", 
        2: "Wednesday", 
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }

    return synonyms.get(day_name, "Invalid day of week")

# [1 - 12], 1 = Jan
def getSynonymMonth(month_name):
    synonyms = {
        1: "January", 
        2: "February", 
        3: "March", 
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "Augustus",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    return synonyms.get(month_name, "Invalid month")

synonym_of_day = getSynonymDay(current_local_time.tm_wday)
synonym_of_month = getSynonymMonth(current_local_time.tm_mon)
date = current_local_time.tm_mday
year = current_local_time.tm_year
current_local_clock = current_local_time.tm_hour
old_local_clock = old_local_time.tm_hour