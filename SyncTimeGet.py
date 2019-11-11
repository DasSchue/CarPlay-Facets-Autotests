import json
import time
import datetime

y=0

dateTime=datetime.datetime.now()
dDateTime=(dateTime.strftime("%d"))
bDateTime=(dateTime.strftime("%b"))
yDateTime=(dateTime.strftime("%y"))
tDateTime=dDateTime+bDateTime+yDateTime

jsonIn=tDateTime+"Data.json"

with open(jsonIn, "r") as dataIn:

    dataIn=json.load(dataIn)
    fixedData=(dataIn["fixed"][0])
    startTime=(fixedData["startTime"])#The time from Python when the program started.
    syncTime=(fixedData["syncTime"])#sync time event to line program time to JSON time

with open("CarPlay Session.json", "r", encoding="utf8") as timeFile: #Apple uses the utf8 encoding for json
    xdata=json.load(timeFile)

    timeSyncFound=False
    for key in xdata:
        if "Timestamp" in (xdata[y]):
            timeStamp=((xdata [y]["Timestamp"])/1000000000)
            timeStampRaw=(xdata [y]["Timestamp"])
        
        if "Title" in (xdata[y]):
            title=(xdata [y]["Title"])
            if title=="Request Siri Command" and timeStamp >20 and timeSyncFound==False:   #Change timeStamp ">" as needed.
                timeSyncFound=True
                aTSSyncTime=timeStamp   #The JSON time sync stamp.
                #print ("aTSSyncTime:",aTSSyncTime)
                syncTime=(syncTime-startTime)
                #print ("syncTime:",syncTime)
                timeOffset=aTSSyncTime-syncTime
                #print ("Time Offset:" ,timeOffset)
                
        y=y+1

             
            
