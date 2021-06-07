import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.pyplot import Rectangle # Used to make dummy legend

# Open CSV File
datafile = open('3DHiiRegions.csv', 'r')
datafileCombine = open('3DHiiRegionsCombine.csv', 'r')
csvFile = []
csvFileCombine = []
for row in datafile:
    csvFile.append(row.strip().split(','))

for row in datafileCombine:
    csvFileCombine.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
xdata = list()
ydata = list()
zdata = list()
rad = list()
index = 0
while index < len(csvFile) :
    xdata.append(float(csvFile[index][1]))
    ydata.append(float(csvFile[index][2]))
    zdata.append(float(csvFile[index][3]))
    rad.append(float(csvFile[index][7]))
    index += 1

xdataCombine = list()
ydataCombine = list()
zdataCombine = list()
radCombine = list()
index = 0
while index < len(csvFileCombine) :
    xdataCombine.append(float(csvFileCombine[index][1]))
    ydataCombine.append(float(csvFileCombine[index][2]))
    zdataCombine.append(float(csvFileCombine[index][3]))
    radCombine.append(float(csvFileCombine[index][7]))
    index += 1

fig=p.figure()
ax = p3.Axes3D(fig)
ax = p3.Axes3D(fig)
orig = ax.scatter(xdata, ydata, zdata, s=rad, label='Original Simulation', facecolor='g', lw = 0)
comb = ax.scatter(xdataCombine, ydataCombine, zdataCombine, s=radCombine, label='Clustered Regions', facecolor='r', lw = 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
prox1 = Rectangle((0, 0), 1, 1, fc="g")
prox2 = Rectangle((0, 0), 1, 1, fc="r")
ax.legend([prox1, prox2], ["Original Regions", "Clustered Regions"])
p.show()
