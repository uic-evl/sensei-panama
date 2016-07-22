from omega import *
from cyclops import *
from pointCloud import *
from math import *

def createCustomGeom(f, scene, color, geomName):
    firstRun = True

    numVertices = 0
    prevV3 = Vector3(0,0,0)
    prevV4 = Vector3(0,0,0)
    prevV7 = Vector3(0,0,0)
    prevV8 = Vector3(0,0,0)

    prevLine = ""

    unitY = Vector3(0,1,0)
    unitZ = Vector3(0,0,1)

    geom = ModelGeometry.create(geomName)
    for line in f:
        # if numVertices == 6:
        #     break
        line2 = f.next()
        
        if not line2:
            break
        tokens2 = line2.split(" ")
        if firstRun:
            tokens = line.split(" ")
            dayCounter = tokens[4]
            nodeCounter = 1
        else:
            tokens = prevLine.split(" ")

        pos1 = Vector3(float(tokens[0]), float(tokens[1]), float(tokens[2]))
        
        pos2 = Vector3(float(tokens2[0]), float(tokens2[1]), float(tokens2[2]))

        vec = pos2 - pos1
        d = vec.normalize()
        unitZV1 = d.cross(unitZ)
        unitYV1 = d.cross(unitY)

        v1 = pos1+1*unitZV1+1*unitYV1       #list of vertices
        v2 = pos1+1*unitZV1-1*unitYV1
        v3 = pos2+1*unitZV1+1*unitYV1
        v4 = pos2+1*unitZV1-1*unitYV1

        v5 = pos1-1*unitZV1+1*unitYV1
        v6 = pos1-1*unitZV1-1*unitYV1
        v7 = pos2-1*unitZV1+1*unitYV1
        v8 = pos2-1*unitZV1-1*unitYV1

    #####################Front Panel##################################################
        geom.addVertex( v3 )
        geom.addColor(Color(color))
        if firstRun:
            geom.addVertex( v2 )
            geom.addColor(Color(color))
            geom.addVertex( v1 )
            geom.addColor(Color(color))
        else:
            geom.addVertex( prevV4 )
            geom.addColor(Color(color))
            geom.addVertex( prevV3 )
            geom.addColor(Color(color))

        if firstRun:
            geom.addVertex( v2 )
            geom.addColor(Color(color))
        else:
            geom.addVertex( prevV4 )
            geom.addColor(Color(color))
        geom.addVertex( v3 )
        geom.addColor(Color(color))
        geom.addVertex( v4 )
        geom.addColor(Color(color))
    ##################################################################################
    #####################Back Panel##################################################
        geom.addVertex( v7 )
        geom.addColor(Color(color))
        if firstRun:
            geom.addVertex( v6 )
            geom.addColor(Color(color))
            geom.addVertex( v5 )
            geom.addColor(Color(color))
        else:
            geom.addVertex( prevV8 )
            geom.addColor(Color(color))
            geom.addVertex( prevV7 )
            geom.addColor(Color(color))

        if firstRun:
            geom.addVertex( v6 )
            geom.addColor(Color(color))
        else:
            geom.addVertex( prevV8)
            geom.addColor(Color(color))
        geom.addVertex( v7 )
        geom.addColor(Color(color))
        geom.addVertex( v8 )
        geom.addColor(Color(color))
    ##################################################################################
    #####################Top Panel##################################################
        geom.addVertex( v7 )
        geom.addColor(Color(color))
        if firstRun:
            geom.addVertex( v1 )
            geom.addColor(Color(color))
            geom.addVertex( v5 )
            geom.addColor(Color(color))
        else:
            geom.addVertex( prevV3 )
            geom.addColor(Color(color))
            geom.addVertex( prevV7 )
            geom.addColor(Color(color))
        
        geom.addVertex( v7 )
        geom.addColor(Color(color))
        geom.addVertex( v3 )
        geom.addColor(Color(color))
        if firstRun:
            geom.addVertex( v1 )
            geom.addColor(Color(color))
        else:
            geom.addVertex( prevV3 )
            geom.addColor(Color(color))
    ##################################################################################
    #####################Bottom Panel##################################################
        
        if firstRun:
            geom.addVertex( v2 )
            geom.addColor(Color(color))
            geom.addVertex( v6 )
            geom.addColor(Color(color))
        else:
            geom.addVertex( prevV4 )
            geom.addColor(Color(color))
            geom.addVertex( prevV8 )
            geom.addColor(Color(color))
        geom.addVertex( v4 )
        geom.addColor(Color(color)) 

        if firstRun:
            geom.addVertex( v6 )
            geom.addColor(Color(color))
            firstRun = False
        else:
            geom.addVertex( prevV8 )
            geom.addColor(Color(color))
        geom.addVertex( v4 )
        geom.addColor(Color(color))    
        geom.addVertex( v8 )
        geom.addColor(Color(color))
        
    ##################################################################################
        
        numVertices = numVertices + 24

        prevV3 = v3                 #Store beginning points of next line
        prevV4 = v4
        prevV7 = v7
        prevV8 = v8

        prevLine = line2
        
    f.close()
    geom.addPrimitive(PrimitiveType.Triangles, 0, numVertices)

    scene.addModel(geom)
    obj = StaticObject.create(geomName)
    obj.setPosition(0, 0, 0)
    obj.setEffect('colored -e blue -C -t -a')

    obj.getMaterial().setProgram('colored byvertex-emissive')
    obj.getMaterial().setTransparent(True)
    obj.getMaterial().setAlpha(0.75)
    print 'finished Parsing'

    return obj 

#----------------------------------------------------------------------------
#UI Module code

# uim = UiModule.createAndInitialize()

# mainLayout = Container.create( ContainerLayout.LayoutFree, uim.getUi())
# mainLayout.setStyle( 'fill: #00000080' ) #'fill: #655E8280' ) #c0beff80 ' ) # #80808080' )##00000080' )
# mainLayout.setSize( Vector2( float(2000), float(2000) ) ) #Vector2( xPixelsPerScreen, yPixelsPerScreen) )#xPixelsPerScreen*2.0, yPixelsPerScreen/2.0 ))
# mainLayout.setAutosize(False)
# mainLayout.setPosition( Vector2(19224, 100) )

#----------------------------------------------------------------------------
#Planeview code
imgResRatioX = 0.18/(float(10260)/32064)
imgResRatioY = 0.18/(float(9850)/30780)
plane = PlaneShape.create(imgResRatioX*10260, imgResRatioY*9850)
plane.setPosition(Vector3(imgResRatioX*10260/2, imgResRatioY*9850/2, 0))
plane.setEffect("textured -v emissive -d 50Island.png")

#-----------------------------------------------------------------------------
#PointCloud code
scene = getSceneManager()
getDefaultCamera().setBackgroundColor(Color('black'))
scene.addLoader(BinaryPointsLoader())

setNearFarZ(0.1, 1000000)

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
globalAlpha = Uniform.create('globalAlpha', UniformType.Float, 2)
globalAlpha.setFloat(1)

pointCloudModel = ModelInfo()
pointCloudModel.name = 'pointCloud'
pointCloudModel.path = 'hmColorHighFinal.xyzb'
#pointCloudModel.options = "10000 100:1000000:5 20:100:4 6:20:2 0:5:1"
pointCloudModel.options = "10000 100:1000000:20 20:100:10 6:20:5 0:5:5"
#pointCloudModel.options = "10000 0:1000000:1"
scene.loadModel(pointCloudModel)

pointCloud = StaticObject.create(pointCloudModel.name)
# attach shader uniforms
mat = pointCloud.getMaterial()
mat.setProgram(pointProgram.name)
mat.attachUniform(pointScale)
mat.attachUniform(globalAlpha)
getDefaultCamera().setPosition(imgResRatioX*10260/2, imgResRatioY*9850/2, 2500)

#---------------------------------------------------------------------------
# Movement point cloud code GPU Version

#filters
# startDay = Uniform.create('startDay', UniformType.Int, 1)
# endDay = Uniform.create('endDay', UniformType.Int, 1)

# myStartDay = 0
# myEndDay = 1
# dayIncrement = 1
# numberOfDays = 84
currentPitch = 0
currentYaw = 0
currentRoll = 0

# startDay.setInt(myStartDay)
# endDay.setInt(myEndDay)

# colorBy = Uniform.create('colorBy', UniformType.Int, 1) #if 1, shaders turn on.  If 0, shaders turn off
# colorBy.setInt(0)

# selectedIndividual1 = Uniform.create('selectedIndividual1', UniformType.Int, 1) #if 1, shaders turn on.  If 0, shaders turn off
# selectedIndividual1.setInt(4693)

# selectedIndividual2 = Uniform.create('selectedIndividual2', UniformType.Int, 1) #if 1, shaders turn on.  If 0, shaders turn off
# selectedIndividual2.setInt(4693)

# movePointScale = Uniform.create('movePointScale', UniformType.Float, 1)
# movePointScale.setFloat(8.0)

# #Point cloud created here- makes sure it is different name from James point cloud
# movePointProgram = ProgramAsset()
# movePointProgram.name = "movePoints"
# movePointProgram.vertexShaderName = "movementShaders/Sphere.vert" #here are our shaders
# movePointProgram.fragmentShaderName = "movementShaders/Sphere.frag"
# movePointProgram.geometryShaderName = "movementShaders/mySphere.geom"
# movePointProgram.geometryOutVertices = 4
# movePointProgram.geometryInput = PrimitiveType.Points
# movePointProgram.geometryOutput = PrimitiveType.TriangleStrip
# scene.addProgram(movePointProgram)

# movePointCloudModel = ModelInfo()
# movePointCloudModel.name = 'movePointCloud'
# movePointCloudModel.path = 'allChibi.xyzb'#'XY_Chibi_Christmas_Parsed.xyzb'#'Chibi_Christmas_Parsed.xyzb' #'newpng.xyzb'
# #movePointCloudModel.options = "10000 100:1000000:5 20:100:4 6:20:2 0:5:1"
# movePointCloudModel.options = "10000 100:1000000:20 20:100:10 6:20:5 0:5:5"
# #movePointCloudModel.options = "10000 0:1000000:1"
# scene.loadModel(movePointCloudModel)

# movePointCloud = StaticObject.create(movePointCloudModel.name)
# # attach shader uniforms
# moveMat = movePointCloud.getMaterial()
# moveMat.setProgram(movePointProgram.name)

# moveMat.attachUniform(movePointScale)
# moveMat.attachUniform(startDay)
# moveMat.attachUniform(endDay)
# moveMat.attachUniform(selectedIndividual1)
# moveMat.attachUniform(selectedIndividual2)
# moveMat.attachUniform(colorBy)


#CPU Version
# movement = open("parsedAllChibi.txt", "r")
# thickness3 = 8
# c3 = LineSet.create()
# moveList = []
# moveIndex = 0

# for line in movement:
#     tokens = line.split(" ")
#     moveList.append([])
#     moveList[moveIndex].append(tokens[0])
#     moveList[moveIndex].append(tokens[1])
#     moveList[moveIndex].append(tokens[2])
#     moveIndex += 1

# for i in range(0,moveIndex):
#     if (i+1 < moveIndex):
#         l3 = c3.addLine()
#         l3.setStart(Vector3(float(moveList[i][0]), float(moveList[i][1]), float(moveList[i][2])))
#         l3.setEnd(Vector3(float(moveList[i+1][0]), float(moveList[i+1][1]), float(moveList[i+1][2])))
#         l3.setThickness(thickness3)
#         c3.setEffect('colored -e blue')
# movement.close()

#Cylinder and Sphere Version

f = open("gpsMovement/Chibi.txt", "r")

chibi = createCustomGeom(f, scene, 'blue', 'chibi')

f = open("gpsMovement/Abby.txt", "r")

abby = createCustomGeom(f, scene, 'purple', 'abby')

f = open("gpsMovement/Veruca.txt", "r")

veruca = createCustomGeom(f, scene, 'red', 'veruca')

#-----------------------------------------------------------------------------
#Terrain code

# def loadModelAsync(name, path):
#     model = ModelInfo()
#     model.name = name
#     model.path = path
#     model.optimize = True
#     model.usePowerOfTwoTextures = False
#     scene.loadModelAsync(model, "onModelLoaded('" + model.name + "')")

# def onModelLoaded(name):
#     model = StaticObject.create(name)
#     model.setEffect('textured')

# modelPath = "/home/evl/jhwang47/v1"
# def loadModel(name, path):
#     model = ModelInfo()
#     model.name = name
#     model.path = path
#     model.optimize = True
#     model.usePowerOfTwoTextures = False
#     scene.loadModel(model)
#     model = StaticObject.create(name)
#     #model.setEffect("colored -d #4d4d4d")
#     model.setEffect("textured -d 20Island.png")
#     #model.setEffect("20Island")

# loadModel("Terrain", modelPath+"/terrainMap.fbx")

#---------------------------------------------------------------------------
#Set up Lights

light = Light.create()
light.setColor(Color("#AAADAD"))
light.setPosition(Vector3(imgResRatioX*10260, imgResRatioY*9850, 1000))
light.setEnabled(True)

headlight = Light.create()
headlight.setColor(Color("#AAADAD"))
headlight.setEnabled(True)

light3 = Light.create()
light3.setColor(Color("#A3BCC4"))
light3.setAmbient(Color("#A3BDC4"))
light3.setEnabled(True)

lightSphere1 = SphereShape.create(100, 4)
lightSphere1.setEffect("colored -d yellow -e #ffffff")
lightSphere1.setPosition(Vector3(0, imgResRatioY*9850/2, 1000))
lightSphere1.addChild(light3)
lightSphere1.castShadow(False)

light4 = Light.create()
light4.setColor(Color("#AAADAD"))
light4.setPosition(Vector3(0, imgResRatioY*9850/4, 1000))
light4.setEnabled(True)

light5 = Light.create()
light5.setColor(Color("#AAADAD"))
light5.setPosition(Vector3(imgResRatioX*10260, imgResRatioY*9850/4, 250))
light5.setEnabled(True)

light2 = Light.create()
light2.setAmbient(Color("#393A3B"))
light2.setPosition(Vector3(0, 0, 250))
light2.setEnabled(True)

getDefaultCamera().addChild(headlight)


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
#CPU Submenu Items
ss2 = mm.getMainMenu().addSubMenu("Selected Individual")
subMenuChibi = ss2.addSubMenu("Chibi 4693")
#subMenuChibi.setStyleValue('fill', '#954FEA')
subMenuChibi.addLabel("# of Days to Show")
daySliderChibi = subMenuChibi.addSlider(4, "setDaySize(%value%)")
daySliderC = daySliderChibi.getSlider()
daySliderC.setValue(1)

subMenuChibi.addButton("Show Next Day(s)", "showNextDay(4693)")
subMenuChibi.addButton("Show Previous Day(s)", "showPrevDay(4693)")

subMenuAbby = ss2.addSubMenu("Abby 4652")
subMenuAbby.addLabel("# of Days to Show")
daySliderAbby = subMenuAbby.addSlider(4, "setDaySize(%value%)")
daySliderA = daySliderAbby.getSlider()
daySliderA.setValue(1)

subMenuAbby.addButton("Show Next Day(s)", "showNextDay(4652)")
subMenuAbby.addButton("Show Previous Day(s)", "showPrevDay(4652)")

#------------------------------------------------------------------------------
#GPU Submenu Items

# #SUBMENU STEPTHRO
# ss2 = mm.getMainMenu().addSubMenu("Step Through Options")
# btnOneUp = ss2.addButton("Forward a day", "oneDayStepUp(1)")
# btnOneDown = ss2.addButton("Backward a day", "oneDayStepDown(1)")
# btnSvnUp = ss2.addButton("7 Days Forward", "sevenDayStepUp(1)")
# btnSvnUp = ss2.addButton("7 Days Backward", "sevenDayStepDown(1)")
# ss2.addLabel("--------------------")
# btnAll = ss2.addButton("All Days", "allDay(1)")

# #SUBMENU COLOR
# ss3 = mm.getMainMenu().addSubMenu("Color Options")
# btnGrad1 = ss3.addButton("Hour Gradient 1", "setColorBy(0)")
# btnGrad2 = ss3.addButton("Hour Gradient 2", "setColorBy(1)")
# btnGrad3 = ss3.addButton("Hour Gradient 3", "setColorBy(2)")
# btnGrad4 = ss3.addButton("Day Gradient 1", "setColorBy(3)")
# btnGrad5 = ss3.addButton("Day Gradient 2", "setColorBy(4)")
# btnGrad6 = ss3.addButton("Color by individual", "setColorBy(5)")

# ss4 = mm.getMainMenu().addSubMenu("selected Individual 1")
# #ss4.setStyleValue('fill', '#954FEA')
# btn1 = ss4.addButton("Veruca 4690", "setSelInd1(4690)")
# btn2 = ss4.addButton("Chibi 4693", "setSelInd1(4693)")
# btn3 = ss4.addButton("Abby 4652", "setSelInd1(4652)")
# btn4 = ss4.addButton("Ben Bob 4653", "setSelInd1(4653)")
# btn5 = ss4.addButton("Bonnie 4658", "setSelInd1(4658)")
# btn6 = ss4.addButton("Chloe 4052", "setSelInd1(4052)")
# btn7 = ss4.addButton("Clementina 4672", "setSelInd1(4672)")
# btn8 = ss4.addButton("Ellie 4668", "setSelInd1(4668)")
# btn9 = ss4.addButton("Gillian 4671", "setSelInd1(4671)")
# btn10 = ss4.addButton("Ornette 4669", "setSelInd1(4669)")
# btn11 = ss4.addButton("Pliny 4675", "setSelInd1(4675)")
# btn12 = ss4.addButton("Ripley 4650", "setSelInd1(4650)")
# btn13 = ss4.addButton("Serge 4670", "setSelInd1(4670)")
# btn14 = ss4.addButton("Sofie 4674", "setSelInd1(4674)")
# btn15 = ss4.addButton("Greg 4689", "setSelInd1(4689)")
# btn16 = ss4.addButton("Ibeth 4654", "setSelInd1(4654)")
# btn17 = ss4.addButton("Olga 4657", "setSelInd1(4657)")
# btn18 = ss4.addButton("Mimi 4660", "setSelInd1(4660)")
# btn19 = ss4.addButton("Kyle 4692", "setSelInd1(4692)")
# btn20 = ss4.addButton("Atlas 4673", "setSelInd1(4673)")
# btn21 = ss4.addButton("Vielle 4670", "setSelInd1(4670)")
# btn22 = ss4.addButton("Judy 4656", "setSelInd1(4656)")
# btn23 = ss4.addButton("Merk 4665", "setSelInd1(4665)")

# ss5 = mm.getMainMenu().addSubMenu("selected Individual 2")
# #ss5.setStyleValue('fill', '#5588F4')
# btn1 = ss5.addButton("Veruca 4690", "setSelInd2(4690)")
# btn2 = ss5.addButton("Chibi 4693", "setSelInd2(4693)")
# btn3 = ss5.addButton("Abby 4652", "setSelInd2(4652)")
# btn4 = ss5.addButton("Ben Bob 4653", "setSelInd2(4653)")
# btn5 = ss5.addButton("Bonnie 4658", "setSelInd2(4658)")
# btn6 = ss5.addButton("Chloe 4052", "setSelInd2(4052)")
# btn7 = ss5.addButton("Clementina 4672", "setSelInd2(4672)")
# btn8 = ss5.addButton("Ellie 4668", "setSelInd2(4668)")
# btn9 = ss5.addButton("Gillian 4671", "setSelInd2(4671)")
# btn10 = ss5.addButton("Ornette 4669", "setSelInd2(4669)")
# btn11 = ss5.addButton("Pliny 4675", "setSelInd2(4675)")
# btn12 = ss5.addButton("Ripley 4650", "setSelInd2(4650)")
# btn13 = ss5.addButton("Serge 4670", "setSelInd2(4670)")
# btn14 = ss5.addButton("Sofie 4674", "setSelInd2(4674)")
# btn15 = ss5.addButton("Greg 4689", "setSelInd2(4689)")
# btn16 = ss5.addButton("Ibeth 4654", "setSelInd2(4654)")
# btn17 = ss5.addButton("Olga 4657", "setSelInd2(4657)")
# btn18 = ss5.addButton("Mimi 4660", "setSelInd2(4660)")
# btn19 = ss5.addButton("Kyle 4692", "setSelInd2(4692)")
# btn20 = ss5.addButton("Atlas 4673", "setSelInd2(4673)")
# btn21 = ss5.addButton("Vielle 4670", "setSelInd2(4670)")
# btn22 = ss5.addButton("Judy 4656", "setSelInd2(4656)")
# btn23 = ss5.addButton("Merk 4665", "setSelInd2(4665)")

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
    #hasCameraMoved = False

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
                lineList.append(l2)
                drawnCamPos = getDefaultCamera().getPosition()

        #showOtherTrees.addChild(c2)
setUpdateFunction(onUpdate)
        

#--------------------------------------------------------------------------------------
#Functions

# def oneDayStepUp(value):
#     global myStartDay
#     global myEndDay
#     global numberOfDays

#     myStartDay = myStartDay + 1
#     if myStartDay > numberOfDays:
#         myStartDay = 0
#     myEndDay = myStartDay + 1
#     endDay.setInt(myEndDay)
#     startDay.setInt(myStartDay)

#     # print( "one day step up" + myStartDay)

# def oneDayStepDown(value):
#     global myStartDay
#     global myEndDay
#     global numberOfDays

#     myStartDay = myStartDay - 1
#     if myStartDay < 0:
#         myStartDay = numberOfDays-1
#     myEndDay = myStartDay + 1
#     endDay.setInt(myEndDay)
#     startDay.setInt(myStartDay)

#     # print( "one day step down " + myStartDay)

# def sevenDayStepUp(value):
#     global myStartDay
#     global myEndDay
#     global numberOfDays

#     myStartDay = myStartDay + 7
#     if myStartDay > numberOfDays:
#         myStartDay = 0
#     myEndDay = myStartDay + 7
#     endDay.setInt(myEndDay)
#     startDay.setInt(myStartDay)

#     # print( "seven day step up" + myStartDay)

# def sevenDayStepDown(value):
#     global myStartDay
#     global myEndDay
#     global numberOfDays

#     myStartDay = myStartDay - 7
#     if myStartDay < 0:
#         myStartDay = numberOfDays-7
#     myEndDay = myStartDay + 7
#     endDay.setInt(myEndDay)
#     startDay.setInt(myStartDay)

    # print( "seven day step down " + myStartDay)

# def allDay(value):
#     global numberOfDays
#     endDay.setInt(numberOfDays)
#     startDay.setInt(0)

#     # print( "one day step " + myStartDay)

# def setColorBy(value):
#     colorBy.setInt(value)

#     # print( "set color by " + value)

# def setSelIn1(value):
#     colorBy.setInt(value)

#     # print( "set color by " + value)

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
    #globalAlpha.setFloat(a)
    pointCloud.getMaterial().setAlpha(a)

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
