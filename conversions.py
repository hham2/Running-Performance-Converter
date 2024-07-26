def conversion1500mto800m(time):
    totalseconds = time * 0.4907
    minutes = int(totalseconds // 60)
    seconds = ((totalseconds / 60) - minutes)*60
    seconds = round(seconds, 2)
    print(f"{minutes}:{seconds}")

#Jakob Kingebrigtsen
conversion1500mto800m(206.73)