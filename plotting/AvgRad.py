import matplotlib.pyplot as plt

# Open CSV File from Simulation
datafileS = open('3DHiiRegions.csv', 'r')
csvFileS = []
for row in datafileS:
    csvFileS.append(row.strip().split(','))
# Save Galactic Radius Info from Simulation to new list
print len(csvFileS)
avgR = list()
longS = list()
indexS = 0
srcTot = 0
srcCount = 0
radRunningCount = 0
longStart=-180
longBin=5
longEnd=longStart+longBin
while (indexS < len(csvFileS)) and (longEnd <= 180) :
    lS = float(csvFileS[indexS][8])
    x = float(csvFileS[indexS][1])
    y = float(csvFileS[indexS][2])
    z = float(csvFileS[indexS][3])
    d = pow(pow(x,2)+pow(y-8.5,2)+pow(z,2),0.5) # Distance from sun
    if (lS > longStart) and (lS < longEnd) :
        radRunningCount += d
        srcCount += 1
        srcTot += 1
    indexS += 1
    if (indexS == len(csvFileS)) and (srcCount != 0) :
        longS.append(longStart+longBin/2)
        avgR.append(radRunningCount/srcCount)
        longStart += longBin
        longEnd += longBin
        indexS = 0
        srcCount = 0
        radRunningCount = 0
    elif (indexS == len(csvFileS)) and (srcCount == 0) :
        longStart += longBin
        longEnd += longBin
        indexS = 0
        radRunningCount = 0

# Produce histogram of data
plt.title("Average Distance to HII Regions at Varying Longitudes")
plt.xlabel("Galactic Longitude (deg)")
plt.ylabel("Average Distance (kpc)")
plt.scatter(longS,avgR,s=3,facecolor='0',lw=0)
#plt.yscale('log')
plt.grid(True)
#plt.legend(loc='upper right')
#plt.xticks([-85,-65,-45,-25])
#plt.xticks([0,10,20,30,40,50,60,70,80,90])
plt.xticks([-180,-135,-90,-45,0,45,90,135,180])
plt.gca().invert_xaxis()
plt.savefig('AvgDistvsLong.eps', format='eps', dpi=1000)
plt.show()





