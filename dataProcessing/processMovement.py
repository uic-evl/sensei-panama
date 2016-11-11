#Authors: Oliver San Juan, Jillian Aurisano

"""
This file is responsible for taking the utm and height information from the csv file and then converting it into
x, y, and z coordinates for omegalib. This file makes the assumption that the necessary information is found in the follwing
columns:
utm-easting                 (column 30)
utm-northing                (column 31)
height_above_ellipsoid      (column 34)
Furthermore, the program will get the name of the file that the user wants to write to on the command line. 
"""

from datetime import date
import sys
import struct

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

#Constants for the desired column values
eastingColumn = 30
northingColumn = 31
individualId = 27
heightColumn = 23

#Values used to keep track of each iteration's values
# The program needs to keep track of the previous values because it won't know
# whether or not it should store the values to the CSV file until it's reached a different time burst.  

prevMin = -1
currMin = -1        #currMin will always store the minute value of every valid iteration

#Get the name of the file that the user wants to write to from the command line
fileToWrite = sys.argv[1]

#Redirect standard output to write to that file
f2 = open(fileToWrite, 'w')
    
f = open('FoodForThought_ComparativeFrugivoreTracking.csv', "r")

#print rest
firstIter = True
firstItemParsed = False
fileString = ""

for line in f:
    tokens = line.split(",")
    if (tokens[30] and tokens[31] and not firstIter):
        timeStamp = tokens[34].split()
        time= timeStamp[1].split(":")

        
        #Get the current iteration's minute
        currMin = int(time[1])

        if(prevMin < 1):

            #assign prevMin to currMin because this is the first iteration
            prevMin = currMin
        elif (prevMin != currMin and tokens[27] == "\"4665\""):
            prevUtmE = tokens[eastingColumn]
            prevUtmN = tokens[northingColumn]
            prevHeight = tokens[heightColumn]

            dates = tokens[34].split(" ")
            dateT = dates[0].split("-")

            individualIdString = tokens[27].replace("\"", " ")
            individualId = int(individualIdString)

            if not firstItemParsed:
                firstDate = date(int(dateT[0]), int(dateT[1]), int(dateT[2]))
                firstItemParsed = True

            secondDate = date(int(dateT[0]), int(dateT[1]), int(dateT[2]))

            diffDate = secondDate - firstDate
            delta = diffDate.days

            #We are on a different burst and it's time to store it to the CSV
            xy = calculateXY(float(prevUtmE), float(prevUtmN))

            print "string ", str(xy[0])
            print "float ", float(xy[0])
            
            fileString += str(xy[0]) + " " + str(xy[1]) + " " + str(prevHeight) + " " + str(delta) + " " + str(time[0]) + " " + str(time[1]) + " " + str(individualId) + "\n"

            #Move prevMin to currMin
            prevMin = currMin
    firstIter = False
#fileString += '-999'
f2.write(fileString)
f.close()
f2.close()