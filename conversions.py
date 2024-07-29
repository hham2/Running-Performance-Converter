def conversionhub(time, distance):
    """
    converts user-input time to an equivalent 1500m time, from 
    which all other conversions will be made so as to not have
    to make functions for every possible combination of input 
    distances and output distances
    """
    #temp code begins
    print(time_format(time))
    #temp code ends
    if distance == "800m":
        time = time * 2.038
    elif distance == "1600m":
        time = time * 0.934
    elif distance == "3000m":
        time = time * 0.463
    elif distance == "3200m":
        time = time * 0.434
    elif distance == "5000m":
        time = convert5000mto1600m(time)
    # elif distance == "10000m":
    # elif distance == "half-marathon":
    # elif distance == "marathon":
    return time



def convert5000mto1600m(time):
    """
    uses a piecewise function I made to convert a 5000m time to a roughly equivalent
    1600m time
    """
    x = time
    if time < 780:
        output = 0.36*x - 50.9
    elif 780 < time <= 840:
        output = 0.1833333*x + 87
    elif 840 < time <= 900:
        output = 0.18333333*x + 87
    elif 900 < time <= 960: #I think my conversions in this range are a little too generous
        output = 0.2*x + 72
    elif 960 < time <= 1020:
        output = 0.2166666*x + 56
    elif 1020 < time <= 1080:
        output = 0.3*x - 29
    elif 1080 < time <= 1140:
        output = 0.28333333*x - 11
    elif 1140 < time <= 1200: 
        output = 0.4333333*x - 182
    else:
        output = 0.33333*x - 62
    return output
    
#Jakob Kingebrigtsen
# convert1500mto800m(206.73)

def time_format(time):
    minutes = int(time // 60)
    seconds = ((time / 60) - minutes)*60
    seconds = round(seconds, 2)
    strseconds = str(seconds)
    if seconds == 0:
        strseconds = "00.00"
    else:
        if seconds < 10:
            strseconds = "0" + strseconds 
            if "." in strseconds[-2:]:
                strseconds = strseconds + "0"
        elif "." in strseconds[-2:]:
            strseconds = strseconds + "0"
    result = f"{minutes}:{strseconds}"
    return result

print(time_format(conversionhub(952, "5000m")))
# print(time_format(480))