import json
import time
import datetime
from SyncTimeGet import *  #Intentional import all


y=0 #Just acts as a counter for JSON file parsing
tC4AF72=True
infoResponseCnt=0
infoResponseCnt1=0
tCD05C2=True
tCC6485=True
tCC6485TimeStamp=0
tCC6485Cnt=0
tCC6485Cnt1=0
oG2Pass="oG2Pass: "
oG2Fail="oG2Fail: "


oPtGroup2Data=(dataIn["optGroup2"])
#print ((dataIn["optGroup2"]))
oG2StartTime=((oPtGroup2Data["oG2StartTime"])-startTime)+timeOffset
tCC6485Time1=((oPtGroup2Data["tCC6485Time1"])-startTime)+timeOffset
tCC6485Time2=((oPtGroup2Data["tCC6485Time2"])-startTime)+timeOffset
tCC6485Time3=((oPtGroup2Data["tCC6485Time3"])-startTime)+timeOffset
tC4AF72Time1=((oPtGroup2Data["tC4AF72Time1"])-startTime)+timeOffset
tC4AF72Time2=((oPtGroup2Data["tC4AF72Time2"])-startTime)+timeOffset
tC4AF72Time3=((oPtGroup2Data["tC4AF72Time3"])-startTime)+timeOffset
tCD05C2Time1=((oPtGroup2Data["tCD05C2Time1"])-startTime)+timeOffset
tCD05C2Time2=((oPtGroup2Data["tCD05C2Time2"])-startTime)+timeOffset
tCD05C2Time3=((oPtGroup2Data["tCD05C2Time3"])-startTime)+timeOffset
tC0BB6FTime1=((oPtGroup2Data["tC0BB6FTime1"])-startTime)+timeOffset
tCC6485Correct=(oPtGroup2Data["tCC6485Correct"])
oG2EndTime=((oPtGroup2Data["oG2EndTime"])-startTime)+timeOffset
tC4AF72_9= (oPtGroup2Data["tC4AF72_9"])

if tC4AF72_9!=True: #imported result
    tC4AF72=False

#print("tCC6485Time1:",tCC6485Time1)
#print("tCC6485Time2:",tCC6485Time2)
#print("tCC6485Time3:",tCC6485Time3)
#print("tC0BB6FTime1:",tC0BB6FTime1)
#print("oG2StartTime:",oG2StartTime)

with open("CarPlay Session.json", "r", encoding="utf8") as file2: #Apple uses the utf8 encoding for json
    oG2Data=json.load(file2)

    for key in oG2Data:
        
        
        if "Timestamp" in (oG2Data[y]):
            timeStamp2=((oG2Data [y]["Timestamp"])/1000000000)
        if "Details" in (oG2Data[y]):
            Details2=(oG2Data [y]["Details"])
            if "details" in (oG2Data [y]["Details"]):
                details2=(oG2Data [y]["Details"]["details"])
        
        if "Title" in (oG2Data[y]):
            title2=(oG2Data [y]["Title"])
            


#####tC4AF72#####tC4AF72#####tC4AF72#####tC4AF72#####tC4AF72#####tC4AF72

            if title2 == "Info Response" and infoResponseCnt==0:
                infoResponseCnt=infoResponseCnt+1
                if(details2["limitedUI"])==False:
                    tC4AF72_4=True
                else:
                    tC4AF72_4=False
                    tC4AF72=False
                if (details2["limitedUIElements"])== ["softKeyboard", "softPhoneKeypad"]:
                    tC4AF72_5=True
                else:
                    tC4AF72_5=False
                    tC4AF72=False

            elif title2 == "Info Response" and infoResponseCnt==1:  #all tests are "elif" to run faster
                infoResponseCnt=infoResponseCnt+1
                #print ((details2["limitedUI"]))
                if(details2["limitedUI"])==True:
                    tC4AF72_12=True
                else:
                    tC4AF72_12=False
                    tC4AF72=False

            elif title2 == "Set Limited UI Command" and timeStamp2>tCC6485Time3 and timeStamp2<tCD05C2Time1+5:
                if(details2["params"]["limitedUI"])==True:
                    tC4AF72_8=True
                else:
                    tC4AF72_8=False
                    tC4AF72=False

            

            elif title2 == "Set Limited UI Command" and timeStamp2>tC4AF72Time2 and timeStamp2<tCD05C2Time3:
                if(details2["params"]["limitedUI"])==False:
                    tC4AF72_16=True
                else:
                    tC4AF72_16=False
                    tC4AF72=False

#####tC4AF72

#####tCD05C2#####tCD05C2#####tCD05C2#####tCD05C2#####tCD05C2#####tCD05C2

            elif title2 == "Info Response" and infoResponseCnt1==0:
                infoResponseCnt1=infoResponseCnt1+1
                if(details2["nightMode"])==False:
                    tCD05C2_4=True
                else:
                    tCD05C2_4=False
                    tCD05C2=False

            elif title2 == "Info Response" and infoResponseCnt1==1:
                infoResponseCnt1=infoResponseCnt1+1
                #print ((details2["limitedUI"]))
                if(details2["nightMode"])==True:
                    tCD05C2_9=True
                else:
                    tCD05C2_9=False
                    tCD05C2=False

            elif title2 == "Set Night Mode Cmmand" and timeStamp2>tC4AF72Time1 and timeStamp2<tCD05C2Time1+5:
                if(details2["params"]["nightMode"])==True:
                    tCD05C2_6=True
                else:
                    tCD05C2_6=False
                    tCD05C2=False

            

            elif title2 == "Set Limited UI Command" and timeStamp2>tC4AF72Time3 and timeStamp2<tC0BB6FTime1:
                if(details2["params"]["limitedUI"])==False:
                    tCD05C2_11=True
                else:
                    tCD05C2_11=False
                    tCD05C2=False
#####tCD05C2

#####tCC6485#####tCC6485#####tCC6485#####tCC6485#####tCC6485#####tCC6485

            elif title2 =="Change Modes Command" and timeStamp2>oG2StartTime and timeStamp2<tCC6485Time1 and tCC6485TimeStamp==0:
                resourcesCMC=(details2["params"]["resources"][0])
                #print ("AA")

                tCC6485TimeStamp=tCC6485TimeStamp+1
                
                for i in  resourcesCMC.values():

                    if i=="500 - User-Initiated":
                        tCC6485Cnt=tCC6485Cnt+1
                    elif i=="3 - Borrow":
                        tCC6485Cnt=tCC6485Cnt+10
                    elif i=="1 - Main Screen":
                        tCC6485Cnt=tCC6485Cnt+100
                         
                if tCC6485Cnt==112:
                    tCC6485_4a=True
                else:
                    tCC6485_4a=False
                    tCC6485=False
                    print ("A")
                

            elif title2 =="Change Modes Command" and timeStamp2>oG2StartTime and timeStamp2<tCC6485Time1 and tCC6485TimeStamp==1:
                resourcesCMC=(details2["params"]["resources"][0])
                tCC6485TimeStamp=tCC6485TimeStamp+1
                tCC6485Cnt=0
                #print ("BB")
                
                for i in  resourcesCMC.values():

                    if i=="1 - Main Screen":
                        tCC6485Cnt=tCC6485Cnt+100
                    elif i=="4 - Unborrow":
                        tCC6485Cnt=tCC6485Cnt+1000
                        
                if tCC6485Cnt==1100:
                    tCC6485_4b=True
                else:
                    tCC6485_4b=False
                    tCC6485=False
                    print ("b", tCC6485Cnt)
                

            elif title2 =="Change Modes Command" and timeStamp2>tCC6485Time1 and timeStamp2<tC0BB6FTime1 and tCC6485TimeStamp==2:
                resourcesCMC=(details2["params"]["resources"][0])
                tCC6485TimeStamp=tCC6485TimeStamp+1
                tCC6485Cnt=0
                #print ("CC")

                for i in  resourcesCMC.values():

                    if i=="500 - User-Initiated":
                        tCC6485Cnt=tCC6485Cnt+1
                    elif i=="3 - Borrow":
                        tCC6485Cnt=tCC6485Cnt+10
                    elif i=="1 - Main Screen":
                        tCC6485Cnt=tCC6485Cnt+100
                         
                if tCC6485Cnt==112:
                    tCC6485_4c=True
                else:
                    tCC6485_4c=False
                    tCC6485=False
                    print ("c",tCC6485Cnt)
                    
                    

            elif title2 =="Change Modes Command" and timeStamp2>tCC6485Time1 and timeStamp2<tC0BB6FTime1 and tCC6485TimeStamp==3:
                resourcesCMC=(details2["params"]["resources"][0])
                tCC6485TimeStamp=tCC6485TimeStamp+1
                tCC6485Cnt=0
                #print ("DD")
                
                for i in  resourcesCMC.values():

                    if i=="1 - Main Screen":
                        tCC6485Cnt=tCC6485Cnt+100
                    elif i=="4 - Unborrow":
                        tCC6485Cnt=tCC6485Cnt+1000
                        
                if tCC6485Cnt==1100:
                    tCC6485_4d=True
                else:
                    tCC6485_4d=False
                    tCC6485=False
                    print ("D", tCC6485Cnt)
                tCC6485Cnt==0
                   

        y=y+1

            


#print("tC4AF72:",tC4AF72)
#print("tCD05C2:",tCD05C2)
#print("tCC6485:",tCC6485)

if tC4AF72 ==True:
    oG2Pass= oG2Pass+ "4AF72 "
else:
    oG2Fail= oG2Fail+ "4AF72 "

if tCD05C2 ==True:
    oG2Pass= oG2Pass+ "D05C2 "
else:
    oG2Fail= oG2Fail+ "D05C2 "

if tCC6485 ==True and tCC6485Correct==True:
    oG2Pass= oG2Pass+ "C6485 "
else:
    oG2Fail= oG2Fail+ "C6485 "





#print(oG2Pass)
#print(oG2Fail)
            
