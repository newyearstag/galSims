import matplotlib.pyplot as plt
import argparse
import matplotlib
import matplotlib.font_manager as font_manager

parser = argparse.ArgumentParser()
parser.add_argument("numberBins", type=int,
                    help="Set number of bins for histogram")
args = parser.parse_args()
numBins = args.numberBins # Prompt User for number of bins

quad1Sim = 0
quad4Sim = 0
quad1Wise = 0
quad4Wise = 0

# Open CSV File from Simulation
datafileS = open('3DHiiRegions.csv', 'r')
csvFileS = []
for row in datafileS:
    csvFileS.append(row.strip().split(','))
# Save Galactic Radius Info from Simulation to new list
dataS = list()
indexS = 0
while indexS < len(csvFileS) :
    lS = float(csvFileS[indexS][8]) 
    dataS.append(lS)
    indexS += 1
    if (lS < 90) and (lS > 0) :
        quad1Sim +=1
    elif (lS < 0) and (lS > -90) :
        quad4Sim +=1

# Open CSV File from Simulation
datafileW = open('wise_hii_V1.3_hrds.csv', 'r')
csvFileW = []
for row in datafileW:
    csvFileW.append(row.strip().split(','))
# Save Galactic Radius Info from WISE data to new list
dataW = list()
indexW = 1
while indexW < len(csvFileW) :
    if (str(csvFileW[indexW][1]) == (" K")) or (str(csvFileW[indexW][1]) == (" G")) or (str(csvFileW[indexW][1]) == (" C")):
        lW = float(csvFileW[indexW][2]) 
        if float(lW) > 180.0 :
            dataW.append(lW-360.0)
        else :
            dataW.append(lW)
        if (lW < 90) and (lW > 0) :
            quad1Wise +=1
        elif (lW < 0) and (lW > -90) :
            quad4Wise +=1
    indexW += 1
print "Length WISE : " + str(len(dataW))
print " "
print "Quadrant 1 Simulation : " + str(quad1Sim)
print "Quadrant 1 WISE : " + str(quad1Wise)
print " "
print "Quadrant 4 Simulation : " + str(quad4Sim)
print "Quadrant 4 WISE : " + str(quad4Wise)

print "Number of Candidates Assuming HRDS Sensitivity : " + str((quad4Sim-500))

# Produce histogram of data
font_prop = font_manager.FontProperties(size=18)
plt.xlabel("X (kpc)", fontproperties=font_prop)
plt.ylabel("Y (kpc)", fontproperties=font_prop)
plt.yticks(fontproperties=font_prop)
plt.xticks(fontproperties=font_prop)
plt.hist(dataS, bins = range(-180,180,10), alpha=0.5, histtype='step', label = "Simulated")
plt.hist(dataW, bins = range(-180,180,5), alpha=0.5, histtype='step', label = "WISE")
plt.title("Longitude Binned HII Regions - WISE and Simulation Comparison")
plt.xlabel("Galactic Longitude (deg)")
plt.grid(True)
plt.ylabel("Number")
plt.legend(loc='upper right',prop=font_prop)
plt.xticks([-180,-135,-90,-45,0,45,90,135,180])
plt.gca().invert_xaxis()
plt.savefig('LongitudeHistogramComparison_18_5degr.eps', format='eps', dpi=1000)
plt.show()





