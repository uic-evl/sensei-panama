# SENSEI-Panama
The goal of SENSEI-Panama is to use virtual reality in order to aid ecologists at UC Davis and
UIC to track the movements of animals that live on an island without having to be in the field.

Table of Contents
Necessary Files (6)
Image File Creating Scripts (39)
Mesh with Terrain Mapping
GPS Coordinate Encoding/Custom Geometry
Accessing Movement Data List

---------------------------------------------------------------------------
Necessary Files
---------------------------------------------------------------------------
Currently, the necessary files that are required to make this application work are the
following:  
/gpsMovement/all.txt  
/gpsMovement/all.xyzb  
/iridium_SSD/panama/10mesh.fbx  
/islandShaders/Sphere.frag  
/islandShaders/Sphere.geom  
/islandShaders/Sphere.vert  
/lineShaders/Line.frag  
/lineShaders/Line.geom  
/lineShaders/Line.vert  
/movementShaders/Sphere.vert  
/movementShader/mySphere.geom  
/movementShaders/Sphere.frag  
/fonts/RobotoCondensed-Light.ttf  
/fonts/RobotoCondensed-Regular.ttf  
arrow.fbx  
caveutilcustom.py  
CustomGeom.py  
islandAndMovement.py (Main Program)  
MenuOptions.py  
treesFloat.txt  

---------------------------------------------------------------------------
Image File Creating Scripts
---------------------------------------------------------------------------
These scripts will be located in the dataProcessing folder.  
binProcessMovement and processMovement.py will parse the gps point cvs file for a specific individual ID  
that the user specifies as a command line argument 2 and output it to a file name that the user chooses
as command line argument 1. 
EX: python processMovement Chibi.txt 4693  
Please use the UniqueIDs.txt for a comprehensive breakdown of all animals ID #'s and species.  

hmPlanePointCloudGenerator.py creates a xyzb file out of a png. It was used to create the canopy of the  
island.  

objTriGen.py creates an obj file for the terrain which was later used to convert to an FBX and add a  
texture mapping to it.  
  
---------------------------------------------------------------------------
Mesh with Terrain Mapping
---------------------------------------------------------------------------
An ASCII fbx file contains the mesh with image mapping.
Labelled under  
Terrain Code  
  
In order to see the textures on the terrain, we need lights that have been  
set up labelled under  
Lights  
  
---------------------------------------------------------------------------
GPS Coordinate Encoding/Custom Geometry
---------------------------------------------------------------------------
The file CustomGeom.py contains code that creates a single shape that corresponds to the movement
points of every single gps coordinate currently available. It uses GLSL shaders that are located in the
movementShaders folder in order to maximize filtering performance. If you would like to increase or
decrease the height and width of rectangles than change the thickness variable.

GPS coordinates are encoded also with spheres using a point cloud in Omegalib. This code is labelled under  
Movement point cloud code GPU Version  
  
---------------------------------------------------------------------------
Accessing Movement Data List
---------------------------------------------------------------------------
There are several different structures that are used in order to find the position of a specific day.  
  
The first is every tracked animal has a list in order to find their position of the day.  
The indexes go from 0-20, and each index corresponds to an animal's ID.  
Positions are as follow:  
namesOfIndividuals = ["Veruca", "Chibi", "Abby", "Ben Bob", "Bonnie", "Chloe", "Clementina",  
                      "Ellie", "Gillian", "Ornette", "Pliny", "Ripley", "Sofie", "Greg", "Ibeth",  
                      "Olga", "Mimi", "Kyle", "Atlas", "Judy", "Merk"]  
  
The next two lists keep track of the start of the tracked day range and the end of the tracked day  
range. They are labelled as myStartDay and myEndDay and can be indexed with the animal's ID.  
myStartDay[individualId]  
myEndDay[individualId]  
  
Finally, we can find the position of any vector by indexing the list, movementData.  
In order to grab the positions of all active days we can create a loop using movementData:  
for time in range(myStartDay[individualId], myEndDay[individualId]:  
    for tuple in movementData[individualId][time]  
        # Your code goes here  
  
Each day in this loop will correspond to a tuple. The tuple values correspond to the following:  
0 = x position  
1 = y position  
2 = z position  
3 = hour  
4 = minute  
5 = Days passed since first tracking point was captured.  
  
---------------------------------------------------------------------------


