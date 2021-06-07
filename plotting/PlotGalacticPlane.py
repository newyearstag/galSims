import pylab as p
from matplotlib.pyplot import Rectangle # Used to make dummy legend

# Open CSV File
datafile = open('3DHiiRegions.csv', 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
ldata = list()
bdata = list()
sizedata = list()
index = 0
while index < len(csvFile) :
    ldata.append(float(csvFile[index][8]))
    bdata.append(float(csvFile[index][11]))
    sizedata.append(float(float(csvFile[index][7])/float(csvFile[index][0])))
    index += 1


p.scatter(ldata,bdata,s=sizedata, lw = 0)
p.xlabel('l (deg)')
p.ylabel('b (deg)')
p.title('3D HII Region Simulation - View From Position of Sun')
p.savefig('GalacticPlanePlot.eps', format='eps', dpi=1000)
p.show()
