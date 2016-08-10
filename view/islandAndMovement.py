from omega import *
from cyclops import *
from pointCloud import *
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

        line2 = f.next()
        
        if line2 == '-999':
            break

        tokens2 = line2.split(" ")

        if prevID != int(tokens2[6]):
            firstRun = True

        if firstRun:
            tokens = line.split(" ")
            firstRun = False
        else:
            tokens = prevLine.split(" ")

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

        color = []
        color.append(int(tokens[3]))
        color.append(int(tokens[4]))
        color.append(int(tokens[5]))
        color.append(int(tokens[6]))
        color.append(int(tokens2[3]))
        color.append(int(tokens2[4]))
        color.append(int(tokens2[5]))
        color.append(int(tokens2[6]))

    #####################Front Panel##################################################
        geom.addVertex( v1 )
        geom.addColor(Color(color[0], color[1], color[2], color[3]))
        geom.addVertex( v2 )
        geom.addColor(Color(color[0], color[1], color[2], color[3]))
        geom.addVertex( v3 )
        geom.addColor(Color(color[4], color[5], color[6], color[7]))

        geom.addVertex( v3 )
        geom.addColor(Color(color[4], color[5], color[6], color[7]))
        geom.addVertex( v2 )
        geom.addColor(Color(color[0], color[1], color[2], color[3]))
        geom.addVertex( v4 )
        geom.addColor(Color(color[4], color[5], color[6], color[7]))
    ##################################################################################
    #####################Back Panel##################################################
        geom.addVertex( v7 )
        geom.addColor(Color(color[4], color[5], color[6], color[7]))
        geom.addVertex( v6 )
        geom.addColor(Color(color[0], color[1], color[2], color[3]))
        geom.addVertex( v5 )
        geom.addColor(Color(color[0], color[1], color[2], color[3]))

        geom.addVertex( v8 )
        geom.addColor(Color(color[4], color[5], color[6], color[7]))
        geom.addVertex( v6 )
        geom.addColor(Color(color[0], color[1], color[2], color[3]))
        geom.addVertex( v7 )
        geom.addColor(Color(color[4], color[5], color[6], color[7]))
    ##################################################################################
    #####################Top Panel##################################################
        geom.addVertex( v1 )
        geom.addColor(Color(color[0], color[1], color[2], color[3]))
        geom.addVertex( v7 )
        geom.addColor(Color(color[4], color[5], color[6], color[7]))
        geom.addVertex( v5 )
        geom.addColor(Color(color[0], color[1], color[2], color[3]))
        
        geom.addVertex( v7 )
        geom.addColor(Color(color[4], color[5], color[6], color[7]))
        geom.addVertex( v1 )
        geom.addColor(Color(color[0], color[1], color[2], color[3]))
        geom.addVertex( v3 )
        geom.addColor(Color(color[4], color[5], color[6], color[7]))
    ##################################################################################
    #####################Bottom Panel##################################################
        
        geom.addVertex( v8 )
        geom.addColor(Color(color[4], color[5], color[6], color[7]))
        geom.addVertex( v4 )
        geom.addColor(Color(color[4], color[5], color[6], color[7]))
        geom.addVertex( v2 )
        geom.addColor(Color(color[0], color[1], color[2], color[3])) 

        geom.addVertex( v6 )
        geom.addColor(Color(color[0], color[1], color[2], color[3]))
        geom.addVertex( v8 )
        geom.addColor(Color(color[4], color[5], color[6], color[7]))    
        geom.addVertex( v2 )
        geom.addColor(Color(color[0], color[1], color[2], color[3]))
        
    ##################################################################################
        
        numVertices = numVertices + 24

        prevV3 = v3                 #Store beginning points of next line
        prevV4 = v4
        prevV7 = v7
        prevV8 = v8

        prevVec = vec
        prevID = int(tokens2[6])
        prevLine = line2
        
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
globalAlpha = Uniform.create('globalAlpha', UniformType.Float, 1)
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
mat.setTransparent(True)
mat.setProgram(pointProgram.name)
mat.attachUniform(pointScale)
mat.attachUniform(globalAlpha)
getDefaultCamera().setPosition(imgResRatioX*10260/2, imgResRatioY*9850/2, 2500)

#---------------------------------------------------------------------------
#Cylinder and Sphere Version

myStartDay = 0
myEndDay = 1
dayIncrement = 1
numberOfDays = 84
currentPitch = 0
currentYaw = 0
currentRoll = 0

moveLineProgram = ProgramAsset()
moveLineProgram.name = "moveLine"
moveLineProgram.vertexShaderName = "lineShaders/Line.vert"
moveLineProgram.fragmentShaderName = "lineShaders/Line.frag"
scene.addProgram(moveLineProgram)

startDay = Uniform.create('startDay', UniformType.Int, 1)
startDay.setInt(myStartDay)
endDay = Uniform.create('endDay', UniformType.Int, 1)
endDay.setInt(myEndDay)
# colorBy = Uniform.create('colorBy', UniformType.Int, 1)
# colorBy.setInt(0)
bitMapSelectedIndividuals = Uniform.create('bitMapSelectedIndividuals', UniformType.Int, 21)
colorByBitMap = Uniform.create('colorByBitMap', UniformType.Int, 21)

for i in range(0,21):
    if i == 1:
        bitMapSelectedIndividuals.setIntElement(1, i)
    else:
        bitMapSelectedIndividuals.setIntElement(0, i)

for i in range(0, 21):
    bitMapSelectedIndividuals.setIntElement(0, i)

f = open("gpsMovement/all.txt", "r")

allAnimals = createCustomGeom(f, scene, 'allAnimals')             #Ateles geoffroyi

allMat = allAnimals.getMaterial()
allMat.setProgram(moveLineProgram.name)
allMat.attachUniform(startDay)
allMat.attachUniform(endDay)
allMat.attachUniform(colorByBitMap)
allMat.attachUniform(bitMapSelectedIndividuals)

#--------------------------------------------------------------------------------------------
# Movement point cloud code GPU Version

#filters
# startDay = Uniform.create('startDay', UniformType.Int, 1)
# endDay = Uniform.create('endDay', UniformType.Int, 1)

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
movePointCloudModel.path = 'all.xyzb'
movePointCloudModel.options = "10000 100:1000000:20 20:100:10 6:20:5 0:5:5"
scene.loadModel(movePointCloudModel)

movePointCloud = StaticObject.create(movePointCloudModel.name)
# attach shader uniforms
moveMat = movePointCloud.getMaterial()
moveMat.setProgram(movePointProgram.name)
moveMat.attachUniform(startDay)
moveMat.attachUniform(endDay)
# moveMat.attachUniform(colorBy)
moveMat.attachUniform(bitMapSelectedIndividuals)
moveMat.attachUniform(colorByBitMap)
moveMat.attachUniform(movePointScale)

#----------------------------------------------------------------------------

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
#GPU Submenu Items

# #SUBMENU STEPTHRO
ss2 = mm.getMainMenu().addSubMenu("Step Through Options")
btnOneUp = ss2.addButton("Forward a day", "oneDayStepUp(1)")
btnOneDown = ss2.addButton("Backward a day", "oneDayStepDown(1)")
btnSvnUp = ss2.addButton("7 Days Forward", "sevenDayStepUp(1)")
btnSvnUp = ss2.addButton("7 Days Backward", "sevenDayStepDown(1)")
ss2.addLabel("--------------------")
btnAll = ss2.addButton("All Days", "allDay(1)")

# #SUBMENU COLOR
# ss3 = mm.getMainMenu().addSubMenu("Color Options")
# btnGrad1 = ss3.addButton("Hour Gradient 1", "setColorBy(0)")
# btnGrad2 = ss3.addButton("Hour Gradient 2", "setColorBy(1)")
# btnGrad3 = ss3.addButton("Hour Gradient 3", "setColorBy(2)")
# btnGrad4 = ss3.addButton("Day Gradient 1", "setColorBy(3)")
# btnGrad5 = ss3.addButton("Day Gradient 2", "setColorBy(4)")
# btnGrad6 = ss3.addButton("Color by individual", "setColorBy(5)")

subSelectInd = mm.getMainMenu().addSubMenu("Selected Individuals")
verucaMenu = subSelectInd.addSubMenu("Veruca 4690")
verBtn1 = verucaMenu.addButton("Show Data", "setSelInd(0)")
verCO = verucaMenu.addSubMenu("Color Options")
verBtnGrad1 = verCO.addButton("Hour Gradient 1", "setColorBy(0, 0)")
verBtnGrad2 = verCO.addButton("Hour Gradient 2", "setColorBy(0, 1)")
verBtnGrad3 = verCO.addButton("Hour Gradient 3", "setColorBy(0, 2)")
verBtnGrad4 = verCO.addButton("Day Gradient 1", "setColorBy(0, 3)")
verBtnGrad5 = verCO.addButton("Day Gradient 2", "setColorBy(0, 4)")
verBtnGrad6 = verCO.addButton("Color by individual", "setColorBy(0, 5)")

chibiMenu = subSelectInd.addSubMenu("Chibi 4693")
chibiBtn1 = chibiMenu.addButton("Show Data", "setSelInd(1)")
chibiCO = chibiMenu.addSubMenu("Color Options")
chibiBtnGrad1 = chibiCO.addButton("Hour Gradient 1", "setColorBy(1, 0)")
chibiBtnGrad2 = chibiCO.addButton("Hour Gradient 2", "setColorBy(1, 1)")
chibiBtnGrad3 = chibiCO.addButton("Hour Gradient 3", "setColorBy(1, 2)")
chibiBtnGrad4 = chibiCO.addButton("Day Gradient 1", "setColorBy(1, 3)")
chibiBtnGrad5 = chibiCO.addButton("Day Gradient 2", "setColorBy(1, 4)")
chibiBtnGrad6 = chibiCO.addButton("Color by individual", "setColorBy(1, 5)")

abbyMenu = subSelectInd.addSubMenu("Abby 4652")
abbyBtn1 = subSelectInd.addButton("Show Data", "setSelInd(2)")
abbyCO = abbyMenu.addSubMenu("Color Options")
abbyBtnGrad1 = abbyCO.addButton("Hour Gradient 1", "setColorBy(2, 0)")
abbyBtnGrad2 = abbyCO.addButton("Hour Gradient 2", "setColorBy(2, 1)")
abbyBtnGrad3 = abbyCO.addButton("Hour Gradient 3", "setColorBy(2, 2)")
abbyBtnGrad4 = abbyCO.addButton("Day Gradient 1", "setColorBy(2, 3)")
abbyBtnGrad5 = abbyCO.addButton("Day Gradient 2", "setColorBy(2, 4)")
abbyBtnGrad6 = abbyCO.addButton("Color by individual", "setColorBy(2, 5)")

benbobMenu = subSelectInd.addSubMenu("Ben Bob 4653")
benbobBtn1 = subSelectInd.addButton("Show Data", "setSelInd(3)")
benBobCO = benBobMenu.addSubMenu("Color Options")
benBtnGrad1 = benBobCO.addButton("Hour Gradient 1", "setColorBy(3, 0)")
benBtnGrad2 = benBobCO.addButton("Hour Gradient 2", "setColorBy(3, 1)")
benBtnGrad3 = benBobCO.addButton("Hour Gradient 3", "setColorBy(3, 2)")
benBtnGrad4 = benBobCO.addButton("Day Gradient 1", "setColorBy(3, 3)")
benBtnGrad5 = benBobCO.addButton("Day Gradient 2", "setColorBy(3, 4)")
benBtnGrad6 = benBobCO.addButton("Color by individual", "setColorBy(3, 5)")

bonnieMenu = subSelectInd.addSubMenu("Bonnie 4658")
bonnieBtn1 = subSelectInd.addButton("Show Data", "setSelInd(4)")
bonCO = bonnieMenu.addSubMenu("Color Options")
bonBtnGrad1 = bonCO.addButton("Hour Gradient 1", "setColorBy(4, 0)")
bonBtnGrad2 = bonCO.addButton("Hour Gradient 2", "setColorBy(4, 1)")
bonBtnGrad3 = bonCO.addButton("Hour Gradient 3", "setColorBy(4, 2)")
bonBtnGrad4 = bonCO.addButton("Day Gradient 1", "setColorBy(4, 3)")
bonBtnGrad5 = bonCO.addButton("Day Gradient 2", "setColorBy(4, 4)")
bonBtnGrad6 = bonCO.addButton("Color by individual", "setColorBy(4, 5)")

chloeMenu = subSelectInd.addSubMenu("Chloe 4052")
chloeBtn1 = subSelectInd.addButton("Chloe 4052", "setSelInd(5)")
chloeCO = chloeMenu.addSubMenu("Color Options")
chloeBtnGrad1 = chloeCO.addButton("Hour Gradient 1", "setColorBy(5, 0)")
chloeBtnGrad2 = chloeCO.addButton("Hour Gradient 2", "setColorBy(5, 1)")
chloeBtnGrad3 = chloeCO.addButton("Hour Gradient 3", "setColorBy(5, 2)")
chloeBtnGrad4 = chloeCO.addButton("Day Gradient 1", "setColorBy(5, 3)")
chloeBtnGrad5 = chloeCO.addButton("Day Gradient 2", "setColorBy(5, 4)")
chloeBtnGrad6 = chloeCO.addButton("Color by individual", "setColorBy(5, 5)")

clementinaMenu = subSelectInd.addSubMenu("Clementina 4672")
clemBtn1 = subSelectInd.addButton("Clementina 4672", "setSelInd(6)")
clemCO = clementinaMenu.addSubMenu("Color Options")
clemBtnGrad1 = clemCO.addButton("Hour Gradient 1", "setColorBy(6, 0)")
clemBtnGrad2 = clemCO.addButton("Hour Gradient 2", "setColorBy(6, 1)")
clemBtnGrad3 = clemCO.addButton("Hour Gradient 3", "setColorBy(6, 2)")
clemBtnGrad4 = clemCO.addButton("Day Gradient 1", "setColorBy(6, 3)")
clemBtnGrad5 = clemCO.addButton("Day Gradient 2", "setColorBy(6, 4)")
clemBtnGrad6 = clemCO.addButton("Color by individual", "setColorBy(6, 5)")


ellieMenu = subSelectInd.addSubMenu("Ellie 4668")
ellieBtn1 = subSelectInd.addButton("Ellie 4668", "setSelInd(7)")
elCO = ellieMenu.addSubMenu("Color Options")
elBtnGrad1 = elCO.addButton("Hour Gradient 1", "setColorBy(7, 0)")
elBtnGrad2 = elCO.addButton("Hour Gradient 2", "setColorBy(7, 1)")
elBtnGrad3 = elCO.addButton("Hour Gradient 3", "setColorBy(7, 2)")
elBtnGrad4 = elCO.addButton("Day Gradient 1", "setColorBy(7, 3)")
elBtnGrad5 = elCO.addButton("Day Gradient 2", "setColorBy(7, 4)")
elBtnGrad6 = elCO.addButton("Color by individual", "setColorBy(7, 5)")

gillianMenu = subSelectInd.addSubMenu("Gillian 4671")
gillBtn1 = subSelectInd.addButton("Gillian 4671", "setSelInd(8)")
gilCO = gillianMenu.addSubMenu("Color Options")
gilBtnGrad1 = gilCO.addButton("Hour Gradient 1", "setColorBy(8, 0)")
gilBtnGrad2 = gilCO.addButton("Hour Gradient 2", "setColorBy(8, 1)")
gilBtnGrad3 = gilCO.addButton("Hour Gradient 3", "setColorBy(8, 2)")
gilBtnGrad4 = gilCO.addButton("Day Gradient 1", "setColorBy(8, 3)")
gilBtnGrad5 = gilCO.addButton("Day Gradient 2", "setColorBy(8, 4)")
gilBtnGrad6 = gilCO.addButton("Color by individual", "setColorBy(8, 5)")

ornetteMenu = subSelectInd.addSubMenu("Ornette 4669")
ornetteBtn1 = subSelectInd.addButton("Ornette 4669", "setSelInd(9)")
ornCO = ornetteMenu.addSubMenu("Color Options")
ornBtnGrad1 = ornCO.addButton("Hour Gradient 1", "setColorBy(9, 0)")
ornBtnGrad2 = ornCO.addButton("Hour Gradient 2", "setColorBy(9, 1)")
ornBtnGrad3 = ornCO.addButton("Hour Gradient 3", "setColorBy(9, 2)")
ornBtnGrad4 = ornCO.addButton("Day Gradient 1", "setColorBy(9, 3)")
ornBtnGrad5 = ornCO.addButton("Day Gradient 2", "setColorBy(9, 4)")
ornBtnGrad6 = ornCO.addButton("Color by individual", "setColorBy(9, 5)")

plinyMenu = subSelectInd.addSubMenu("Pliny 4675")
plinyBtn1 = subSelectInd.addButton("Pliny 4675", "setSelInd(10)")
pliCO = plinyMenu.addSubMenu("Color Options")
pliBtnGrad1 = pliCO.addButton("Hour Gradient 1", "setColorBy(10, 0)")
pliBtnGrad2 = pliCO.addButton("Hour Gradient 2", "setColorBy(10, 1)")
pliBtnGrad3 = pliCO.addButton("Hour Gradient 3", "setColorBy(10, 2)")
pliBtnGrad4 = pliCO.addButton("Day Gradient 1", "setColorBy(10, 3)")
pliBtnGrad5 = pliCO.addButton("Day Gradient 2", "setColorBy(10, 4)")
pliBtnGrad6 = pliCO.addButton("Color by individual", "setColorBy(10, 5)")

ripleyMenu = subSelectInd.addSubMenu("Ripley 4650")
ripleyBtn1 = subSelectInd.addButton("Ripley 4650", "setSelInd(11)")
ripCO = ripleyMenu.addSubMenu("Color Options")
ripBtnGrad1 = ripCO.addButton("Hour Gradient 1", "setColorBy(11, 0)")
ripBtnGrad2 = ripCO.addButton("Hour Gradient 2", "setColorBy(11, 1)")
ripBtnGrad3 = ripCO.addButton("Hour Gradient 3", "setColorBy(11, 2)")
ripBtnGrad4 = ripCO.addButton("Day Gradient 1", "setColorBy(11, 3)")
ripBtnGrad5 = ripCO.addButton("Day Gradient 2", "setColorBy(11, 4)")
ripBtnGrad6 = ripCO.addButton("Color by individual", "setColorBy(11, 5)")

sofieMenu = subSelectInd.addSubMenu("Sofie 4674")
sofieBtn1 = subSelectInd.addButton("Sofie 4674", "setSelInd(12)")
sofCO = sofieMenu.addSubMenu("Color Options")
sofBtnGrad1 = sofCO.addButton("Hour Gradient 1", "setColorBy(12, 0)")
sofBtnGrad2 = sofCO.addButton("Hour Gradient 2", "setColorBy(12, 1)")
sofBtnGrad3 = sofCO.addButton("Hour Gradient 3", "setColorBy(12, 2)")
sofBtnGrad4 = sofCO.addButton("Day Gradient 1", "setColorBy(12, 3)")
sofBtnGrad5 = sofCO.addButton("Day Gradient 2", "setColorBy(12, 4)")
sofBtnGrad6 = sofCO.addButton("Color by individual", "setColorBy(12, 5)")

gregMenu = subSelectInd.addSubMenu("Greg 4689")
gregBtn1 = subSelectInd.addButton("Greg 4689", "setSelInd(13)")
gregCO = gregMenu.addSubMenu("Color Options")
gregBtnGrad1 = gregCO.addButton("Hour Gradient 1", "setColorBy(13, 0)")
gregBtnGrad2 = gregCO.addButton("Hour Gradient 2", "setColorBy(13, 1)")
gregBtnGrad3 = gregCO.addButton("Hour Gradient 3", "setColorBy(13, 2)")
gregBtnGrad4 = gregCO.addButton("Day Gradient 1", "setColorBy(13, 3)")
gregBtnGrad5 = gregCO.addButton("Day Gradient 2", "setColorBy(13, 4)")
gregBtnGrad6 = gregCO.addButton("Color by individual", "setColorBy(13, 5)")

ibethMenu = subSelectInd.addSubMenu("Ibeth 4654")
ibethBtn1 = subSelectInd.addButton("Ibeth 4654", "setSelInd(14)")
ibeCO = ibethMenu.addSubMenu("Color Options")
ibeBtnGrad1 = ibeCO.addButton("Hour Gradient 1", "setColorBy(14, 0)")
ibeBtnGrad2 = ibeCO.addButton("Hour Gradient 2", "setColorBy(14, 1)")
ibeBtnGrad3 = ibeCO.addButton("Hour Gradient 3", "setColorBy(14, 2)")
ibeBtnGrad4 = ibeCO.addButton("Day Gradient 1", "setColorBy(14, 3)")
ibeBtnGrad5 = ibeCO.addButton("Day Gradient 2", "setColorBy(14, 4)")
ibeBtnGrad6 = ibeCO.addButton("Color by individual", "setColorBy(14, 5)")

olgaMenu = subSelectInd.addSubMenu("Olga 4657")
olgaBtn1 = subSelectInd.addButton("Olga 4657", "setSelInd(15)")
olgaCO = olgaMenu.addSubMenu("Color Options")
olgaBtnGrad1 = olgaCO.addButton("Hour Gradient 1", "setColorBy(15, 0)")
olgaBtnGrad2 = olgaCO.addButton("Hour Gradient 2", "setColorBy(15, 1)")
olgaBtnGrad3 = olgaCO.addButton("Hour Gradient 3", "setColorBy(15, 2)")
olgaBtnGrad4 = olgaCO.addButton("Day Gradient 1", "setColorBy(15, 3)")
olgaBtnGrad5 = olgaCO.addButton("Day Gradient 2", "setColorBy(15, 4)")
olgaBtnGrad6 = olgaCO.addButton("Color by individual", "setColorBy(15, 5)")

mimiMenu = subSelectInd.addSubMenu("Mimi 4660")
mimiBtn1 = subSelectInd.addButton("Mimi 4660", "setSelInd(16)")
mimiCO = mimiMenu.addSubMenu("Color Options")
mimiBtnGrad1 = mimiCO.addButton("Hour Gradient 1", "setColorBy(16, 0)")
mimiBtnGrad2 = mimiCO.addButton("Hour Gradient 2", "setColorBy(16, 1)")
mimiBtnGrad3 = mimiCO.addButton("Hour Gradient 3", "setColorBy(16, 2)")
mimiBtnGrad4 = mimiCO.addButton("Day Gradient 1", "setColorBy(16, 3)")
mimiBtnGrad5 = mimiCO.addButton("Day Gradient 2", "setColorBy(16, 4)")
mimiBtnGrad6 = mimiCO.addButton("Color by individual", "setColorBy(16, 5)")

kyleMenu = subSelectInd.addSubMenu("Kyle 4692")
kyleBtn1 = subSelectInd.addButton("Kyle 4692", "setSelInd(17)")
kyleCO = kyleMenu.addSubMenu("Color Options")
kyleBtnGrad1 = kyleCO.addButton("Hour Gradient 1", "setColorBy(17, 0)")
kyleBtnGrad2 = kyleCO.addButton("Hour Gradient 2", "setColorBy(17, 1)")
kyleBtnGrad3 = kyleCO.addButton("Hour Gradient 3", "setColorBy(17, 2)")
kyleBtnGrad4 = kyleCO.addButton("Day Gradient 1", "setColorBy(17, 3)")
kyleBtnGrad5 = kyleCO.addButton("Day Gradient 2", "setColorBy(17, 4)")
kyleBtnGrad6 = kyleCO.addButton("Color by individual", "setColorBy(17, 5)")

atlasMenu = subSelectInd.addSubMenu("Atlas 4673")
atlasBtn1 = subSelectInd.addButton("Atlas 4673", "setSelInd(18)")
atlasCO = atlasMenu.addSubMenu("Color Options")
atlasBtnGrad1 = atlasCO.addButton("Hour Gradient 1", "setColorBy(18, 0)")
atlasBtnGrad2 = atlasCO.addButton("Hour Gradient 2", "setColorBy(18, 1)")
atlasBtnGrad3 = atlasCO.addButton("Hour Gradient 3", "setColorBy(18, 2)")
atlasBtnGrad4 = atlasCO.addButton("Day Gradient 1", "setColorBy(18, 3)")
atlasBtnGrad5 = atlasCO.addButton("Day Gradient 2", "setColorBy(18, 4)")
atlasBtnGrad6 = atlasCO.addButton("Color by individual", "setColorBy(18, 5)")

judyMenu = subSelectInd.addSubMenu("Judy 4656")
judyBtn1 = subSelectInd.addButton("Judy 4656", "setSelInd(19)")
judyCO = judyMenu.addSubMenu("Color Options")
judyBtnGrad1 = judyCO.addButton("Hour Gradient 1", "setColorBy(19, 0)")
judyBtnGrad2 = judyCO.addButton("Hour Gradient 2", "setColorBy(19, 1)")
judyBtnGrad3 = judyCO.addButton("Hour Gradient 3", "setColorBy(19, 2)")
judyBtnGrad4 = judyCO.addButton("Day Gradient 1", "setColorBy(19, 3)")
judyBtnGrad5 = judyCO.addButton("Day Gradient 2", "setColorBy(19, 4)")
judyBtnGrad6 = judyCO.addButton("Color by individual", "setColorBy(19, 5)")

merkMenu = subSelectInd.addSubMenu("Merk 4665")
merkBtn1 = subSelectInd.addButton("Merk 4665", "setSelInd(20)")
merkCO = merkMenu.addSubMenu("Color Options")
merkBtnGrad1 = merkCO.addButton("Hour Gradient 1", "setColorBy(20, 0)")
merkBtnGrad2 = merkCO.addButton("Hour Gradient 2", "setColorBy(20, 1)")
merkBtnGrad3 = merkCO.addButton("Hour Gradient 3", "setColorBy(20, 2)")
merkBtnGrad4 = merkCO.addButton("Day Gradient 1", "setColorBy(20, 3)")
merkBtnGrad5 = merkCO.addButton("Day Gradient 2", "setColorBy(20, 4)")
merkBtnGrad6 = merkCO.addButton("Color by individual", "setColorBy(20, 5)")

# btn1 = subSelectInd.addButton("Veruca 4690", "setSelInd(0)")
# btn2 = subSelectInd.addButton("Chibi 4693", "setSelInd(1)")
# btn3 = subSelectInd.addButton("Abby 4652", "setSelInd(2)")
# btn4 = subSelectInd.addButton("Ben Bob 4653", "setSelInd(3)")
# btn5 = subSelectInd.addButton("Bonnie 4658", "setSelInd(4)")
# btn6 = subSelectInd.addButton("Chloe 4052", "setSelInd(5)")
# btn7 = subSelectInd.addButton("Clementina 4672", "setSelInd(6)")
# btn8 = subSelectInd.addButton("Ellie 4668", "setSelInd(7)")
# btn9 = subSelectInd.addButton("Gillian 4671", "setSelInd(8)")
# btn10 = subSelectInd.addButton("Ornette 4669", "setSelInd(9)")
# btn11 = subSelectInd.addButton("Pliny 4675", "setSelInd(10)")
# btn12 = subSelectInd.addButton("Ripley 4650", "setSelInd(11)")
# #btn13 = subSelectInd.addButton("Serge 4670", "setSelInd(12)")
# btn13 = subSelectInd.addButton("Sofie 4674", "setSelInd(12)")
# btn14 = subSelectInd.addButton("Greg 4689", "setSelInd(13)")
# btn15 = subSelectInd.addButton("Ibeth 4654", "setSelInd(14)")
# btn16 = subSelectInd.addButton("Olga 4657", "setSelInd(15)")
# btn17 = subSelectInd.addButton("Mimi 4660", "setSelInd(16)")
# btn18 = subSelectInd.addButton("Kyle 4692", "setSelInd(17)")
# btn19 = subSelectInd.addButton("Atlas 4673", "setSelInd(18)")
# #btn21 = subSelectInd.addButton("Vielle 4670", "setSelInd(20)")
# btn20 = subSelectInd.addButton("Judy 4656", "setSelInd(19)")
# btn21 = subSelectInd.addButton("Merk 4665", "setSelInd(20)")

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
def oneDayStepUp(value):
    global myStartDay
    global myEndDay
    global numberOfDays

    myStartDay = myStartDay + 1
    if myStartDay > numberOfDays:
        myStartDay = 0
    myEndDay = myStartDay + 1
    endDay.setInt(myEndDay)
    startDay.setInt(myStartDay)

    # print( "one day step up" + myStartDay)

def oneDayStepDown(value):
    global myStartDay
    global myEndDay
    global numberOfDays

    myStartDay = myStartDay - 1
    if myStartDay < 0:
        myStartDay = numberOfDays-1
    myEndDay = myStartDay + 1
    endDay.setInt(myEndDay)
    startDay.setInt(myStartDay)

    # print( "one day step down " + myStartDay)

def sevenDayStepUp(value):
    global myStartDay
    global myEndDay
    global numberOfDays

    myStartDay = myStartDay + 7
    if myStartDay > numberOfDays:
        myStartDay = 0
    myEndDay = myStartDay + 7
    endDay.setInt(myEndDay)
    startDay.setInt(myStartDay)

    # print( "seven day step up" + myStartDay)

def sevenDayStepDown(value):
    global myStartDay
    global myEndDay
    global numberOfDays

    myStartDay = myStartDay - 7
    if myStartDay < 0:
        myStartDay = numberOfDays-7
    myEndDay = myStartDay + 7
    endDay.setInt(myEndDay)
    startDay.setInt(myStartDay)

    # print( "seven day step down " + myStartDay)

def allDay(value):
    global numberOfDays
    endDay.setInt(numberOfDays)
    startDay.setInt(0)

    # print( "one day step " + myStartDay)

def setColorBy(individual, value):
    global colorByBitMap

    colorByBitMap.setIntElement(value, individual)

    # print( "set color by " + value)

def setSelInd(value):
    global bitMapSelectedIndividuals

    val = bitMapSelectedIndividuals.getIntElement(value)
    bitMapSelectedIndividuals.setIntElement((not val), value)

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
