import struct;

def calculateXY (utmE, utmN):
    utmE1 = 624030.0137255481  #0.18/(float(10260)/32064) * 10260
    utmN1 = 1015207.0834458455 #.18/(float(9850)/30780) * 9850
    utmE2 = 629801.5337255481  #624030.0137255481 + 32064.0 * .18
    utmN2 = 1009666.6834458455 #1015207.0834458455 - 30780.0 * .18
    totalW = 5771.52
    totalH = 5540.4

    x = (utmE-utmE1)/(utmE2-utmE1) * totalW
    y = (utmN2-utmN)/(utmN2-utmN1) * totalH
    xInt = x
    yInt = y

    return (xInt, yInt)

#open file
filename = "2015_flowering_dipp.txt"
writeto = "treesFloat.txt"
fo = open(filename, "r")
wo = open(writeto, "w")
iteration = 0
#read line
content = fo.readlines()
#for all lines
for line in content:
    #read line
    #tokenize
    if (iteration > 0):
        tokens = line.split(",")
        #get params utme utmn ht localtimestamp individualId
        if (tokens[0] == "\"1"):
            index = 3
        else:
            index = 2

        endQuoteFound = False

        utme = tokens[index]
        index += 1
        while (not endQuoteFound):
            utme += tokens[index]
            if (tokens[index].find('\"') != -1):
                endQuoteFound = True
            index += 1
        removeQuotesUTME = utme.replace("\"", "")
        utmeFloat = float(removeQuotesUTME)

        utmn = tokens[index]
        endQuoteFound2 = False
        index += 1

        while (not endQuoteFound2):

            utmn += tokens[index]
            if (tokens[index].find('\"') != -1):
                endQuoteFound2 = True
            index += 1
        removeQuotesUTMN = utmn.replace("\"", "") 
        utmnFloat = float(removeQuotesUTMN)

        xy = calculateXY(utmeFloat, utmnFloat)

        z = tokens[index]
        if (tokens[index] == "\"1"):
            z += tokens[index+1]
            removeQuotesZ = z.replace("\"", "")
            zFloat = int(removeQuotesZ)
        else:
            removeQuotesZ = z.replace("\"", "")
            zFloat = int(removeQuotesZ)

        #write bytes
        #dataBytes = struct.pack('ddd', xy[0], xy[1], zFloat)
        dataBytes = str(xy[0]) + " " + str(xy[1]) + " " + str(zFloat/10) + "\n"
        wo.write(dataBytes)
    iteration += 1
fo.close()
wo.close()  