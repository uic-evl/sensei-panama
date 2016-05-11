import struct;
from datetime import date

def calculateXY (utmE, utmN):
    utmE1 = 624030.0137255481  #0.18/(float(10260)/32064) * 10260
    utmN1 = 1015207.0834458455 #.18/(float(9850)/30780) * 9850
    utmE2 = 629801.5337255481  #624030.0137255481 + 32064.0 * .18
    utmN2 = 1009666.6834458455 #1015207.0834458455 - 30780.0 * .18
    totalW = 5771.52
    totalH = 5540.4

    x = (utmE-utmE1)/(utmE2-utmE1) * totalW
    y = (utmN2-utmN)/(utmN2-utmN1) * totalH

    return (x, y)



#open file
filename = "allChibi.csv" #"Chibi_Christmas.csv"
writeto = "allChibi.xyzb"#"XY_Chibi_Christmas_Parsed.xyzb"
fo = open(filename, "r")
wo = open(writeto, "wb")
z = 1.0
#read line
content = fo.readlines()
#for all lines
for line in content:
    #read line
    #tokenize
    tokens = line.split(",")
    #get params utme utmn ht localtimestamp individualId
    if (tokens[30] and tokens[31]):
        utme = float(tokens[30])
        utmn = float(tokens[31])
        ht = float(tokens[23])
        localts = tokens[34]
        removeQuotes = tokens[27].replace("\"", "")
        individualId = int(removeQuotes)
        #break up timestamp, get hr, min, day, month
        tokens2 = localts.split(" ")
        datetokens = tokens2[0].split("-")

        timetokens = tokens2[1].split(".")
        timetokens2 = timetokens[0].split(":")
        hr = int(timetokens2[0])
        minute = int(timetokens2[1])

        secondDate = date(int(datetokens[0]), int(datetokens[1]), int(datetokens[2]))

        #get day as distance from dec
        firstDate = date(2015, 12, 11)

        delta = secondDate.day - firstDate.day
        intDelta = delta

        xy = calculateXY(utme, utmn)
        #print "X "+xy[0]
        #print "Y "+xy[1]
        #write bytes
        print "x %d y %d z %d day %d hr %d min %d indId %d " %(  xy[0], xy[1], 5.0, intDelta, hr,minute, individualId)

        dataBytes = struct.pack('ddddddd', float(xy[0]), float(xy[1]), float(ht), float(intDelta), float(hr), float(minute), float(individualId))
        wo.write(dataBytes)
fo.close()
wo.close()  