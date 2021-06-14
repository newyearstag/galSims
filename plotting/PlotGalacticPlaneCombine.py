import pylab as p
from matplotlib.pyplot import Rectangle # Used to make dummy legend

ocol = str('#FF0000') # Sets color of original regions
ccol = str('#5FB404') # Sets color of clustered regions

# Open CSV File
datafile = open(r'C:\Users\newye\OneDrive\Documents\GitHub\galSims\misc\3DHiiRegions.csv', 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))
print (len(csvFile))

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


# Open CSV File
#datafileC = open('3DHiiRegionsAngularCombine.csv', 'r')
datafileC = open(r'C:\Users\newye\OneDrive\Documents\GitHub\galSims\misc\3DHiiRegions.csv', 'r')
csvFileC = []
for row in datafileC:
    csvFileC.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
ldataC = list()
bdataC = list()
sizedataC = list()
indexC = 0
while indexC < len(csvFileC) :
    ldataC.append(float(csvFileC[indexC][8]))
    bdataC.append(float(csvFileC[indexC][11]))
    sizedataC.append(float(float(csvFileC[indexC][7])/float(csvFileC[indexC][0])))
    indexC += 1

p.scatter(ldata,bdata,s=sizedata,facecolor=ocol, lw = 0)
p.scatter(ldataC,bdataC,s=sizedataC,facecolor=ccol, lw = 0)
p.xlabel('l (deg)')
p.ylabel('b (deg)')
p.title('3D HII Region Simulation - View From Position of Sun')
prox1 = Rectangle((0, 0), 1, 1, fc=ocol)
prox2 = Rectangle((0, 0), 1, 1, fc=ccol)
p.legend([prox1, prox2], ["Original", "Clustered"], loc='lower right')
#p.savefig('GalacticPlanePlotCombine.eps', format='eps', dpi=1000)
p.show()
