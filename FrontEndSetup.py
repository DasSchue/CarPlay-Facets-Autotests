import time
import datetime
import json


    #fixed TC variables

tCFAE9C_5 = ""
tCB66A0_5 = ""
    #optional TC variables
runOptGroup1 = ""
optGroup1Tele=""
optGroup1Siri=""
runOptGroup2 = ""
tC4AF72_9=""
tCC6485Correct=""

#####Version information block
print("\nThis test is set up for the following:")
print("Intended IVI: 2020 Indian HW 7in with CarPlay")
print("ATS version: ATS 7.0.1")
print("Facets version: Facets 2.3.2")
#print("Covered Test Cases: 306B2,3C105,4C0D8,4F8E0,5F282,62C2F,80B49,9619C,9ADAE,B66A0,F8326,FAE9C")
#print("Covered Test Cases: 0BE0D,37320,39935,67EFB,A3C1D,A568C,C3941,EC29F,EEFF1")
#print("Covered Test Cases: 20E9D")
#print("\nOptional Test Cases: 4E15E,964FB,0BCE9")

input("\n>>>> Press 'ENTER' to continue.")

########################################################################
# There are two sections to this test. The first one is done while the #
# ATS data is being recorded, the second after the ATS data has been   #
# ported over to the proper location for analysis. Test cases are      #                   
# listed as appropriate for each location.                             #
########################################################################

#vvvvvv Portion of test run concurent with ATS vvvvvv#

print("\n \n \n")
print("Ensure wireless headset is connected to the IVI and the IVI FM radio is selected as music source.")
input(">>>> Press 'ENTER' to continue.\n")
print("Make sure iPhone has new name and that there are no saved vehicles for CarPlay on the phone.")
print("    This insures CarPlay will act as a first time connection.")
input(">>>> Press 'ENTER' to continue.\n")
print("Make sure both nightMode and limitedUI are set to OFF on the IVI.")
input(">>>> Press 'ENTER' to continue.\n")
print("Make sure RIGHT trigger is fuctional.")
input(">>>> Press 'ENTER' to continue.\n")




print("Start the ATS Tool recording. Connect iPhone to IVI.")
input(">>>> Once iPhone is connected, press 'ENTER' to continue .\n")
startTime=time.time()
print("\n\n!!!WARNING: Do not interact with the IVI until notified to continue!!!\n\n")
time.sleep(2) #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<SLEEP
print("\n\nContinue with testing. Interface with the IVI as needed.\n\n")

########TCFAE9C########TCFAE9C
while tCFAE9C_5 =="":
    print("Verify the IVI displayed the CarPlay UI automatically.") 
    tCFAE9C_5=input (">>>>Type 'y' or 'n' and press 'ENTER'.\n")
    tCFAE9C_5=tCFAE9C_5.upper()
    if tCFAE9C_5 == "Y" or tCFAE9C_5 == "N":
        print("\n")
    else:
        tCFAE9C_5=""
if tCFAE9C_5=="Y":
    tCFAE9C_5=True
else:
    tCFAE9C_5=False
########TCFAE9C


  

########TCB66A0########TCB66A0

print("On the IVI, navigate to the CarPlay main screen if not already displayed.")
while tCB66A0_5=="":
    print ("Is the 'Indian' icon present? ")
    tCB66A0_5=input(">>>>Type 'y' or 'n' and press 'ENTER'.\n")
    tCB66A0_5=tCB66A0_5.upper()
    if tCB66A0_5 == "Y" or tCB66A0_5 == "N":
        print("\n")
    else:
        tCB66A0_5=""
if tCB66A0_5=="Y":
    tCB66A0_5=True
else:
    tCB66A0_5=False
########TCB66A0

print ("When counter reaches '0', press and quickly release Siri Button on IVI test unit.\n\n") #timing marker vvv
input (">>>> Press 'ENTER' to continue.\n\n\n")
sl=3
while sl !=-1:
    time.sleep (1)
    print ("         ", sl)
    sl=sl-1

#print ("0")
print ("\nPress and quickly release Siri Button on IVI test unit.\n\n\n\n\n")

syncTime=time.time()
#print (syncTime)
time.sleep (2)  #timing marker ^^^

#****************************************************************************************************************************************
#Begin Optional Test Cases Section Begin Optional Test Cases Section Begin Optional Test Cases Section Begin Optional Test Cases Section*
#Begin Optional Test Cases Section Begin Optional Test Cases Section Begin Optional Test Cases Section Begin Optional Test Cases Section* 
#****************************************************************************************************************************************

#OptGroup1 #OptGroup1 #OptGroup1 #OptGroup1 #OptGroup1 #OptGroup1 #OptGroup1 


while runOptGroup1 =="":
    
    print("Run Optional Test Group 1:")
    print("    Test Cases 0BCE9,19B1D,4E15E,62210,823D0,B5E07?")
    
    runOptGroup1=input (">>>>Type 'y' or 'n' and press 'ENTER'.\n")
    runOptGroup1=runOptGroup1.upper()
    if runOptGroup1 == "Y":
        runOptGroup1 = True
    

        
        print("\n\n\nMake sure CarPlay UI showing on IVI.\n\n\n")
        print("When prompted, swip finger across IVI screen consistently for 2-3 seconds.\n")
        input(">>>>When ready, press 'ENTER' to continue.\n\n\n")
        oG1StartTime=time.time()
        print("Swipe finger across screen.\n")
        input(">>>> Press 'ENTER' when finished.\n\n\n")
        tC4E15EEndTime=time.time()

        print("Press the lower right switch on the left hand control pod UP and then DOWN rapidly one time.")
        print("Then press it UP, wait 1 second, and then press it DOWN.\n")        
        input(">>>> Press 'ENTER' when finished.\n\n\n")
        tC19B1DEndTime=time.time()
        

        print("1: Use the switch to highlight the 'Now Playing' icon', then press it IN once.\n")
        #time.sleep (3)
        print("2: Pull RIGHT trigger then the LEFT trigger.\n")
        #time.sleep (3)
        print("3: Press the 'volume/Siri' button RIGHT then LEFT.\n")
        #time.sleep (3)
        print("4: Short press IN the 'volume/Siri' button.\n")
        #time.sleep (3)
        print("5: Call the iPhone and use RIGHT trigger to accept call and the LEFT trigger to end call.\n\n")           
        while optGroup1Tele=="":
            print ("Did the telephony controls work as expected?")
            optGroup1Tele=input (">>>>Type 'y' or 'n' and press 'ENTER'.\n")
            optGroup1Tele=optGroup1Tele.upper()
            if optGroup1Tele == "Y":
                optGroup1Tele = True
            elif optGroup1Tele == "N":
                optGroup1Tele = False
            else:
                optGroup1Tele=""
        tC0BCE9EndTime=time.time()

        
        print("\n\n\nActivate all other switches on both hand control pods, but do NOT re-activate any of the above controls.\n")
        print (">>Note: Do press the 'volume' button UP and DOWN.")
        #time.sleep (3)
        input(">>>> Press 'ENTER' when finished.\n\n\n\n")

        

        print ("Return to native UI using the 'Home' hardkey.\n")
        input (">>>> Press 'ENTER' when in native UI.\n\n\n\n")
        tC31FE6EndTime=time.time()
        #time.sleep (3)
        print ("1: Activate all hand controls on both hand control pods EXCEPT:") #Covers TC964FB and TC823D0
        print ("    DO NOT press 'Siri-Play/Pause' IN or LEFT or RIGHT. \n")
        
        print ("2:  Swipe finger across display.\n")
        input (">>>> Press 'ENTER' when finished.\n\n\n\n")      
        tC964FBEndTime=time.time()

        print ("1: Short press Siri button.\n")# Covers TC62210, 26EBD, 31FE6, TC6F99C and TCB5E07
        print ("2: Press and hold Siri button.\n")
        print ("3: While holding the Siri button down, ask Siri to send a message.\n")
        print ("4: Release Siri button.")
        print ("5: While Siri is still active, short press Siri button. \n")
        while optGroup1Siri=="":
            print ("Did the Siri UI come and go properly and was Siri audible?")
            optGroup1Siri=input (">>>>Type 'y' or 'n' and press 'ENTER'.\n")
            optGroup1Siri=optGroup1Siri.upper()
            if optGroup1Siri == "Y":
                optGroup1Siri = True
            elif optGroup1Siri == "N":
                optGroup1Siri = False
            else:
                optGroup1Siri=""

        tC62210EndTime=time.time()

    elif runOptGroup1 == "N":
        runOptGroup1 = False
    else:
        runOptGroup1=""

    oG1EndTime=time.time()
#OptGroup1

        
#OptGroup2 #OptGroup2 #OptGroup2 #OptGroup2 #OptGroup2 #OptGroup2
    
while runOptGroup2 =="":
    
    print("Run Optional Test Group 2:")
    print("    Test Cases 4AF72,D05C2?")
    
    runOptGroup2=input (">>>>Type 'y' or 'n' and press 'ENTER'.\n")
    runOptGroup2=runOptGroup2.upper()
    if runOptGroup2 == "Y":
        runOptGroup2 = True
    elif runOptGroup2 == "N":
        runOptGroup2 = False
    else:
        runOptGroup2=""

if runOptGroup2 == True:
    

    print("\n\n\nMake sure CarPlay UI showing on IVI.\n")
    input(">>>> Press 'ENTER' when finished.\n\n\n")
    oG2StartTime=time.time()

    print("1: Using B1, turn 'MSG 19' ON.") 
    print("2: Dismiss notification using touch screen.")
    input(">>>> Press 'ENTER' when finished.\n\n\n")
    tCC6485Time1=time.time()
    print("1: Using B1, turn 'MSG 19' OFF.")
    input(">>>> Press 'ENTER' when finished.\n\n\n")
    tCC6485Time2=time.time()
    print("1: Using B1, turn 'MSG 19' ON.")
    time.sleep(1.5)
    print("1: Using B1, turn 'MSG 19' OFF.\n\n")

    print ("Did the warning message clear off and IVI return to CarPlay as expected both times?")
    tCC6485Correct=input (">>>>Type 'y' or 'n' and press 'ENTER'.\n\n\n")
    tCC6485Correct=tCC6485Correct.upper()
    if tCC6485Correct == "Y":
        tCC6485Correct = True
    elif tCC6485Correct == "N":
        tCC6485Correct = False
    else:
        tCC6485Correct=""
    tCC6485Time3=time.time()

    print ("Set B1 speed to 30 km/h.")
    input (">>>> Press 'ENTER' when finished.") 
    tC4AF72Time1=time.time()
    time.sleep(3)
    while tC4AF72_9=="":
        print("\nAre the soft keyboards/keypads in CarPlay disabled on IVI?") 
        tC4AF72_9=input (">>>>Type 'y' or 'n' and press 'ENTER'.\n")
        tC4AF72_9=tC4AF72_9.upper()
        if tC4AF72_9 == "Y":
            tC4AF72_9 = True
            
        elif tC4AF72_9 == "N":
            tC4AF72_9 = False
        else:
            tC4AF72_9=""

    print ("Set B1 'light' from 0 to 100 (or 100-0 as needed) to trigger Night Mode.")
    input (">>>> Press 'ENTER' when IVI in Night Mode.\n") 
    tCD05C2Time1=time.time()

    print("Disconnect iPhone from IVI.")
    input(">>>> Press 'ENTER' when finished.\n")
    time.sleep (5) # Apple recommended time between connections
    print("Connect iPhone to IVI.")
    input(">>>> Once CarPlay launches, press 'ENTER' to continue .\n")
    tC4AF72Time2=time.time()
    tCD05C2Time2=time.time()
    time.sleep (2) #to allow CarPlay to start properly
    print ("Set B1 speed to 0 km/h.")
    input (">>>> Press 'ENTER' when finished.\n") 
    tC4AF72Time3=time.time()
        
    
    print ("Set B1 'light'to 0.")
    time.sleep(15)
    input (">>>> Press 'ENTER' when IVI leaves Night Mode.\n") 
    tCD05C2Time3=time.time()

    time.sleep(2)
    
    tC0BB6FTime1=time.time()

    
    oG2EndTime=time.time()
   




#******************************************************************************************************************************
#Post Test Wrap Up Post Test Wrap Up Post Test Wrap Up Post Test Wrap Up Post Test Wrap Up Post Test Wrap Up Post Test Wrap Up* 
#Post Test Wrap Up Post Test Wrap Up Post Test Wrap Up Post Test Wrap Up Post Test Wrap Up Post Test Wrap Up Post Test Wrap Up* 
#******************************************************************************************************************************



endTime=time.time()

dateTime=datetime.datetime.now()
dDateTime=(dateTime.strftime("%d"))
bDateTime=(dateTime.strftime("%b"))
yDateTime=(dateTime.strftime("%y"))
hDateTime=(dateTime.strftime("%H"))
mDateTime=(dateTime.strftime("%M"))
tDateTime=dDateTime+bDateTime+yDateTime

#print (tDateTime)


fixedDict={ 
    "startTime":startTime,
    "tCFAE9C_5":tCFAE9C_5,
    "tCB66A0_5":tCB66A0_5,
    "endTime":endTime,
    "syncTime":syncTime,
    
}
#print (fixedDict)



dataOut={"fixed":[fixedDict]}


#*** Optional tests

if runOptGroup1==True:
    oG1Dict={
        "tC4E15EEndTime":tC4E15EEndTime,
        "oG1StartTime":oG1StartTime,
        "tC19B1DEndTime":tC19B1DEndTime,
        "optGroup1Tele":optGroup1Tele,
        "tC0BCE9EndTime":tC0BCE9EndTime,
        "tC964FBEndTime":tC964FBEndTime,
        "tC62210EndTime":tC62210EndTime,
        "oG1EndTime":oG1EndTime,
        "tC31FE6EndTime":tC31FE6EndTime,
        "optGroup1Siri":optGroup1Siri
        }

    dataOut["optGroup1"]=oG1Dict

if runOptGroup2==True:
    oG2Dict={
        "oG2StartTime":oG2StartTime,
        "tCC6485Time1":tCC6485Time1,
        "tCC6485Time2":tCC6485Time2,
        "tCC6485Time3":tCC6485Time3,
        "tC4AF72Time1":tC4AF72Time1,
        "tC4AF72Time2":tC4AF72Time2,
        "tC4AF72Time3":tC4AF72Time3,
        "tCD05C2Time1":tCD05C2Time1,
        "tCD05C2Time2":tCD05C2Time2,
        "tCD05C2Time3":tCD05C2Time3,
        "tCC6485Correct":tCC6485Correct,
        "tC0BB6FTime1": tC0BB6FTime1,
        "tC4AF72_9":tC4AF72_9,
        "oG2EndTime":oG2EndTime
        }

    dataOut["optGroup2"]=oG2Dict
        

print ("\n\n\n", dataOut,"\n\n\n")



jsonOut=tDateTime+"DataZ.json"
with open(jsonOut, "w+") as jsonFile:
    json.dump(dataOut, jsonFile)

print("Save ATS trace JSON files to the correct folder.")
input(">>>> Press 'ENTER' to finish.\n")




