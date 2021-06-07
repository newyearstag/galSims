import matplotlib.pyplot as plt
from scipy.stats import norm
import powerlaw
import matplotlib.mlab as mlab
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("numberBins", type=int,
                    help="Set number of bins for histogram")
args = parser.parse_args()
numBins = args.numberBins # Prompt User for number of bins

# Open CSV File
datafile = open('3DHiiRegions.csv', 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
data = list()
dataAnalysis = list()
index = 0
while index < len(csvFile) :
    radIndex = float(csvFile[index][0])
    data.append(radIndex)
    index += 1

fit = powerlaw.Fit(data,xmin=4.5)
fit.power_law.plot_pdf(color='g', linestyle='--')
fit2 = powerlaw.Fit(data,xmin=(4,5))
fit2.power_law.plot_pdf(color='r', linestyle='--')

plt.hist(data, bins=numBins, histtype='step',normed=True)

plt.title("Distribution of HII Regions in 3D Galaxy Simulation")
plt.xlabel("Galactocentric Radius")
plt.ylabel("HII Region Count")
print "Alpha (green) = " + str(fit.power_law.alpha)
print "Kolmogorov-Smirnov Distance (green) = " + str(fit.power_law.D)
print "Alpha (red) = " + str(fit2.power_law.alpha)
print "Kolmogorov-Smirnov Distance (red) = " + str(fit2.power_law.D)
plt.show()
