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
        if 900 < time <= 940:
            time = ((time*0.262)+(time*0.264))/2
        elif 840 < time <= 900:
            time = time * 0.264 # y=0.219x + 41.3 works for this time range
        elif 800 < time <= 840:
            time = ((time*0.271)+(time*0.264))/2 #maybe instead of repeatedly adjusting the code here I can use some sort of a function generator to get this working
                                                 #will probably just test a piecewise function in Desmos 
        elif 780 < time <= 800:
            time = time * 0.271
        else:
            time = time * 0.262
    # elif distance == "10000m":
    # elif distance == "half-marathon":
    # elif distance == "marathon":
    return time



def convert1500mto800m(time):
    """converts 1500m time to 800m time"""
    totalseconds = time * 0.4907
    minutes = int(totalseconds // 60)
    seconds = ((totalseconds / 60) - minutes)*60
    seconds = round(seconds, 2)
    print(f"{minutes}:{seconds}")

#Jakob Kingebrigtsen
# convert1500mto800m(206.73)

def time_format(time):
    minutes = int(time // 60)
    seconds = ((time / 60) - minutes)*60
    seconds = round(seconds, 2)
    strseconds = str(seconds)
    if seconds == 0:
        strseconds = "00.00"
    elif True:
        if seconds < 10:
            strseconds = "0" + strseconds 
            if "." in strseconds[-2:]:
                strseconds = strseconds + "0"
        elif "." in strseconds[-2:]:
            strseconds = strseconds + "0"
    result = f"{minutes}:{strseconds}"
    return result

print(conversionhub(900, "5000m"))
# print(time_format(480))