#Covers TestCases: 19B1D
y=0

    
import json
import time
import datetime



from SyncTimeGet import *  #Intentional import all


oPtGroup1=True
oldWheel=""
tC19B1D=True
tCE5D68=True
tC0BCE9=True
tC964FB=True
tC823D0=True
tC5FE06=False
tCF05EA=False
tC0BB6F=True
oG1Pass="oG1Pass: "
oG1Fail="oG1Fail: "


y=0
wheelTimeStamp=0
hidCounter=0
oldhidTimeStamp=0

wheel1Found=False
wheeln1Found=False
button1Found=False
aCBackFound=False
hookSwitchFound=False
touchFound=False
playPauseFound=False
scanNTFound=False
scanPTFound=False
noneFound=""
noMultiHIDSend=True
hidCount=0
siriState=0
siriPrewarmCnt=0
siriDownCnt=0
siriUpCnt=0
siriTest1=False
siriTest2=False
siriTest3=False
siriTest4=False
tC26EBD=True
tC31FE6=True

#print ("Offset: ", timeOffset)

#print (dataIn)

oPtGroup1Data=(dataIn["optGroup1"])
#print ((dataIn["optGroup1"]))
oG1StartTime=((oPtGroup1Data["oG1StartTime"])-startTime)+timeOffset
tC4E15EEndTime=((oPtGroup1Data["tC4E15EEndTime"])-startTime)+timeOffset
tC19B1DEndTime=((oPtGroup1Data["tC19B1DEndTime"])-startTime)+timeOffset
optGroup1Tele=((oPtGroup1Data["optGroup1Tele"])-startTime)+timeOffset
tC0BCE9EndTime=((oPtGroup1Data["tC0BCE9EndTime"])-startTime)+timeOffset
tC964FBEndTime=((oPtGroup1Data["tC964FBEndTime"])-startTime)+timeOffset
tC62210EndTime=((oPtGroup1Data["tC62210EndTime"])-startTime)+timeOffset
oG1EndTime=((oPtGroup1Data["oG1EndTime"])-startTime)+timeOffset
tC31FE6EndTime=((oPtGroup1Data["tC31FE6EndTime"])-startTime)+timeOffset
optGroup1Siri=(oPtGroup1Data["optGroup1Siri"])   




#print ("tC964FBEndTime:",tC964FBEndTime)
#print ("oG1StartTime:",oG1StartTime)
#print("tC0BCE9EndTime:",tC0BCE9EndTime)
#print ("optGroup1Siri:", optGroup1Siri)
    
#tC4AF72_9=(dataIn["tC4AF72_9"])

with open("CarPlay Session.json", "r", encoding="utf8") as file: #Apple uses the utf8 encoding for json
    oG1Data=json.load(file)

    for key in oG1Data:
        
        
        if "Timestamp" in (oG1Data[y]):
            timeStamp=((oG1Data [y]["Timestamp"])/1000000000)
        if "Details" in (oG1Data[y]):
            Details=(oG1Data [y]["Details"])
            if "details" in (oG1Data [y]["Details"]):
                details=(oG1Data [y]["Details"]["details"])
        
        if "Title" in (oG1Data[y]):
            title=(oG1Data [y]["Title"])

            if timeStamp>oG1StartTime and timeStamp<oG1EndTime:
                if title=="HID Send Report Command":
                    if "hidReport" in (oG1Data[y]["Details"]["details"]):
                        hidReport=(oG1Data[y]["Details"]["details"]["hidReport"])



#####4E15E#####4E15E#####4E15E#####4E15E#####4E15E
                        if timeStamp>oG1StartTime and timeStamp<tC4E15EEndTime:
                            if "Touch: 1" in hidReport:
                                if hidCount==0:
                                    startHIDTime=timeStamp
                                endHIDTime=timeStamp
                                hidCount=hidCount+1
#####4E15E                        

#####TC19B1D#####TC19B1D#####TC19B1D#####TC19B1D#####TC19B1D
                        
                        if timeStamp>tC4E15EEndTime and timeStamp<tC19B1DEndTime:
                            if wheelTimeStamp!=0:
                                oldWheel=wheel
                                oldWheelTimeStamp=wheelTimeStamp

                            if "Wheel: 1" in hidReport:
                                wheel1Found=True
                                wheel=1
                                wheelTimeStamp=timeStamp
                            elif "Wheel: -1" in hidReport:
                                wheeln1Found=True
                                wheel=-1
                                wheelTimeStamp=timeStamp
                            elif "Wheel: 0" in hidReport:
                                wheel=0
                                wheelTimeStamp=timeStamp

                            if oldWheel==1 or oldWheel==-1:
                                if wheel==0 and (wheelTimeStamp-oldWheelTimeStamp)>.05 and tC19B1D==True:
                                    pass
                                else:
                                    tC19B1D=False
#####TC19B1D
                    

#####TC0BCE9 and TCE5D68#####TC0BCE9 and TCE5D68#####TC0BCE9 and TCE5D68                    

                        if timeStamp>tC19B1DEndTime and timeStamp<tC0BCE9EndTime:

                            if noneFound!="":
                                oldHidTimeStamp=hidTimeStamp
                                oldHidCounter=hidCounter
                                hidCounter=0



                            if "Button: 1" in hidReport:
                                button1Found=True
                                hidCounter=hidCounter+1
                                hidTimeStamp=timeStamp
                            if "AC Back: 1" in hidReport:
                                aCBackFound=True
                                hidCounter=hidCounter+1
                                hidTimeStamp=timeStamp
                            if "Hook Switch: 1" in hidReport:
                                hookSwitchFound=True
                                hidCounter=hidCounter+1
                                hidTimeStamp=timeStamp
                                tC5FE06=True
                                tCF05EA=True
                            if "Drop: 1" in hidReport:
                                dropFound=True
                                hidCounter=hidCounter+1
                                hidTimeStamp=timeStamp
                            if "Touch: 1" in hidReport:
                                touchFound=True
                                hidCounter=hidCounter+1
                                hidTimeStamp=timeStamp

                            if "Play/Pause: 1" in hidReport:                        
                                playPauseFound=True
                                hidCounter=hidCounter+1
                                hidTimeStamp=timeStamp
                            if "Scan Next Track: 1" in hidReport:
                                scanNTFound=True
                                hidCounter=hidCounter+1
                                hidTimeStamp=timeStamp
                            if "Scan Previous Track: 1" in hidReport:                            
                                scanPTFound=True
                                hidCounter=hidCounter+1
                                hidTimeStamp=timeStamp                       


                                
                            if "Wheel: 1" or "Wheel: 1" in hidReport: #Should not be seen
                                hidCounter=hidCounter+1
                                hidTimeStamp=timeStamp

                            if hidCounter>1:
                                noMultiHIDSend=False

                            if hidCounter==0:
                                noneFound=True
                                if oldhidCounter>0 and tC0BCE9==True:
                                    if(hidTimeStamp-oldHidTimeStamp)>.05 and tCE5D68==True:
                                        tCE5D68=False                   
                                else:
                                    tC0BCE9==False
                                    
                            else:
                                noneFound=False
                            
#####TC0BCE9 and TCE5D68

#####TC964FB#####TC964FB#####TC964FB#####TC964FB#####TC964FB

                        if timeStamp>tC0BCE9EndTime and timeStamp<tC964FBEndTime:
                            tC964FB=False
#####TC964FB                        



#####END "if hidReport in". BEGIN "Siri".


            if timeStamp>tC0BCE9EndTime:# and timeStamp<oG1EndTime:  <<<<Have an issue with timing........
                if title=="Request Siri Command":
                    if "siriAction" in (oG1Data[y]["Details"]["details"]["params"]):
                        siriAction=(oG1Data[y]["Details"]["details"]["params"]["siriAction"])
                        #print (siriAction)

#####TC823D0#####TC823D0#####TC823D0#####TC823D0#####TC823D0

                        if timeStamp>tC0BCE9EndTime and timeStamp<tC964FBEndTime:
                            tC823D0=False
#####TC823D0
                        

                        

#####TC62210 and TCB5E07#####TC62210 and TCB5E07#####TC62210 and TCB5E07
            
                        if siriState!=0:
                               oldSiriState=siriState
                               oldSiriTimeStamp=siriTimeStamp
                        if siriAction=="1 - Prewarm":
                            siriState=1
                            siriPrewarmCnt=siriPrewarmCnt+1
                            siriTimeStamp=timeStamp
                        if siriAction=="2 - ButtonDown":
                            siriState=2
                            siriDownCnt=siriDownCnt+1
                            siriTimeStamp=timeStamp
                        if siriAction=="3 - ButtonUp":
                            siriState=3
                            siriUpCnt=siriUpCnt+1
                            siriTimeStamp=timeStamp

                        if siriTest1==False:
                            if siriPrewarmCnt==1 and siriUpCnt==1 and siriDownCnt==0:
                                siriTest1=True
                        if siriTest1==True and siriTest2==False:
                            if siriPrewarmCnt==2 and siriUpCnt==1 and siriDownCnt==1: 
                                if siriTimeStamp-oldSiriTimeStamp<0.6 and siriTimeStamp-oldSiriTimeStamp>0.5:
                                    siriTest2=True
                                else:
                                    siriTest2=""
                                    #print("TS:",siriTimeStamp-oldSiriTimeStamp)
                        if (siriTest2==True or siriTest2=="") and siriTest3==False:
                            if siriPrewarmCnt==2 and siriUpCnt==2 and siriDownCnt==1:
                                siriTest3=True
                        if siriTest3==True and siriTest4==False:
                            if siriPrewarmCnt==2 and siriUpCnt==3 and siriDownCnt==2:
                                siriTest4=True

                        #print(siriPrewarmCnt)
                        #print(siriUpCnt)
                        #print(siriDownCnt)
                        
#####ChangeMode tests.

            if timeStamp>tC964FBEndTime and timeStamp<tC62210EndTime:  #tC26EBD
                if title=="Change Modes Command":
                    tC26EBD=False

            if timeStamp>tC31FE6EndTime and timeStamp<tC964FBEndTime:
                if title=="Change Modes Command":
                    tC0BB6F=False

            if timeStamp>tC0BCE9EndTime and timeStamp<tC31FE6EndTime:  #tC31FE6
                if title=="Change Modes Command":
                    cMResources= ((oG1Data [y]["Details"]["details"]["params"]["resources"][0]))
                    if (cMResources["borrowConstraint"])!= "100 - Anytime"  and tC31FE6==True:
                        tC31FE6=False
                        
                    if (cMResources["resourceID"])!= "1 - Main Screen" and tC31FE6==True:
                        tC31FE6=False
                    if (cMResources["takeConstraint"])!= "500 - User-Initiated" and tC31FE6==True:
                        tC31FE6=False
                    if (cMResources["transferPriority"])!= "500 - User-Initiated" and tC31FE6==True:
                        tC31FE6=False
                    if (cMResources["transferType"])!=  "1 - Take" and tC31FE6==True:
                        tC31FE6=False

                    #print ("tC31FE6 ",tC31FE6)
        y=y+1



fpsCalc=hidCount/(endHIDTime-startHIDTime)
if fpsCalc> 55 and fpsCalc< 65:
    oG1Pass= oG1Pass+ "4E15E "
else:
    oG1Fail= oG1Fail+ "4E15E "

if siriTest4==True and siriTest3==True and siriTest2==True and siriTest1==True:
    oG1Pass= oG1Pass+ "62210 B5E07 "    
else:
    oG1Fail= oG1Fail+ "62210 B5E07 "
    #print(siriTest1)
    #print(siriTest2)
    #print(siriTest3)
    #print(siriTest4)
    

if siriTest4==True and siriTest3==True and siriTest2==True and siriTest1==True and optGroup1Siri==True:
    oG1Pass= oG1Pass+ "6F99C "    
else:
    oG1Fail= oG1Fail+ "6F99C "

if tC19B1D ==True:
    oG1Pass= oG1Pass+ "19B1D "
else:
    oG1Fail= oG1Fail+ "19B1D "

if tCE5D68 ==True:
    oG1Pass= oG1Pass+ "E5D68 "
else:
    oG1Fail= oG1Fail+ "E5D68 "

if tC0BCE9 ==True:
    oG1Pass= oG1Pass+ "0BCE9 "
else:
    oG1Fail= oG1Fail+ "0BCE9 "

if tC964FB ==True:
    oG1Pass= oG1Pass+ "964FB "
else:
    oG1Fail= oG1Fail+ "964FB "

if tC823D0 ==True:
    oG1Pass= oG1Pass+ "823D0 "
else:
    oG1Fail= oG1Fail+ "823D0 "

if tC5FE06==True:
    oG1Pass= oG1Pass+ "5FE06 F05EA "
else:
    oG1Fail= oG1Fail+ "5FE06 F05EA "

if tC26EBD==True and optGroup1Siri==True:
    oG1Pass= oG1Pass+ "26EBD "
else:
    oG1Fail= oG1Fail+ "26EBD "

if tC31FE6==True:
    oG1Pass= oG1Pass+ "31FE6 "
else:
    oG1Fail= oG1Fail+ "31FE6 "

if tC0BB6F==True:
    oG1Pass= oG1Pass+ "0BB6F "
else:
    oG1Fail= oG1Fail+ "0BB6F "

#print(oG1Pass)
#print(oG1Fail)

