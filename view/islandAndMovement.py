from omega import *
from cyclops import *
from pointCloud import *
from math import *
from datetime import *


def createCustomGeom(f, scene, geomName):        #Function parses file and creates lines
                                                        #that represent movement into a single
                                                        #custom shape.
    global moveLineProgram
    global movementData

    firstRun = True

    numVertices = 0
    prevV3 = Vector3(0,0,0)
    prevV4 = Vector3(0,0,0)
    prevV7 = Vector3(0,0,0)
    prevV8 = Vector3(0,0,0)

    individualIter = 0
    dayIter = 0

    prevDayDelta = ""
    prevID = ""
    prevLine = ""

    unitY = Vector3(0,1,0)
    unitZ = Vector3(0,0,1)

    thickness = 2
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

def setUpLines(lineList, i):            #function sets up lines for text. Text includes START, END, and INDIVIDUALNAME. i corresponds to individual
    global XYOFFSET
    global STARTOFFSET
    global ENDOFFSET
    global INDNAMEOFFSET
    global movementData
    global myStartDay
    global myEndDay

    lineList[i].append(lineList[i][0].addLine())
    lineList[i].append(lineList[i][0].addLine())
    lineList[i].append(lineList[i][0].addLine())
    lineList[i][1].setStart(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]+XYOFFSET, movementData[i][myStartDay[i]][0][2]+STARTOFFSET))
    lineList[i][2].setStart(Vector3(movementData[i][myEndDay[i]][0][0]-XYOFFSET, movementData[i][myEndDay[i]][0][1]-XYOFFSET, movementData[i][myEndDay[i]][0][2]+ENDOFFSET))
    lineList[i][3].setStart(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]-XYOFFSET, movementData[i][myStartDay[i]][0][2]+INDNAMEOFFSET))
    lineList[i][1].setEnd(Vector3(movementData[i][myStartDay[i]][0][0], movementData[i][myStartDay[i]][0][1], movementData[i][myStartDay[i]][0][2]))
    lineList[i][2].setEnd(Vector3(movementData[i][myEndDay[i]][0][0], movementData[i][myEndDay[i]][0][1], movementData[i][myEndDay[i]][0][2]))
    lineList[i][3].setEnd(Vector3(movementData[i][myStartDay[i]][0][0], movementData[i][myStartDay[i]][0][1], movementData[i][myStartDay[i]][0][2]))
    lineList[i][1].setThickness(5)
    lineList[i][2].setThickness(5)
    lineList[i][3].setThickness(5)
    lineList[i][0].setEffect('colored -e red')
    lineList[i].append(SphereShape.create(5/2,2))
    lineList[i].append(SphereShape.create(5/2,2))
    lineList[i].append(SphereShape.create(5/2,2))
    lineList[i][4].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]+XYOFFSET, movementData[i][myStartDay[i]][0][2]+STARTOFFSET))
    lineList[i][5].setPosition(Vector3(movementData[i][myEndDay[i]][0][0]-XYOFFSET, movementData[i][myEndDay[i]][0][1]-XYOFFSET, movementData[i][myEndDay[i]][0][2]+ENDOFFSET))
    lineList[i][6].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]-XYOFFSET, movementData[i][myStartDay[i]][0][2]+INDNAMEOFFSET))
    lineList[i][4].setEffect('colored -e red')
    lineList[i][5].setEffect('colored -e red')
    lineList[i][6].setEffect('colored -e red')

def setLinePos(lineList, i):            #function updates line positions based on what days we are looking at. Modifies arraylist, lineList, that holds
                                        #LineSet information. i corresponds to individuals.
    global XYOFFSET
    global STARTOFFSET
    global ENDOFFSET
    global INDNAMEOFFSET
    global movementData
    global myStartDay
    global myEndDay

    lineList[i][1].setStart(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]+XYOFFSET, movementData[i][myStartDay[i]][0][2]+STARTOFFSET))
    lineList[i][2].setStart(Vector3(movementData[i][myEndDay[i]][0][0]-XYOFFSET, movementData[i][myEndDay[i]][0][1]-XYOFFSET, movementData[i][myEndDay[i]][0][2]+ENDOFFSET))
    lineList[i][3].setStart(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]-XYOFFSET, movementData[i][myStartDay[i]][0][2]+INDNAMEOFFSET))
    lineList[i][1].setEnd(Vector3(movementData[i][myStartDay[i]][0][0], movementData[i][myStartDay[i]][0][1], movementData[i][myStartDay[i]][0][2]))
    lineList[i][2].setEnd(Vector3(movementData[i][myEndDay[i]][0][0], movementData[i][myEndDay[i]][0][1], movementData[i][myEndDay[i]][0][2]))
    lineList[i][3].setEnd(Vector3(movementData[i][myStartDay[i]][0][0], movementData[i][myStartDay[i]][0][1], movementData[i][myStartDay[i]][0][2]))

    lineList[i][4].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]+XYOFFSET, movementData[i][myStartDay[i]][0][2]+STARTOFFSET))
    lineList[i][5].setPosition(Vector3(movementData[i][myEndDay[i]][0][0]-XYOFFSET, movementData[i][myEndDay[i]][0][1]-XYOFFSET, movementData[i][myEndDay[i]][0][2]+ENDOFFSET))
    lineList[i][6].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]-XYOFFSET, movementData[i][myStartDay[i]][0][2]+INDNAMEOFFSET))

#----------------------------------------------------------------------------
#Constants

numberOfDaysByIndividual = [85, 70, 78, 80, 52, 18, 83, 80, 79, 67, 65, 72, 73, 71, 72, 66, 82, 86, 35, 39, 2]
namesOfIndividuals = ["Veruca", "Chibi", "Abby", "Ben Bob", "Bonnie", "Chloe", "Clementina", "Ellie", "Gillian", "Ornette", "Pliny", "Ripley", "Sofie", "Greg", "Ibeth", "Olga", "Mimi", "Kyle", "Atlas", "Judy", "Merk"]
startDateByIndividual = [date(2015,12,11), date(2015,12,11), date(2015,12,15), date(2015,12,15), date(2015,12,15), date(2015,12,15), date(2015,12,14), date(2015,12,14), date(2015,12,14), date(2015,12,14), date(2015,12,14), date(2015,12,15), date(2015,12,14), date(2015,12,11), date(2015,12,25), date(2015,12,15), date(2015,12,15), date(2015,12,11), date(2016,1,12), date(2016,1,27), date(2016,3,2)]
XYOFFSET = 100                    # X and Y offset for all text
STARTOFFSET = 100                 # Z offset for start line
ENDOFFSET = 200                   # Z offset for end line
INDNAMEOFFSET = 300               # Z offset for individual name line
STARTTXTOFFSET = 110              # Z offset for start text
ENDTXTOFFSET = 210                # Z offset for end text
INDNAMETXTOFFSET = 310            # Z offset for individual name text
movementData = []                 # All GPS Data movementData[individualID][day][numPoints][tuple(x, y, z, hour, minute)]
myStartDay = []                   # Start Days of Individuals myStartDay[individualID]
myEndDay = []                     # End Days of Individuals myEndday[individualID]
txtArr = []                       # textArray of Individuals txtArr[individualID]
textNodeList = []                 # text SceneNode of Individuals textNodeList[individualID]
lineToTxt = []                    # Lines to text

#-----------------------------------------------------------------------------
#Terrain code

scene = getSceneManager()

def loadModelAsync(name, path):
    model = ModelInfo()
    model.name = name
    model.path = path
    model.optimize = True
    model.usePowerOfTwoTextures = False
    scene.loadModelAsync(model, "onModelLoaded('" + model.name + "')")
    return model

def onModelLoaded(name):
    model = StaticObject.create(name)
    model.setEffect('textured')

loadModelAsync("Terrain", "/iridium_SSD/panama/10mesh.fbx")

#---------------------------------------------------------------------------
#Set up Lights

light1 = Light.create()
light1.setColor(Color(0.4, 0.4, 0.4, 1))
light1.setAmbient(Color(0.5, 0.5, 0.5, 1))
light1.setLightType(LightType.Directional)
light1.setLightDirection(Vector3(-0.4, -0.2, -0.2))
light1.setEnabled(True)

light2 = Light.create()
light2.setColor(Color(0.4, 0.38, 0.35, 1))
light2.setAmbient(Color(0.5, 0.5, 0.5, 1))
light2.setLightType(LightType.Directional)
light2.setLightDirection(Vector3(1.5, 0.5, 1.1))
light2.setEnabled(True)

headlight = Light.create()
headlight.setColor(Color(0.5, 0.5, 0.5, 1))
headlight.setEnabled(True)

getDefaultCamera().addChild(headlight)

#----------------------------------------------------------------------------
#Planeview code
imgResRatioX = 0.18/(float(10260)/32064)
imgResRatioY = 0.18/(float(9850)/30780)
# plane = PlaneShape.create(imgResRatioX*10260, imgResRatioY*9850)
# plane.setPosition(Vector3(imgResRatioX*10260/2, imgResRatioY*9850/2, 0))
# plane.setEffect("textured -v emissive -d 50Island.png")

getDefaultCamera().setPosition(imgResRatioX*10260/2, imgResRatioY*9850/2, 2500)
getDefaultCamera().setBackgroundColor(Color('black'))
scene.addLoader(BinaryPointsLoader())

setNearFarZ(0.1, 1000000)


#---------------------------------------------------------------------------
#Cylinder and Sphere Version

for i in range(0, 21):
    myStartDay.append(0)
    myEndDay.append(1)

currentPitch = 0
currentYaw = 0
currentRoll = 0

moveLineProgram = ProgramAsset()
moveLineProgram.name = "moveLine"
moveLineProgram.vertexShaderName = "lineShaders/Line.vert"
moveLineProgram.fragmentShaderName = "lineShaders/Line.frag"
scene.addProgram(moveLineProgram)

startDay = Uniform.create('startDay', UniformType.Int, 21)
endDay = Uniform.create('endDay', UniformType.Int, 21)

bitMapSelectedIndividuals = Uniform.create('bitMapSelectedIndividuals', UniformType.Int, 21)
colorByBitMap = Uniform.create('colorByBitMap', UniformType.Int, 21)

for i in range(0,21):
    if i == 1:
        bitMapSelectedIndividuals.setIntElement(1, i)
    else:
        bitMapSelectedIndividuals.setIntElement(0, i)
    startDay.setIntElement(myStartDay[i], i)
    endDay.setIntElement(myEndDay[i], i)

f = open("gpsMovement/all.txt", "r")

allAnimals = createCustomGeom(f, scene, 'allAnimals')             #Read data into movementData

allMat = allAnimals.getMaterial()
allMat.setTransparent(True)
allMat.setProgram(moveLineProgram.name)
allMat.attachUniform(startDay)
allMat.attachUniform(endDay)
allMat.attachUniform(colorByBitMap)
allMat.attachUniform(bitMapSelectedIndividuals)

for i in range(0,21):
    lineToTxt.append([])
    lineToTxt[i].append(LineSet.create())
    setUpLines(lineToTxt, i)

for i in range(0,21):
    txtArr.append([])
    txtArr[i].append(Text3D.create('fonts/arial.tff', 25, "Start"))
    txtArr[i][0].setFontResolution(500)
    txtArr[i][0].setColor(Color('red'))
    txtArr[i].append(Text3D.create('fonts/arial.tff', 25, "End"))
    txtArr[i][1].setFontResolution(500)
    txtArr[i][1].setColor(Color('red'))
    txtArr[i].append(Text3D.create('fonts/arial.tff', 25, namesOfIndividuals[i]))
    txtArr[i][2].setFontResolution(500)
    txtArr[i][2].setColor(Color('red'))

    txtArr[i][0].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]+XYOFFSET, movementData[i][myStartDay[i]][0][2]+STARTTXTOFFSET))
    txtArr[i][1].setPosition(Vector3(movementData[i][myEndDay[i]][0][0]-XYOFFSET, movementData[i][myEndDay[i]][0][1]-XYOFFSET, movementData[i][myEndDay[i]][0][2]+ENDTXTOFFSET))
    txtArr[i][2].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]-XYOFFSET, movementData[i][myStartDay[i]][0][2]+INDNAMETXTOFFSET))

#Scene Node List for all Text
for i in range(0,21):
    textNodeList.append(SceneNode.create('textNode'+str(i)))
    getScene().addChild(textNodeList[i])
    textNodeList[i].addChild(txtArr[i][0])
    textNodeList[i].addChild(txtArr[i][1])
    textNodeList[i].addChild(txtArr[i][2])
    textNodeList[i].addChild(lineToTxt[i][0])
    textNodeList[i].addChild(lineToTxt[i][4])
    textNodeList[i].addChild(lineToTxt[i][5])
    textNodeList[i].addChild(lineToTxt[i][6])
    if i == 1:
        textNodeList[i].setChildrenVisible(True)
    else:
        textNodeList[i].setChildrenVisible(False)

    


#----------------------------------------------------------------------------
#UI Module code

uim = UiModule.createAndInitialize()

mainLayout = Container.create( ContainerLayout.LayoutVertical, uim.getUi())
mainLayout.setStyle( 'fill: #00000080' ) #'fill: #655E8280' ) #c0beff80 ' ) # #80808080' )##00000080' )
mainLayout.setSize( Vector2( float(2000), float(2000) ) ) #Vector2( xPixelsPerScreen, yPixelsPerScreen) )#xPixelsPerScreen*2.0, yPixelsPerScreen/2.0 ))
mainLayout.setAutosize(False)
mainLayout.setPosition( Vector2(1366*15, 0) )
caption1Txt = Label.create(mainLayout)
lastIndividualTxt = Label.create(mainLayout)
caption2Txt = Label.create(mainLayout)
dayRangeTxt = Label.create(mainLayout)

caption1Txt.setFont('fonts/arial.ttf 40')
caption1Txt.setText('Last selected animal:')

lastIndividualTxt.setFont('fonts/arial.ttf 40')
lastIndividualTxt.setText('Chibi')

caption2Txt.setFont('fonts/arial.ttf 40')
caption2Txt.setText('Visible date range:')

dayRangeTxt.setFont('fonts/arial.ttf 40')
dayRangeTxt.setText(str(startDateByIndividual[1]+timedelta(days=myStartDay[1]))+" - "+str(startDateByIndividual[1]+timedelta(days=myEndDay[1])))

#--------------------------------------------------------------------------------------------
# Movement point cloud code GPU Version

#filters
movePointScale = Uniform.create('movePointScale', UniformType.Float, 1)
movePointScale.setFloat(8.0)

movePointProgram = ProgramAsset()
movePointProgram.name = "movePoints"
movePointProgram.vertexShaderName = "movementShaders/Sphere.vert" #here are our shaders
movePointProgram.fragmentShaderName = "movementShaders/Sphere.frag"
movePointProgram.geometryShaderName = "movementShaders/mySphere.geom"
movePointProgram.geometryOutVertices = 4
movePointProgram.geometryInput = PrimitiveType.Points
movePointProgram.geometryOutput = PrimitiveType.TriangleStrip
scene.addProgram(movePointProgram)

movePointCloudModel = ModelInfo()
movePointCloudModel.name = 'movePointCloud'
movePointCloudModel.path = 'gpsMovement/all.xyzb'
movePointCloudModel.options = "10000 100:1000000:1 20:100:1 6:20:1 0:5:1"
scene.loadModel(movePointCloudModel)

movePointCloud = StaticObject.create(movePointCloudModel.name)
# attach shader uniforms
moveMat = movePointCloud.getMaterial()
moveMat.setTransparent(True)
moveMat.setProgram(movePointProgram.name)
moveMat.attachUniform(startDay)
moveMat.attachUniform(endDay)
moveMat.attachUniform(bitMapSelectedIndividuals)
moveMat.attachUniform(colorByBitMap)
moveMat.attachUniform(movePointScale)

#----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
#PointCloud code

pointProgram = ProgramAsset()
pointProgram.name = "points"
pointProgram.vertexShaderName = "islandShaders/Sphere.vert"
pointProgram.fragmentShaderName = "islandShaders/Sphere.frag"
pointProgram.geometryShaderName = "islandShaders/Sphere.geom"
pointProgram.geometryOutVertices = 4
pointProgram.geometryInput = PrimitiveType.Points
pointProgram.geometryOutput = PrimitiveType.TriangleStrip
scene.addProgram(pointProgram)

pointScale = Uniform.create('pointScale', UniformType.Float, 1)
pointScale.setFloat(1)
globalAlpha = Uniform.create('globalAlpha', UniformType.Float, 1)
globalAlpha.setFloat(1)

pointCloudModel = ModelInfo()
pointCloudModel.name = 'pointCloud'
pointCloudModel.path = '/iridium_SSD/panama/hmColorHigh.xyzb'
pointCloudModel.options = "10000 100:1000000:40 20:100:20 6:20:15 0:5:20"
scene.loadModel(pointCloudModel)

pointCloud = StaticObject.create(pointCloudModel.name)
# attach shader uniforms
mat = pointCloud.getMaterial()
mat.setTransparent(True)
mat.setProgram(pointProgram.name)
mat.attachUniform(pointScale)
mat.attachUniform(globalAlpha)

#---------------------------------------------------------------------------
#Menu items
#PointSize slider created by: Alessandro
mm = MenuManager.createAndInitialize()
mm.getMainMenu().addLabel("Point Size")
pointss = mm.getMainMenu().addSlider(40, "onPointSizeSliderValueChanged(%value%)")
pointSlider = pointss.getSlider()
pointSlider.setValue(1)

#Controls alpha values of points created by: Alessandro
mm.getMainMenu().addLabel("Point Transparency")
alphass = mm.getMainMenu().addSlider(11, "onAlphaSliderValueChanged(%value%)")
alphaSlider = alphass.getSlider()
alphaSlider.setValue(10)

#SUBMENU CAMERA
ss = mm.getMainMenu().addSubMenu("Camera Options")
vbtn = ss.addButton("Vertical View", "viewVertical(1)")
hbtn = ss.addButton("Horizontal View", "viewHorizontal(1)")

#------------------------------------------------------------------------------
#GPU Submenu Items

# #SUBMENU STEPTHRO
ss2 = mm.getMainMenu().addSubMenu("Global Step Through Options")
btnOneUp = ss2.addButton("Forward a day", "globalOneDayStepUp(1)")
btnOneDown = ss2.addButton("Backward a day", "globalOneDayStepDown(1)")
btnSvnUp = ss2.addButton("7 Days Forward", "globalSevenDayStepUp(1)")
btnSvnUp = ss2.addButton("7 Days Backward", "globalSevenDayStepDown(1)")
ss2.addLabel("--------------------")
btnAll = ss2.addButton("All Days", "globalAllDay(1)")

#-----------------------------------------------------------------------------
#Selected Individuals Menu
subSelectInd = mm.getMainMenu().addSubMenu("Selected Individuals")
subSelectInd2 = mm.getMainMenu().addSubMenu("Selected Individuals (2nd Half)")

#Veruca-----------------------------------------------------------------------

verucaMenu = subSelectInd.addSubMenu("Veruca 4690")
verBtn1 = verucaMenu.addButton("Show Data", "setSelInd(0)")

verucaMenu.addButton("Forward a day", "oneDayStepUp(0)")
verucaMenu.addButton("Backward a day", "oneDayStepDown(0)")
verucaMenu.addButton("7 Days Forward", "sevenDayStepUp(0)")
verucaMenu.addButton("7 Days Backward", "sevenDayStepDown(0)")
verucaMenu.addLabel("----------------")
verucaMenu.addButton("All Days", "allDay(0)")

verCO = verucaMenu.addSubMenu("Color Options")
verBtnGrad1 = verCO.addButton("Hour Gradient 1", "setColorBy(0, 0)")
verBtnGrad2 = verCO.addButton("Hour Gradient 2", "setColorBy(0, 1)")
verBtnGrad3 = verCO.addButton("Hour Gradient 3", "setColorBy(0, 2)")
verBtnGrad4 = verCO.addButton("Day Gradient 1", "setColorBy(0, 3)")
verBtnGrad5 = verCO.addButton("Day Gradient 2", "setColorBy(0, 4)")
verBtnGrad6 = verCO.addButton("Color by individual", "setColorBy(0, 5)")

#Chibi-----------------------------------------------------------------------
chibiMenu = subSelectInd.addSubMenu("Chibi 4693")
chibiBtn1 = chibiMenu.addButton("Show Data", "setSelInd(1)")

chibiMenu.addButton("Forward a day", "oneDayStepUp(1)")
chibiMenu.addButton("Backward a day", "oneDayStepDown(1)")
chibiMenu.addButton("7 Days Forward", "sevenDayStepUp(1)")
chibiMenu.addButton("7 Days Backward", "sevenDayStepDown(1)")
chibiMenu.addLabel("----------------")
chibiMenu.addButton("All Days", "allDay(1)")

chibiCO = chibiMenu.addSubMenu("Color Options")
chibiBtnGrad1 = chibiCO.addButton("Hour Gradient 1", "setColorBy(1, 0)")
chibiBtnGrad2 = chibiCO.addButton("Hour Gradient 2", "setColorBy(1, 1)")
chibiBtnGrad3 = chibiCO.addButton("Hour Gradient 3", "setColorBy(1, 2)")
chibiBtnGrad4 = chibiCO.addButton("Day Gradient 1", "setColorBy(1, 3)")
chibiBtnGrad5 = chibiCO.addButton("Day Gradient 2", "setColorBy(1, 4)")
chibiBtnGrad6 = chibiCO.addButton("Color by individual", "setColorBy(1, 5)")

#Abby---------------------------------------------------------------------
abbyMenu = subSelectInd.addSubMenu("Abby 4652")
abbyBtn1 = abbyMenu.addButton("Show Data", "setSelInd(2)")

abbyMenu.addButton("Forward a day", "oneDayStepUp(2)")
abbyMenu.addButton("Backward a day", "oneDayStepDown(2)")
abbyMenu.addButton("7 Days Forward", "sevenDayStepUp(2)")
abbyMenu.addButton("7 Days Backward", "sevenDayStepDown(2)")
abbyMenu.addLabel("----------------")
abbyMenu.addButton("All Days", "allDay(2)")

abbyCO = abbyMenu.addSubMenu("Color Options")
abbyBtnGrad1 = abbyCO.addButton("Hour Gradient 1", "setColorBy(2, 0)")
abbyBtnGrad2 = abbyCO.addButton("Hour Gradient 2", "setColorBy(2, 1)")
abbyBtnGrad3 = abbyCO.addButton("Hour Gradient 3", "setColorBy(2, 2)")
abbyBtnGrad4 = abbyCO.addButton("Day Gradient 1", "setColorBy(2, 3)")
abbyBtnGrad5 = abbyCO.addButton("Day Gradient 2", "setColorBy(2, 4)")
abbyBtnGrad6 = abbyCO.addButton("Color by individual", "setColorBy(2, 5)")

#Ben Bob-----------------------------------------------------------------
benbobMenu = subSelectInd.addSubMenu("Ben Bob 4653")
benbobBtn1 = benbobMenu.addButton("Show Data", "setSelInd(3)")

benbobMenu.addButton("Forward a day", "oneDayStepUp(3)")
benbobMenu.addButton("Backward a day", "oneDayStepDown(3)")
benbobMenu.addButton("7 Days Forward", "sevenDayStepUp(3)")
benbobMenu.addButton("7 Days Backward", "sevenDayStepDown(3)")
benbobMenu.addLabel("----------------")
benbobMenu.addButton("All Days", "allDay(3)")

benBobCO = benbobMenu.addSubMenu("Color Options")
benBtnGrad1 = benBobCO.addButton("Hour Gradient 1", "setColorBy(3, 0)")
benBtnGrad2 = benBobCO.addButton("Hour Gradient 2", "setColorBy(3, 1)")
benBtnGrad3 = benBobCO.addButton("Hour Gradient 3", "setColorBy(3, 2)")
benBtnGrad4 = benBobCO.addButton("Day Gradient 1", "setColorBy(3, 3)")
benBtnGrad5 = benBobCO.addButton("Day Gradient 2", "setColorBy(3, 4)")
benBtnGrad6 = benBobCO.addButton("Color by individual", "setColorBy(3, 5)")

#Bonnie------------------------------------------------------------------
bonnieMenu = subSelectInd.addSubMenu("Bonnie 4658")
bonnieBtn1 = bonnieMenu.addButton("Show Data", "setSelInd(4)")

bonnieMenu.addButton("Forward a day", "oneDayStepUp(4)")
bonnieMenu.addButton("Backward a day", "oneDayStepDown(4)")
bonnieMenu.addButton("7 Days Forward", "sevenDayStepUp(4)")
bonnieMenu.addButton("7 Days Backward", "sevenDayStepDown(4)")
bonnieMenu.addLabel("----------------")
bonnieMenu.addButton("All Days", "allDay(4)")

bonCO = bonnieMenu.addSubMenu("Color Options")
bonBtnGrad1 = bonCO.addButton("Hour Gradient 1", "setColorBy(4, 0)")
bonBtnGrad2 = bonCO.addButton("Hour Gradient 2", "setColorBy(4, 1)")
bonBtnGrad3 = bonCO.addButton("Hour Gradient 3", "setColorBy(4, 2)")
bonBtnGrad4 = bonCO.addButton("Day Gradient 1", "setColorBy(4, 3)")
bonBtnGrad5 = bonCO.addButton("Day Gradient 2", "setColorBy(4, 4)")
bonBtnGrad6 = bonCO.addButton("Color by individual", "setColorBy(4, 5)")

#Chloe-------------------------------------------------------------------
chloeMenu = subSelectInd.addSubMenu("Chloe 4052")
chloeBtn1 = chloeMenu.addButton("Show Data", "setSelInd(5)")

chloeMenu.addButton("Forward a day", "oneDayStepUp(5)")
chloeMenu.addButton("Backward a day", "oneDayStepDown(5)")
chloeMenu.addButton("7 Days Forward", "sevenDayStepUp(5)")
chloeMenu.addButton("7 Days Backward", "sevenDayStepDown(5)")
chloeMenu.addLabel("----------------")
chloeMenu.addButton("All Days", "allDay(5)")

chloeCO = chloeMenu.addSubMenu("Color Options")
chloeBtnGrad1 = chloeCO.addButton("Hour Gradient 1", "setColorBy(5, 0)")
chloeBtnGrad2 = chloeCO.addButton("Hour Gradient 2", "setColorBy(5, 1)")
chloeBtnGrad3 = chloeCO.addButton("Hour Gradient 3", "setColorBy(5, 2)")
chloeBtnGrad4 = chloeCO.addButton("Day Gradient 1", "setColorBy(5, 3)")
chloeBtnGrad5 = chloeCO.addButton("Day Gradient 2", "setColorBy(5, 4)")
chloeBtnGrad6 = chloeCO.addButton("Color by individual", "setColorBy(5, 5)")

#Clementina---------------------------------------------------------------
clementinaMenu = subSelectInd.addSubMenu("Clementina 4672")
clemBtn1 = clementinaMenu.addButton("Show Data", "setSelInd(6)")

clementinaMenu.addButton("Forward a day", "oneDayStepUp(6)")
clementinaMenu.addButton("Backward a day", "oneDayStepDown(6)")
clementinaMenu.addButton("7 Days Forward", "sevenDayStepUp(6)")
clementinaMenu.addButton("7 Days Backward", "sevenDayStepDown(6)")
clementinaMenu.addLabel("----------------")
clementinaMenu.addButton("All Days", "allDay(6)")

clemCO = clementinaMenu.addSubMenu("Color Options")
clemBtnGrad1 = clemCO.addButton("Hour Gradient 1", "setColorBy(6, 0)")
clemBtnGrad2 = clemCO.addButton("Hour Gradient 2", "setColorBy(6, 1)")
clemBtnGrad3 = clemCO.addButton("Hour Gradient 3", "setColorBy(6, 2)")
clemBtnGrad4 = clemCO.addButton("Day Gradient 1", "setColorBy(6, 3)")
clemBtnGrad5 = clemCO.addButton("Day Gradient 2", "setColorBy(6, 4)")
clemBtnGrad6 = clemCO.addButton("Color by individual", "setColorBy(6, 5)")

#Ellie---------------------------------------------------------------------
ellieMenu = subSelectInd.addSubMenu("Ellie 4668")
ellieBtn1 = ellieMenu.addButton("Show Data", "setSelInd(7)")

ellieMenu.addButton("Forward a day", "oneDayStepUp(7)")
ellieMenu.addButton("Backward a day", "oneDayStepDown(7)")
ellieMenu.addButton("7 Days Forward", "sevenDayStepUp(7)")
ellieMenu.addButton("7 Days Backward", "sevenDayStepDown(7)")
ellieMenu.addLabel("----------------")
ellieMenu.addButton("All Days", "allDay(7)")

elCO = ellieMenu.addSubMenu("Color Options")
elBtnGrad1 = elCO.addButton("Hour Gradient 1", "setColorBy(7, 0)")
elBtnGrad2 = elCO.addButton("Hour Gradient 2", "setColorBy(7, 1)")
elBtnGrad3 = elCO.addButton("Hour Gradient 3", "setColorBy(7, 2)")
elBtnGrad4 = elCO.addButton("Day Gradient 1", "setColorBy(7, 3)")
elBtnGrad5 = elCO.addButton("Day Gradient 2", "setColorBy(7, 4)")
elBtnGrad6 = elCO.addButton("Color by individual", "setColorBy(7, 5)")

#Gillian-------------------------------------------------------------------
gillianMenu = subSelectInd.addSubMenu("Gillian 4671")
gillBtn1 = gillianMenu.addButton("Show Data", "setSelInd(8)")

gillianMenu.addButton("Forward a day", "oneDayStepUp(8)")
gillianMenu.addButton("Backward a day", "oneDayStepDown(8)")
gillianMenu.addButton("7 Days Forward", "sevenDayStepUp(8)")
gillianMenu.addButton("7 Days Backward", "sevenDayStepDown(8)")
gillianMenu.addLabel("----------------")
gillianMenu.addButton("All Days", "allDay(8)")

gilCO = gillianMenu.addSubMenu("Color Options")
gilBtnGrad1 = gilCO.addButton("Hour Gradient 1", "setColorBy(8, 0)")
gilBtnGrad2 = gilCO.addButton("Hour Gradient 2", "setColorBy(8, 1)")
gilBtnGrad3 = gilCO.addButton("Hour Gradient 3", "setColorBy(8, 2)")
gilBtnGrad4 = gilCO.addButton("Day Gradient 1", "setColorBy(8, 3)")
gilBtnGrad5 = gilCO.addButton("Day Gradient 2", "setColorBy(8, 4)")
gilBtnGrad6 = gilCO.addButton("Color by individual", "setColorBy(8, 5)")

#Ornette------------------------------------------------------------------
ornetteMenu = subSelectInd.addSubMenu("Ornette 4669")
ornetteBtn1 = ornetteMenu.addButton("Show Data", "setSelInd(9)")

ornetteMenu.addButton("Forward a day", "oneDayStepUp(9)")
ornetteMenu.addButton("Backward a day", "oneDayStepDown(9)")
ornetteMenu.addButton("7 Days Forward", "sevenDayStepUp(9)")
ornetteMenu.addButton("7 Days Backward", "sevenDayStepDown(9)")
ornetteMenu.addLabel("----------------")
ornetteMenu.addButton("All Days", "allDay(9)")

ornCO = ornetteMenu.addSubMenu("Color Options")
ornBtnGrad1 = ornCO.addButton("Hour Gradient 1", "setColorBy(9, 0)")
ornBtnGrad2 = ornCO.addButton("Hour Gradient 2", "setColorBy(9, 1)")
ornBtnGrad3 = ornCO.addButton("Hour Gradient 3", "setColorBy(9, 2)")
ornBtnGrad4 = ornCO.addButton("Day Gradient 1", "setColorBy(9, 3)")
ornBtnGrad5 = ornCO.addButton("Day Gradient 2", "setColorBy(9, 4)")
ornBtnGrad6 = ornCO.addButton("Color by individual", "setColorBy(9, 5)")

#Pliny-------------------------------------------------------------------
plinyMenu = subSelectInd.addSubMenu("Pliny 4675")
plinyBtn1 = plinyMenu.addButton("Show Data", "setSelInd(10)")

plinyMenu.addButton("Forward a day", "oneDayStepUp(10)")
plinyMenu.addButton("Backward a day", "oneDayStepDown(10)")
plinyMenu.addButton("7 Days Forward", "sevenDayStepUp(10)")
plinyMenu.addButton("7 Days Backward", "sevenDayStepDown(10)")
plinyMenu.addLabel("----------------")
plinyMenu.addButton("All Days", "allDay(10)")

pliCO = plinyMenu.addSubMenu("Color Options")
pliBtnGrad1 = pliCO.addButton("Hour Gradient 1", "setColorBy(10, 0)")
pliBtnGrad2 = pliCO.addButton("Hour Gradient 2", "setColorBy(10, 1)")
pliBtnGrad3 = pliCO.addButton("Hour Gradient 3", "setColorBy(10, 2)")
pliBtnGrad4 = pliCO.addButton("Day Gradient 1", "setColorBy(10, 3)")
pliBtnGrad5 = pliCO.addButton("Day Gradient 2", "setColorBy(10, 4)")
pliBtnGrad6 = pliCO.addButton("Color by individual", "setColorBy(10, 5)")

#Ripley-----------------------------------------------------------------
ripleyMenu = subSelectInd2.addSubMenu("Ripley 4650")
ripleyBtn1 = ripleyMenu.addButton("Show Data", "setSelInd(11)")

ripleyMenu.addButton("Forward a day", "oneDayStepUp(11)")
ripleyMenu.addButton("Backward a day", "oneDayStepDown(11)")
ripleyMenu.addButton("7 Days Forward", "sevenDayStepUp(11)")
ripleyMenu.addButton("7 Days Backward", "sevenDayStepDown(11)")
ripleyMenu.addLabel("----------------")
ripleyMenu.addButton("All Days", "allDay(11)")

ripCO = ripleyMenu.addSubMenu("Color Options")
ripBtnGrad1 = ripCO.addButton("Hour Gradient 1", "setColorBy(11, 0)")
ripBtnGrad2 = ripCO.addButton("Hour Gradient 2", "setColorBy(11, 1)")
ripBtnGrad3 = ripCO.addButton("Hour Gradient 3", "setColorBy(11, 2)")
ripBtnGrad4 = ripCO.addButton("Day Gradient 1", "setColorBy(11, 3)")
ripBtnGrad5 = ripCO.addButton("Day Gradient 2", "setColorBy(11, 4)")
ripBtnGrad6 = ripCO.addButton("Color by individual", "setColorBy(11, 5)")

#Sofie-------------------------------------------------------------------
sofieMenu = subSelectInd2.addSubMenu("Sofie 4674")
sofieBtn1 = sofieMenu.addButton("Show Data", "setSelInd(12)")

sofieMenu.addButton("Forward a day", "oneDayStepUp(12)")
sofieMenu.addButton("Backward a day", "oneDayStepDown(12)")
sofieMenu.addButton("7 Days Forward", "sevenDayStepUp(12)")
sofieMenu.addButton("7 Days Backward", "sevenDayStepDown(12)")
sofieMenu.addLabel("----------------")
sofieMenu.addButton("All Days", "allDay(12)")

sofCO = sofieMenu.addSubMenu("Color Options")
sofBtnGrad1 = sofCO.addButton("Hour Gradient 1", "setColorBy(12, 0)")
sofBtnGrad2 = sofCO.addButton("Hour Gradient 2", "setColorBy(12, 1)")
sofBtnGrad3 = sofCO.addButton("Hour Gradient 3", "setColorBy(12, 2)")
sofBtnGrad4 = sofCO.addButton("Day Gradient 1", "setColorBy(12, 3)")
sofBtnGrad5 = sofCO.addButton("Day Gradient 2", "setColorBy(12, 4)")
sofBtnGrad6 = sofCO.addButton("Color by individual", "setColorBy(12, 5)")

#Greg--------------------------------------------------------------------
gregMenu = subSelectInd2.addSubMenu("Greg 4689")
gregBtn1 = gregMenu.addButton("Show Data", "setSelInd(13)")

gregMenu.addButton("Forward a day", "oneDayStepUp(13)")
gregMenu.addButton("Backward a day", "oneDayStepDown(13)")
gregMenu.addButton("7 Days Forward", "sevenDayStepUp(13)")
gregMenu.addButton("7 Days Backward", "sevenDayStepDown(13)")
gregMenu.addLabel("----------------")
gregMenu.addButton("All Days", "allDay(13)")

gregCO = gregMenu.addSubMenu("Color Options")
gregBtnGrad1 = gregCO.addButton("Hour Gradient 1", "setColorBy(13, 0)")
gregBtnGrad2 = gregCO.addButton("Hour Gradient 2", "setColorBy(13, 1)")
gregBtnGrad3 = gregCO.addButton("Hour Gradient 3", "setColorBy(13, 2)")
gregBtnGrad4 = gregCO.addButton("Day Gradient 1", "setColorBy(13, 3)")
gregBtnGrad5 = gregCO.addButton("Day Gradient 2", "setColorBy(13, 4)")
gregBtnGrad6 = gregCO.addButton("Color by individual", "setColorBy(13, 5)")

#Ibeth------------------------------------------------------------------
ibethMenu = subSelectInd2.addSubMenu("Ibeth 4654")
ibethBtn1 = ibethMenu.addButton("Show Data", "setSelInd(14)")

ibethMenu.addButton("Forward a day", "oneDayStepUp(14)")
ibethMenu.addButton("Backward a day", "oneDayStepDown(14)")
ibethMenu.addButton("7 Days Forward", "sevenDayStepUp(14)")
ibethMenu.addButton("7 Days Backward", "sevenDayStepDown(14)")
ibethMenu.addLabel("----------------")
ibethMenu.addButton("All Days", "allDay(14)")

ibeCO = ibethMenu.addSubMenu("Color Options")
ibeBtnGrad1 = ibeCO.addButton("Hour Gradient 1", "setColorBy(14, 0)")
ibeBtnGrad2 = ibeCO.addButton("Hour Gradient 2", "setColorBy(14, 1)")
ibeBtnGrad3 = ibeCO.addButton("Hour Gradient 3", "setColorBy(14, 2)")
ibeBtnGrad4 = ibeCO.addButton("Day Gradient 1", "setColorBy(14, 3)")
ibeBtnGrad5 = ibeCO.addButton("Day Gradient 2", "setColorBy(14, 4)")
ibeBtnGrad6 = ibeCO.addButton("Color by individual", "setColorBy(14, 5)")

#Olga-------------------------------------------------------------------
olgaMenu = subSelectInd2.addSubMenu("Olga 4657")
olgaBtn1 = olgaMenu.addButton("Show Data", "setSelInd(15)")

olgaMenu.addButton("Forward a day", "oneDayStepUp(15)")
olgaMenu.addButton("Backward a day", "oneDayStepDown(15)")
olgaMenu.addButton("7 Days Forward", "sevenDayStepUp(15)")
olgaMenu.addButton("7 Days Backward", "sevenDayStepDown(15)")
olgaMenu.addLabel("----------------")
olgaMenu.addButton("All Days", "allDay(15)")

olgaCO = olgaMenu.addSubMenu("Color Options")
olgaBtnGrad1 = olgaCO.addButton("Hour Gradient 1", "setColorBy(15, 0)")
olgaBtnGrad2 = olgaCO.addButton("Hour Gradient 2", "setColorBy(15, 1)")
olgaBtnGrad3 = olgaCO.addButton("Hour Gradient 3", "setColorBy(15, 2)")
olgaBtnGrad4 = olgaCO.addButton("Day Gradient 1", "setColorBy(15, 3)")
olgaBtnGrad5 = olgaCO.addButton("Day Gradient 2", "setColorBy(15, 4)")
olgaBtnGrad6 = olgaCO.addButton("Color by individual", "setColorBy(15, 5)")

#Mimi--------------------------------------------------------------------
mimiMenu = subSelectInd2.addSubMenu("Mimi 4660")
mimiBtn1 = mimiMenu.addButton("Show Data", "setSelInd(16)")

mimiMenu.addButton("Forward a day", "oneDayStepUp(16)")
mimiMenu.addButton("Backward a day", "oneDayStepDown(16)")
mimiMenu.addButton("7 Days Forward", "sevenDayStepUp(16)")
mimiMenu.addButton("7 Days Backward", "sevenDayStepDown(16)")
mimiMenu.addLabel("----------------")
mimiMenu.addButton("All Days", "allDay(16)")

mimiCO = mimiMenu.addSubMenu("Color Options")
mimiBtnGrad1 = mimiCO.addButton("Hour Gradient 1", "setColorBy(16, 0)")
mimiBtnGrad2 = mimiCO.addButton("Hour Gradient 2", "setColorBy(16, 1)")
mimiBtnGrad3 = mimiCO.addButton("Hour Gradient 3", "setColorBy(16, 2)")
mimiBtnGrad4 = mimiCO.addButton("Day Gradient 1", "setColorBy(16, 3)")
mimiBtnGrad5 = mimiCO.addButton("Day Gradient 2", "setColorBy(16, 4)")
mimiBtnGrad6 = mimiCO.addButton("Color by individual", "setColorBy(16, 5)")

#Kyle---------------------------------------------------------------------
kyleMenu = subSelectInd2.addSubMenu("Kyle 4692")
kyleBtn1 = kyleMenu.addButton("Show Data", "setSelInd(17)")

kyleMenu.addButton("Forward a day", "oneDayStepUp(17)")
kyleMenu.addButton("Backward a day", "oneDayStepDown(17)")
kyleMenu.addButton("7 Days Forward", "sevenDayStepUp(17)")
kyleMenu.addButton("7 Days Backward", "sevenDayStepDown(17)")
kyleMenu.addLabel("----------------")
kyleMenu.addButton("All Days", "allDay(17)")

kyleCO = kyleMenu.addSubMenu("Color Options")
kyleBtnGrad1 = kyleCO.addButton("Hour Gradient 1", "setColorBy(17, 0)")
kyleBtnGrad2 = kyleCO.addButton("Hour Gradient 2", "setColorBy(17, 1)")
kyleBtnGrad3 = kyleCO.addButton("Hour Gradient 3", "setColorBy(17, 2)")
kyleBtnGrad4 = kyleCO.addButton("Day Gradient 1", "setColorBy(17, 3)")
kyleBtnGrad5 = kyleCO.addButton("Day Gradient 2", "setColorBy(17, 4)")
kyleBtnGrad6 = kyleCO.addButton("Color by individual", "setColorBy(17, 5)")

#Atlas-------------------------------------------------------------------
atlasMenu = subSelectInd2.addSubMenu("Atlas 4673")
atlasBtn1 = atlasMenu.addButton("Show Data", "setSelInd(18)")

atlasMenu.addButton("Forward a day", "oneDayStepUp(18)")
atlasMenu.addButton("Backward a day", "oneDayStepDown(18)")
atlasMenu.addButton("7 Days Forward", "sevenDayStepUp(18)")
atlasMenu.addButton("7 Days Backward", "sevenDayStepDown(18)")
atlasMenu.addLabel("----------------")
atlasMenu.addButton("All Days", "allDay(18)")

atlasCO = atlasMenu.addSubMenu("Color Options")
atlasBtnGrad1 = atlasCO.addButton("Hour Gradient 1", "setColorBy(18, 0)")
atlasBtnGrad2 = atlasCO.addButton("Hour Gradient 2", "setColorBy(18, 1)")
atlasBtnGrad3 = atlasCO.addButton("Hour Gradient 3", "setColorBy(18, 2)")
atlasBtnGrad4 = atlasCO.addButton("Day Gradient 1", "setColorBy(18, 3)")
atlasBtnGrad5 = atlasCO.addButton("Day Gradient 2", "setColorBy(18, 4)")
atlasBtnGrad6 = atlasCO.addButton("Color by individual", "setColorBy(18, 5)")

#Judy----------------------------------------------------------------------
judyMenu = subSelectInd2.addSubMenu("Judy 4656")
judyBtn1 = judyMenu.addButton("Show Data", "setSelInd(19)")

judyMenu.addButton("Forward a day", "oneDayStepUp(19)")
judyMenu.addButton("Backward a day", "oneDayStepDown(19)")
judyMenu.addButton("7 Days Forward", "sevenDayStepUp(19)")
judyMenu.addButton("7 Days Backward", "sevenDayStepDown(19)")
judyMenu.addLabel("----------------")
judyMenu.addButton("All Days", "allDay(19)")

judyCO = judyMenu.addSubMenu("Color Options")
judyBtnGrad1 = judyCO.addButton("Hour Gradient 1", "setColorBy(19, 0)")
judyBtnGrad2 = judyCO.addButton("Hour Gradient 2", "setColorBy(19, 1)")
judyBtnGrad3 = judyCO.addButton("Hour Gradient 3", "setColorBy(19, 2)")
judyBtnGrad4 = judyCO.addButton("Day Gradient 1", "setColorBy(19, 3)")
judyBtnGrad5 = judyCO.addButton("Day Gradient 2", "setColorBy(19, 4)")
judyBtnGrad6 = judyCO.addButton("Color by individual", "setColorBy(19, 5)")

#Merk---------------------------------------------------------------------
merkMenu = subSelectInd2.addSubMenu("Merk 4665")
merkBtn1 = merkMenu.addButton("Show Data", "setSelInd(20)")

merkMenu.addButton("Forward a day", "oneDayStepUp(20)")
merkMenu.addButton("Backward a day", "oneDayStepDown(20)")
merkMenu.addButton("7 Days Forward", "sevenDayStepUp(20)")
merkMenu.addButton("7 Days Backward", "sevenDayStepDown(20)")
merkMenu.addLabel("----------------")
merkMenu.addButton("All Days", "allDay(20)")

merkCO = merkMenu.addSubMenu("Color Options")
merkBtnGrad1 = merkCO.addButton("Hour Gradient 1", "setColorBy(20, 0)")
merkBtnGrad2 = merkCO.addButton("Hour Gradient 2", "setColorBy(20, 1)")
merkBtnGrad3 = merkCO.addButton("Hour Gradient 3", "setColorBy(20, 2)")
merkBtnGrad4 = merkCO.addButton("Day Gradient 1", "setColorBy(20, 3)")
merkBtnGrad5 = merkCO.addButton("Day Gradient 2", "setColorBy(20, 4)")
merkBtnGrad6 = merkCO.addButton("Color by individual", "setColorBy(20, 5)")

ss6 = mm.getMainMenu().addButton("Show Fruit Trees", "markTrees(1)")
ss7 = mm.getMainMenu().addButton("Draw Lines to Trees", "drawLinesToTrees(1)")

#btnAll.setRadio(True)

#--------------------------------------------------------------------------------------
#Cylinder Code
toggleTrees = False

thickness = 10
treeNode = SceneNode.create('treeNode')
getScene().addChild(treeNode)
treeList = []
treeIndex = 0
trees = open("treesFloat.txt", "r")
treeContent = trees.readlines()
c1 = LineSet.create()
for line in treeContent:
    tokens = line.split(" ")

    treeList.append([])
    treeList[treeIndex].append(float(tokens[0]))
    treeList[treeIndex].append(float(tokens[1]))
    treeList[treeIndex].append(float(tokens[2]))
    treeIndex += 1

    l = c1.addLine()
    l.setStart(Vector3(float(tokens[0]), float(tokens[1]), 0))
    l.setEnd(Vector3(float(tokens[0]), float(tokens[1]), int(tokens[2])))
    l.setThickness(thickness)
    s = SphereShape.create(thickness/2, 2)
    c1.addChild(s)
    s.setEffect('colored -e #9b30ff')
    s.setPosition(Vector3(float(tokens[0]), float(tokens[1]), int(tokens[2])))
    c1.setEffect('colored -e #9b30ff')
trees.close()
treeNode.addChild(c1)
treeNode.setChildrenVisible(False)

def markTrees(value):
    global toggleTrees
    global treeNode

    if (value == 1):
        toggleTrees = not toggleTrees
        treeNode.setChildrenVisible(toggleTrees)

showOtherTrees = SceneNode.create('showOtherTrees')
getScene().addChild(showOtherTrees)

c2 = LineSet.create()
toggleLineToTrees = False
lineList = []
numLines = 0

def drawLinesToTrees(value):
    global toggleLineToTrees
    if (value == 1):
        toggleLineToTrees = not toggleLineToTrees


hasCameraMoved = False
drawnCamPos = getDefaultCamera().getPosition()

def onUpdate(frame, time, dt):
    global treeList
    global toggleLineToTrees
    global showOtherTrees
    global c2
    global lineList
    global hasCameraMoved
    global drawnCamPos
    global movementData
    global textNodeList

    #Draw Lines To Trees Code#########################################################################
    currCamPos = getDefaultCamera().getPosition()
    xPos = currCamPos[0]
    yPos = currCamPos[1]
    zPos = currCamPos[2]

    hasCameraMoved = False

    if (drawnCamPos[0]+5 < xPos or drawnCamPos[0]-5 > xPos) or (drawnCamPos[1]+5 < yPos or drawnCamPos[1]-5 > yPos) or (drawnCamPos[2]+5 < zPos or drawnCamPos[2]-5 > zPos):
        hasCameraMoved = True

    
    while lineList and hasCameraMoved:
        line = lineList.pop()
        c2.removeLine(line)
        
    if (toggleLineToTrees and hasCameraMoved):
        thickness2 = 3
        for node in treeList:
            vec = Vector3(node[0], node[1], node[2]*0.18)
            camVec = getDefaultCamera().getPosition()
            if (abs(vec - camVec) <= 100):
                lineList.append(c2.addLine())
                lineList[numLines].setStart(vec)
                vec2 = vec - camVec
                normal = vec2.normalize()
                lineList[numLines].setEnd(camVec - 10*normal)
                lineList[numLines].setThickness(thickness2)
                s2 = SphereShape.create(thickness2/2, 2)
                c2.addChild(s2)
                s2.setEffect('colored -e red')
                s2.setPosition(camVec - 10*normal)
                c2.setEffect('colored -e red')
                lineList.append(lastIndividualTxt)
                drawnCamPos = getDefaultCamera().getPosition()
    ################################################################################################
    

        #showOtherTrees.addChild(c2)
setUpdateFunction(onUpdate)
        

#--------------------------------------------------------------------------------------
#Functions
def oneDayStepUp(value):        #value is the individualID
    global myStartDay
    global myEndDay
    global startDay
    global endDay
    global numberOfDaysByIndividual
    global movementData
    global txtArr
    global namesOfIndividuals
    global lastIndividualTxt, dayRangeTxt
    global lineToTxt

    myStartDay[value] = myStartDay[value] + 1
    if myStartDay[value] > numberOfDaysByIndividual[value]:
        myStartDay[value] = 0
    myEndDay[value] = myStartDay[value] + 1
    endDay.setIntElement(myEndDay[value], value)
    startDay.setIntElement(myStartDay[value], value)
    txtArr[value][0].setPosition(Vector3(movementData[value][myStartDay[value]][0][0]+XYOFFSET, movementData[value][myStartDay[value]][0][1]+XYOFFSET, movementData[value][myStartDay[value]][0][2]+STARTTXTOFFSET))
    txtArr[value][1].setPosition(Vector3(movementData[value][myEndDay[value]][0][0]-XYOFFSET, movementData[value][myEndDay[value]][0][1]-XYOFFSET, movementData[value][myEndDay[value]][0][2]+ENDTXTOFFSET))
    txtArr[value][2].setPosition(Vector3(movementData[value][myStartDay[value]][0][0]+XYOFFSET, movementData[value][myStartDay[value]][0][1]-XYOFFSET, movementData[value][myStartDay[value]][0][2]+INDNAMETXTOFFSET))

    setLinePos(lineToTxt, value)
    
    lastIndividualTxt.setText(namesOfIndividuals[value])
    dayRangeTxt.setText(str(startDateByIndividual[value]+timedelta(days=myStartDay[value]))+" - "+str(startDateByIndividual[value]+timedelta(days=myEndDay[value])))

def globalOneDayStepUp(value):
    global myStartDay
    global myEndDay
    global startDay
    global endDay
    global numberOfDaysByIndividual
    global movementData
    global txtArr
    global lineToTxt


    for i in range(0, 21):
        myStartDay[i] = myStartDay[i] + 1
        if myStartDay[i] > numberOfDaysByIndividual[i]:
            myStartDay[i] = 0
        myEndDay[i] = myStartDay[i] + 1
        endDay.setIntElement(myEndDay[i], i)
        startDay.setIntElement(myStartDay[i], i)

        #Update text positions to location of animals
        txtArr[i][0].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]+XYOFFSET, movementData[i][myStartDay[i]][0][2]+STARTTXTOFFSET))
        txtArr[i][1].setPosition(Vector3(movementData[i][myEndDay[i]][0][0]-XYOFFSET, movementData[i][myEndDay[i]][0][1]-XYOFFSET, movementData[i][myEndDay[i]][0][2]+ENDTXTOFFSET))
        txtArr[i][2].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]-XYOFFSET, movementData[i][myStartDay[i]][0][2]+INDNAMETXTOFFSET))

        setLinePos(lineToTxt, i)
        
    # print( "one day step up" + myStartDay)

def oneDayStepDown(value):
    global myStartDay
    global myEndDay
    global startDay
    global endDay
    global numberOfDaysByIndividual
    global movementData
    global txtArr
    global namesOfIndividuals
    global lastIndividualTxt
    global dayRangeTxt
    global lineToTxt

    myStartDay[value] = myStartDay[value] - 1
    if myStartDay[value] < 0:
        myStartDay[value] = numberOfDaysByIndividual[value]-1
    myEndDay[value] = myStartDay[value] + 1
    endDay.setIntElement(myEndDay[value], value)
    startDay.setIntElement(myStartDay[value], value)
    txtArr[value][0].setPosition(Vector3(movementData[value][myStartDay[value]][0][0]+XYOFFSET, movementData[value][myStartDay[value]][0][1]+XYOFFSET, movementData[value][myStartDay[value]][0][2]+STARTTXTOFFSET))
    txtArr[value][1].setPosition(Vector3(movementData[value][myEndDay[value]][0][0]-XYOFFSET, movementData[value][myEndDay[value]][0][1]-XYOFFSET, movementData[value][myEndDay[value]][0][2]+ENDTXTOFFSET))
    txtArr[value][2].setPosition(Vector3(movementData[value][myStartDay[value]][0][0]+XYOFFSET, movementData[value][myStartDay[value]][0][1]-XYOFFSET, movementData[value][myStartDay[value]][0][2]+INDNAMETXTOFFSET))

    setLinePos(lineToTxt, value)

    lastIndividualTxt.setText(namesOfIndividuals[value])
    dayRangeTxt.setText(str(startDateByIndividual[value]+timedelta(days=myStartDay[value]))+" - "+str(startDateByIndividual[value]+timedelta(days=myEndDay[value])))

def globalOneDayStepDown(value):
    global myStartDay
    global myEndDay
    global startDay
    global endDay
    global numberOfDaysByIndividual
    global movementData
    global txtArr

    for i in range(0, 21):
        myStartDay[i] = myStartDay[i] - 1
        if myStartDay[i] < 0:
            myStartDay[i] = numberOfDaysByIndividual[i]-1
        myEndDay[i] = myStartDay[i] + 1
        endDay.setIntElement(myEndDay[i], i)
        startDay.setIntElement(myStartDay[i], i)
        txtArr[i][0].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]+XYOFFSET, movementData[i][myStartDay[i]][0][2]+STARTTXTOFFSET))
        txtArr[i][1].setPosition(Vector3(movementData[i][myEndDay[i]][0][0]-XYOFFSET, movementData[i][myEndDay[i]][0][1]-XYOFFSET, movementData[i][myEndDay[i]][0][2]+ENDTXTOFFSET))
        txtArr[i][2].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]-XYOFFSET, movementData[i][myStartDay[i]][0][2]+INDNAMETXTOFFSET))

        setLinePos(lineToTxt, i)

    # print( "one day step down " + myStartDay)

def sevenDayStepUp(value):
    global myStartDay
    global myEndDay
    global startDay
    global endDay
    global numberOfDaysByIndividual
    global movementData
    global txtArr
    global namesOfIndividuals
    global lastIndividualTxt
    global dayRangeTxt
    global lineToTxt

    myStartDay[value] = myStartDay[value] + 7
    if myStartDay[value] > numberOfDaysByIndividual[value]:
        myStartDay[value] = 0
    myEndDay[value] = myStartDay[value] + 7
    endDay.setIntElement(myEndDay[value], value)
    startDay.setIntElement(myStartDay[value], value)
    txtArr[value][0].setPosition(Vector3(movementData[value][myStartDay[value]][0][0]+XYOFFSET, movementData[value][myStartDay[value]][0][1]+XYOFFSET, movementData[value][myStartDay[value]][0][2]+STARTTXTOFFSET))
    txtArr[value][1].setPosition(Vector3(movementData[value][myEndDay[value]][0][0]-XYOFFSET, movementData[value][myEndDay[value]][0][1]-XYOFFSET, movementData[value][myEndDay[value]][0][2]+ENDTXTOFFSET))
    txtArr[value][2].setPosition(Vector3(movementData[value][myStartDay[value]][0][0]+XYOFFSET, movementData[value][myStartDay[value]][0][1]-XYOFFSET, movementData[value][myStartDay[value]][0][2]+INDNAMETXTOFFSET))

    setLinePos(lineToTxt, value)

    lastIndividualTxt.setText(namesOfIndividuals[value])
    dayRangeTxt.setText(str(startDateByIndividual[value]+timedelta(days=myStartDay[value]))+" - "+str(startDateByIndividual[value]+timedelta(days=myEndDay[value])))

def globalSevenDayStepUp(value):
    global myStartDay
    global myEndDay
    global startDay
    global endDay
    global numberOfDaysByIndividual
    global movementData
    global txtArr

    for i in range(0, 21):
        myStartDay[i] = myStartDay[i] + 7
        if myStartDay[i] > numberOfDaysByIndividual[i]:
            myStartDay[i] = 0
        myEndDay[i] = myStartDay[i] + 7
        endDay.setIntElement(myEndDay[i], i)
        startDay.setIntElement(myStartDay[i], i)
        txtArr[i][0].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]+XYOFFSET, movementData[i][myStartDay[i]][0][2]+STARTTXTOFFSET))
        txtArr[i][1].setPosition(Vector3(movementData[i][myEndDay[i]][0][0]-XYOFFSET, movementData[i][myEndDay[i]][0][1]-XYOFFSET, movementData[i][myEndDay[i]][0][2]+ENDTXTOFFSET))
        txtArr[i][2].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]-XYOFFSET, movementData[i][myStartDay[i]][0][2]+INDNAMETXTOFFSET))

        setLinePos(linetoTxt, i)

    # print( "seven day step up" + myStartDay)

def sevenDayStepDown(value):
    global myStartDay
    global myEndDay
    global startDay
    global endDay
    global numberOfDaysByIndividual
    global movementData
    global txtArr
    global namesOfIndividuals
    global lastIndividualTxt
    global dayRangeTxt
    global lineToTxt

    myStartDay[value] = myStartDay[value] - 7
    if myStartDay[value] < 0:
        myStartDay[value] = numberOfDaysByIndividual[i]-7
    myEndDay[value] = myStartDay[value] + 7
    endDay.setIntElement(myEndDay[value], value)
    startDay.setIntElement(myStartDay[value], value)
    txtArr[value][0].setPosition(Vector3(movementData[value][myStartDay[value]][0][0]+XYOFFSET, movementData[value][myStartDay[value]][0][1]+XYOFFSET, movementData[value][myStartDay[value]][0][2]+STARTTXTOFFSET))
    txtArr[value][1].setPosition(Vector3(movementData[value][myEndDay[value]][0][0]-XYOFFSET, movementData[value][myEndDay[value]][0][1]-XYOFFSET, movementData[value][myEndDay[value]][0][2]+ENDTXTOFFSET))
    txtArr[value][2].setPosition(Vector3(movementData[value][myStartDay[value]][0][0]+XYOFFSET, movementData[value][myStartDay[value]][0][1]+XYOFFSET, movementData[value][myStartDay[value]][0][2]+INDNAMETXTOFFSET))

    setLinePos(lineToTxt, value)

    lastIndividualTxt.setText(namesOfIndividuals[value])
    dayRangeTxt.setText(str(startDateByIndividual[value]+timedelta(days=myStartDay[value]))+" - "+str(startDateByIndividual[value]+timedelta(days=myEndDay[value])))

def globalSevenDayStepDown(value):
    global myStartDay
    global myEndDay
    global startDay
    global endDay
    global numberOfDaysByIndividual
    global movementData
    global txtArr

    for i in range(0, 21):
        myStartDay[i] = myStartDay[i] - 7
        if myStartDay[i] < 0:
            myStartDay[i] = numberOfDaysByIndividual[i]-7
        myEndDay[i] = myStartDay[i] + 7
        endDay.setIntElement(myEndDay[i], i)
        startDay.setIntElement(myStartDay[i], i)
        txtArr[i][0].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]+XYOFFSET, movementData[i][myStartDay[i]][0][2]+STARTTXTOFFSET))
        txtArr[i][1].setPosition(Vector3(movementData[i][myEndDay[i]][0][0]-XYOFFSET, movementData[i][myEndDay[i]][0][1]-XYOFFSET, movementData[i][myEndDay[i]][0][2]+ENDTXTOFFSET))
        txtArr[i][2].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]-XYOFFSET, movementData[i][myStartDay[i]][0][2]+INDNAMETXTOFFSET))

        setLinePos(lineToTxt, i)

    # print( "seven day step down " + myStartDay)

def allDay(value):
    global numberOfDaysByIndividual
    global startDay
    global endDay
    global myStartDay
    global myEndDay
    global movementData
    global txtArr
    global namesOfIndividuals
    global lastIndividualTxt
    global dayRangeTxt
    global lineToTxt

    myStartDay[value] = 0
    myEndDay[value] = numberOfDaysByIndividual[value]
    endDay.setIntElement(numberOfDaysByIndividual[value], value)
    startDay.setIntElement(0, value)
    txtArr[value][0].setPosition(Vector3(movementData[value][myStartDay[value]][0][0]+XYOFFSET, movementData[value][myStartDay[value]][0][1]+XYOFFSET, movementData[value][myStartDay[value]][0][2]+STARTTXTOFFSET))
    txtArr[value][1].setPosition(Vector3(movementData[value][myEndDay[value]][0][0]-XYOFFSET, movementData[value][myEndDay[value]][0][1]-XYOFFSET, movementData[value][myEndDay[value]][0][2]+ENDTXTOFFSET))
    txtArr[value][2].setPosition(Vector3(movementData[value][myStartDay[value]][0][0]+XYOFFSET, movementData[value][myStartDay[value]][0][1]-XYOFFSET, movementData[value][myStartDay[value]][0][2]+INDNAMETXTOFFSET))

    setLinePos(lineToTxt, value)

    lastIndividualTxt.setText(namesOfIndividuals[value])
    dayRangeTxt.setText(str(startDateByIndividual[value]+timedelta(days=myStartDay[value]))+" - "+str(startDateByIndividual[value]+timedelta(days=myEndDay[value])))

def globalAllDay(value):
    global numberOfDaysByIndividual
    global startDay
    global endDay
    global movementData
    global txtArr
    global lineToTxt

    for i in range(0, 21):
        endDay.setIntElement(numberOfDaysByIndividual[i], i)
        startDay.setIntElement(0, i)
        txtArr[i][0].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]+XYOFFSET, movementData[i][myStartDay[i]][0][2]+STARTTXTOFFSET))
        txtArr[i][1].setPosition(Vector3(movementData[i][myEndDay[i]][0][0]-XYOFFSET, movementData[i][myEndDay[i]][0][1]-XYOFFSET, movementData[i][myEndDay[i]][0][2]+ENDTXTOFFSET))
        txtArr[i][2].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, movementData[i][myStartDay[i]][0][1]-XYOFFSET, movementData[i][myStartDay[i]][0][2]+INDNAMETXTOFFSET))

        setLinePos(lineToTxt, i)

    # print( "one day step " + myStartDay)

def setColorBy(individual, value):
    global colorByBitMap

    colorByBitMap.setIntElement(value, individual)

    # print( "set color by " + value)

def setSelInd(value):
    global bitMapSelectedIndividuals
    global textNodeList
    global namesOfIndividuals
    global lastIndividualTxt
    global dayRangeTxt

    val = bitMapSelectedIndividuals.getIntElement(value)
    bitMapSelectedIndividuals.setIntElement((not val), value)
    if val == 1:
        textNodeList[value].setChildrenVisible(False)
    else:
        textNodeList[value].setChildrenVisible(True)

    lastIndividualTxt.setText(namesOfIndividuals[value])
    dayRangeTxt.setText(str(startDateByIndividual[value]+timedelta(days=myStartDay[value]))+" - "+str(startDateByIndividual[value]+timedelta(days=myEndDay[value])))

def onPointSizeSliderValueChanged(value):
    if (value != 0):
        size = .95 + value * .05
    else:
        size = 0.0
    pointScale.setFloat(size)

def onAlphaSliderValueChanged(value):
    if (value != 0):
        a = value/10.0
    else:
        a = 0.0
    globalAlpha.setFloat(a)

def viewVertical(value):
    global currentPitch
    global currentYaw
    global currentRoll
    if (value == 1):
        getDefaultCamera().setPosition(Vector3(imgResRatioX*10260/2, imgResRatioY*9850/2, 2500))
        currentPitch = 0
        getDefaultCamera().setPitchYawRoll(Vector3(currentPitch,currentYaw,currentRoll))

def viewHorizontal(value):
    global currentYaw
    global currentPitch
    if (value == 1):
        currentPitch = 45
        getDefaultCamera().setPitchYawRoll(Vector3(currentPitch, currentYaw,0))
        getDefaultCamera().setPosition(Vector3(imgResRatioX*10260/2, 0, 500))



# --Event handler
#  EVENT HANDLERS
def handleEvent():
    global currentPitch

    e = getEvent()
    analogUD = e.getAxis(1)

    # if (analogUD < -0.500):
    #     print "movingUp"
    #     currentPitch += 0.000000174533
    #     getDefaultCamera().pitch(currentPitch)
    #     # getDefaultCamera().setPitchYawRoll(Vector3(currentPitch, currentYaw, currentRoll))
    # elif (analogUD > 0.500):
    #     print "movingDown"
    #     currentPitch -= 0.000000174533
    #     getDefaultCamera().pitch(currentPitch)
        # getDefaultCamera().setPitchYawRoll(Vector3(currentPitch, currentYaw, currentRoll))
    # if (analogLR > 0.500):
    #     print "movingRight"
    #     currentYaw += 0.002
    #     getDefaultCamera().setPitchYawRoll(Vector3(currentPitch, currentYaw, currentRoll))
    # elif (analogLR < -0.500):
    #     print "movingLeft"
    #     currentYaw -= 0.002
    #     getDefaultCamera.setPitchYawRoll(Vector3(currentPitch, currentYaw, currentRoll))

    if (e.isButtonDown(EventFlags.Button5)):
        print "Button5 Pushed"
        getDefaultCamera().setPosition(Vector3(imgResRatioX*10260/2, 0, 500))
        getDefaultCamera().lookAt(Vector3(imgResRatioX*10260/2, 0, 500), Vector3(0, .25, 0))
setEventFunction(handleEvent)

# def handleEvent():
#     e = getEvent()
    # if(e.isButtonDown(EventFlags.ButtonLeft)): 
    #     print("Left button pressed ")
    #     myStartDay = myStartDay + dayIncrement
    #     myEndDay = myEndDay + dayIncrement
    #     if( myStartDay > numberOfDays ):
    #         myStartDay = 0
    #         myEndDay = dayIncrement
    #     endDay.setInt(myEndDay)
    #     startDay.setInt(myStartDay)
    # if(e.isButtonDown(EventFlags.ButtonRight)):
    #     myStartDay = myStartDay - dayIncrement
    #     myEndDay = myEndDay - dayIncrement
    #     if( myStartDay < 0 ):
    #         myStartDay = numberOfDays - dayIncrement
    #         myEndDay = numberOfDays
    #     endDay.setInt(myEndDay)
    #     startDay.setInt(myStartDay)
    # if(e.isButtonDown(EventFlags.ButtonUp)): 
    #     print("Up button pressed turning off white")
    # if(e.isButtonDown(EventFlags.ButtonDown)):
    #     print("Up button pressed turning on white")

# setEventFunction(handleEvent)
