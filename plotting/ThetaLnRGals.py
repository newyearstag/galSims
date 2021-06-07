import pylab as p
import math

# Open CSV File
datafile = open("3DHiiRegions.csv", 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
thetaData = list()
lnRData = list()
index = 0
while index < len(csvFile) :
    x = float(csvFile[index][1])
    y = float(csvFile[index][2])
    theta = math.atan2(y,x)
    r = pow(pow(x,2)+pow(y,2),.5)
    if r > 4 :
        thetaData.append(theta)
        lnRData.append(math.log10(r))
    index += 1

p.scatter(thetaData, lnRData, s=3, facecolor='0', lw = 0)
p.xlabel('Theta (Radians)')
p.ylabel('log(R) (kiloparsecs)')
p.title('Theta Versus Log(R)')
p.savefig(openFile)
p.show()
