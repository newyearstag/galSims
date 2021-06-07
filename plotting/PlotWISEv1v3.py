import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.pyplot import Rectangle # Used to make dummy legend
import math

# Open CSV File

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


datafileW3 = open('wise_hii_V1.3_hrds.csv', 'r')
csvFileW3 = []
for row in datafileW3:
    csvFileW3.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
xdataW3 = list()
ydataW3 = list()
zdataW3 = list()
indexW3 = 1

# GLong in column 2
# GLat in column 3
# Distance in Column 13

while indexW3 < len(csvFileW3) :
    try:
        d = float(csvFileW3[indexW3][32])
        l = (float(csvFileW3[indexW3][2])+90)*math.pi/180
        b = math.pi/2-float(csvFileW3[indexW3][3])*math.pi/180
        xdataW3.append(d*math.sin(b)*math.cos(l))
        ydataW3.append(d*math.sin(b)*math.sin(l)-8.4)
        zdataW3.append(d*math.cos(b))
    except:
        pass
    indexW3 += 1

fig=p.figure()
ax = p3.Axes3D(fig)
orig = ax.scatter(xdataW, ydataW, zdataW, s=10, label='Wise Data v1', facecolor='g', lw = 0)
comb = ax.scatter(xdataW3, ydataW3, zdataW3, s=10, label='Wise Data v3', facecolor='r', lw = 0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
prox1 = Rectangle((0, 0), 1, 1, fc="g")
prox2 = Rectangle((0, 0), 1, 1, fc="r")
ax.legend([prox1, prox2], ["Wise Data v1", "Wise Data v3"])
p.show()
