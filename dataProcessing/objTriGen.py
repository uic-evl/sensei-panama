import Image;
import png;

def computeIMGUTMtoHMXY (imgx, imgy):               #function converts pixel in original image 
                                                    #to utm coordinate
                                                    #then converts the utm to pixel in height map
    #Images UTM Coordinates
    startIMGUTMX = 624030.0137255481
    startIMGUTMY = 1015207.0834458455

    #Height Maps UTM Coordinates
    startHMUTMX = 619764.479784366560000
    lastHMUTMX = startHMUTMX + 5000*4.335008086253366
    startHMUTMY = 1023894.520215633300000
    lastHMUTMY = startHMUTMY - 5000*4.335008086253366

    imgResRatioX = 0.18/(float(962)/32064)
    imgResRatioY = 0.18/(float(924)/30780)

    utmX = startIMGUTMX + (imgx*imgResRatioX)       #Calculates the E-W utm coordinate
    utmY = startIMGUTMY - (imgy*imgResRatioY)       #Calculates the N-S utm coordinate

    hmx = int(((utmX-startHMUTMX)/(lastHMUTMX-startHMUTMX) * 5000))     #X-coordinate of height map
    hmy = int(((utmY-startHMUTMY)/(lastHMUTMY-startHMUTMY) * 5000))     #Y-coordinate of height map

    return (hmx, hmy)                               #return as a tuple

imgResRatioX = 0.18/(float(962)/32064)
imgResRatioY = 0.18/(float(924)/30780)
picname = "3island.png"
image = Image.open(picname)
#outImage = image.transpose(Image.FLIP_TOP_BOTTOM)
pixInfo = image.load()
(i,_) = image.size
(_,j) = image.size

hm = "bciMap500.png"
hmImage = Image.open(hm)                            #open the height map
#outHM = hmImage.transpose(Image.FLIP_TOP_BOTTOM)
hmPixInfo = hmImage.load()  
(hi,_) = hmImage.size                               #gives x-size
(_,hj) = hmImage.size                               #gives y-size

text_file = open("3terrainMap.obj", 'w')

vertex = 1
fileString = ""
vList = []

for x in range(i):
    for y in range(j):
        utmXY = computeIMGUTMtoHMXY(x, y)
        hmX = utmXY[0]
        hmY = utmXY[1]
        if (hmX >= 0 and hmX < 5000 and hmY >= 0 and hmY < 5000):
            if hmPixInfo[hmX, hmY][3] != 0:
                val = float(hmPixInfo[hmX, hmY][0])
            else:
                val = 0.0
        else:
            val = 0.0
        vList.append(val)

#use a list as a stack to reverse order of values
for x in range(i):
    for y in range(j):
        if vList:
            val = vList.pop()
            fileString += "v " + str(imgResRatioX*(i-x-1)) + " " + str(imgResRatioY*y) + " " + str(val) + "\n" #18/3.000249501 is imgResRatioX
                                                                                                                   #18/3.001949317 is imgResRatioY
fileString += "\n"
for v in range(vertex, i*j-j):
    #fileString += "f " + str(v) + " " + str(v+1) + " " + str(v+i) + "\n" + "f " + str(v+1) + " " + str(v+i+1) + " " + str(v+i) + "\n"
    #fileString += "f " + str(v) + " " + str(v+1) + " " + str(v+j) + "\n" + "f " + str(v+1) + " " + str(v+j+1) + " " + str(v+j) + "\n"
    #fileString += "f " + str(v+i) + " " + str(v+i+1) + " " + str(v+1) + " " + str(v) + "\n" + "f " + str(v+1) + " " + str(v+i) + " " + str(v+i+1) + "\n"
    #fileString += "f " + str(v+j) + " " + str(v+j+1) + " " + str(v+1) + " " + str(v) + "\n"
    fileString += "f " + str(v) + " " + str(v+1) + " " + str(v+j+1) + " " + str(v+j) + "\n"
    #v += 1

text_file.write(fileString)
text_file.close()
