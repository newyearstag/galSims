import matplotlib.pyplot as plt
import math
import csv
import argparse

'''parser = argparse.ArgumentParser()
parser.add_argument("iterTotal", type=int,
                    help="Number of Clustering Iterations")
args = parser.parse_args()
iterTot = args.iterTotal''' # Prompt User for number of iterations of clustering
iterTot = 1 #random number

# Open CSV File
datafile = open(r'C:\Users\newye\OneDrive\Documents\GitHub\galSims\misc\3DHiiRegions.csv', 'r')
csvFile = []
newFile = []
removeList = []
for row in datafile:
    newFile.append(row.strip().split(','))
originalSize = len(newFile)

# Save Galactic Radius Info from CSV to new list
(iterNum,index,target,engulf,overlap,separate)=(0,0,0,0,0,0)
sunPos = 8.4
sunHeight = 0.02
maxVelo = 10 # Sets max velocity difference in clustered sources to be (x) km/s

while iterNum < iterTot :
    csvFile = newFile
    newFile = []
    
    while (target < len(csvFile)) :
        
        xTarget = float(csvFile[target][1])
        yTarget = float(csvFile[target][2])
        zTarget = float(csvFile[target][3])
        massTarget = float(csvFile[target][4])
        lumTarget = float(csvFile[target][5])
        ageTarget = float(csvFile[target][6])
        radTarget = float(csvFile[target][7])
        lTarget = float(csvFile[target][8])*math.pi/180
        veloTarget = float(csvFile[target][9])
        regNumTarget = float(csvFile[target][10])
        bTarget = float(csvFile[target][11])*math.pi/180
        index = 0
        
        while (index < len(csvFile)) :
        
            xIndex = float(csvFile[index][1])
            yIndex = float(csvFile[index][2])
            zIndex = float(csvFile[index][3])
            massIndex = float(csvFile[index][4])        
            lumIndex = float(csvFile[index][5])
            ageIndex = float(csvFile[index][6])
            radIndex = float(csvFile[index][7])
            lIndex = float(csvFile[target][8])*math.pi/180
            veloIndex = float(csvFile[index][9])
            regNumIndex = float(csvFile[target][10])
            bIndex = float(csvFile[index][11])*math.pi/180

            indexDist = pow(pow(xIndex,2)+pow(yIndex-sunPos,2),0.5)*1000
            targetDist = pow(pow(xTarget,2)+pow(yTarget-sunPos,2),0.5)*1000
            #print(str(bTarget) + " " + str(bIndex) + " " + str(lTarget) + " " + str(lIndex))
            
            try :
                angDist = math.acos(math.sin(bTarget)*math.sin(bIndex)+math.cos(bTarget)*math.cos(bIndex)*math.cos(lTarget-lIndex))
            except :
                print("angDist problem")
            #print(angDist)
            angRadIndex = math.atan(radIndex/indexDist)
            angRadTarget = math.atan(radTarget/targetDist)
            
            # IN FUTURE SIMULATIONS : Throw away overlapping/engulfed regions
            # and repopulate. I would imagine these to be fairly rare.

            # One region is totally engulfed by the other.
            if (abs(veloTarget-veloIndex) < maxVelo) and (index != target) :
                if angDist < abs(angRadIndex - angRadTarget) : # Region is engulfed
                    if (angRadIndex - angRadTarget) < 0 : # Target is larger
                        xNew = xTarget
                        yNew = yTarget
                        zNew = zTarget
                        galRad = pow(pow(xNew,2)+pow(yNew,2),.5)
                        radNew = radTarget
                        effMass = massTarget + massIndex
                        lumNew = lumIndex + lumTarget
                        ageNew = (massTarget*ageTarget+massIndex*ageIndex)/(massTarget+massIndex)
## NEED A BETTER WAY TO DEAL WITH LUMINOSITIES
                        try :
                            veloNew = (lumTarget*veloTarget+lumIndex*veloIndex)/(lumTarget+lumIndex)
                        except :
                            veloNew = veloTarget
                            print ("Velo Problem" + str(index))
                        sunDist = pow(pow(xNew,2)+pow(yNew-sunPos,2),0.5)                               
                        lNew = math.copysign(math.acos((pow(sunDist,2)+pow(sunPos,2)-pow(galRad,2))/(2*sunPos*sunDist))*180/math.pi,xNew)
                        bNew = math.atan((zNew-sunHeight)/sunDist)
                    else : # Index is larger
                        xNew = xIndex
                        yNew = yIndex
                        zNew = zIndex
                        galRad = pow(pow(xNew,2)+pow(yNew,2),.5)
                        radNew = radIndex
                        effMass = massTarget + massIndex
                        lumNew = lumIndex + lumTarget
                        ageNew = (massTarget*ageTarget+massIndex*ageIndex)/(massTarget+massIndex)
                        try :
                            veloNew = (lumTarget*veloTarget+lumIndex*veloIndex)/(lumTarget+lumIndex)
                        except :
                            veloNew = veloTarget
                            print ("Velo Problem" + str(index))
                        sunDist = pow(pow(xNew,2)+pow(yNew-sunPos,2),0.5)                               
                        lNew = math.copysign(math.acos((pow(sunDist,2)+pow(sunPos,2)-pow(galRad,2))/(2*sunPos*sunDist))*180/math.pi,xNew)
                        bNew = math.atan((zNew-sunHeight)/sunDist)
                    removeList.append(index)
                    removeList.append(target)
                    engulf += 1
                    index = int(len(csvFile)) # Skip remaining regions
                    newFile.append([galRad,xNew,yNew,zNew,effMass,lumNew,ageNew,radNew,lNew,veloNew,regNumTarget,bNew]) # Add new region to end of file.
     #               print "Engulf : " + str(target)
            
                # Regions overlap. Place new region in barycenter of old regions.
                elif angDist < abs(angRadTarget + angRadIndex) :
                    xNew = (xTarget*massTarget + xIndex*massIndex)/(massTarget+massIndex)
                    yNew = (yTarget*massTarget + yIndex*massIndex)/(massTarget+massIndex)
                    zNew = (zTarget*massTarget + zIndex*massIndex)/(massTarget+massIndex)
                    galRad = pow(pow(xNew,2)+pow(yNew,2),.5)
                    radNew = (radTarget + radIndex + angDist)/2
                    effMass = massTarget + massIndex
                    lumNew = lumTarget + lumIndex
                    ageNew = (massTarget*ageTarget+massIndex*ageIndex)/(massTarget+massIndex)
                    try :
                        veloNew = (lumTarget*veloTarget+lumIndex*veloIndex)/(lumTarget+lumIndex)
                    except :
                        veloNew = veloTarget
                        print ("Velo Problem" + str(index))
                    sunDist = pow(pow(xNew,2)+pow(yNew-sunPos,2),0.5)                               
                    lNew = math.copysign(math.acos((pow(sunDist,2)+pow(sunPos,2)-pow(galRad,2))/(2*sunPos*sunDist))*180/math.pi,xNew)
                    bNew = math.atan((zNew-sunHeight)/sunDist)
                    removeList.append(index)
                    removeList.append(target)
                    overlap += 1
                    index = int(len(csvFile)) # Skip remaining regions
                    newFile.append([galRad,xNew,yNew,zNew,effMass,lumNew,ageNew,radNew,lNew,veloNew,regNumTarget,bNew])
     #               print "Overlap : " + str(target)
                
            # Regions don't interact.
            elif int(index) == int(len(csvFile)-1) :
                separate += 1
                galRad = pow(pow(xIndex,2)+pow(yIndex,2),.5)
                newFile.append([galRad,xIndex,yIndex,zIndex,massIndex,lumIndex,ageIndex,radIndex,lIndex,veloIndex,regNumIndex,bIndex])

            if int(index) == int(len(csvFile)-1) :
                i = 0
                while i < len(removeList):
                    try:
                        b=removeList.index(i)
 #                       print csvFile[b]
                        del csvFile[b]
                    except:
                        pass
                    i += 1
 #               newFile.extend(csvFile)
            index += 1    
        target += 1
    iterNum += 1       

with open(r"C:/Users/newye/OneDrive/Documents/GitHub/galSims/misc/3DHiiRegionsAngularCombine.csv", "w", newline = "") as f:
    writer = csv.writer(f)
    writer.writerows(newFile)

print ("Engulfed Regions : " + str(float(engulf*100/len(csvFile))) + "%")
print ("Overlapped Regions : " + str(float(overlap*100/len(csvFile))) + "%")
print ("Separate Regions : " + str(float(separate*100/len(csvFile))) + "%")
print (engulf)
print (overlap)
print (separate)
print (len(csvFile))
