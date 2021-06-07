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
index = 0
while index < len(csvFile) :
    galRad.append(float(csvFile[index][0]))
    index += 1

index=0
while index < len(csvFile) :
    if galRad[index] > 3 :
        ldata.append(float(csvFile[index][8]))
        vdata.append(float(csvFile[index][9]))
    index += 1

# Open CSV File
datafileW = open('wise_hii_V1.0.csv', 'r')
csvFileW = []
for row in datafileW:
    csvFileW.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
ldataW = list()
vdataW = list()
indexW = 1

while indexW < len(csvFileW):
    try:
        vdataW.append(float(csvFileW[indexW][9]))
        if float(csvFileW[indexW][2]) > 180 :
            ldataW.append(float(csvFileW[indexW][2])-360)
        else :
            ldataW.append(float(csvFileW[indexW][2]))
    except:
        pass
    indexW += 1



p.scatter(ldataW,vdataW,s=3,facecolor="r", lw = 0)
p.scatter(ldata,vdata,s=3,facecolor="g", lw = 0)
p.xlabel('Galactic Longitude (deg)')
p.ylabel('VLSR (km/s)')
p.title('Longitude-Velocity Plot for WISE and Simulated HII Regions')
prox1 = Rectangle((0, 0), 1, 1, fc="r")
prox2 = Rectangle((0, 0), 1, 1, fc="g")
p.legend([prox1, prox2], ["WISE Data", "Simulated Data"])
p.savefig('Longitude-Velocity Plot Combine')
p.show()
