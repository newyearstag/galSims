import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.pyplot import Rectangle # Used to make dummy legend
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("quadrant", type=int,
                    help="Options : 1, 2, 3, 4")
parser.add_argument("binSize", type=int,
                    help="Set size of bins for histogram")
parser.add_argument("minDistance", type=int,
                    help="Set minimum search distance from location (kpc)")
parser.add_argument("maxDistance", type=int,
                    help="Set maximum search distance from location (kpc)")
args = parser.parse_args()
quad = args.quadrant # Prompt User for location
binSize = args.binSize # Prompt User for bin size
minDist = args.minDistance # Prompt User for minimum search distance
maxDist = args.maxDistance # Prompt User for maximum search distance
pos = 8.4 # Sun is set 8.4 kpc from the galactic center

# Open CSV File for Simulated Data
datafileS = open('3DHiiRegions.csv', 'r')
csvFileS = []
for row in datafileS:
    csvFileS.append(row.strip().split(','))

# Save x, y, and l Info from Simulated Data to new list
xDataS = list()
xDataQuadS = list()
yDataS = list()
yDataQuadS = list()
zDataS = list()
zDataQuadS = list()
lDataS = list()
lDataQuadS = list()
indexS = 0
numTotS = 0
numInQuadS = 0

while indexS < len(csvFileS) :
    xS = float(csvFileS[indexS][1])
    yS = float(csvFileS[indexS][2])
    zS = float(csvFileS[indexS][3])
    lS = float(csvFileS[indexS][8])
    
    xDataS.append(xS)
    yDataS.append(yS + pos)
    zDataS.append(zS)
    lDataS.append(lS)

    distS = pow(pow(xS,2)+pow(yS,2),.5)

    if quad == 1 :
        if (lS >= 0)\
        and (lS < 90)\
        and (distS > minDist)\
        and (distS < maxDist):
            xDataQuadS.append(xS)
            yDataQuadS.append(yS + pos)
            zDataQuadS.append(zS)
            lDataQuadS.append(lS)
            numInQuadS += 1
    elif quad == 2 :
        if (lS >= 90)\
        and (lS < 180)\
        and (distS > minDist)\
        and (distS < maxDist):
            xDataQuadS.append(xS)
            yDataQuadS.append(yS + pos)
            zDataQuadS.append(zS)
            lDataQuadS.append(lS)
            numInQuadS += 1
    elif quad == 3 :
        if (lS < -90)\
        and (lS >= -180)\
        and (distS > minDist)\
        and (distS < maxDist):
            xDataQuadS.append(xS)
            yDataQuadS.append(yS + pos)
            zDataQuadS.append(zS)
            lDataQuadS.append(lS)
            numInQuadS += 1
    elif quad == 4 :
        if (lS < 0)\
        and (lS >= -90)\
        and (distS > minDist)\
        and (distS < maxDist):
            xDataQuadS.append(xS)
            yDataQuadS.append(yS + pos)
            zDataQuadS.append(zS)
            lDataQuadS.append(lS)
            numInQuadS += 1
    else :
        print "Invalid Quadrant Selection"
        break
        
    indexS += 1
    numTotS +=1

# Open CSV File for Simulated Data
datafileW = open('wise_hii_V1.0.csv', 'r')
csvFileW = []
for row in datafileW:
    csvFileW.append(row.strip().split(','))

# Save x, y, and l Info from Simulated Data to new list
xDataW = list()
xDataQuadW = list()
yDataW = list()
yDataQuadW = list()
zDataW = list()
zDataQuadW = list()
lDataW = list()
lDataQuadW = list()
indexW = 1
numTotW = 0
numInQuadW = 0

while indexW < len(csvFileW) :
    try :
        dW = float(csvFileW[indexW][13])
        lW = float(csvFileW[indexW][2])
        if float(lW) > 180 :
            lW = lW-360
        else :
            lW = lW
        bW = 90 - float(csvFileW[indexW][3])
        xW = dW*math.sin(bW*math.pi/180)*math.cos((lW-90)*math.pi/180)
        yW = dW*math.sin(bW*math.pi/180)*math.sin((lW-90)*math.pi/180)
        zW = dW*math.cos(bW*math.pi/180)

        distW = pow(pow(xW,2)+pow(yW,2),.5)

        if quad == 1 :
            if (lW >= 0)\
            and (lW < 90)\
            and (distW > minDist)\
            and (distW < maxDist):
                xDataQuadW.append(xW)
                yDataQuadW.append(yW + pos)
                zDataQuadW.append(zW)
                lDataQuadW.append(lW)
                numInQuadW += 1
        elif quad == 2 :
            if (lW >= 90)\
            and (lW < 180)\
            and (distW > minDist)\
            and (distW < maxDist):
                xDataQuadW.append(xW)
                yDataQuadW.append(yW + pos)
                zDataQuadW.append(zW)
                lDataQuadW.append(lW)
                numInQuadW += 1
        elif quad == 3 :
            if (lW < -90)\
            and (lW >= -180)\
            and (distW > minDist)\
            and (distW < maxDist):
                xDataQuadW.append(xW)
                yDataQuadW.append(yW + pos)
                zDataQuadW.append(zW)
                lDataQuadW.append(lW)
                numInQuadW += 1
        elif quad == 4 :
            if (lW < 0)\
            and (lW >= -90)\
            and (distW > minDist)\
            and (distW < maxDist):
                xDataQuadW.append(xW)
                yDataQuadW.append(yW + pos)
                zDataQuadW.append(zW)
                lDataQuadW.append(lW)
                numInQuadW += 1
        xDataW.append(xW)
        yDataW.append(yW + pos)
        zDataW.append(zW)
        lDataW.append(lW)
        numTotW += 1
    except :
        lW = float(csvFileW[indexW][2])
        if float(lW) > 180 :
            lW = lW-360
        else :
            lW = lW
        lDataW.append(lW)

        if quad == 1 :
            if (lW >= 0)\
            and (lW < 90):
                lDataQuadW.append(lW)
                numInQuadW += 1
        elif quad == 2 :
            if (lW >= 90)\
            and (lW < 180):
                lDataQuadW.append(lW)
                numInQuadW += 1
        elif quad == 3 :
            if (lW < -90)\
            and (lW >= -180):
                lDataQuadW.append(lW)
                numInQuadW += 1
        elif quad == 4 :
            if (lW < 0)\
            and (lW >= -90):
                lDataQuadW.append(lW)
                numInQuadW += 1
        numTotW += 1
        #pass
    indexW += 1

fig = plt.figure(1)
fig.subplots_adjust(hspace=0.6)

# 3D Plot of Galaxy   FIX TITLE
ax = fig.add_subplot(3,2,1,projection='3d')
orig = ax.scatter(xDataW, yDataW, zDataW, s=3, label='WISE Regions', facecolor='g', lw = 0)
comb = ax.scatter(xDataS, yDataS, zDataS, s=3, label='Simulated Regions', facecolor='r', lw = 0)
ax.set_xlabel('X (kpc)')
ax.set_ylabel('Y (kpc)')
ax.set_zlabel('Z (kpc)')
plt.title('3D Overlay')

# Face on Plot of Quadrant in Question
ax = fig.add_subplot(3,2,2)
plt.scatter(xDataQuadW,yDataQuadW,s=3,facecolor='g', lw = 0)
plt.scatter(xDataQuadS,yDataQuadS,s=3,facecolor='r', lw = 0)
plt.xlabel('X (kpc)')
plt.ylabel('Y (kpc)')
plt.title('Face On View')

# Histogram of Full Galaxy
ax = fig.add_subplot(3,2,3)
plt.hist(lDataW, bins = range(-180,180,binSize), alpha=0.5, histtype='step', color='g')
plt.hist(lDataS, bins = range(-180,180,binSize), alpha=0.5, histtype='step', color='r')
plt.xticks([-180,-135,-90,-45,0,45,90,135,180])
plt.title("Full Galaxy - Longitude Binned")
plt.xlabel("Galactic Longitude (deg)")
plt.ylabel("Count")
plt.gca().invert_xaxis()

# Histogram of Quadrant (x) NEEDS EDITED (PROBLEM IN QUAD 2)
ax = fig.add_subplot(3,2,4)
if quad == 1 :
    plt.xticks([90,75,60,45,30,15,0])
    binRange = range(0,91,binSize)
elif quad == 2 :
    plt.xticks([180,165,150,135,120,105,90])
    binRange = range(90,181,binSize)
elif quad == 3 :
    plt.xticks([-180,-165,-150,-135,-120,-105,-90])
    binRange = range(-180,-89,binSize)
elif quad == 4 :
    plt.xticks([-90,-75,-60,-45,-30,-15,0])
    binRange = range(-90,1,binSize)
plt.hist(lDataS, bins = binRange, alpha=0.5, histtype='step', color='r')
plt.hist(lDataW, bins = binRange, alpha=0.5, histtype='step', color='g')
plt.title('Quadrant '+str(quad)+' - Longitude Binned')
plt.xlabel("Galactic Longitude (deg)")
plt.ylabel("Count")
plt.gca().invert_xaxis()

# Stats of WISE Data
ax = fig.add_subplot(3,2,5)
ax.text(0.5, 0.5, 'Quadrant '+str(quad)+' Composition'\
        '\nWISE : '+str(numInQuadW*100/numTotW)+'% of Regions'+\
        '\nSim : '+str(numInQuadS*100/numTotS)+'% of Regions'\
        , size=24, ha='center',va='center')
ax.axes.get_yaxis().set_visible(False)
ax.axes.get_xaxis().set_visible(False)

# Stats of Simulated Data
ax = fig.add_subplot(3,2,6)
prox1 = Rectangle((0, 0), 1, 1, fc='g')
prox2 = Rectangle((0, 0), 1, 1, fc='r')
plt.legend([prox1, prox2], ["WISE Regions", "Simulated Regions"], loc='center',frameon=False)
ax.axes.get_yaxis().set_visible(False)
ax.axes.get_xaxis().set_visible(False)

plt.suptitle('WISE vs Simulation - Quadrant '+str(quad)+' Analysis')
plt.savefig('Plots/Quadrant'+str(quad)+'_min'+str(minDist)+'_max'+str(maxDist)+'.eps', format='eps', dpi=1000)
plt.show()
