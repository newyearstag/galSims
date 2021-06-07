import pylab as p
import math
from matplotlib.pyplot import Rectangle # Used to make dummy legend

# Open CSV File
datafile = open('3DHiiRegions.csv', 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
ldata = list()
vdata = list()
galRad = list()
regNum = list()
index = 0
while index < len(csvFile) :
    galRad.append(float(csvFile[index][0]))
    index += 1

index=0
while index < len(csvFile) :
    if galRad[index] > 3 :
        ldata.append(float(csvFile[index][8]))
        vdata.append(float(csvFile[index][9]))
        if (csvFile[index][10] == str(1)) :
            regNum.append(str('#FF0000'))
        elif csvFile[index][10] == str(2) :
            regNum.append(str('black'))
        elif csvFile[index][10] == str(3) :
            regNum.append(str('y'))
        elif csvFile[index][10] == str(4) :
            regNum.append(str('g'))
        elif csvFile[index][10] == str(5) :
            regNum.append(str('b'))
        elif csvFile[index][10] == str(6) :
            regNum.append(str('#FF9900'))
        elif csvFile[index][10] == str(7) :
            regNum.append(str('#00FF00'))
        elif csvFile[index][10] == str(8) :
            regNum.append(str('#00CCFF'))
    index += 1

p.scatter(ldata,vdata,s=3,facecolor=regNum, lw = 0)
p.xlabel('Galactic Longitude (deg)')
p.ylabel('VLSR (km/s)')
p.title('Longitude-Velocity Plot for Simulated HII Regions')
prox1 = Rectangle((0, 0), 1, 1, fc="#FF0000")
prox2 = Rectangle((0, 0), 1, 1, fc="black")
prox3 = Rectangle((0, 0), 1, 1, fc="y")
prox4 = Rectangle((0, 0), 1, 1, fc="g")
prox5 = Rectangle((0, 0), 1, 1, fc="b")
prox6 = Rectangle((0, 0), 1, 1, fc="#FF9900")
prox7 = Rectangle((0, 0), 1, 1, fc="#00FF00")
prox8 = Rectangle((0, 0), 1, 1, fc="#00CCFF")
p.legend([prox1, prox2,prox3,prox4,prox5,prox6,prox7,prox8], ["Diffuse", "Bar", "3kpc Arm","Ring","Outer Arm", "Outer Scutum-Centaurus Arm","Perseus Arm","Scutum-Centaurus Arm"])
p.savefig('Longitude-Velocity Plot')
p.show()
