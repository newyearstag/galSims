import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.pyplot import Rectangle # Used to make dummy legend
import math

# Open CSV File

datafileS = open('3DHiiRegions.csv', 'r')
csvFileS = []
for row in datafileS:
    csvFileS.append(row.strip().split(','))

xdataS = list()
ydataS = list()
zdataS = list()
indexS = 0
while indexS < len(csvFileS) :
    xdataS.append(float(csvFileS[indexS][1]))
    ydataS.append(float(csvFileS[indexS][2]))
    zdataS.append(float(csvFileS[indexS][3]))
    indexS += 1


datafileW = open('wise_hii_V1.0.csv', 'r')
csvFileW = []
for row in datafileW:
    csvFileW.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
xdataW = list()
ydataW = list()
zdataW = list()
indexW = 1

# GLong in column 2
# GLat in column 3
# Distance in Column 13

while indexW < len(csvFileW) :
    try:
        d = float(csvFileW[indexW][13])
        l = (float(csvFileW[indexW][2])+90)*math.pi/180
        b = math.pi/2-float(csvFileW[indexW][3])*math.pi/180
        xdataW.append(d*math.sin(b)*math.cos(l))
        ydataW.append(d*math.sin(b)*math.sin(l)-8.4)
        zdataW.append(d*math.cos(b))
    except:
        pass
    indexW += 1

fig=p.figure()
ax = p3.Axes3D(fig)
comb = ax.scatter(xdataS, ydataS, zdataS, s=3, label='Simulated Regions', facecolor='r', lw = 0)
orig = ax.scatter(xdataW, ydataW, zdataW, s=3, label='Wise Data', facecolor='g', lw = 0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
prox1 = Rectangle((0, 0), 1, 1, fc="g")
prox2 = Rectangle((0, 0), 1, 1, fc="r")
ax.legend([prox1, prox2], ["Wise Data", "Simulated Regions"])
p.show()
