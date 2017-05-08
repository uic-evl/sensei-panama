from euclid import *
from omega import *
from cyclops import *
from pointCloud import *
from datetime import *

from CustomGeom import *
from MenuOptions import *
from caveutilcustom import *

def setLastSphereColor(individual, value):
    '''
    Keeps track of last point and puts a sphere with the correct
    color
    '''
    global movementData
    global myEndDay
    global lastPointSphere

    if value == 0:
        if movementData[individual][myEndDay[individual]][0][3] < 4:
            lastPointSphere[individual].getMaterial().setColor(Color(255.0/255.0, 255.0/255.0,
                                                                     204.0/255.0, 1.0),
                                                               Color(255.0/255.0, 255.0/255.0,
                                                                     204.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 4 and \
           movementData[individual][myEndDay[individual]][0][3] < 8:
            lastPointSphere[individual].getMaterial().setColor(Color(199.0/255.0, 233.0/255.0,
                                                                     180.0/255.0, 1.0),
                                                               Color(199.0/255.0, 233.0/255.0,
                                                                     180.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 8 and \
           movementData[individual][myEndDay[individual]][0][3] < 12:
            lastPointSphere[individual].getMaterial().setColor(Color(127.0/255.0, 205.0/255.0,
                                                                     187.0/255.0, 1.0),
                                                               Color(127.0/255.0, 205.0/255.0,
                                                                     187.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 12 and \
           movementData[individual][myEndDay[individual]][0][3] < 16:
            lastPointSphere[individual].getMaterial().setColor(Color(65.0/255.0, 182.0/255.0,
                                                                     196.0/255.0, 1.0),
                                                               Color(65.0/255.0, 182.0/255.0,
                                                                     196.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 16 and \
           movementData[individual][myEndDay[individual]][0][3] < 20:
            lastPointSphere[individual].getMaterial().setColor(Color(44.0/255.0, 127.0/255.0,
                                                                     184.0/255.0, 1.0),
                                                               Color(44.0/255.0, 127.0/255.0,
                                                                     184.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 20 and \
           movementData[individual][myEndDay[individual]][0][3] < 24:
            lastPointSphere[individual].getMaterial().setColor(Color(37.0/255.0, 52.0/255.0,
                                                                     148.0/255.0, 1.0),
                                                               Color(37.0/255.0, 52.0/255.0,
                                                                     148.0/255.0, 1.0))
    if value == 1:
        if movementData[individual][myEndDay[individual]][0][3] < 3:
            lastPointSphere[individual].getMaterial().setColor(Color(69.0/255.0, 117.0/255.0,
                                                                     180.0/255.0, 1.0),
                                                               Color(69.0/255.0, 117.0/255.0,
                                                                     180.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 3 and \
           movementData[individual][myEndDay[individual]][0][3] < 6:
            lastPointSphere[individual].getMaterial().setColor(Color(116.0/255.0, 173.0/255.0,
                                                                     209.0/255.0, 1.0),
                                                               Color(116.0/255.0, 173.0/255.0,
                                                                     209.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 6 and \
           movementData[individual][myEndDay[individual]][0][3] < 9:
            lastPointSphere[individual].getMaterial().setColor(Color(171.0/255.0, 217.0/255.0,
                                                                     233.0/255.0, 1.0),
                                                               Color(171.0/255.0, 217.0/255.0,
                                                                     233.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 9 and \
           movementData[individual][myEndDay[individual]][0][3] < 12:
            lastPointSphere[individual].getMaterial().setColor(Color(224.0/255.0, 243.0/255.0,
                                                                     248.0/255.0, 1.0),
                                                               Color(224.0/255.0, 243.0/255.0,
                                                                     248.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 12 and \
           movementData[individual][myEndDay[individual]][0][3] < 15:
            lastPointSphere[individual].getMaterial().setColor(Color(254.0/255.0, 224.0/255.0,
                                                                     144.0/255.0, 1.0),
                                                               Color(254.0/255.0, 224.0/255.0,
                                                                     144.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 15 and \
           movementData[individual][myEndDay[individual]][0][3] < 18:
            lastPointSphere[individual].getMaterial().setColor(Color(253.0/255.0, 174.0/255.0,
                                                                     97.0/255.0, 1.0),
                                                               Color(253.0/255.0, 174.0/255.0,
                                                                     97.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 18 and \
           movementData[individual][myEndDay[individual]][0][3] < 21:
            lastPointSphere[individual].getMaterial().setColor(Color(244.0/255.0, 109.0/255.0,
                                                                     67.0/255.0, 1.0),
                                                               Color(244.0/255.0, 109.0/255.0,
                                                                     67.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 21 and \
           movementData[individual][myEndDay[individual]][0][3] < 24:
            lastPointSphere[individual].getMaterial().setColor(Color(215.0/255.0, 48.0/255.0,
                                                                     39.0/255.0, 1.0),
                                                               Color(215.0/255.0, 48.0/255.0,
                                                                     39.0/255.0, 1.0))
    if value == 2:
        if movementData[individual][myEndDay[individual]][0][3] < 3:
            lastPointSphere[individual].getMaterial().setColor(Color(104.0/255.0, 79.0/255.0,
                                                                     227.0/255.0, 1.0),
                                                               Color(104.0/255.0, 79.0/255.0,
                                                                     227.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 3 and \
           movementData[individual][myEndDay[individual]][0][3] < 6:
            lastPointSphere[individual].getMaterial().setColor(Color(78.0/255.0, 181.0/255.0,
                                                                     226.0/255.0, 1.0),
                                                               Color(78.0/255.0, 181.0/255.0,
                                                                     226.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 6 and \
           movementData[individual][myEndDay[individual]][0][3] < 9:
            lastPointSphere[individual].getMaterial().setColor(Color(138.0/255.0, 227.0/255.0,
                                                                     244.0/255.0, 1.0),
                                                               Color(138.0/255.0, 227.0/255.0,
                                                                     244.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 9 and \
           movementData[individual][myEndDay[individual]][0][3] < 12:
            lastPointSphere[individual].getMaterial().setColor(Color(253.0/255.0, 247.0/255.0,
                                                                     155.0/255.0, 1.0),
                                                               Color(253.0/255.0, 247.0/255.0,
                                                                     155.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 12 and \
           movementData[individual][myEndDay[individual]][0][3] < 15:
            lastPointSphere[individual].getMaterial().setColor(Color(253.0/255.0, 222.0/255.0,
                                                                     115.0/255.0, 1.0),
                                                               Color(253.0/255.0, 222.0/255.0,
                                                                     115.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 15 and \
           movementData[individual][myEndDay[individual]][0][3] < 18:
            lastPointSphere[individual].getMaterial().setColor(Color(253.0/255.0, 247.0/255.0,
                                                                     155.0/255.0, 1.0),
                                                               Color(253.0/255.0, 247.0/255.0,
                                                                     155.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 18 and \
           movementData[individual][myEndDay[individual]][0][3] < 21:
            lastPointSphere[individual].getMaterial().setColor(Color(138.0/255.0, 227.0/255.0,
                                                                     244.0/255.0, 1.0),
                                                               Color(138.0/255.0, 227.0/255.0,
                                                                     244.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][3] >= 21 and \
           movementData[individual][myEndDay[individual]][0][3] < 24:
            lastPointSphere[individual].getMaterial().setColor(Color(78.0/255.0, 181.0/255.0,
                                                                     226.0/255.0, 1.0),
                                                               Color(78.0/255.0, 181.0/255.0,
                                                                     226.0/255.0, 1.0))
    if value == 3:
        if movementData[individual][myEndDay[individual]][0][5] < 10:
            lastPointSphere[individual].getMaterial().setColor(Color(247.0/255.0, 251.0/255.0,
                                                                     255.0/255.0, 1.0),
                                                               Color(247.0/255.0, 251.0/255.0,
                                                                     255.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][5] >= 10 and \
           movementData[individual][myEndDay[individual]][0][5] < 20:
            lastPointSphere[individual].getMaterial().setColor(Color(222.0/255.0, 235.0/255.0,
                                                                     247.0/255.0, 1.0),
                                                               Color(222.0/255.0, 235.0/255.0,
                                                                     247.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][5] >= 20 and \
           movementData[individual][myEndDay[individual]][0][5] < 30:
            lastPointSphere[individual].getMaterial().setColor(Color(198.0/255.0, 219.0/255.0,
                                                                     239.0/255.0, 1.0),
                                                               Color(198.0/255.0, 219.0/255.0,
                                                                     239.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][5] >= 30 and \
           movementData[individual][myEndDay[individual]][0][5] < 40:
            lastPointSphere[individual].getMaterial().setColor(Color(158.0/255.0, 202.0/255.0,
                                                                     225.0/255.0, 1.0),
                                                               Color(158.0/255.0, 202.0/255.0,
                                                                     225.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][5] >= 40 and \
           movementData[individual][myEndDay[individual]][0][5] < 50:
            lastPointSphere[individual].getMaterial().setColor(Color(107.0/255.0, 174.0/255.0,
                                                                     214.0/255.0, 1.0),
                                                               Color(107.0/255.0, 174.0/255.0,
                                                                     214.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][5] >= 50 and \
           movementData[individual][myEndDay[individual]][0][5] < 60:
            lastPointSphere[individual].getMaterial().setColor(Color(66.0/255.0, 146.0/255.0,
                                                                     198.0/255.0, 1.0),
                                                               Color(66.0/255.0, 146.0/255.0,
                                                                     198.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][5] >= 60 and \
           movementData[individual][myEndDay[individual]][0][5] < 70:
            lastPointSphere[individual].getMaterial().setColor(Color(33.0/255.0, 113.0/255.0,
                                                                     181.0/255.0, 1.0),
                                                               Color(33.0/255.0, 113.0/255.0,
                                                                     181.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][5] >= 70 and \
           movementData[individual][myEndDay[individual]][0][5] < 84:
            lastPointSphere[individual].getMaterial().setColor(Color(8.0/255.0, 81.0/255.0,
                                                                     156.0/255.0, 1.0),
                                                               Color(8.0/255.0, 81.0/255.0,
                                                                     156.0/255.0, 1.0))
    if value == 4:
        if movementData[individual][myEndDay[individual]][0][5] < 10:
            lastPointSphere[individual].getMaterial().setColor(Color(255.0/255.0, 247.0/255.0,
                                                                     243.0/255.0, 1.0),
                                                               Color(255.0/255.0, 247.0/255.0,
                                                                     243.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][5] >= 10 and \
           movementData[individual][myEndDay[individual]][0][5] < 20:
            lastPointSphere[individual].getMaterial().setColor(Color(253.0/255.0, 224.0/255.0,
                                                                     221.0/255.0, 1.0),
                                                               Color(253.0/255.0, 224.0/255.0,
                                                                     221.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][5] >= 20 and \
           movementData[individual][myEndDay[individual]][0][5] < 30:
            lastPointSphere[individual].getMaterial().setColor(Color(252.0/255.0, 197.0/255.0,
                                                                     192.0/255.0, 1.0),
                                                               Color(252.0/255.0, 197.0/255.0,
                                                                     192.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][5] >= 30 and \
           movementData[individual][myEndDay[individual]][0][5] < 40:
            lastPointSphere[individual].getMaterial().setColor(Color(250.0/255.0, 159.0/255.0,
                                                                     181.0/255.0, 1.0),
                                                               Color(250.0/255.0, 159.0/255.0,
                                                                     181.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][5] >= 40 and \
           movementData[individual][myEndDay[individual]][0][5] < 50:
            lastPointSphere[individual].getMaterial().setColor(Color(247.0/255.0, 104.0/255.0,
                                                                     161.0/255.0, 1.0),
                                                               Color(247.0/255.0, 104.0/255.0,
                                                                     161.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][5] >= 50 and \
           movementData[individual][myEndDay[individual]][0][5] < 60:
            lastPointSphere[individual].getMaterial().setColor(Color(221.0/255.0, 52.0/255.0,
                                                                     151.0/255.0, 1.0),
                                                               Color(221.0/255.0, 52.0/255.0,
                                                                     151.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][5] >= 60 and \
           movementData[individual][myEndDay[individual]][0][5] < 70:
            lastPointSphere[individual].getMaterial().setColor(Color(174.0/255.0, 1.0/255.0,
                                                                     126.0/255.0, 1.0),
                                                               Color(174.0/255.0, 1.0/255.0,
                                                                     126.0/255.0, 1.0))
        if movementData[individual][myEndDay[individual]][0][5] >= 70 and \
           movementData[individual][myEndDay[individual]][0][5] < 84:
            lastPointSphere[individual].getMaterial().setColor(Color(122.0/255.0, 1.0/255.0,
                                                                     119.0/255.0, 1.0),
                                                               Color(122.0/255.0, 1.0/255.0,
                                                                     119.0/255.0, 1.0))
    # if( value == 5 ){
    #   if( individualID == selectedIndividual1 )
    #     lastPointSphere[individual].setColor(Color( 149.0/255.0,79.0/255.0,234.0/255.0, 1.0 ))
    #   if( individualID == selectedIndividual2 )
    #     lastPointSphere[individual].setColor(Color( 85.0/255.0,136.0/255.0,244.0/255.0, 1.0 ))
    # }


def setUpLines(lineList, i):
    '''
    function sets up lines for text. Text includes START, END, and INDIVIDUALNAME. i corresponds to
    individual global XYOFFSET
    '''
    global STARTOFFSET
    global ENDOFFSET
    global movementData
    global myStartDay
    global myEndDay

    lineList[i].append(lineList[i][0].addLine())
    lineList[i].append(lineList[i][0].addLine())
    lineList[i][1].setStart(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET+TEXTOFFSET,
                                    movementData[i][myStartDay[i]][0][1],
                                    movementData[i][myStartDay[i]][0][2]+STARTOFFSET))
    lineList[i][2].setStart(Vector3(movementData[i][myEndDay[i]][0][0]-XYOFFSET+TEXTOFFSET,
                                    movementData[i][myEndDay[i]][0][1],
                                    movementData[i][myEndDay[i]][0][2]+ENDOFFSET))
    lineList[i][1].setEnd(Vector3(movementData[i][myStartDay[i]][0][0],
                                  movementData[i][myStartDay[i]][0][1],
                                  movementData[i][myStartDay[i]][0][2]))
    lineList[i][2].setEnd(Vector3(movementData[i][myEndDay[i]][0][0],
                                  movementData[i][myEndDay[i]][0][1],
                                  movementData[i][myEndDay[i]][0][2]))
    lineList[i][1].setThickness(5)
    lineList[i][2].setThickness(5)
    lineList[i][0].setEffect('colored -e #900020')
    lineList[i].append(SphereShape.create(5/2, 2))
    lineList[i].append(SphereShape.create(5/2, 2))
    lineList[i][3].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET+TEXTOFFSET,
                                       movementData[i][myStartDay[i]][0][1],
                                       movementData[i][myStartDay[i]][0][2]+STARTOFFSET))
    lineList[i][4].setPosition(Vector3(movementData[i][myEndDay[i]][0][0]-XYOFFSET+TEXTOFFSET,
                                       movementData[i][myEndDay[i]][0][1],
                                       movementData[i][myEndDay[i]][0][2]+ENDOFFSET))
    lineList[i][3].setEffect('colored -e #900020')
    lineList[i][4].setEffect('colored -e #900020')


def setLinePos(lineList, i):
    '''
    function updates line positions based on what days we are looking at. Modifies list, lineList, 
    that holds LineSet information. i corresponds to individuals.
    '''
    global XYOFFSET
    global STARTOFFSET
    global ENDOFFSET
    global movementData
    global myStartDay
    global myEndDay

    lineList[i][1].setStart(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET+TEXTOFFSET, 
                                    movementData[i][myStartDay[i]][0][1], 
                                    movementData[i][myStartDay[i]][0][2]+STARTOFFSET))
    lineList[i][2].setStart(Vector3(movementData[i][myEndDay[i]][0][0]-XYOFFSET+TEXTOFFSET, 
                                    movementData[i][myEndDay[i]][0][1], 
                                    movementData[i][myEndDay[i]][0][2]+ENDOFFSET))
    lineList[i][1].setEnd(Vector3(movementData[i][myStartDay[i]][0][0], 
                                  movementData[i][myStartDay[i]][0][1], 
                                  movementData[i][myStartDay[i]][0][2]))
    lineList[i][2].setEnd(Vector3(movementData[i][myEndDay[i]][0][0], 
                                  movementData[i][myEndDay[i]][0][1], 
                                  movementData[i][myEndDay[i]][0][2]))

    lineList[i][3].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET+TEXTOFFSET, 
                                       movementData[i][myStartDay[i]][0][1], 
                                       movementData[i][myStartDay[i]][0][2]+STARTOFFSET))
    lineList[i][4].setPosition(Vector3(movementData[i][myEndDay[i]][0][0]-XYOFFSET+TEXTOFFSET, 
                                       movementData[i][myEndDay[i]][0][1], 
                                       movementData[i][myEndDay[i]][0][2]+ENDOFFSET))


def setTextPos(textList, i):
    '''
    sets text position for individual start and end text for movement
    '''
    global XYOFFSET
    global STARTOFFSET
    global ENDOFFSET
    global movementData
    global myStartDay
    global myEndDay

    textList[i][0].setPosition(Vector3(movementData[i][myStartDay[i]][0][0]+XYOFFSET, 
                                       movementData[i][myStartDay[i]][0][1], 
                                       movementData[i][myStartDay[i]][0][2]+STARTTXTOFFSET))
    textList[i][1].setPosition(Vector3(movementData[i][myEndDay[i]][0][0]-XYOFFSET, 
                                       movementData[i][myEndDay[i]][0][1], 
                                       movementData[i][myEndDay[i]][0][2]+ENDTXTOFFSET))

#----------------------------------------------------------------------------
#Constants

numberOfDaysByIndividual = [85, 70, 78, 80, 52, 18, 83, 80, 79, 67, 65, 72, 73, 71, 72, 66, 82, 86, 
                            35, 39, 2]
namesOfIndividuals = ["Veruca", "Chibi", "Abby", "Ben Bob", "Bonnie", "Chloe", "Clementina",
                      "Ellie", "Gillian", "Ornette", "Pliny", "Ripley", "Sofie", "Greg", "Ibeth",
                      "Olga", "Mimi", "Kyle", "Atlas", "Judy", "Merk"]
startDateByIndividual = [date(2015, 12, 11), date(2015, 12, 11), date(2015, 12, 15),
                         date(2015, 12, 15), date(2015, 12, 15), date(2015, 12, 15),
                         date(2015, 12, 14), date(2015, 12, 14), date(2015, 12, 14),
                         date(2015, 12, 14), date(2015, 12, 14), date(2015, 12, 15),
                         date(2015, 12, 14), date(2015, 12, 11), date(2015, 12, 25),
                         date(2015, 12, 15), date(2015, 12, 15), date(2015, 12, 11),
                         date(2016, 1, 12), date(2016, 1, 27), date(2016, 3, 2)]

XYOFFSET = 80                    # X and Y offset for all text
TEXTOFFSET = 50                   # Moves line to center of text
STARTOFFSET = 300                 # Z offset for start line
ENDOFFSET = 400                   # Z offset for end line
STARTTXTOFFSET = 310              # Z offset for start text
ENDTXTOFFSET = 410                # Z offset for end text
currentYaw = 0
currentPitch = 0
currentRoll = 0
toggleTrees = False
hasCameraMoved = False
drawnCamPos = getDefaultCamera().getPosition()

txtArr = []                       # textArray of Individuals txtArr[individualID]
textNodeList = []                 # text SceneNode of Individuals textNodeList[individualID]
lineToTxt = []                    # Lines to text
uiModuleTxt = []                  # UI Module Text
lastPointSphere = []              # List of Sphere objects for last point in current dataset

#---------------------------------------------------------------------------
#Traversal setting, constants, functions


posArray = []                     # List of positions for traversal
oriArray = []                     # List of orientations for traversal
ghost = SceneNode.create('ghost') # ghost scene node for orientation array filling
g_arrayTraversal = 0

# interpolation actor
g_arrow = caveutil.loadObject(getSceneManager(), "arrow", "arrow2.fbx", False,
                              False, False, True, False)

# actor settings
interp = InterpolActor(g_arrow)
interp.setTransitionType(InterpolActor.SMOOTH)                      # Use SMOOTH ease-in/ease-out interpolation rather than LINEAR
interp.setPositionDuration(3)                                       # position interpolation time
interp.setOrientationDuration(1)                                    # orientation interpolation time
interp.setOperation(InterpolActor.POSITION | InterpolActor.ORIENT)  # Interpolate both position and orientation

# fill Position Array for Traversal
def fillArray():
  global posArray
  global bitMapSelectedIndividuals

  found = False
  fir = False

  print("in fill array")
 
  for i in range(0, 21):
    if (bitMapSelectedIndividuals.getIntElement(i) == 1 and not found):
      found = True
      print('The Monkey Selected is {}'.format(namesOfIndividuals[i]))
      print('The days shown is from: {} to: {}'.format(myStartDay[i]+1,myEndDay[i]+1))

      for time in range(myStartDay[i], myEndDay[i]):
        print('Points in Day {}: {}'.format(time,len(movementData[i][time])))
        for point in movementData[i][time]:
          posArray.append(Vector3(point[0], point[1], point[2]))
          '''
          if(fir == False):
            s = SphereShape.create(20,4)
            s.setEffect('colored -e blue')
            s.setPosition(posArray[-1]+Vector3(0,.5,0))
            fir = True
          else:
            s = SphereShape.create(10,4)
            s.setEffect('colored -e red')
            s.setPosition(posArray[-1]+Vector3(0,.5,0))
          '''

  print('Position Array Len: {}'.format(len(posArray)))
    # animate()  

# create Orientation List from position array
def createOrientationList(interpObj):
  global posArray
  global oriArray
  global ghost

  ghost.setPosition(posArray[0])
  
  index = 0
    
  if not oriArray:

    ghost.lookAt(getDefaultCamera().getPosition(), Vector3(0, 1, 0))
    oriArray.append(ghost.getOrientation())
    index = index+1
    ghost.setPosition(posArray[index])

    while(index < (len(posArray))):

      ghost.lookAt(posArray[index-1], Vector3(0, 1, 0))
      oriArray.append(ghost.getOrientation())
      index = index+1

      if(index < len(posArray)):
        ghost.setPosition(posArray[index])

    oriArray.append(oriArray[-1])
  print('Orientation Array Len: {}'.format(len(oriArray)))

# This function is used to iterate over the stored navigation waypoints.
def WaypointTraversalFunc(interpObj):
  global g_arrayTraversal
  global posArray
  
  if g_arrayTraversal < len(posArray):
    interpObj.setTargetPosition(posArray[g_arrayTraversal] + Vector3(0,.5,0))
    interpObj.setTargetOrientation(oriArray[g_arrayTraversal])
    interpObj.startInterpolation()
    g_arrayTraversal = g_arrayTraversal + 1  

# Tell the camera's InterpolActor to call the WaypointTraversalFunc at the end of each interpolated waypoint so that it can cue up
# the next waypoint.
interp.setEndOfInterpolationFunction(WaypointTraversalFunc)
#----------------------------------------------------------------------------
#UI Module code

uim = UiModule.createAndInitialize()

mainLayout = Container.create( ContainerLayout.LayoutVertical, uim.getUi())
mainLayout.setStyle('fill: #00000080')
mainLayout.setSize(Vector2(float(2000), float(2000)))
mainLayout.setAutosize(False)
mainLayout.setPosition(Vector2(1366*15, -200))

#-----------------------------------------------------------------------------
#Terrain code

scene = getSceneManager()
scene.addLoader(BinaryPointsLoader())                         #adds a binary loader for GLSL code
setNearFarZ(0.1, 1000000)                                     #Gives more depth

def loadModelAsync(name, path):   # Loads model asynchronously
    model = ModelInfo()
    model.name = name
    model.path = path
    model.optimize = True
    model.usePowerOfTwoTextures = False
    scene.loadModelAsync(model, "onModelLoaded('" + model.name + "')")
    return model

def onModelLoaded(name):           # Loads model
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
# plane = PlaneShape.create(imgResRatioX*10260, imgResRatioY*9850)              #this code sets up a
# plane.setPosition(Vector3(imgResRatioX*10260/2, imgResRatioY*9850/2, 0))      #2D plane image
# plane.setEffect("textured -v emissive -d 50Island.png")

getDefaultCamera().setPosition(imgResRatioX*10260/2, imgResRatioY*9850/2, 2500) #Default position
                                                                                #or camera
getDefaultCamera().setBackgroundColor(Color('black'))                           #sets background 
                                                                                #to black

#---------------------------------------------------------------------------
#Cylinder and Sphere Version

allAnimals = createCustomGeom()                             #Read data into movementData

allMat = allAnimals.getMaterial()                           #Get material of movement data geometry
allMat.setTransparent(True)
allMat.setProgram(moveLineProgram.name)
allMat.attachUniform(startDay)
allMat.attachUniform(endDay)
allMat.attachUniform(colorByBitMap)
allMat.attachUniform(bitMapSelectedIndividuals)

for i in range(0, 21):
    lastPointSphere.append(SphereShape.create(8, 4))
    lastPointSphere[i].setPosition(Vector3(movementData[i][myEndDay[i]][0][0],
                                           movementData[i][myEndDay[i]][0][1],
                                           movementData[i][myEndDay[i]][0][2]))
    setLastSphereColor(i, 0)

for i in range(0, 21):           #Set up Lines to Text
    lineToTxt.append([])
    lineToTxt[i].append(LineSet.create())
    setUpLines(lineToTxt, i)

for i in range(0, 21):           #Set up START and END text
    txtArr.append([])
    txtArr[i].append(Text3D.create('fonts/RobotoCondensed-Regular.ttf', 25,
                                   str(namesOfIndividuals[i])+" Start"))
    txtArr[i][0].setFontResolution(500)
    txtArr[i][0].setColor(Color('#900020'))
    txtArr[i].append(Text3D.create('fonts/RobotoCondensed-Regular.ttf', 25,
                                   str(namesOfIndividuals[i])+" End"))
    txtArr[i][1].setFontResolution(500)
    txtArr[i][1].setColor(Color('#900020'))
    txtArr[i][0].setFacingCamera(getDefaultCamera())
    txtArr[i][1].setFacingCamera(getDefaultCamera())

    setTextPos(txtArr, i)

for i in range(0, 21):
    uiModuleTxt.append([])
    uiModuleTxt[i].append(Label.create(mainLayout))
    uiModuleTxt[i][0].setFont('fonts/RobotoCondensed-Light.ttf 40')
    uiModuleTxt[i][0].setText(namesOfIndividuals[i] + ": " + str(startDateByIndividual[i] + \
                              timedelta(days=myStartDay[i])) + " - " + \
                              str(startDateByIndividual[i] + timedelta(days=myEndDay[i])))
    if i == 1:
        uiModuleTxt[i][0].setColor(Color('#FFFFFF'))
    else:
        uiModuleTxt[i][0].setColor(Color('#333333'))
    uiModuleTxt[i].append(Label.create(mainLayout))
    uiModuleTxt[i][1].setText(" ")

#Scene Node List for all Text
for i in range(0, 21):           #Add lines and text to a scenenode to toggle visibility
    textNodeList.append(SceneNode.create('textNode'+str(i)))
    getScene().addChild(textNodeList[i])
    textNodeList[i].addChild(txtArr[i][0])
    textNodeList[i].addChild(txtArr[i][1])
    textNodeList[i].addChild(lineToTxt[i][0])
    textNodeList[i].addChild(lineToTxt[i][3])
    textNodeList[i].addChild(lineToTxt[i][4])
    textNodeList[i].addChild(lastPointSphere[i])
    if i == 1:
        textNodeList[i].setChildrenVisible(True)
    else:
        textNodeList[i].setChildrenVisible(False)

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
movePointCloudModel.options = '10000 100:1000000:1 20:100:1 6:20:1 0:5:1'
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
pointProgram.name = 'points'
pointProgram.vertexShaderName = 'islandShaders/Sphere.vert'
pointProgram.fragmentShaderName = 'islandShaders/Sphere.frag'
pointProgram.geometryShaderName = 'islandShaders/Sphere.geom'
pointProgram.geometryOutVertices = 4
pointProgram.geometryInput = PrimitiveType.Points
pointProgram.geometryOutput = PrimitiveType.TriangleStrip
scene.addProgram(pointProgram)

toggleHighlight = Uniform.create('toggleHighlight', UniformType.Int, 1)
toggleHighlight.setInt(1)
pointScale = Uniform.create('pointScale', UniformType.Float, 1)
pointScale.setFloat(1)
globalAlpha = Uniform.create('globalAlpha', UniformType.Float, 1)
globalAlpha.setFloat(1)

pointCloudModel = ModelInfo()
pointCloudModel.name = 'pointCloud'
pointCloudModel.path = '/iridium_SSD/panama/hmColorHigh.xyzb'
pointCloudModel.options = '10000 100:1000000:40 20:100:20 6:20:15 0:5:20'
scene.loadModel(pointCloudModel)

pointCloud = StaticObject.create(pointCloudModel.name)
# attach shader uniforms
pointMat = pointCloud.getMaterial()
pointMat.setTransparent(True)
pointMat.setProgram(pointProgram.name)
pointMat.attachUniform(pointScale)
pointMat.attachUniform(globalAlpha)
pointMat.attachUniform(toggleHighlight)

#btnAll.setRadio(True)

#--------------------------------------------------------------------------------------
#Sound Environment
env = getSoundEnvironment()
s_animal = env.setAssetDirectory("animal", "animalSoundFile.wav")
si_animal = SoundInstance(s_animal)

si_animal.setIDPosition(1, 100.1314, 13413.423, 134.13414)
si_animal.playStereo()



#--------------------------------------------------------------------------------------
#Cylinder Code

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

    if value == 1:
        toggleTrees = not toggleTrees
        treeNode.setChildrenVisible(toggleTrees)

showOtherTrees = SceneNode.create('showOtherTrees')
getScene().addChild(showOtherTrees)

c2 = LineSet.create()
toggleLineToTrees = False
lineList = []
numLines = 0


def drawLinesToTrees(value):
    '''
    Turns line mode to trees on or off
    '''

    global toggleLineToTrees

    if value == 1:
        toggleLineToTrees = not toggleLineToTrees


def highlightTrees(value):
    '''
    Reduces alpha for all non fruit trees
    '''
    global toggleHighlight

    if toggleHighlight == 1:
        toggleHighlight.setInt(2)
    else:
        toggleHighlight.setInt(1)


def onUpdate(frame, time, dt):
    '''
    On Update function for omegalib. https://github.com/uic-evl/omegalib/wiki/Callbacks
    '''
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

    if (drawnCamPos[0]+5 < xPos or drawnCamPos[0]-5 > xPos) or (drawnCamPos[1]+5 < yPos or \
        drawnCamPos[1]-5 > yPos) or (drawnCamPos[2]+5 < zPos or drawnCamPos[2]-5 > zPos):
        hasCameraMoved = True

    while lineList and hasCameraMoved:
        line = lineList.pop()
        c2.removeLine(line)

    if toggleLineToTrees and hasCameraMoved:
        thickness2 = 3
        for node in treeList:
            vec = Vector3(node[0], node[1], node[2]*0.18)
            camVec = getDefaultCamera().getPosition()
            if abs(vec - camVec) <= 100:
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

# if isMaster():
#     UDP_IP = '131.193.76.77'
#     UDP_PORT = 8081
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     singlePoint = ['a', movementData[1][myStartDay[1]][0][0], movementData[1][myStartDay[1]][0][1], movementData[1][myStartDay[1]][0][2]]
#     sock.sendto(bytes(singlePoint), (UDP_IP, UDP_PORT))

#--------------------------------------------------------------------------------------
#Functions
def oneDayStepUp(value):
    '''
    Shows the next day for a given individual. value is the individualID
    '''

    global myStartDay
    global myEndDay
    global startDay
    global endDay
    global numberOfDaysByIndividual
    global movementData
    global txtArr
    global namesOfIndividuals
    global uiModuleTxt
    global lineToTxt
    global lastPointSphere

    myStartDay[value] = myStartDay[value] + 1
    if myStartDay[value] > numberOfDaysByIndividual[value]:
        myStartDay[value] = 0
    myEndDay[value] = myStartDay[value] + 1
    endDay.setIntElement(myEndDay[value], value)
    startDay.setIntElement(myStartDay[value], value)
    setTextPos(txtArr, value)

    setLinePos(lineToTxt, value)

    lastPointSphere[value].setPosition(Vector3(movementData[value][myEndDay[value]][0][0],
                                               movementData[value][myEndDay[value]][0][1],
                                               movementData[value][myEndDay[value]][0][2]))
    uiModuleTxt[value][0].setText(namesOfIndividuals[value] + ": " + \
                                  str(startDateByIndividual[value] + \
                                  timedelta(days=myStartDay[value])) + " - " + \
                                  str(startDateByIndividual[value] + \
                                  timedelta(days=myEndDay[value])))


def globalOneDayStepUp(value):
    '''
    Shows the next day for every given individual that is turned on.
    '''
    global myStartDay
    global myEndDay
    global startDay
    global endDay
    global numberOfDaysByIndividual
    global movementData
    global txtArr
    global lineToTxt
    global uiModuleTxt
    global lastPointSphere

    for i in range(0, 21):
        myStartDay[i] = myStartDay[i] + 1
        if myStartDay[i] > numberOfDaysByIndividual[i]:
            myStartDay[i] = 0
        myEndDay[i] = myStartDay[i] + 1
        endDay.setIntElement(myEndDay[i], i)
        startDay.setIntElement(myStartDay[i], i)

        #Update text positions to location of animals
        setTextPos(txtArr, i)
        setLinePos(lineToTxt, i)
        lastPointSphere[i].setPosition(Vector3(movementData[i][myEndDay[i]][0][0],
                                               movementData[i][myEndDay[i]][0][1],
                                               movementData[i][myEndDay[i]][0][2]))
        uiModuleTxt[i][0].setText(namesOfIndividuals[i] + ": " + str(startDateByIndividual[i] + \
                                  timedelta(days=myStartDay[i])) + " - " + \
                                  str(startDateByIndividual[i] + timedelta(days=myEndDay[i])))


def oneDayStepDown(value):
    '''
    Shows the previous day for any given individual.
    '''

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
    global uiModuleTxt
    global lastPointSphere

    myStartDay[value] = myStartDay[value] - 1
    if myStartDay[value] < 0:
        myStartDay[value] = numberOfDaysByIndividual[value]
    myEndDay[value] = myStartDay[value] + 1
    endDay.setIntElement(myEndDay[value], value)
    startDay.setIntElement(myStartDay[value], value)
    setTextPos(txtArr, value)
    setLinePos(lineToTxt, value)

    lastPointSphere[value].setPosition(Vector3(movementData[value][myEndDay[value]][0][0],
                                               movementData[value][myEndDay[value]][0][1],
                                               movementData[value][myEndDay[value]][0][2]))
    uiModuleTxt[value][0].setText(namesOfIndividuals[value] + ": " + \
                                  str(startDateByIndividual[value] + \
                                  timedelta(days=myStartDay[value])) + " - " + \
                                  str(startDateByIndividual[value] + \
                                  timedelta(days=myEndDay[value])))


def globalOneDayStepDown(value):
    '''
    Shows the previous day for all individuals that are turned on
    '''

    global myStartDay
    global myEndDay
    global startDay
    global endDay
    global numberOfDaysByIndividual
    global movementData
    global txtArr
    global uiModuleTxt
    global lastPointSphere

    for i in range(0, 21):
        myStartDay[i] = myStartDay[i] - 1
        if myStartDay[i] < 0:
            myStartDay[i] = numberOfDaysByIndividual[i]-1
        myEndDay[i] = myStartDay[i] + 1
        endDay.setIntElement(myEndDay[i], i)
        startDay.setIntElement(myStartDay[i], i)
        setTextPos(txtArr, i)
        setLinePos(lineToTxt, i)
        lastPointSphere[i].setPosition(Vector3(movementData[i][myEndDay[i]][0][0],
                                               movementData[i][myEndDay[i]][0][1],
                                               movementData[i][myEndDay[i]][0][2]))
        uiModuleTxt[i][0].setText(namesOfIndividuals[i] + ": " + str(startDateByIndividual[i] + \
                                  timedelta(days=myStartDay[i])) + " - " + \
                                  str(startDateByIndividual[i] + timedelta(days=myEndDay[i])))


def sevenDayStepUp(value):
    '''
    Shows the next seven days of movement for a given individual.
    '''

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
    global uiModuleTxt
    global lastPointSphere

    myStartDay[value] = myStartDay[value] + 7
    if myStartDay[value] > numberOfDaysByIndividual[value]:
        myStartDay[value] = 0
    myEndDay[value] = myStartDay[value] + 7
    endDay.setIntElement(myEndDay[value], value)
    startDay.setIntElement(myStartDay[value], value)
    setTextPos(txtArr, value)
    setLinePos(lineToTxt, value)

    lastPointSphere[value].setPosition(Vector3(movementData[value][myEndDay[value]][0][0],
                                               movementData[value][myEndDay[value]][0][1],
                                               movementData[value][myEndDay[value]][0][2]))
    uiModuleTxt[value][0].setText(namesOfIndividuals[value] + ": " + \
                                  str(startDateByIndividual[value] + \
                                  timedelta(days=myStartDay[value])) + " - " + \
                                  str(startDateByIndividual[value] + \
                                  timedelta(days=myEndDay[value])))


def globalSevenDayStepUp(value):
    '''
    Shows the next seven days of movement for all individuals that are turned on.
    '''

    global myStartDay
    global myEndDay
    global startDay
    global endDay
    global numberOfDaysByIndividual
    global movementData
    global txtArr
    global lineToTxt
    global uiModuleTxt
    global lastPointSphere

    for i in range(0, 21):
        myStartDay[i] = myStartDay[i] + 7
        if myStartDay[i] > numberOfDaysByIndividual[i]:
            myStartDay[i] = 0
        myEndDay[i] = myStartDay[i] + 7
        endDay.setIntElement(myEndDay[i], i)
        startDay.setIntElement(myStartDay[i], i)
        setTextPos(txtArr, i)
        setLinePos(lineToTxt, i)
        lastPointSphere[i].setPosition(Vector3(movementData[i][myEndDay[i]][0][0],
                                               movementData[i][myEndDay[i]][0][1],
                                               movementData[i][myEndDay[i]][0][2]))
        uiModuleTxt[i][0].setText(namesOfindividuals[i] + ": " + str(startDateByIndividual[i] + \
                                  timedelta(days=myStartDay[i])) + " - " + \
                                  str(startDateByIndividual[i] + timedelta(days=myEndDay[i])))


def sevenDayStepDown(value):
    '''
    Shows the previous seven days of movement for any given individual
    '''

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
    global uiModuleTxt
    global lastPointSphere

    myStartDay[value] = myStartDay[value] - 7
    if myStartDay[value] < 0:
        myStartDay[value] = numberOfDaysByIndividual[i]-7
    myEndDay[value] = myStartDay[value] + 7
    endDay.setIntElement(myEndDay[value], value)
    startDay.setIntElement(myStartDay[value], value)
    setTextPos(txtArr, value)
    setLinePos(lineToTxt, value)
    lastPointSphere[value].setPosition(Vector3(movementData[value][myEndDay[value]][0][0],
                                               movementData[value][myEndDay[value]][0][1],
                                               movementData[value][myEndDay[value]][0][2]))
    uiModuleTxt[value][0].setText(namesOfIndividuals[value] + ": " + \
                                  str(startDateByIndividual[value] + \
                                  timedelta(days=myStartDay[value])) + " - " + \
                                  str(startDateByIndividual[value] + \
                                  timedelta(days=myEndDay[value])))


def globalSevenDayStepDown(value):
    '''
    Shows the previous seven days of movement for all individuals.
    '''

    global myStartDay
    global myEndDay
    global startDay
    global endDay
    global numberOfDaysByIndividual
    global movementData
    global txtArr
    global uiModuleTxt
    global lastPointSphere

    for i in range(0, 21):
        myStartDay[i] = myStartDay[i] - 7
        if myStartDay[i] < 0:
            myStartDay[i] = numberOfDaysByIndividual[i]-7
        myEndDay[i] = myStartDay[i] + 7
        endDay.setIntElement(myEndDay[i], i)
        startDay.setIntElement(myStartDay[i], i)
        setTextPos(txtArr, i)
        setLinePos(lineToTxt, i)
        lastPointSphere[i].setPosition(Vector3(movementData[i][myEndDay[i]][0][0],
                                               movementData[i][myEndDay[i]][0][1],
                                               movementData[i][myEndDay[i]][0][2]))
        uiModuleTxt[i][0].setText(namesOfIndividuals[i] + ": " + \
                                  str(startDateByIndividual[i] + timedelta(days=myStartDay[i])) + \
                                  " - " + str(startDateByIndividual[i] + \
                                  timedelta(days=myEndDay[i])))


def allDay(value):
    '''
    Shows all days for a given individual. value is the individualID.
    '''

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
    global uiModuleTxt
    global lastPointSphere

    myStartDay[value] = 0
    myEndDay[value] = numberOfDaysByIndividual[value]
    endDay.setIntElement(numberOfDaysByIndividual[value], value)
    startDay.setIntElement(0, value)
    setTextPos(txtArr, value)
    setLinePos(lineToTxt, value)
    lastPointSphere[value].setPosition(Vector3(movementData[value][myEndDay[value]][0][0],
                                               movementData[value][myEndDay[value]][0][1],
                                               movementData[value][myEndDay[value]][0][2]))
    uiModuleTxt[value][0].setText(namesOfIndividuals[value] + ": " + \
                                  str(startDateByIndividual[value] + \
                                  timedelta(days=myStartDay[value])) + \
                                  " - " + str(startDateByIndividual[value] + \
                                  timedelta(days=myEndDay[value])))


def globalAllDay(value):
    '''
    Shows all days for every individual that is turned on.
    '''

    global numberOfDaysByIndividual
    global startDay
    global endDay
    global movementData
    global txtArr
    global lineToTxt
    global uiModuleTxt
    global lastPointSphere

    for i in range(0, 21):
        endDay.setIntElement(numberOfDaysByIndividual[i], i)
        startDay.setIntElement(0, i)
        setTextPos(txtArr, i)
        setLinePos(lineToTxt, i)
        lastPointSphere[i].setPosition(Vector3(movementData[i][myEndDay[i]][0][0],
                                               movementData[i][myEndDay[i]][0][1],
                                               movementData[i][myEndDay[i]][0][2]))
        uiModuleTxt[i][0].setText(namesOfIndividuals[i] + ": " + str(startDateByIndividual[i] + \
                                  timedelta(days=myStartDay[i]))+ " - " + \
                                  str(startDateByIndividual[i] + timedelta(days=myEndDay[i])))


def setColorBy(individual, value):
    '''
    Sets the color scheme for movement of any individual
    '''

    global colorByBitMap

    setLastSphereColor(individual, value)
    colorByBitMap.setIntElement(value, individual)


def setSelInd(value):
    '''
    Toggles individual's line movement on or off
    '''

    global bitMapSelectedIndividuals
    global textNodeList
    global namesOfIndividuals
    global lastIndividualTxt
    global dayRangeTxt

    val = bitMapSelectedIndividuals.getIntElement(value)
    bitMapSelectedIndividuals.setIntElement((not val), value)
    if val == 1:
        textNodeList[value].setChildrenVisible(False)
        uiModuleTxt[value][0].setColor(Color('#333333'))
    else:
        textNodeList[value].setChildrenVisible(True)
        uiModuleTxt[value][0].setColor(Color('#FFFFFF'))

    uiModuleTxt[value][0].setText(namesOfIndividuals[value] + ": " + \
                                  str(startDateByIndividual[value] + \
                                  timedelta(days=myStartDay[value])) + " - " + \
                                  str(startDateByIndividual[value] + \
                                  timedelta(days=myEndDay[value])))


def onPointSizeSliderValueChanged(value):
    '''
    Changes point size of canopy point cloud
    '''

    if value != 0:
        size = .95 + value * .05
    else:
        size = 0.0
    pointScale.setFloat(size)


def onAlphaSliderValueChanged(value):
    '''
    Changes alpha of canopy point cloud
    '''

    if value != 0:
        alpha = value/10.0
    else:
        alpha = 0.0
    globalAlpha.setFloat(alpha)


def viewVertical(value):
    '''
    Changes the view to a vertical view
    '''

    global currentPitch
    global currentYaw
    global currentRoll
    if value == 1:
        getDefaultCamera().setPosition(Vector3(imgResRatioX*10260/2, imgResRatioY*9850/2, 2500))
        currentPitch = 0
        getDefaultCamera().setPitchYawRoll(Vector3(currentPitch, currentYaw, currentRoll))


def viewHorizontal(value):
    '''
    Changes the view to a horizontal view
    '''

    global currentYaw
    global currentPitch
    if value == 1:
        currentPitch = 45
        getDefaultCamera().setPitchYawRoll(Vector3(currentPitch, currentYaw, 0))
        getDefaultCamera().setPosition(Vector3(imgResRatioX*10260/2, 0, 500))


# --Event handler
#  EVENT HANDLERS
def handleEvent():
    global currentPitch
    global g_arrayTraversal
    global posArray
    global oriArray

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
        print("Button5 Pushed")
        getDefaultCamera().setPosition(Vector3(imgResRatioX*10260/2, 0, 500))
        getDefaultCamera().lookAt(Vector3(imgResRatioX*10260/2, 0, 500), Vector3(0, .25, 0))

    if (e.isKeyDown(ord('b')) or e.isButtonDown(EventFlags.ButtonLeft)):
        print("setting up positon and orientation")
        posArray = []
        oriArray = []
        fillArray()
        createOrientationList(interp)

    if (e.isKeyDown(ord('n')) or e.isButtonDown(EventFlags.ButtonRight)):
        print("start traversal")
        g_arrayTraversal = 0
        WaypointTraversalFunc(interp)
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
