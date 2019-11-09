def timeConversion(s):
    h = int(s[0:2])
    if s[-2:] == "PM":
        if h != 12:
            h+=12
    else:
        if h == 12:
            h = 0
    return"%02d%s" % (h,s[2:-2])

s="07:05:45PM"
print(timeConversion(s))
