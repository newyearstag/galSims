import matplotlib.pyplot as plt
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("location", type=str,
                    help="Options : gc, sun")
parser.add_argument("numberBins", type=int,
                    help="Set number of bins for histogram")
parser.add_argument("minDistance", type=int,
                    help="Set minimum search distance from location (kpc)")
parser.add_argument("maxDistance", type=int,
                    help="Set maximum search distance from location (kpc)")
args = parser.parse_args()
loc = args.location # Prompt User for location
numBins = args.numberBins # Prompt User for location
minDist = args.minDistance # Prompt User for minimum search distance
maxDist = args.maxDistance # Prompt User for maximum search distance

# Open CSV File
datafile = open('3DHiiRegions.csv', 'r')
if loc == "gc" :
    pos = 0
if loc == "sun" :
    pos = 8.4 # Sun is set 8.4 kpc from the galactic center
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
thetaData = list()
index = 0
while index < len(csvFile) :
    x = float(csvFile[index][1])
    y = float(csvFile[index][2]) + pos
    dist = pow(pow(x,2)+pow(y,2),.5)
    theta = math.atan2(x,y)
    if (dist > minDist) and (dist < maxDist) :
        thetaData.append(theta)
    index += 1

# Produce histogram of data
plt.hist(thetaData, bins=numBins, histtype='step')
plt.title("Distribution of HII Regions in 3D Galaxy Simulation")
plt.xlabel("")
plt.ylabel("HII Region Count")
plt.tick_params(\
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off') # labels along the bottom edge are off
plt.show()
