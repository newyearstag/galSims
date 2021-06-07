import pylab as p
import math
from matplotlib.pyplot import Rectangle # Used to make dummy legend

scol = str('#FF0000') # Sets color of simulated regions
wcol = str('#5FB404') # Sets color of WISE regions

# Open CSV File
datafile = open('3DHiiRegions.csv', 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
lData = list()
bData = list()
sizeData = list()
index = 0
while index < len(csvFile) :
    if (float(csvFile[index][11])*180/math.pi < 20) and (float(csvFile[index][11])*180/math.pi > -20) :
        lData.append(float(csvFile[index][8]))
        bData.append(float(csvFile[index][11])*180/math.pi)
        sizeData.append(float(float(csvFile[index][7])/float(csvFile[index][0])))
    index += 1

# Open CSV File for Simulated Data
datafileW = open('wise_hii_V1.0.csv', 'r')
csvFileW = []
for row in datafileW:
    csvFileW.append(row.strip().split(','))

# Save x, y, and l Info from Simulated Data to new list
bDataW = list()
lDataW = list()
indexW = 1

while indexW < len(csvFileW) :
    try :
        bW = float(csvFileW[indexW][3])
        lW = float(csvFileW[indexW][2])
        if float(lW) > 180 :
            lW = lW-360
        else :
            lW = lW
        if (bW < 20) and (bW > -20):    
            lDataW.append(lW)
            bDataW.append(bW)
    except :
        pass
    indexW += 1
print lDataW
p.scatter(lData,bData,s=2,facecolor=scol, lw = 0)
p.scatter(lDataW,bDataW,s=2,facecolor=wcol, lw = 0)
p.xlabel('l (deg)')
p.ylabel('b (deg)')
p.title('Galactic Plane Plot from Sun\'s Position')
prox1 = Rectangle((0, 0), 1, 1, fc=scol)
prox2 = Rectangle((0, 0), 1, 1, fc=wcol)
p.legend([prox1, prox2], ["Simulation", "WISE"], loc='lower right')
p.savefig('GalacticPlaneWiseSim_v1_0.eps', format='eps', dpi=1000)
p.show()
