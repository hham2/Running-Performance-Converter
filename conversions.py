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
    
    return time

def convert_marathon_to_halfmarathon(time):
    """
    uses a piecewise function to convert a marathon time to
    a roughly equivalent half marathon time; can be used to convert half marathon
    time to an equivalent time at a different distance via a second function
    """
    if time <= 7480:
        output = 0.552*time - 559.36
    elif 7480 < time <= 8200:
        output = 0.375*time + 764.6
    elif 8200 < time <= 8920:
        output = 0.51666666*time - 602.0666666
    elif 8920 < time <= 9640:
        output = 0.48333333*time + 141.2666666
    elif 9640 < time <= 10360:
        output = 0.41666666*time + 542.9333333
    elif 10360 < time <= 11080:
        output = 0.5*time - 320.4
    elif 11080 < time <= 12600:
        output = 0.395*time + 843
    else:
        output = 0.4333333*time + 360
    return output

def convert_halfmarathon_to_10000m(time):
    """
    uses a piecewise function to convert a half marathon time to
    a roughly equivalent 10000m time; can be used to convert half marathon
    time to an equivalent time at a different distance via a second function
    """
    if time <= 3540:
        output = 0.41666666*time + 135
    elif 3540 < time <= 3600:
        output = 0.5*time - 160
    elif 3720 < time <= 3840:
        output = 0.58333333*time - 480
    elif 3840 < time <= 4200:
        output = 0.36111*time + 373.33333
    elif 4200 < time <= 4560:
        output = 0.333333*time + 490
    elif 4560 < time <= 4920:
        output = 0.5*time - 270
    elif 4920 < time <= 5640: 
        output = 0.41666666*time + 140
    elif 5640 < time <= 6000:
        output = 0.5*time - 330
    else:
        output = 0.58333333*time - 830
    return output


def convert_10000m_to_5000m(time):
    """
    uses a piecewise function to convert a 10000m time to a roughly equivalent
    5000m time; can be used to convert 10000m time to an equivalent time at 
    a different distance via a second function
    """
    if time <= 1620:
        output = 0.6333333*time - 241
    elif 1620 < time <= 1680:
        output = 0.41666666*time + 110
    elif 1680 < time <= 1800:
        output = 0.458333333*time + 40
    elif 1800 < time <= 1920:
        output = 0.5*time - 35
    elif 1920 < time <= 2280:
        output = 0.458333333*time + 45
    elif 2280 < time <= 2520:
        output = 0.41666666*time + 140
    else:
        output = 0.541666666*time - 175
    return output

def convert_5000m_to_1600m(time):
    """
    uses a piecewise function I made to convert a 5000m time to a roughly equivalent
    1600m time
    """
    if time < 780:
        output = 0.28*time + 10.5936
    elif 780 < time <= 840:
        output = 0.25*time + 33.9936
    elif 840 < time <= 900:
        output = 0.2333333*time + 47.9936003
    elif 900 < time <= 960: 
        output = 0.1*time + 167.9936
    elif 960 < time <= 1020:
        output = 0.2166666*time + 56
    elif 1020 < time <= 1080:
        output = 0.3*time - 29
    elif 1080 < time <= 1140:
        output = 0.28333333*time - 11
    elif 1140 < time <= 1200: 
        output = 0.4333333*time - 182
    else:
        output = 0.33333*time - 62
    return output

def convert_3200m_to_1600m(time):
    """
    converts a 3200m time to a roughly equivalent
    1600m time; can be used to convert 3200m time to an equivalent time at 
    a different distance via a second function
    """
    if time <= 480:
        output = 0.444444*time - 61.1333333
    elif 480 < time <= 500:
        output = 0.6*time - 137.8
    elif 500 < time <= 520:
        output = 0.34*time - 7.8
    elif 520 < time <= 560:
        output = 0.45*time - 65
    elif 560 < time <= 600:
        output = 0.4*time - 37
    elif 600 < time <= 660:
        output = 0.3666666*time - 17
    elif 660 < time <= 720:
        output = 0.58333333*time - 160
    elif 720 < time <= 780:
        output = 0.41666*time - 40
    elif 780 < time <= 900:
        output = 0.5*time - 105
    else:
        output = 0.41666666*time - 30

def convert_3200m_to_3000m(time):
    """
    converts a 3200m time to a roughly equivalent
    3000m time
    """
    output = time * 0.932
    return output

def convert_1600m_to_mile(time):
    """
    converts a 1600m time to a roughly 
    equivalent mile (1609.344m) time
    """
    output = time * 1.0063
    return output

def convert_1600m_to_1500m(time):
    """
    converts a 1600m time to a roughly
    equivalent 1500m time
    """
    output = time * 0.932
    return output

def convert_1600m_to_800m(time):
    """
    uses a piecewise function to convert a 1600m time
    to a very roughly equivalent 800m time (since 800m
    conversions are difficult to predict due
    to the difficulty of training speed endurance relative
    to the more effective means we have of training endurance
    in athletes)
    """
    if time <= 225:
        output = 0.471*time - 3.225
    elif 225 < time <= 230:
        output = 0.35*time + 24
    elif 230 < time <= 240:
        output = 0.5*time - 10.5
    elif 240 < time <= 250:
        output = 0.35*time + 25.5
    elif 250 < time <= 260:
        output = 0.5*time - 12
    elif 260 < time <= 280:
        output = 0.35*time + 27
    elif 280 < time <= 300:
        output = 0.4*time + 13
    elif 300 < time <= 320:
        output = 0.45*time - 2
    elif 320 < time <= 340:
        output = 0.3*time + 46
    elif 340 < time <= 360:
        output = 0.35*time + 29
    elif 360 < time <= 380:
        output = 0.75*time - 115
    else: 
        output = 0.65*time - 77
    return output

def time_format(time):
    """
    formats a time input as the number of seconds to a 
    hh:mm:ss time format, where the "hh" component is omitted
    if the total time equates to less than 1 hour
    """
    minutes = int(time // 60)
    seconds = ((time / 60) - minutes)*60
    seconds = round(seconds, 2)
    strseconds = str(seconds)
    if time < 60: #configuration for times under 60 seconds; omits hours and minutes display
        if time < 10:
            strseconds = "0" + strseconds
        if "." in strseconds[-2:]:
            strseconds += "0"
        result = strseconds
    elif time < 3600: #configuration for times under 1 hour; omits hours display
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
    else: #configuration for times over 1 hour
        hours = int(time // 3600)
        strhours = str(hours)
        minutes = int((time // 60)-(hours*60))
        strminutes = str(minutes)
        if hours < 10:
            strhours = "0" + str(hours)
        if minutes == 0 and seconds == 0:
            strminutes = "00"
            strseconds = "00.00"
        else:
            if minutes == 0:
                strminutes = "00"
            if seconds == 0:
                strseconds = "00.00"
        #These conditions check if the minutes column has less than two values and uses the placement of "." to determine if a zero
        #needs to be added to the seconds columns or tenths/hundredths columns to ensure that there are always 11 characters
        #when the total time is over 1 hour in length
        if len(strminutes) != 2 and "." in strseconds[0:2]: #the only scenario where this'd be true is one where the minutes value is less than 10
            strminutes = "0" + strminutes
            strseconds = "0" + strseconds
        elif "." in strseconds[0:2] and len(strminutes) == 2:
            strseconds = "0" + strseconds
        elif len(strminutes) != 2 and "." not in strseconds[0:2]:
            strminutes = "0" + strminutes
        if "." in strseconds[-2:]:
            strseconds += "0"
        result = f"{strhours}:{strminutes}:{strseconds}"
    return result

# print(time_format(conversionhub(952, "5000m")))
print(time_format(convert_1600m_to_800m(193)))