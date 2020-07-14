#in this function we will be doing conversions
from datetime import datetime

#generate the timestamp
def timestamp():
    unformatted_time  =datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
    return formatted_time
