from omega import *
from cyclops import *
from math import *

def createCustomGeom(f, scene, geomName):        #Function parses file and creates lines
                                                        #that represent movement into a single
                                                        #custom shape.
    global moveLineProgram

    firstRun = True

    numVertices = 0
    prevV3 = Vector3(0,0,0)
    prevV4 = Vector3(0,0,0)
    prevV7 = Vector3(0,0,0)
    prevV8 = Vector3(0,0,0)

    prevID = ""
    prevLine = ""

    unitY = Vector3(0,1,0)
    unitZ = Vector3(0,0,1)

    thickness = 2
    geom = ModelGeometry.create(geomName)
    for line in f:
        # if numVertices == 6:
        #     break
        if line == '-999':
            break

        if firstRun:
            prevLine = line
            firstRun = False
        else:
            tokens = prevLine.split(" ")
            tokens2 = line.split(" ")

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

            dayDelta = int(tokens2[3])
            hr = int(tokens2[4])
            minute = int(tokens2[5])
            individualID = int(tokens2[6])

        #####################Front Panel##################################################
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
        ##################################################################################
        #####################Back Panel##################################################
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
        ##################################################################################
        #####################Top Panel##################################################
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
        ##################################################################################
        #####################Bottom Panel##################################################
            
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
            
        ##################################################################################
            
            numVertices = numVertices + 24

            prevV3 = v3                 #Store beginning points of next line
            prevV4 = v4
            prevV7 = v7
            prevV8 = v8

            prevVec = vec
            prevID = int(tokens2[6])
            prevLine = line
        
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
