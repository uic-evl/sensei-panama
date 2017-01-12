from euclid import *
from omega import *
from cyclops import *
from pointCloud import *


scene = getSceneManager()

movementData = []
myStartDay = []
myEndDay = []

for i in range(0, 21):
    myStartDay.append(0)
    myEndDay.append(1)

moveLineProgram = ProgramAsset()
moveLineProgram.name = "moveLine"
moveLineProgram.vertexShaderName = "lineShaders/Line.vert"
moveLineProgram.fragmentShaderName = "lineShaders/Line.frag"
scene.addProgram(moveLineProgram)

startDay = Uniform.create('startDay', UniformType.Int, 21)
endDay = Uniform.create('endDay', UniformType.Int, 21)

bitMapSelectedIndividuals = Uniform.create('bitMapSelectedIndividuals', UniformType.Int, 21)
colorByBitMap = Uniform.create('colorByBitMap', UniformType.Int, 21)

for i in range(0,21):                                            #Bit map used by GLSL to toggle individuals on and off
    if i == 1:
        bitMapSelectedIndividuals.setIntElement(1, i)
    else:
        bitMapSelectedIndividuals.setIntElement(0, i)
    startDay.setIntElement(myStartDay[i], i)
    endDay.setIntElement(myEndDay[i], i)

f = open("gpsMovement/all.txt", "r")

def createCustomGeom():       #Function parses file and creates lines
                                                #that represent movement into a single
                                                #custom shape.
    global moveLineProgram
    global movementData
    global scene

    geomName = 'allAnimals'
    thickness = 2                               #Line thickness
    firstRun = True
    numVertices = 0
    prevV3 = Vector3(0, 0, 0)
    prevV4 = Vector3(0, 0, 0)
    prevV7 = Vector3(0, 0, 0)
    prevV8 = Vector3(0, 0, 0)

    individualIter = 0
    dayIter = 0

    prevDayDelta = ""
    prevID = ""
    prevLine = ""

    unitY = Vector3(0, 1, 0)
    unitZ = Vector3(0, 0, 1)
    

    f = open("gpsMovement/all.txt", "r")

    geom = ModelGeometry.create(geomName)
    for line in f:
        if line == '-999':
            break
        #numberOfDaysByIndividual = [85, 70, 78, 80, 54, 18, 83, 80, 79, 67, 65, 72, 73, 71, 72, 67, 82, 86, 35, 39, 2]
        if firstRun:
            tokens = line.split(" ")
            prevDayDelta = tokens[3]
            prevLine = line
            firstRun = False
            movementData.append([])
            movementData[individualIter].append([])
            #Inputs x, y, z, hr, minute of gps point
            movementData[individualIter][dayIter].append((float(tokens[0]), float(tokens[1]), float(tokens[2]), tokens[4], tokens[5]))
            prevID = tokens[6]
            prevDayDelta = tokens[3]
        else:
            tokens = prevLine.split(" ")
            tokens2 = line.split(" ")

            if prevID != tokens2[6]:
                movementData.append([])
                individualIter += 1
                dayIter = 0
                movementData[individualIter].append([])
                #Inputs x, y, z, hr, minute of gps point
                movementData[individualIter][dayIter].append((float(tokens2[0]), float(tokens2[1]), float(tokens2[2]), tokens2[4], tokens2[5]))
            else:
                #Inputs x, y, z, hr, minute of gps point
                if (prevDayDelta != tokens2[3]):
                    movementData[individualIter].append([])
                    dayIter += 1
                movementData[individualIter][dayIter].append((float(tokens2[0]), float(tokens2[1]), float(tokens2[2]), tokens2[4], tokens2[5]))


            pos1 = Vector3(float(tokens[0]), float(tokens[1]), float(tokens[2]))
            
            pos2 = Vector3(float(tokens2[0]), float(tokens2[1]), float(tokens2[2]))

            vec = pos2 - pos1
            d = vec.normalize()
            unitZV1 = d.cross(unitZ)
            unitYV1 = d.cross(unitY)

            v1 = pos1+thickness*unitZV1+thickness*unitYV1       #list of vertices
            v2 = pos1+thickness*unitZV1-thickness*unitYV1       
            v3 = pos2+thickness*unitZV1+thickness*unitYV1
            v4 = pos2+thickness*unitZV1-thickness*unitYV1
            v5 = pos1-thickness*unitZV1+thickness*unitYV1
            v6 = pos1-thickness*unitZV1-thickness*unitYV1
            v7 = pos2-thickness*unitZV1+thickness*unitYV1
            v8 = pos2-thickness*unitZV1-thickness*unitYV1

            dayDelta = int(tokens[3])
            hr = int(tokens[4])
            minute = int(tokens[5])
            individualID = int(tokens[6])

        #####################Front Panel##################################################
            if pos1.x <= pos2.x:
                geom.addVertex( v1 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v2 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v3 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))

                geom.addVertex( v3 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v2 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v4 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))

            if pos1.x > pos2.x:
                geom.addVertex( v3 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v2 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v1 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))

                geom.addVertex( v4 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v2 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v3 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
        ##################################################################################
        #####################Back Panel##################################################
            if pos1.x <= pos2.x:
                geom.addVertex( v7 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v6 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v5 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))

                geom.addVertex( v8 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v6 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v7 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))

            if pos1.x > pos2.x:
                geom.addVertex( v5 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v6 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v7 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))

                geom.addVertex( v7 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v6 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v8 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
        ##################################################################################
        #####################Top Panel##################################################
            if pos1.x <= pos2.x:
                geom.addVertex( v1 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v7 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v5 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                
                geom.addVertex( v7 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v1 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v3 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))

            if pos1.x > pos2.x:
                geom.addVertex( v5 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v7 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v1 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))

                geom.addVertex( v3 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v1 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v7 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
        ##################################################################################
        #####################Bottom Panel##################################################
            if pos1.x <= pos2.x:
                geom.addVertex( v8 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v4 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v2 )
                geom.addColor(Color(dayDelta, hr, minute, individualID)) 

                geom.addVertex( v6 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v8 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))    
                geom.addVertex( v2 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))

            if pos1.x > pos2.x:
                geom.addVertex( v2 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v4 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v8 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))

                geom.addVertex( v2 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v8 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
                geom.addVertex( v6 )
                geom.addColor(Color(dayDelta, hr, minute, individualID))
            
        ##################################################################################
            
            numVertices = numVertices + 24

            prevV3 = v3                 #Store beginning points of next line
            prevV4 = v4
            prevV7 = v7
            prevV8 = v8

            prevVec = vec
            prevLine = line
            prevID = tokens2[6]
            prevDayDelta = tokens2[3]
        
    f.close()
    geom.addPrimitive(PrimitiveType.Triangles, 0, numVertices)

    scene.addModel(geom)
    obj = StaticObject.create(geomName)
    obj.setPosition(0, 0, 0)
    # obj.setEffect('-C')

    # obj.getMaterial().setProgram('colored byvertex-emissive')
    obj.getMaterial().setTransparent(True)
    print 'finished Parsing'

    return obj 