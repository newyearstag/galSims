import pylab as p
import math
from matplotlib.pyplot import Rectangle # Used to make dummy legend

scol = str('#FF0000') # Sets color of simulated regions
wcol = str('#5FB404') # Sets color of WISE regions


# Open CSV File for Simulated Data
datafileW1 = open('wise_hii_V1.0.csv', 'r')
csvFileW1 = []
for row in datafileW1:
    csvFileW1.append(row.strip().split(','))

# Save x, y, and l Info from Wise Version 1
bDataW1 = list()
lDataW1 = list()
indexW1 = 1

while indexW1 < len(csvFileW1) :
    try :
        bW1 = float(csvFileW1[indexW1][3])
        lW1 = float(csvFileW1[indexW1][2])
        if float(lW1) > 180 :
            lW1 = lW1-360
        else :
            lW1 = lW1
        if (bW1 < 20) and (bW1 > -20):    
            lDataW1.append(lW1)
            bDataW1.append(bW1)
    except :
        pass
    indexW1 += 1






# Open CSV File for Wise Version 3
datafileW3 = open('wise_hii_V1.3_hrds.csv', 'r')
csvFileW3 = []
for row in datafileW3:
    csvFileW3.append(row.strip().split(','))

# Save x, y, and l Info from Simulated Data to new list
bDataW3 = list()
lDataW3 = list()
indexW3 = 1

while indexW3 < len(csvFileW3) :
    try :
        bW3 = float(csvFileW3[indexW3][3])
        lW3 = float(csvFileW3[indexW3][2])
        if float(lW3) > 180 :
            lW3 = lW3-360
        else :
            lW3 = lW3
        if (bW3 < 20) and (bW3 > -20):    
            lDataW3.append(lW3)
            bDataW3.append(bW3)
    except :
        pass
    indexW3 += 1
print lDataW3
p.scatter(lDataW1,bDataW1,s=2,facecolor=scol, lw = 0)
p.scatter(lDataW3,bDataW3,s=2,facecolor=wcol, lw = 0)
p.xlabel('l (deg)')
p.ylabel('b (deg)')
p.title('Galactic Plane Plot from Sun\'s Position')
prox1 = Rectangle((0, 0), 1, 1, fc=scol)
prox2 = Rectangle((0, 0), 1, 1, fc=wcol)
p.legend([prox1, prox2], ["WISE V1", "WISE V3"], loc='lower right')
p.savefig('GalacticPlaneWiseSim_v1_v3.eps', format='eps', dpi=1000)
p.show()
