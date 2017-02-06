from omega import *
from omegaToolkit import *

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

#SUBMENU CAMERA OPTIONS
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

ss8 = mm.getMainMenu().addButton("Highlight Fruit Trees", "highlightTrees(1)")