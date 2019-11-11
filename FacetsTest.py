


import json
import time
import datetime
import os



#Variables for CarPlay Session.json parsing

y=0
errorCount=0
z=0
w=0
timeStamp1=0
timeStamp2=0


tCF8326_2=""
tCF8326_3=True
tCF8326_4=True
tCF8326_5=True
tCF8326_6=True
tCF8326_7=True
tC3C105_3=""
tC3C105_4=False
tC9619Ca=False
tC9619Cb=False
tC9619Cc=False
tC9619Cd=False
tC9619Ce=False
tC9619Cf=False
tC9619Cg=False
tC9619Ch=False
tC9619Ci=False
tC9619Cj=False
tC9619Ck=False
tC9619Cl=False
tC9619Cm=False
tC9619Cn=False
tC9619Co=False
tC9619Cp=False
tC5F282_3=""
tC5F282_4=False
tC5F282_7=""
tC306B2a=False
tC306B2b=""
tCB66A0_3=False
tCB66A0_4=False
tCB66A0_5=""
tC80B49=False
tC62C2F=False
tC62C2Fa=0
tCFAE9C_4=False
tCFAE9C_5=""
tCFAE9C_6=True
tC9ADAE=True
tC4F8E0=False
tC964FB_4=False
baseTestPass="baseTestPass: "
baseTestFail="baseTestFail: "


tC4E15E=""
maxFPS=0





#####Version information block
print("\nThis test is set up for the following:")
print("Intended IVI: 2020 Indian HW 7in with CarPlay")
print("ATS version: ATS 7.0")
print("Facets version: Facets 2.3.1")
print("Covered Test Cases: 306B2,3C105,4C0D8,4F8E0,5F282,62C2F,80B49,9619C,9ADAE,B66A0,F8326,FAE9C")
print("Covered Test Cases: 0BE0D,37320,39935,67EFB,A3C1D,A568C,C3941,EC29F,EEFF1")
print("Covered Test Cases: 20E9D")
print("\nOptional Test Cases: 4E15E,964FB,0BCE9")

input("\n>>>> Press 'ENTER' to continue.")

########################################################################
# There are two sections to this test. The first one is done while the #
# ATS data is being recorded, the second after the ATS data has been   #
# ported over to the proper location for analysis. Test cases are      #                   
# listed as appropriate for each location.                             #
########################################################################



dateTime=datetime.datetime.now()
dDateTime=(dateTime.strftime("%d"))
bDateTime=(dateTime.strftime("%b"))
yDateTime=(dateTime.strftime("%y"))
tDateTime=dDateTime+bDateTime+yDateTime

jsonIn=tDateTime+"Data.json"

with open(jsonIn, "r") as dataIn:

    dataIn=json.load(dataIn)

#print (dataIn)

fixedData=(dataIn["fixed"][0])

#input ("JJ")

#tC3C105_3=(fixedData["tC3C105_3"])
endTime=(fixedData["endTime"])
startTime=(fixedData["startTime"])
tCFAE9C_5=(fixedData["tCFAE9C_5"])
tCB66A0_5=(fixedData["tCB66A0_5"])
#runTC4E15E=(fixedData["runTC4E15E"])
syncTime=(fixedData["syncTime"])

if "tC4E15E" in dataIn:
    runTC4E15E=True
else:
    runTC4E15E=False

if "tC964FB" in dataIn:
    runTC964FB=True
else:
    runTC964FB=False


    

#print(tC3C105_3, endTime, startTime, tCFAE9C_5, tCB66A0_5, runTC4E15E, syncTime)


#input ("HI")


#********************************************************************************************************************************
#CarPlay Session CarPlay Session CarPlay Session CarPlay Session CarPlay Session CarPlay Session CarPlay Session CarPlay Session*
#CarPlay Session CarPlay Session CarPlay Session CarPlay Session CarPlay Session CarPlay Session CarPlay Session CarPlay Session*
#********************************************************************************************************************************


with open("CarPlay Session.json", "r", encoding="utf8") as timeFile: #Apple uses the utf8 encoding for json
    timeData=json.load(timeFile)

    timeSyncFound=False
    for key in timeData:
        if "Timestamp" in (timeData[y]):
            timeStamp=((timeData [y]["Timestamp"])/1000000000)
        
        if "Title" in (timeData[y]):
            title=(timeData [y]["Title"])
            if title=="Request Siri Command" and timeStamp >60 and timeSyncFound==False:
                timeSyncFound=True
                aTSSyncTime=timeStamp
                print ("aTSSyncTime:",aTSSyncTime)
                syncTime=(syncTime-startTime)
                print ("syncTime:",syncTime)
                timeOffset=aTSSyncTime-syncTime
                print ("Time Offset:" ,timeOffset)
        y=y+1

#input ("HI")

y=0

with open("CarPlay Session.json", "r", encoding="utf8") as file: #Apple uses the utf8 encoding for json
    data=json.load(file)

    for key in data:
        if "Status" in (data[y]):
            if (data[y]["Status"])=="Error":
                #print ("\n\nCarPlay ERROR!!!\n",(data [y]),"\n\n")
                errorCount=errorCount+1
        
        if "Timestamp" in (data[y]):
            timeStamp=((data [y]["Timestamp"])/1000000000)
        
        if "Title" in (data[y]):
            title=(data [y]["Title"])


        
        




########TCB66A0########TCB66A0########TCB66A0########TCB66A0########TCB66A0########TCB66A0########TCB66A0########TCB66A0########TCB66A0

            if "carplay-ctrl._tcp.local" in title and timeStamp1==0:
                timeStamp1=timeStamp
                #print (timeStamp1)
    
            if title == "Auth Setup Request" and timeStamp2==0:
                timeStamp2=timeStamp
                #print (timeStamp2)

            if timeStamp1>0 and timeStamp2>0:
                if timeStamp2-timeStamp1>0:
                    tC62C2F=True
                #print ("Pass")    
########TCB66A0

########TCFAE9C########TCFAE9C########TCFAE9C########TCFAE9C########TCFAE9C########TCFAE9C########TCFAE9C########TCFAE9C########TCFAE9C
#Part 1
            if title =="Change Modes Command" and timeStamp< 59.999999999:  #(59.99999999 seconds)
                print ("TCFAE9C_6 and TC9ADAE ERROR at raw Timestamp", timeStamp, "\n\n")
                tCFAE9C_6=False
            if title =="Request UI Command" and timeStamp< 59.999999999:  #(59.99999999 seconds)
                tCFAE9C_6=False
                print ("TCFAE9C_6 and TC9ADAE ERROR at raw Timestamp", timeStamp, "\n\n")
########TCFAE9C

########TC9ADAE########TC9ADAE########TC9ADAE########TC9ADAE########TC9ADAE########TC9ADAE########TC9ADAE########TC9ADAE########TC9ADAE
                
            if title =="HID Send Report Command" and timeStamp< 59.999999999:  #(59.99999999 seconds)
                print ("tC9ADAE ERROR at raw Timestamp", timeStamp, "\n\n")
                tC9ADAE=False
########TC9ADAE


#vvvvvv Info Response section vvvvvv#
                
            if title == "Info Response" and timeStamp< 59.999999999 : 
                #print ("Title")
                details=(data[y]["Details"]["details"])
                tSF=(data[y]["Timestamp Formatted"])###<<<<<<<<<   tSF
                tSRaw=(data[y]["Timestamp"])###<<<<<<<<<   tSRaw
                infoResponse=(data[y])
                audioFormats=(details["audioFormats"])
                audioLatencies= (details["audioLatencies"])
                #print (audioFormats)


########TC4F8E0########TC4F8E0########TC4F8E0########TC4F8E0########TC4F8E0########TC4F8E0########TC4F8E0########TC4F8E0########TC4F8E0
                displaysCnt=0
                displays=details["displays"][0]
                
                if "heightPhysical" in displays:
                    if displays["heightPhysical"]== 91:
                        displaysCnt=displaysCnt+1                    
                if "heightPixels" in displays:
                    if displays["heightPixels"]== 480:
                        displaysCnt=displaysCnt+10
                if "widthPhysical" in displays:
                    if displays["widthPhysical"]== 152:
                        displaysCnt=displaysCnt+100
                if "widthPixels" in displays:
                    if displays["widthPixels"]== 800:
                        displaysCnt=displaysCnt+1000
                if displaysCnt==1111:
                    tC4F8E0=True

                if "maxFPS" in displays:
                    maxFPS=displays["maxFPS"]
                                    
########TC4F8E0



########TCFAE9C########TCFAE9C########TCFAE9C########TCFAE9C########TCFAE9C########TCFAE9C########TCFAE9C########TCFAE9C########TCFAE9C
#Part 2
                appStateCnt=0
                appState0=(details["modes"]["appStates"][0])
                appState1=(details["modes"]["appStates"][1])
                appState2=(details["modes"]["appStates"][2])
                resources0=(details["modes"]["resources"][0])
                resources1=(details["modes"]["resources"][1])
                if appState0["appStateID"]=="2 - Phone Call" and appState0["state"]==False:
                    appStateCnt=appStateCnt+1
                    #print ("#1")
                if appState1["appStateID"]=="1 - Speech Operation" and appState1["speechMode"]=="-1 - None":
                    appStateCnt=appStateCnt+1
                    #print ("#2")
                if appState2["appStateID"]=="3 - Turn-by-Turn Navigation" and appState2["state"]==False:
                    appStateCnt=appStateCnt+1
                    #print ("#3")
                if resources0["borrowConstraint"]=="100 - Anytime" and resources0["resourceID"]=="1 - Main Screen" and resources0["takeConstraint"]=="100 - Anytime" and resources0["transferPriority"]== "100 - Nice-to-Have" and resources0["transferType"]== "1 - Take":
                    appStateCnt=appStateCnt+1
                    #print ("#4")
                if resources1["borrowConstraint"]=="100 - Anytime" and resources1["resourceID"]=="2 - Main Audio" and resources1["takeConstraint"]=="100 - Anytime" and resources1["transferPriority"]== "100 - Nice-to-Have" and resources1["transferType"]== "1 - Take":                
                    appStateCnt=appStateCnt+1
                    #print ("#5")
                if appStateCnt==5:
                    tCFAE9C_4=True
                    #print ("tCFAE9C_4=true")

########TCB66A0########TCB66A0########TCB66A0########TCB66A0########TCB66A0########TCB66A0########TCB66A0########TCB66A0########TCB66A0
                if details["oemIconVisible"]==True and (details["oemIcon (5349 bytes)"]) ==['<a 104x104 image was displayed>']:
                    tCB66A0_3=True
                    #print ("HA!!!!")
               
                if tCB66A0_3==True:
                    tCB66A0_3cnt=0
                    oemIcons=details["oemIcons"]
                    if oemIcons[0]["prerendered"]== True and oemIcons[0]["heightPixels"]==120 and oemIcons[0]["widthPixels"]==120:
                        tCB66A0_3cnt=tCB66A0_3cnt+1
                    if oemIcons[1]["prerendered"]== True and oemIcons[1]["heightPixels"]==180 and oemIcons[1]["widthPixels"]==180:
                        tCB66A0_3cnt=tCB66A0_3cnt+1
                    if oemIcons[2]["prerendered"]== True and oemIcons[2]["heightPixels"]==256 and oemIcons[2]["widthPixels"]==256:
                        tCB66A0_3cnt=tCB66A0_3cnt+1
                if tCB66A0_3==True and tCB66A0_3cnt==3:
                    tCB66A0_3=True
                    #print ("Yes")
                else:
                    tCB66A0_3=False
                    #print("No")

                if details["oemIconLabel"]== "Indian":
                    tCB66A0_4=True
                    #print ("Yes")
########TCB66A0
                
########TC80B49########TC80B49########TC80B49########TC80B49########TC80B49########TC80B49########TC80B49########TC80B49########TC80B49
                if details["rightHandDrive"]==False:
                    tC80B49=True
                
########TC80B49




########TC3C105########TC3C105########TC3C105########TC3C105########TC3C105########TC3C105########TC3C105########TC3C105########TC3C105
                
                tele=details["hidDevices"][2]["hidDescriptor"]
                if "(Hook Switch)" in tele and "(Drop)" in tele and "(Flash)" not in tele:
                    tC3C105=True         

########TC3C105



########TC4C0D8########TC4C0D8########TC4C0D8########TC4C0D8########TC4C0D8########TC4C0D8########TC4C0D8########TC4C0D8########TC4C0D8

                if details["displays"][0]["primaryInputDevice"]=="1 - Touchscreen":
                    tC4C0D8=True
                else:
                    tC4C0D8=True

########TC4C0D8
                    
########TC306B2########TC306B2########TC306B2########TC306B2########TC306B2########TC306B2########TC306B2########TC306B2########TC306B2

                bluetoothID= details["bluetoothIDs"]
                bluetoothID=str(bluetoothID)
                bluetoothID=bluetoothID.split(",")
                #print (bluetoothID[1])
                
                bluetoothID1=bluetoothID[0]
                bluetoothID1=bluetoothID1.replace(" ","")
                bluetoothID1=bluetoothID1.replace("[","")
                bluetoothID1=bluetoothID1.replace("]","")
                bluetoothID1=bluetoothID1.replace("'","")

                try:
                    bluetoothID2=bluetoothID[1]
                    bluetoothID2=bluetoothID2.replace(" ","")
                    bluetoothID2=bluetoothID2.replace("[","")
                    bluetoothID2=bluetoothID2.replace("]","")
                    bluetoothID2=bluetoothID2.replace("'","")

                except:
                    pass
                if bluetoothID1[:2]!= "00" and bluetoothID1[:2] != "11" and bluetoothID1[:2] != "01":
                    tC306B2a=True
                try:
                    if bluetoothID2[:2]!= "00" and bluetoothID2[:2] != "11" and bluetoothID2[:2] != "01":
                        tC306B2b=True
                        #print(bluetoothID2)
                except:
                    pass
########TC306B2



########TC5F282########TC5F282########TC5F282########TC5F282########TC5F282########TC5F282########TC5F282########TC5F282########TC5F282
                sourceVersion = details["sourceVersion"]
                print("\nsourceVersion:", sourceVersion )
                while tC5F282_3== "":
                    print ("\nVerify the sourceVersion is valid.")
                    tC5F282_3=input (">>>>Type 'y' or 'n' and press 'ENTER'.\n")
                    tC5F282_3=tC5F282_3.upper()
                    if tC5F282_3 == "Y" or tC5F282_3 == "N":
                        print("\n")
                    else:
                        tC5F282_3=""
                if tC5F282_3 == "Y":
                    tC5F282_3=True
                else:
                    tC5F282_3=False
                    
                    
                deviceID=details["deviceID"]
                
                if deviceID[:2] != "00" and deviceID[:2] != "11" and deviceID[:2] != "01":
                    tC5F282_5=True

                modelNumber = details["model"]
                while tC5F282_7== "":
                    print("\nModel number:",modelNumber)
                    print ("\nVerify the model number is correct.")
                    tC5F282_7=input (">>>>Type 'y' or 'n' and press 'ENTER'.\n")
                    tC5F282_7=tC5F282_7.upper()
                    if tC5F282_7 == "Y" or tC5F282_7 == "N":
                        print("\n")
                    else:
                        tC5F282_7=""
                if tC5F282_7 == "Y":
                    tC5F282_7=True
                else:
                    tC5F282_7=False

                statusFlags=details["statusFlags"]
                if statusFlags==4:
                    tC5F282_8=True
                else:
                    tC5F282_8=False
########TC5F282
                    


########TC9619C########TC9619C########TC9619C########TC9619C########TC9619C########TC9619C########TC9619C########TC9619C########TC9619C
                audLatCount=0
                for key in audioLatencies:
                    aLType= (audioLatencies[w]["type"])
                    aLAudType= (audioLatencies[w]["audioType"])

                    if aLType=="100 - Main Audio":
                        
                        if aLAudType=="compatibility":
                            audLatCount=audLatCount+1
                            if "inputLatencyMicros" in audioLatencies[w]:                                
                                if(audioLatencies[w]["inputLatencyMicros"])>0:
                                    tC9619Ca=True
                            if "outputLatencyMicros" in audioLatencies[w]:                                
                                if(audioLatencies[w]["outputLatencyMicros"])>0:
                                    tC9619Cb=True
                        if aLAudType=="alert":
                            audLatCount=audLatCount+1
                            if "inputLatencyMicros" not in audioLatencies[w]:                                
                                tC9619Cc=True
                            if "outputLatencyMicros" in audioLatencies[w]:                                
                                if(audioLatencies[w]["outputLatencyMicros"])>0:
                                    tC9619Cd=True
                        if aLAudType=="default":
                            audLatCount=audLatCount+1
                            if "inputLatencyMicros" in audioLatencies[w]:                                
                                if(audioLatencies[w]["inputLatencyMicros"])>0:
                                    tC9619Ce=True
                            if "outputLatencyMicros" in audioLatencies[w]:                                
                                if(audioLatencies[w]["outputLatencyMicros"])>0:
                                    tC9619Cf=True
                        if aLAudType=="media":
                            audLatCount=audLatCount+1
                            if "inputLatencyMicros" not in audioLatencies[w]:                                
                                tC9619Cg=True
                            if "outputLatencyMicros" in audioLatencies[w]:                                
                                if(audioLatencies[w]["outputLatencyMicros"])>0:
                                    tC9619Ch=True
                        if aLAudType=="telephony":
                            audLatCount=audLatCount+1
                            if "inputLatencyMicros" in audioLatencies[w]:                                
                                if(audioLatencies[w]["inputLatencyMicros"])>0:
                                    tC9619Ci=True
                            if "outputLatencyMicros" in audioLatencies[w]:                                
                                if(audioLatencies[w]["outputLatencyMicros"])>0:
                                    tC9619Cj=True
                        if aLAudType=="compatibility":
                            audLatCount=audLatCount+1
                            if "inputLatencyMicros" in audioLatencies[w]:                                
                                if(audioLatencies[w]["inputLatencyMicros"])>0:
                                    tC9619Ck=True
                            if "outputLatencyMicros" in audioLatencies[w]:                                
                                if(audioLatencies[w]["outputLatencyMicros"])>0:
                                    tC9619Cl=True

                    if aLType=="101 - Alternate Audio":
                        
                        if aLAudType=="compatibility":
                            audLatCount=audLatCount+1
                            if "inputLatencyMicros" not in audioLatencies[w]:                                
                                tC9619Cm=True
                            if "outputLatencyMicros" in audioLatencies[w]:                                
                                if(audioLatencies[w]["outputLatencyMicros"])>0:
                                    tC9619Cn=True
                        if aLAudType=="default":
                            audLatCount=audLatCount+1
                            if "inputLatencyMicros" not in audioLatencies[w]:                                
                                tC9619Co=True
                            if "outputLatencyMicros" in audioLatencies[w]:                                
                                if(audioLatencies[w]["outputLatencyMicros"])>0:
                                    tC9619Cp=True


                    

                    w=w+1
                if audLatCount==8:
                    tC9619Cq=True
                else:
                    tC9619Cq=False
########TC9619C

########TCF8326########TCF8326########TCF8326########TCF8326########TCF8326########TCF8326########TCF8326########TCF8326########TCF8326
                for key in audioFormats:
                    
                    aFType=(audioFormats[z]["type"])###<<<<<<<<<    aFType
                    aFAudType=(audioFormats[z]["audioType"])###<<<<<<<<<    aFAudType
                    #print("")
                    


                    if aFAudType=="compatibility":
                        if aFType=="100 - Main Audio":
                            passCounter=0
                            if "bit 2" in (audioFormats[z]["audioInputFormats - 0x54"]):
                                passCounter=passCounter+1
                                if (audioFormats[z]["audioInputFormats - 0x54"]["bit 2"])=="PCM, 8000 Hz, 16-Bit, Mono":
                                    passCounter=passCounter+1
                            if "bit 4" in (audioFormats[z]["audioInputFormats - 0x54"]):
                                passCounter=passCounter+10
                                if (audioFormats[z]["audioInputFormats - 0x54"]["bit 4"])=="PCM, 16000 Hz, 16-Bit, Mono":
                                        passCounter=passCounter+10
                            if "bit 6" in (audioFormats[z]["audioInputFormats - 0x54"]):
                                passCounter=passCounter+100
                                if (audioFormats[z]["audioInputFormats - 0x54"]["bit 6"])=="PCM, 24000 Hz, 16-Bit, Mono":
                                    passCounter=passCounter+100

                            if "bit 2" in (audioFormats[z]["audioOutputFormats - 0x8054"]):
                                passCounter=passCounter+1000
                                if (audioFormats[z]["audioOutputFormats - 0x8054"]["bit 2"])=="PCM, 8000 Hz, 16-Bit, Mono":
                                    passCounter=passCounter+1000
                            if "bit 4" in (audioFormats[z]["audioOutputFormats - 0x8054"]):
                                passCounter=passCounter+10000
                                if (audioFormats[z]["audioOutputFormats - 0x8054"]["bit 4"])=="PCM, 16000 Hz, 16-Bit, Mono":
                                    passCounter=passCounter+10000
                            if "bit 6" in (audioFormats[z]["audioOutputFormats - 0x8054"]):
                                passCounter=passCounter+100000                                
                                if (audioFormats[z]["audioOutputFormats - 0x8054"]["bit 6"])=="PCM, 24000 Hz, 16-Bit, Mono":
                                    passCounter=passCounter+100000
                            if "bit 15" in (audioFormats[z]["audioOutputFormats - 0x8054"]):
                                passCounter=passCounter+1000000
                                if (audioFormats[z]["audioOutputFormats - 0x8054"]["bit 15"])=="PCM, 48000 Hz, 16-Bit, Stereo":
                                    passCounter=passCounter+1000000                     
                            
                            #print (passCounter)
                            if passCounter==2222222:
                                tCF8326_2a=True
                            else:
                                tCF8326_2a=False
                        if aFType=="101 - Alternate Audio":
                            passCounter=0
                            
                            if "bit 15" in (audioFormats[z]["audioOutputFormats - 0x8000"]):
                                passCounter=passCounter+1
                                if (audioFormats[z]["audioOutputFormats - 0x8000"]["bit 15"])=="PCM, 48000 Hz, 16-Bit, Stereo":
                                    passCounter=passCounter+1
                                if(len(audioFormats[z]["audioOutputFormats - 0x8000"]))!=1:
                                    passCounter=passCounter-10
                            if(len(audioFormats[z]))!=3:
                                passCounter=passCounter-100
                            
                            #print (passCounter)
                            if passCounter==2:
                                tCF8326_2b=True
                            else:
                                tCF8326_2b=False
                        
                            

                    if aFType=="101 - Alternate Audio":
                        if aFAudType != "compatibility":
                            if aFAudType != "default":
                                tCF8326_3=False
                        aOFCounter=0
                        aOF=(audioFormats[z]["audioOutputFormats - 0x8000"])
                            
                        if "bit 2" in aOF:
                            if (aOF["bit 2"])!= "PCM, 8000 Hz, 16-Bit, Mono":
                                tCF8326_7=False
                            aOFCounter=aOFCounter+1
                        if "bit 4" in aOF:
                            if (aOF["bit 4"])!= "PCM, 16000 Hz, 16-Bit, Mono":
                                tCF8326_7=False
                            aOFCounter=aOFCounter+1
                        if "bit 6" in aOF:
                            if (aOF["bit 6"])!= "PCM, 24000 Hz, 16-Bit, Mono":
                                tCF8326_7=False
                            aOFCounter=aOFCounter+1
                        if "bit 15" in aOF:
                            if (aOF["bit 15"])!= "PCM, 48000 Hz, 16-Bit, Stereo":
                                tCF8326_7=False
                            aOFCounter=aOFCounter+1
                            
                        
                        if(len(audioFormats[z]))==3 and aOFCounter>0 and tCF8326_4!=False:
                            tCF8326_4=True
                        else:
                            tCF8326_4=False

                    
                    if aFAudType == "media" or aFAudType == "alert":
                        aOFCounter=0
                        aOF=(audioFormats[z]["audioOutputFormats - 0x8000"])
                        
                        if "bit 2" in aOF:
                            if (aOF["bit 2"])!= "PCM, 8000 Hz, 16-Bit, Mono":
                                tCF8326_7=False
                            aOFCounter=aOFCounter+1
                        if "bit 4" in aOF:
                            if (aOF["bit 4"])!= "PCM, 16000 Hz, 16-Bit, Mono":
                                tCF8326_7=False
                            aOFCounter=aOFCounter+1
                        if "bit 6" in aOF:
                            if (aOF["bit 6"])!= "PCM, 24000 Hz, 16-Bit, Mono":
                                tCF8326_7=False
                            aOFCounter=aOFCounter+1
                        if "bit 15" in aOF:
                            if (aOF["bit 15"])!= "PCM, 48000 Hz, 16-Bit, Stereo":
                                tCF8326_7=False
                            aOFCounter=aOFCounter+1
                            
                        
                        if(len(audioFormats[z]))==3 and aOFCounter>0 and tCF8326_4!=False:
                            tCF8326_5=True
                            #print (aOFCounter)
                        else:
                            tCF8326_5=False

                    if aFType=="100 - Main Audio":
                        aOFCounter=0
                        if aFAudType == "speechRecognition" or aFAudType == "telephony" or aFAudType == "default":
                            if aFAudType == "default":
                                aOF=(audioFormats[z]["audioOutputFormats - 0x50"])
                                aIF=(audioFormats[z]["audioInputFormats - 0x50"])
                                #print ("Default")
                            if aFAudType == "telephony":
                                aOF=(audioFormats[z]["audioOutputFormats - 0x54"])
                                aIF=(audioFormats[z]["audioInputFormats - 0x54"])
                                #print ("telephony")
                            if aFAudType == "speechRecognition":
                                aOF=(audioFormats[z]["audioOutputFormats - 0x44"])
                                aIF=(audioFormats[z]["audioInputFormats - 0x44"])
                                #print ("speechRecognition")


                                
                            
                            if "bit 2" in aIF:
                                if (aIF["bit 2"])!= "PCM, 8000 Hz, 16-Bit, Mono":
                                    tCF8326_7=False
                                aOFCounter=aOFCounter+1
                            if "bit 4" in aIF:
                                if (aIF["bit 4"])!= "PCM, 16000 Hz, 16-Bit, Mono":
                                    tCF8326_7=False
                                aOFCounter=aOFCounter+1
                            if "bit 6" in aIF:
                                if (aIF["bit 6"])!= "PCM, 24000 Hz, 16-Bit, Mono":
                                    tCF8326_7=False
                                aOFCounter=aOFCounter+1

                            if "bit 2" in aOF:
                                if (aOF["bit 2"])!= "PCM, 8000 Hz, 16-Bit, Mono":
                                    tCF8326_7=False
                                aOFCounter=aOFCounter+1
                            if "bit 4" in aOF:
                                if (aOF["bit 4"])!= "PCM, 16000 Hz, 16-Bit, Mono":
                                    tCF8326_7=False
                                aOFCounter=aOFCounter+1
                            if "bit 6" in aOF:
                                if (aOF["bit 6"])!= "PCM, 24000 Hz, 16-Bit, Mono":
                                    tCF8326_7=False
                                aOFCounter=aOFCounter+1
                            if "bit 15" in aOF:
                                if (aOF["bit 15"])!= "PCM, 48000 Hz, 16-Bit, Stereo":
                                    tCF8326_7=False
                                aOFCounter=aOFCounter+1
                            #print (aOFCounter)
                            
                        
                            if(len(audioFormats[z]))==4 and aOFCounter>0 and tCF8326_6!=False:
                                tCF8326_6=True
                            else:
                                #print ("LEN: ",(len(audioFormats[z])))
                                tCF8326_6=False

                    z=z+1    
########TCF8326                                        

#    !!!END CARPLAY SESSION TEST SECTION                        
        y=y+1 # Must be last line of CarPlay Session Test Section, 2 tabs in. 
#    !!!END CARPLAY SESSION TEST SECTION    END CARPLAY SESSION TEST SECTION    END CARPLAY SESSION TEST SECTION    END CARPLAY SESSION TEST SECTION




#****************************************************************************************************************************************
#Begin Optional Test Cases Section Begin Optional Test Cases Section Begin Optional Test Cases Section Begin Optional Test Cases Section*
#Begin Optional Test Cases Section Begin Optional Test Cases Section Begin Optional Test Cases Section Begin Optional Test Cases Section* 
#****************************************************************************************************************************************







        
          

########TC964FB               ########TC964FB               ########TC964FB               ########TC964FB               ########TC964FB               
               ########TC0BCE9               ########TC0BCE9               ########TC0BCE9               ########TC0BCE9               ########TC0BCE9
if "tC964FB" in dataIn:
    runTC964FB=True
    print("tC964FB == Y")
    hidCount=-1
    y=0
    yy=y+1
    yyy=y+3
    startHIDTime=0
    endHIDTime=0
    opData=(dataIn["tC964FB"])
    wheel1=0
    wheeln1=0
    wheel0=0
    button1=False
    touch1=False
    acBack=False
    hookSwitch=False
    drop=False
    playPause=False
    scanNT=False
    scanPT=False
    hIDError=1
    startTest=0
    

    tC964FBStartTime=(opData["tC964FBStartTime"])-startTime
    tC964FBEndTime=(opData["tC964FBEndTime"])-startTime
    tC964FBStartTime=tC964FBStartTime+timeOffset
    tC964FBEndTime=tC964FBEndTime+timeOffset
    #print("tC964FBStartTime:",tC964FBStartTime)
    #print ("tC964FBEndTime:",tC964FBEndTime)
    
    

    with open("CarPlay Session.json", "r", encoding="utf8") as dfile: #Apple uses the utf8 encoding for json
        xdata=json.load(dfile)
       
        for key in xdata:
            if "Timestamp" in (xdata[y]):
                timeStamp=((xdata [y]["Timestamp"])/1000000000)
                timeStampRaw=(xdata [y]["Timestamp"])
                
        
            if "Title" in (xdata[y]):
                title=(xdata [y]["Title"])
                

                if title=="HID Send Report Command":
                    #print ("\n    >>>>",timeStamp)
                    #print(xdata[y]["Details"]["details"]["hidReport"])
                    if "hidReport" in (xdata[y]["Details"]["details"])and timeStamp>(tC964FBStartTime-15)and button1==False:
                        hidReport=(xdata[y]["Details"]["details"]["hidReport"])
                        #print (timeStamp)
                        
                        if "Wheel: 1" in hidReport:
                            wheel1=wheel1+1
                        if "Wheel: -1" in hidReport:
                            wheeln1=wheeln1+1
                        #if "Wheel: 0" in hidReport:
                            #wheel0=wheel0+1
                        if "Button 1: 1" in hidReport:
                            button1=1
                        elif "Wheel: 0" in hidReport:
                            wheel0=wheel0+1

                    if "hidReport" in (xdata[y]["Details"]["details"])and button1!=False and hIDError==1:
                        hidReport=(xdata[y]["Details"]["details"]["hidReport"])

                        if "Button 1: 1" in hidReport:
                            button1=True
                        if "Touch: 1" in hidReport:
                            touch1=True
                        if "AC Back: 1" in hidReport:
                            acBack=True
                        if "Hook Switch: 1" in hidReport:
                            hookSwitch=True
                        if "Drop: 1" in hidReport:
                            drop=True
                        if "Play/Pause: 1" in hidReport:
                            #print (hidReport)
                            playPause=True
                        if "Scan Next Track: 1" in hidReport:
                            scanNT=True
                        if "Scan Previous Track: 1" in hidReport:                            
                            scanPT=True
                        if "Wheel: 1" in hidReport or "Wheel: -1" in hidReport:
                            hIDError=False
                            startTest=timeStamp+3
                            #print ("startTest:",startTest)

                    if "HID Send Report Command" in title and timeStamp>90 and hIDError==False :
                        print ("    hIDError at:",timeStampRaw)
                        print ((xdata[y]["Details"]["details"]))
                        print("")
                        hIDError=True                            
                        
                        
                        
            y=y+1

        
        
        print ("wheel1:", wheel1)
        print ("wheeln1:", wheeln1)
        print ("wheel0:", wheel0)
        print("Button 1:",button1)                        
        print("Touch:",touch1)
        print("AC Back:",acBack)
        print("Hook Switch:",hookSwitch)
        print("Drop:",drop)
        print("Play/Pause:",playPause)
        print("Scan Next Track:",scanNT)
        print("Scan Previous Track:",scanPT)
        print("hIDError:",hIDError)
        
        
        if wheel1==2 and wheeln1==2 and wheel0==4:
            tC964FB=True
        else:
            tC964FB=False

        if tC964FB==True and button1==True and acBack==True and hookSwitch==True and drop==True and playPause==True and scanNT==True and scanPT==True and hIDError==False:
            tC0BCE9=True
        else:
            tC0BCE9=False

            
########TC964FB
               ########TC0BCE9

#*********************************************************************************************************************************************
#iAP2 Control SessioniAP2 Control SessioniAP2 Control SessioniAP2 Control SessioniAP2 Control SessioniAP2 Control SessioniAP2 Control Session*
#iAP2 Control SessioniAP2 Control SessioniAP2 Control SessioniAP2 Control SessioniAP2 Control SessioniAP2 Control SessioniAP2 Control Session*
#*********************************************************************************************************************************************




                                                                                                                            
#Variables for iAP2 Control Session.json parsing
sCFD=1000  ########>>>>>>>>This is the amount of charging current available to iPhone. SHOULD BE 1000!
v=0
iiFound=0
iAPErrorCount=0
tcA3C1D=0
title=""
details=""
pModel=""
pName=""
pMan=""
pSN=""
pFWV=""
pHWV=""
pPPUUID=""
mAMRNL=""
vICompDisName=""
mAMRNL=""
mCRNL=""
mDNL=""
mGMC=""
mMDL=""
tCIdentifier=""
vICompIdent=""

sPU= False
stopPU=False
vICompEngineType=""
uHTCPIN=""#for TC 20E9D, USB Transfers traffic
aCFD=""
bCI=""
aCFDAfterAuth=""



tcA568C=True
tc39935=True
tcEEFF1=True
tcC3941_4=False
tcC3941_5=False
tcEC29F=True

tcA3C1D=True
tc67EFB=0
tc37320=True
tc0BE0D=True

u=0
tC20E9D_3=False
tC20E9D_6=True
tC20E9D_7=False
tC20E9D_10=False
uSBTranBIN=""


with open("iAP2 Control Session.json", "r") as file: #Apple uses the utf8 encoding for json
    data=json.load(file)

    for key in data:

        if "Title" in (data[v]):
            title=(data [v]["Title"])
        if "Details" in (data[v]):
            details=(data[v]["Details"])

        if (data [v]["Status"])== "Error" and (data [v]["Source"])== "--":
            print ("")
            print ("         !!!ERROR NOTIFICATION FOUND!!!")
            print (title)
            print ("Timestamp: ", data [v]["Timestamp Formatted"])
            print ("")
            print (details)
            print ("")
            iAPErrorCount=iAPErrorCount+1

        
        if "Error" in details:
            print ("")
            print ("         !!!ERROR NOTIFICATION FOUND!!!")
            print (data [v]["Title"])
            print ("Timestamp: ", data [v]["Timestamp Formatted"])
            print ("")
            print (details["Error"])
            print ("")
            iAPErrorCount=iAPErrorCount+1
        
        if title== "AccessoryHIDReport" and (data [v]["Timestamp"])< 60000000000:
            tcA3C1D=False
        
        if title== "IdentificationInformation" and iiFound==0:
            iiFound=iiFound+1
            if "Parameters" in details:
                parameters= (details["Parameters"])
                
                if "MessagesReceivedFromDevice (ID 7, uint16[])" in parameters:
                    pMRFD=(parameters["MessagesReceivedFromDevice (ID 7, uint16[])"])
                if "MessagesSentByAccessory (ID 6, uint16[])" in parameters:
                    pMSBA=(parameters["MessagesSentByAccessory (ID 6, uint16[])"])
                if "ModelIdentifier" in parameters:
                    pModel=(parameters["ModelIdentifier"])
                if "Name" in parameters:
                    pName=(parameters["Name"])               
                if "Manufacturer" in parameters:
                    pMan=(parameters["Manufacturer"])               
                if "SerialNumber" in parameters:
                    pSN=(parameters["SerialNumber"])   
                if "FirmwareVersion" in parameters:
                    pFWV=(parameters["FirmwareVersion"])
                if "HardwareVersion" in parameters:
                    pHWV=(parameters["HardwareVersion"])
                if "ProductPlanUUID" in parameters:
                    pPPUUID=(parameters["ProductPlanUUID"])

                if "VehicleInformationComponent (ID 20, group)" in parameters:
                    vIComp= parameters["VehicleInformationComponent (ID 20, group)"]
                    if "DisplayName" in vIComp:
                        vICompDisName=(vIComp["DisplayName"])
                    if "Identifier" in vIComp:
                        vICompIdent=(vIComp["Identifier"])
                    if "EngineType"in vIComp:
                        vICompEngineType=(vIComp["EngineType"])
                    

                if "RouteGuidanceDisplayComponent (ID 30, group)" in parameters:
                    rGDC=(parameters["RouteGuidanceDisplayComponent (ID 30, group)"])
                    if "MaxAfterManeuverRoadNameLength" in rGDC:
                        mAMRNL=(rGDC["MaxAfterManeuverRoadNameLength"])
                        mAMRNL=mAMRNL[:2]
                    if "MaxCurrentRoadNameLength" in rGDC:
                        mCRNL=(rGDC["MaxCurrentRoadNameLength"])
                        mCRNL=mCRNL[:2]
                    if "MaxDestinationNameLength" in rGDC:
                        mDNL=(rGDC["MaxDestinationNameLength"])
                        mDNL=mDNL[:2]
                    if "MaxGuidanceManeuverCapacity" in rGDC:
                        mGMC=(rGDC["MaxGuidanceManeuverCapacity"])
                        mGMC=mGMC[:2]
                    if "MaxManeuverDescriptionLength" in rGDC:
                        mMDL=(rGDC["MaxManeuverDescriptionLength"])
                        mMDL=mMDL[:2]

                if "USBHostTransportComponent (ID 16, group)" in parameters:
                    uSBHTC=(parameters["USBHostTransportComponent (ID 16, group)"])
                    if "TransportComponentIdentifier" in uSBHTC:
                        tCIdentifier= (uSBHTC["TransportComponentIdentifier"])
                    if "USBHostTransportCarPlayInterfaceNumber" in uSBHTC:
                        uHTCPIN=(uSBHTC["USBHostTransportCarPlayInterfaceNumber"])
                        uHTCPIN=uHTCPIN[:2]

                if "MessagesSentByAccessory (ID 6, uint16[])" in parameters:
                    #print ("MessagesSentByAccessory CHECK!")
                    mSBA=(parameters["MessagesSentByAccessory (ID 6, uint16[])"])
                    if "0xAE00" in mSBA:
                        xAE00=(mSBA["0xAE00"])
                        if "StartPowerUpdates" in xAE00:
                            sPU= True
                    if "0xAE02" in mSBA:
                        xAE02=(mSBA["0xAE02"])
                        if "StopPowerUpdates" in xAE00:
                            stopPU= True
                            



        elif (data [v]["Title"])== "IdentificationInformation" and iiFound>0:
                iiFound=iiFound+1
                #print("ERROR!!! IdentificationInformation found ", iiFound ,"times!")
                #iAPErrorCount=iAPErrorCount+1        
########TC67EFB########TC67EFB########TC67EFB########TC67EFB########TC67EFB########TC67EFB########TC67EFB########TC67EFB########TC67EFB

        if tc67EFB!= True:
            tc67EFB=0
            try:
                if "OOBBTPairingAccessoryInformation" not in pMRFD.values() and "OOBBTPairingCompletionInformation" not in pMRFD.values()and tc67EFB<11 :
                    tc67EFB=tc67EFB+1
                    #print (tc67EFB)

                if "OOBBTPairingAccessoryInformation" not in pMSBA.values() and "OOBBTPairingCompletionInformation" not in pMSBA.values()and tc67EFB<2:
                    tc67EFB=tc67EFB+10
                    #print (tc67EFB)
            except:
                pass
            if tc67EFB==11:
                tc67EFB=True
                #print ("WEEEEEEEEEEEEEEEEEEEEEEE")
########TC67EFB                
            
########TCC3941########TCC3941########TCC3941########TCC3941########TCC3941########TCC3941########TCC3941      

        if (data [v]["Title"])== "PowerSourceUpdate": 
            try:
                aCFD= (data [v]["Details"]["Parameters"]["AvailableCurrentForDevice"])
                if "1000" in aCFD:
                    aCFD=1000
                if aCFD==sCFD:
                    tcC3941_5=True
                if sPU!=True:
                    aCFDAfterAuth=False
                    #print ("FFFFFFFFFFFFFFFFFalse")
                if sPU==True and aCFDAfterAuth!=False:
                    aCFDAfterAuth=True
                    tcC3941_4=True
            except:
                pass
########TCC3941


########TCEC29F########TCEC29F########TCEC29F########TCEC29F########TCEC29F########TCEC29F########TCEC29F########TCEC29F





        if title== "BluetoothComponentInformation" or "BluetoothComponentInformation" in details:
            bCI="ERROR!!! BluetoothComponentInformation found!"
            tcEC29F=False

########TCEC29F
            
        v=v+1

#General error information

#if iiFound!=1:
    #print("ERROR!!!  IdentificationInformation found",iiFound,"times, should be 1.")

########TC37320########TC37320########TC37320########TC37320########TC37320########TC37320########TC37320########TC37320########TC37320  
print ("\n\n\n")
if pName=="":
    print("   TC37320 FAILED! Name not found!")
    tc37320=False
else:
    print("Name: ",pName)
    print("    >should be marketing name of IVI<")
print("")

if pModel=="":
    print("   TC37320 FAILED! ModelIdentifier not found!")
    tc37320=False
else:
    print("ModelIdentifier: ",pModel)
    print("    >should be vehicle model<") 
print("")

if pMan=="":
    print("   TC37320 FAILED! Manuf. not found!")
    tc37320=False
else:    
    print("Manf. :",pMan)
print("")    
    
if pSN=="":
    print("   TC37320 FAILED! SN not found!")
    tc37320=False
else:
    print("SN: ",pSN)
print("")

if pFWV=="":
    print("   TC37320 FAILED! FW Ver. not found!")
    tc37320=False
else:
    print("FW Ver: ",pFWV)
print("")

if pHWV=="":
    print("   TC37320 FAILED! HW Ver. not found!")
    tc37320=False
else:
    print("HW Ver: ",pHWV)
print("")

if pPPUUID=="":
    print("   TC37320 FAILED! PPUUID not found!")
    tc37320=False
else:
    print("UUID: ",pPPUUID)
print("")

if vICompDisName=="":
    print("   ERROR!!! Display Name not found!")
    tc0BE0D=False
    
else:
    print("VIC Display Name: ",vICompDisName)
    print("    Should be the same as Bluetooth name.")
    

tc37320check=0
#print (tc37320)
print("\nAre the above values correct?") 
while tc37320check==0:   
    tc37320check=input (">>>>Type 'y' or 'n' and press 'ENTER'.\n")
    tc37320check=tc37320check.upper()
    if tc37320check == "Y":
        print("\n")
    elif tc37320check == "N":
        print("   TC37320 FAILED! Values not reported correctly!")
        tc0BE0Dcheck=0

            ########TC0BE0D########TC0BE0D########TC0BE0D########TC0BE0D########TC0BE0D########TC0BE0D########TC0BE0D########TC0BE0D
        print("\nAre the Name, Model Identifier, Manufacturer, and DisplayName all correct?") 
        while tc0BE0Dcheck==0:   
            tc0BE0Dcheck=input (">>>>Type 'y' or 'n' and press 'ENTER'.\n")
            tc0BE0Dcheck=tc0BE0Dcheck.upper()
            if tc0BE0Dcheck == "Y":
                print("\n")
            elif tc0BE0Dcheck == "N":
                print("   TC0BE0D FAILED! Values not reported correctly!")
                tc0BE0D=False
            else:
                tc0BE0Dcheck=0
            ########TC0BE0D
        
    else:
        tc37320check=0
if tc37320==True and tc37320check=="Y":
    tc37320=True
else:
    tc37320=False

########TC37320

#vvvvv The numbers below are valid as of 24 Sept 19 for Indian HW only!
print ("\n\n\n")

if "15" not in mAMRNL:
    print("   TCA568C FAILED, returned",mAMRNL,", should be 15")
    tcA568C=False
else:
    mAMRNL = 15
    print("MaxAfterManeuverRoadNameLength: ",mAMRNL)

if "15" not in mCRNL:
    print("   TCA568C FAILED, returned",mCRNL,", should be 15")
    tcA568C=False
else:
    mCRNL=15
    print("MaxCurrentRoadNameLength: ", mCRNL)

if "15" not in mDNL:
    print("   TCA568C FAILED, returned",mDNL,", should be 15")
    tcA568C=False
else:
    mDNL=15
    print("MaxDestinationNameLength: ", mDNL)

if "3 " not in mGMC:
    print("   TCA568C FAILED, returned",mGMC,", should be 3")
    tcA568C=False
else:
    mGMC=3
    print("MaxGuidanceManeuverCapacity: ", mGMC)

if "15" not in mMDL:
    print("   TCA568C FAILED, returned",mMDL,", should be 15")
    tcA568C=False
else:
    mMDL=15
    print("MaxManeuverDescriptionLength: ", mMDL)
#^^^^^

if tCIdentifier=="":
    print ("TC 39935 FAILED, TC Id not found!")
    tc39935=False
#else:
    #print("TransportComponentIdentifier: ", tCIdentifier)
if vICompIdent=="":
    print ("TC 39935 FAILED, VIC Identifier not found!")
    tc39935=False
#else:
    #print("VIC Identifier: ",vICompIdent)
if sPU==False:
    print ("TC 39935 FAILED, StartPowerUpdates not found!")
    tc39935=False
#else:
    #print("StartPowerUpdates: ", sPU)
if stopPU==True:
    print ("TC 39935 FAILED, StopPowerUpdates found!")
    tc39935=False
#print("StopPowerUpdates: ", stopPU)

if "0 (Gasoline)" not in vICompEngineType:
    print ("TC EEFF1 FAILED!!! Wrong Engine Type found!")
    print (">>> Engine Type should be 0 (Gasoline), but is reporting: ",vICompEngineType)
    tcEEFF1=False
else:
    vICompEngineType="0 (Gasoline)"
    #print("EngineType: ", vICompEngineType)
    
if tcC3941_4==False:
    print ("TC C3941 FAILED!!! PowerSourceUpdate message sent before authentication was completed!!!!")
elif tcC3941_4!=True:
    print ("TC C3941 FAILED!!! PowerSourceUpdate message not seen!!!")
if tcC3941_5!=True:
    print ("TC C3941 FAILED!!! Device supplied wrong charging current,",aCFD,"instead of",sCFD,"!!!!")








#print("USBHostTransportCarPlayInterfaceNumber: ", uHTCPIN) #See TC 20E9D
#print ("AvailableCurrentForDevice: ", aCFD)
#print("BluetoothComponentInformation: ", bCI)
#print ("iAP2 Control Session Count= ", v)
print("")
print("")

print("")
print("")


########TC20E9D########TC20E9D########TC20E9D########TC20E9D########TC20E9D########TC20E9D########TC20E9D########TC20E9D########TC20E9D

with open("USB Transfers.json", "r", encoding="utf8") as file: #Apple uses the utf8 encoding for json
    data=json.load(file)

    for key in data:
        if "Timestamp" in (data[u]):
            timeStamp=(data [u]["Timestamp"])
        if "Source" in (data[u]):
            source= (data[u]["Source"])
        if "Details" in (data[u]):
            details=(data[u]["Details"])
        
        if "Title" in (data[u]):
            title=(data [u]["Title"])

            if title=="USB Role Switch (Apple device to USB Host)":
                tC20E9D_3=True
                #print ("Found")
            if title=="Get Configuration Descriptor":
                if "Configuration Descriptor" in details:
                    #print ("YES")
                    configDes=(details["Configuration Descriptor"])
                    #print (configDes)
                    if "Interface Descriptor" in configDes:
                        intDes=(configDes["Interface Descriptor"])
                        #print (intDes,"\n\n")
                        t=0
                        s=0
                        while s==0:
                            try:
                                if "bInterfaceClass" in intDes[t]:
                                    bIC=(intDes[t]["bInterfaceClass"])
                                    if bIC=="0x01 (Audio)":
                                        tC20E9D_6=False
                                    if bIC=="0x02 (CDC Control)":
                                        tC20E9D_7=True
                                        uSBTranBIN=(intDes[t]["bInterfaceNumber"])
                                        #print ("uSBTranBIN:",uSBTranBIN)

                                        
                            except:
                                s=1
                            t=t+1
                            


        u=u+1
#print("uSBTranBIN:",uSBTranBIN,"uHTCPIN:",uHTCPIN)

        
if int(uSBTranBIN)==int(uHTCPIN):
    tC20E9D_10=True
########TC20E9D















        
###############All Test Results#####################
    
print("Test Results. For failures, see log.")
print("")
if errorCount!=0:
    print("General CarPlay failure, Error notice(s) seen",errorCount,"time(s)!")
    baseTestFail=baseTestFail+"General CarPlay failure "
if iAPErrorCount!=0:
    print("General iAP2 failure, Error notice(s) seen",iAPErrorCount,"time(s)!")
    baseTestFail=baseTestFail+"General iAP2 failure "
if tc37320==True:
    baseTestPass=baseTestPass+"37320 "
else:
    baseTestFail=baseTestFail+"37320 "

if tcA568C==True:
    baseTestPass=baseTestPass+"A568C_5 "
else:
    baseTestFail=baseTestFail+"A568C_5 "

if tc39935==True:
    baseTestPass=baseTestPass+"39935 "
else:
    baseTestFail=baseTestFail+"39935 "

if tcEEFF1==True:
    baseTestPass=baseTestPass+"EEFF1 "
else:
    baseTestFail=baseTestFail+"EEFF1 "

if tcC3941_5==True and tcC3941_4==True:
    baseTestPass=baseTestPass+"C3941 "
else:
    baseTestFail=baseTestFail+"C3941 "
    

if tcEC29F==True:
    baseTestPass=baseTestPass+"EC29F "
else:
    baseTestFail=baseTestFail+"EC29F "

if tcA3C1D==True:
    baseTestPass=baseTestPass+"A3C1D "
else:
    baseTestFail=baseTestFail+"A3C1D "

if tc67EFB==True:
    baseTestPass=baseTestPass+"67EFB "
else:
    baseTestFail=baseTestFail+"67EFB "

if tc0BE0D==True:
    baseTestPass=baseTestPass+"0BE0D "
else:
    baseTestFail=baseTestFail+"0BE0D "


if tCF8326_2a==True and tCF8326_2b==True and tCF8326_3==True and tCF8326_4==True and tCF8326_5==True and tCF8326_6==True and tCF8326_7==True:
    baseTestPass=baseTestPass+"F8326 "
else:
    baseTestFail=baseTestFail+"F8326 "
    print ("    F8326_2a and _8:", tCF8326_2a)
    print ("    F8326_2b:", tCF8326_2b)
    print ("    F8326_3:", tCF8326_3)
    print ("    F8326_4:", tCF8326_4)
    print ("    F8326_5:", tCF8326_5)
    print ("    F8326_6:", tCF8326_6)
    print ("    F8326_7:", tCF8326_7)

if tC4C0D8== True:
    baseTestPass=baseTestPass+"4C0D8 "
else:
    baseTestFail=baseTestFail+"4C0D8 "

if tC3C105 ==True:
    baseTestPass=baseTestPass+"3C105 "
else:
    baseTestFail=baseTestFail+"3C105 "  


if tC9619Ca==True and tC9619Cb==True and tC9619Cc==True and tC9619Cd==True and tC9619Ce==True and tC9619Cf==True and tC9619Cg==True and tC9619Ch==True and tC9619Ci==True and tC9619Cj==True and tC9619Ck==True and tC9619Cl==True and tC9619Cm==True and tC9619Cn==True and tC9619Co==True and tC9619Cp==True and tC9619Cq==True :
    baseTestPass=baseTestPass+"9619C "
else:
    baseTestFail=baseTestFail+"9619C "  

    print ("    9619Ca:",tC9619Ca)
    print ("    9619Cb:",tC9619Cb)
    print ("    9619Cc:",tC9619Cc)
    print ("    9619Cd:",tC9619Cd)
    print ("    9619Ce:",tC9619Ce)
    print ("    9619Cf:",tC9619Cf)
    print ("    9619Cg:",tC9619Cg)
    print ("    9619Ch:",tC9619Ch)
    print ("    9619Ci:",tC9619Ci)
    print ("    9619Cj:",tC9619Cj)
    print ("    9619Ck:",tC9619Ck)
    print ("    9619Cl:",tC9619Cl)
    print ("    9619Cm:",tC9619Cm)
    print ("    9619Cn:",tC9619Cn)
    print ("    9619Co:",tC9619Co)
    print ("    9619Cp:",tC9619Cp)
    print ("    9619Cq:",tC9619Cq)

if tC5F282_3 ==True and tC5F282_5 ==True and tC5F282_7 ==True and tC5F282_8 ==True:
    baseTestPass=baseTestPass+"5F282 "
else:
    baseTestFail=baseTestFail+"5F282 " 
    print ("    5F282_3:",tC5F282_3)
    print ("    5F282_5 and _6:",tC5F282_5)
    print ("    5F282_7:",tC5F282_7)
    print ("    5F282_8:",tC5F282_8)

if tC306B2a ==True and tC306B2b ==True:
    baseTestPass=baseTestPass+"306B2 "
else:
    baseTestFail=baseTestFail+"306B2 "
    print ("    306B2a:",tC306B2a)
    print ("    306B2b:",tC306B2b)

if tCB66A0_3==True and tCB66A0_4==True and tCB66A0_5==True:
    baseTestPass=baseTestPass+"B66A0 "
else:
    baseTestFail=baseTestFail+"B66A0 "
    print ("    B66A0_3:",tCB66A0_3)
    print ("    B66A0_4:",tCB66A0_4)
    print ("    B66A0_5:",tCB66A0_5)

if tC80B49==True:
    baseTestPass=baseTestPass+"80B49 "
else:
    baseTestFail=baseTestFail+"80B49 "

if tC62C2F==True:
    baseTestPass=baseTestPass+"62C2F "
else:
    baseTestFail=baseTestFail+"62C2F "

if tCFAE9C_4==True and tCFAE9C_5==True and tCFAE9C_6==True:
    baseTestPass=baseTestPass+"FAE9C "
else:
    baseTestFail=baseTestFail+"FAE9C "
    print ("    FAE9C_4:",tCFAE9C_4)
    print ("    FAE9C_5:",tCFAE9C_5)
    print ("    FAE9C_6:",tCFAE9C_6)

if tC9ADAE==True and tCFAE9C_6==True:
    baseTestPass=baseTestPass+"9ADAE "
else:
    baseTestFail=baseTestFail+"9ADAE "
    print ("    9ADAE:",tC9ADAE)
    print ("    FAE9C_6:",tCFAE9C_6)

if tC4F8E0==True:
    baseTestPass=baseTestPass+"4F8E0 "
else:
    baseTestFail=baseTestFail+"4F8E0 "


if tC20E9D_3==True and tC20E9D_6==True and tC20E9D_7==True and tC20E9D_10==True:
    baseTestPass=baseTestPass+"20E9D "
else:
    baseTestFail=baseTestFail+"20E9D "
    print("    20E9D_3:",tC20E9D_3)
    
    print("    20E9D_6:",tC20E9D_6)
    print("    20E9D_7:",tC20E9D_7)
    print("    20E9D_10:",tC20E9D_10)





    
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nTest results.\n")

saveFile=open("TestResults.txt", "a+")
saveFileTime=datetime.datetime.now()
saveFileTime=str(saveFileTime)
saveFile.write(saveFileTime+ "\n")

print (baseTestPass)
print (baseTestFail)
print ("")
saveFile.write(baseTestPass+ "\n")
saveFile.write(baseTestFail+ "\n")

if "optGroup1" in dataIn :
    from optGroup1 import oG1Pass, oG1Fail
    print (oG1Pass)
    print (oG1Fail)
    print ("")
    saveFile.write(oG1Pass+ "\n")
    saveFile.write(oG1Fail+ "\n")
else:
    print("optGroup1 not run.\n")
    saveFile.write("optGroup1 not run.\n")

if "optGroup2" in dataIn :
    from optGroup2 import oG2Pass, oG2Fail
    print (oG2Pass)
    print (oG2Fail)
    print ("")
    saveFile.write(oG2Pass+ "\n")
    saveFile.write(oG2Fail+ "\n")
    
else:
    print("optGroup2 not run.\n")
    saveFile.write("optGroup1 not run.\n")

saveFile.write("\nEND TEST RESULTS\n\n\n\n")

saveFile.close()

input("\n\n>>>> Press 'ENTER' to exit")
