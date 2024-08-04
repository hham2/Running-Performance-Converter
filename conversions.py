def conversionhub(time, userdistance):
    """
    Takes a user input time for a user input distance and creates a table with
    equivalent times for several other distances
    """
    converted_800m_time = convert_to_800m(time, userdistance)
    conversiontable = conversion_table(converted_800m_time)
    return conversiontable

def convert_to_800m(time, userdistance):
    """
    returns an 800m time roughly equivalent (by my conversion functions) to any user input time for any user input distance
    """
    distance_index = index_user_input_distance(userdistance) #dumb way to do this but it's probably good enough
    if distance_index == 0: #800m
        converted_800m_time = time
    elif distance_index == 1: #1500m
        converted_1600m_time = convert_1500m_to_1600m(time)
        converted_800m_time = convert_1600m_to_800m(converted_1600m_time)
    elif distance_index == 2: #1600m
        converted_800m_time = convert_1600m_to_800m(time)
    elif distance_index == 3: #mile
        converted_1600m_time = convert_mile_to_1600m(time)
        converted_800m_time = convert_1600m_to_800m(converted_1600m_time)
    elif distance_index == 4: #3000m
        converted_3200m_time = convert_3000m_to_3200m(time)
        converted_1600m_time = convert_3200m_to_1600m(converted_3200m_time)
        converted_800m_time = convert_1600m_to_800m(converted_1600m_time)
    elif distance_index == 5: #3200m
        converted_1600m_time = convert_3200m_to_1600m(time)
        converted_800m_time = convert_1600m_to_800m(converted_1600m_time)
    elif distance_index == 6: #2 mile
        converted_3200m_time = convert_2mile_to_3200m(time)
        converted_1600m_time = convert_3200m_to_1600m(converted_3200m_time)
        converted_800m_time = convert_1600m_to_800m(converted_1600m_time)
    elif distance_index == 7: #5000m
        converted_1600m_time = convert_5000m_to_1600m(time)
        converted_800m_time = convert_1600m_to_800m(converted_1600m_time)
    elif distance_index == 8: #10000m
        converted_5000m_time = convert_10000m_to_5000m(time)
        converted_1600m_time = convert_5000m_to_1600m(converted_5000m_time)
        converted_800m_time = convert_1600m_to_800m(converted_1600m_time)
    elif distance_index == 9: #half marathon
        converted_10000m_time = convert_halfmarathon_to_10000m(time)
        converted_5000m_time = convert_10000m_to_5000m(converted_10000m_time)
        converted_1600m_time = convert_5000m_to_1600m(converted_5000m_time)
        converted_800m_time = convert_1600m_to_800m(converted_1600m_time)
    else:                     #marathon
        converted_halfmarathon_time = convert_marathon_to_halfmarathon(time)
        converted_10000m_time = convert_halfmarathon_to_10000m(converted_halfmarathon_time)
        converted_5000m_time = convert_10000m_to_5000m(converted_10000m_time)
        converted_1600m_time = convert_5000m_to_1600m(converted_5000m_time)
        converted_800m_time = convert_1600m_to_800m(converted_1600m_time)
    return converted_800m_time

def conversion_table(converted_800m_time):
    """
    returns a dictionary with a distance as the key for each item and the equivalent 
    time to the original user input time as the value for each item
    """
    conversions = {
        "800m": time_format(converted_800m_time),
        "1500m": time_format(convert_800m_to_1500m(converted_800m_time)),
        "1600m": time_format(convert_800m_to_1600m(converted_800m_time)),
        "Mile": time_format(convert_800m_to_mile(converted_800m_time)),
        "3000m": time_format(convert_800m_to_3000m(converted_800m_time)),
        "3200m": time_format(convert_800m_to_3200m(converted_800m_time)),
        "2 mile": time_format(convert_800m_to_2mile(converted_800m_time)),
        "5000m": time_format(convert_800m_to_5000m(converted_800m_time)),
        "10000m": time_format(convert_800m_to_10000m(converted_800m_time)),
        "Half marathon": time_format(convert_800m_to_halfmarathon(converted_800m_time)),
        "Marathon": time_format(convert_800m_to_marathon(converted_800m_time))
    }
    return conversions

def index_user_input_distance(userdistance):
    """
    returns a numerical value corresponding to the position of the user input (userdistance) in a sequential list of all distances for which I've made
    conversion functions, beginning at the shortest distance and ending at the longest distance.
    """
    list_of_distances = [
    "800m",
    "1500m",
    "1600m",
    "Mile",
    "3000m",
    "3200m",
    "2 mile",
    "5000m",
    "10000m",
    "Half marathon",
    "Marathon"
]
    counter = -1 #this will correspond to the index of the distance input by the user once the for loop has finished iterating over the list of distances
    for distance in list_of_distances:
        counter += 1
        if distance == userdistance:
            break
    return counter

def convert_800m_to_1500m(time_800m):
    """
    converts an 800m time to a roughly equivalent 1500m time 
    """
    converted_1600m = convert_800m_to_1600m(time_800m)
    converted_1500m = convert_1600m_to_1500m(converted_1600m)
    return converted_1500m
    
#800m to 1600m conversions will just use the pre-existing convert_800m_to_1600m() function 

def convert_800m_to_mile(time_800m): 
    """
    converts an 800m time to a roughly equivalent mile time 
    """
    converted_1600m = convert_800m_to_1600m(time_800m)
    converted_mile = convert_1600m_to_mile(converted_1600m)
    return converted_mile

def convert_800m_to_3000m(time_800m):
    """
    converts an 800m time to a roughly equivalent 3000m time 
    """
    converted_1600m = convert_800m_to_1600m(time_800m)
    converted_3200m = convert_1600m_to_3200m(converted_1600m)
    converted_3000m = convert_3200m_to_3000m(converted_3200m)
    return converted_3000m

def convert_800m_to_3200m(time_800m):
    """
    converts an 800m time to a roughly equivalent 3200m time 
    """
    converted_1600m = convert_800m_to_1600m(time_800m)
    converted_3200m = convert_1600m_to_3200m(converted_1600m)
    return converted_3200m

def convert_800m_to_2mile(time_800m):
    """
    converts an 800m time to a roughly equivalent 2 mile time
    """
    converted_3200m = convert_800m_to_3200m(time_800m)
    converted_2mile = convert_3200m_to_2mile(converted_3200m)
    return converted_2mile

def convert_800m_to_5000m(time_800m):
    """
    converts an 800m time to a roughly equivalent 5000m time 
    """
    converted_1600m = convert_800m_to_1600m(time_800m)
    converted_5000m = convert_1600m_to_5000m(converted_1600m)
    return converted_5000m

def convert_800m_to_10000m(time_800m):
    """
    converts an 800m time to a roughly equivalent 10000m time 
    """
    converted_5000m = convert_800m_to_5000m(time_800m)
    converted_10000m = convert_5000m_to_10000m(converted_5000m)
    return converted_10000m

def convert_800m_to_halfmarathon(time_800m):
    """
    converts an 800m time to a roughly equivalent half marathon time 
    """
    converted_10000m = convert_800m_to_10000m(time_800m)
    converted_halfmarathon = convert_10000m_to_halfmarathon(converted_10000m)
    return converted_halfmarathon

def convert_800m_to_marathon(time_800m):
    """
    converts an 800m time to a roughly equivalent marathon time 
    """
    converted_halfmarathon = convert_800m_to_halfmarathon(time_800m)
    converted_marathon = convert_halfmarathon_to_marathon(converted_halfmarathon)
    return converted_marathon


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
        output = 0.541666666*time - 602.0666666
    elif 8920 < time <= 9640:
        output = 0.458333333*time + 141.2666666
    elif 9640 < time <= 10360:
        output = 0.41666666*time + 542.9333333
    elif 10360 < time <= 11080:
        output = 0.5*time - 320.4
    elif 11080 < time <= 12600:
        output = 0.395*time + 843
    else:
        output = 0.4333333*time + 360
    return output

def convert_halfmarathon_to_marathon(time):
    """
    inverse of convert_marathon_to_halfmarathon()
    function
    """
    if time <= 3569.6:
        output = (time + 559.36)*(1/0.552)
    elif 3569.6 < time <= 3839.6:
        output = (time - 764.6)*(1/0.375)
    elif 3839.6 < time <= 4229.6:
        output = (time + 602.0666666)*(1/0.541666666)
    elif 4229.6 < time <= 4559.6:
        output = (time - 141.2666666)*(1/0.458333333)
    elif 4559.6 < time <= 4859.6:
        output = (time - 542.9333333)*(1/0.41666666)
    elif 4859.6 < time <= 5219.6:
        output = (time + 320.4)*(1/0.5)
    elif 5219.6 < time <= 5820:
        output = (time - 843)*(1/0.395)
    else:
        output = (time - 360)*(1/0.4333333)
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
    elif 3600 < time <= 3720:
        output = 0.4166666*time + 140
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

def convert_10000m_to_halfmarathon(time):
    """
    inverse of convert_halfmarathon_to_10000m()
    function
    """
    if time <= 1610:
        output = (time - 135)*(1/0.41666666)
    elif 1610 < time <= 1640:
        output = (time + 160)*(1/0.5)
    elif 1640 < time <= 1690:
        output = (time - 140)*(1/0.4166666)
    elif 1690 < time <= 1760:
        output = (time + 480)*(1/0.58333333)
    elif 1760 < time <= 1890:
        output = (time - 373.33333)*(1/0.36111)
    elif 1890 < time <= 2010:
        output = (time - 490)*(1/0.333333)
    elif 2010 < time <= 2190:
        output = (time + 270)*(1/0.5)
    elif 2190 < time <= 2490:
        output = (time - 140)*(1/0.41666666)
    elif 2490 < time <= 2670:
        output = (time + 330)*(1/0.5)
    else:
        output = (time + 830)*(1/0.58333333)
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

def convert_5000m_to_10000m(time):
    """
    inverse of convert_10000m_to_5000m()
    function
    """
    if time <= 785:
        output = (time + 241)*(1/0.6333333)
    elif 785 < time <= 810:
        output = (time - 110)*(1/0.41666666)
    elif 810 < time <= 865:
        output = (time - 40)*(1/0.458333333)
    elif 865 < time <= 925:
        output = (time + 35)*(1/0.5)
    elif 925 < time <= 1090:
        output = (time - 45)*(1/0.458333333)
    elif 1090 < time <= 1190:
        output = (time - 140)*(1/0.41666666)
    else:
        output = (time + 175)*(1/0.541666666)
    return output

def convert_5000m_to_1600m(time):
    """
    uses a piecewise function I made to convert a 5000m time to a roughly equivalent
    1600m time
    """
    if time <= 780:
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

def convert_1600m_to_5000m(time):
    """
    inverse of convert_5000m_to_1600m()
    function
    """
    if time <= 229:
        output = (time - 10.5936)*(1/0.28)
    elif 229 < time <= 244:
        output = (time - 33.9936)*(1/0.25)
    elif 244 < time <= 258:
        output = (time - 47.9936003)*(1/0.2333333)
    elif 258 < time <= 264:
        output = (time - 167.9936)*(1/0.1)
    elif 264 < time <= 277:
        output = (time - 56)*(1/0.21666666)
    elif 277 < time <= 295:
        output = (time + 29)*(1/0.3)
    elif 295 < time <= 312:
        output = (time + 11)*(1/0.28333333)
    elif 312 < time <= 338:
        output = (time + 182)*(1/0.4333333)
    else:
        output = (time + 62)*(1/0.33333)
    return output

def convert_3200m_to_1600m(time):
    """
    converts a 3200m time to a roughly equivalent
    1600m time; can be used to convert 3200m time to an equivalent time at 
    a different distance via a second function
    """
    if time <= 480:
        output = 0.444444*time + 11.8666666
    elif 480 < time <= 500:
        output = 0.6*time - 62.8
    elif 500 < time <= 520:
        output = 0.34*time + 67.2
    elif 520 < time <= 560:
        output = 0.45*time + 10
    elif 560 < time <= 600:
        output = 0.4*time + 38
    elif 600 < time <= 660:
        output = 0.3666666*time + 58
    elif 660 < time <= 720:
        output = 0.58333333*time - 85
    elif 720 < time <= 780:
        output = 0.41666*time + 35
    elif 780 < time <= 900:
        output = 0.5*time - 30
    else:
        output = 0.41666666*time + 45
    return output

def convert_1600m_to_3200m(time):
    """
    inverse of convert_3200m_to_1600m() 
    function
    """
    if time <= 225.2:
        output = (time - 11.8666666)*(1/0.444444)
    elif 225.2 < time <= 237.2:
        output = (time + 62.8)*(1/0.6)
    elif 237.2 < time <= 244:
        output = (time - 67.2)*(1/0.34)
    elif 244 < time <= 262:
        output = (time - 10)*(1/0.45)
    elif 262 < time <= 278:
        output = (time - 38)*(1/0.4)
    elif 278 < time <= 300:
        output = (time - 58)*(1/0.3666666)
    elif 300 < time <= 335:
        output = (time + 85)*(1/0.58333333)
    elif 335 < time <= 360:
        output = (time - 35)*(1/0.416666)
    elif 360 < time <= 420:
        output = (time + 30)*(1/0.5)
    else:
        output = (time - 45)*(1/0.41666666)
    return output

def convert_3200m_to_2mile(time):
    """
    converts a 3200m time to a roughly equivalent
    2 mile time
    """
    output = time * 1.0063
    return output

def convert_2mile_to_3200m(time):
    """
    converts a 2 mile time to a roughly equivalent
    3200m time
    """
    output = time * (1/1.0063)
    return output

def convert_3200m_to_3000m(time):
    """
    converts a 3200m time to a roughly equivalent
    3000m time
    """
    output = time * 0.932
    return output

def convert_3000m_to_3200m(time):
    """
    inverse of convert_3200m_to_3000m() 
    function
    """
    output = time * (1/0.932)
    return output

def convert_1600m_to_mile(time):
    """
    converts a 1600m time to a roughly 
    equivalent mile (1609.344m) time
    """
    output = time * 1.0063
    return output

def convert_mile_to_1600m(time):
    """
    inverse of convert_1600m_to_mile() 
    function
    """
    output = time * (1/1.0063)
    return output

def convert_1600m_to_1500m(time):
    """
    converts a 1600m time to a roughly
    equivalent 1500m time
    """
    output = time * 0.932
    return output

def convert_1500m_to_1600m(time):
    """
    inverse of convert_1600m_to_1500m() 
    function
    """
    output = time * (1/0.932)
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

def convert_800m_to_1600m(time):
    """
    inverse of convert_1600m_to_800m()
    function
    """
    if time <= 102.75:
        output = (time + 3.225)*(1/0.471)
    elif 102.75 < time <= 104.5:
        output = (time-24)*(1/0.35)
    elif 104.5 < time <= 109.5:
        output = (time + 10.5)*(1/0.5)
    elif 109.5 < time <= 113:
        output = (time - 25.5)*(1/0.35)
    elif 113 < time <= 118:
        output = (time + 12)*(1/0.5)
    elif 118 < time <= 125:
        output = (time - 27)*(1/0.35)
    elif 125 < time <= 133:
        output = (time - 13)*(1/0.4)
    elif 133 < time <= 142:
        output = (time + 2)*(1/0.45)
    elif 142 < time <= 148:
        output = (time - 46)*(1/0.3)
    elif 148 < time <= 155:
        output = (time - 29)*(1/0.35)
    elif 155 < time <= 170:
        output = (time + 115)*(1/0.75)
    else:
        output = (time + 77)*(1/0.65)
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
        elif seconds == 60:
            minutes += 1
            strseconds = "00.00"
        else:
            if seconds < 10:
                strseconds = "0" + strseconds
            if "." in strseconds[-2:]:
                strseconds = strseconds + "0"
        result = f"{minutes}:{strseconds}"
    else: #configuration for times over 1 hour
        hours = int(time // 3600)
        strhours = str(hours)
        minutes = int((time // 60)-(hours*60))
        strminutes = str(minutes)
        # if hours < 10: #I don't think I want this feature anymore so I'm gonna comment it out 
        #     strhours = "0" + str(hours)
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
        #when the total time is over 1 hour and under 100 hours in length
        if len(strminutes) != 2:
            strminutes = "0" + strminutes
        if "." in strseconds[0:2]: #the only scenario where this'd be true is one where the minutes value is less than 10
            strseconds = "0" + strseconds
        if "." in strseconds[-2:]:
            strseconds += "0"
        result = f"{strhours}:{strminutes}:{strseconds}"
    return result