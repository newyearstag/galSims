"""
Created on Thurs March 15, 2018
K-S test for comparing simulated HII regions against known population in first quadrant
@author: wparmentrout
"""

import matplotlib as mpl
from scipy import stats
import aplpy as apl
import numpy as np
import montage_wrapper
import matplotlib.pyplot as plt
from astropy.io import fits
import math
import os
import scipy




######################
## INITIALIZE NAMES ##
######################

fluxBins = np.logspace(-1.5,2,59)
#fluxBins = 200

knownRegions = 'wise_test_NEW_updated.csv'
knownFlux = []
knownFlux_binned = []

#simulatedRegions = ['simulated4000.csv','simulated4500.csv','simulated5000.csv','simulated5500.csv','simulated6000.csv','simulated6500.csv','simulated7000.csv','simulated7500.csv','simulated8000.csv','simulated8500.csv','simulated9000.csv','simulated9500.csv','simulated10000.csv','3DHiiRegions_oldReliable.csv']
simulatedRegions = ['3DHiiRegions.csv']
simulatedLum = []
simulatedFlux = []
simulatedFlux_binned = []

(O85,O9,O95,B0,B05,B1,B15,B2) = (48.1,47.9,47.56,47.4,47,46.5,46.1,45.57)

glongmin = 18.
glongmax = 65.

##########################
## IMPORT KNOWN REGIONS ##
##########################

fluxColumn = 89

# Open CSV File
datafile = open(knownRegions, 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
flux = []
index = 1
numHiiRegions = 0

while index < len(csvFile) :
    glong = float(csvFile[index][4])
    if (glong < glongmax) and (glong > glongmin) :
        flux.append(float(csvFile[index][fluxColumn]))
        numHiiRegions += 1
    index += 1
print "There are " + str(numHiiRegions) + " regions in " + str(knownRegions)
knownFlux.append(flux)

## BIN LUMINOSITY ##
counts, bins, bars = plt.hist(flux, normed=False, bins=fluxBins, histtype='step', color='red',linewidth=2)
knownFlux_binned.append(counts)



##############################
## IMPORT SIMULATED REGIONS ##
##############################

i = 0
lumColumn = 5
while i < len(simulatedRegions) :
    # Open CSV File
    datafile = open('multipleSims/'+simulatedRegions[i], 'r')
    csvFile = []
    for row in datafile:
        csvFile.append(row.strip().split(','))

    # Save Galactic Radius Info from CSV to new list
    lum = []
    flux = []
    index = 1
    numHiiRegions = 0

    while index < len(csvFile) :
        glong = float(csvFile[index][8])
        x = float(csvFile[index][1])
        y = float(csvFile[index][2])
        z = float(csvFile[index][3])
        l = float(csvFile[index][lumColumn])
        d2 = math.pow(x,2)+math.pow(y-8.5,2)+math.pow(z,2)
        #logFl = l/4+47
        logFl = l
        fl = pow(10,logFl)
        b = .9688 # Eq 7 Tremblin et al. Assume Te=10^4, freq=1.4 GHz
        flS = fl/(7.603*pow(10,46))*b/d2
        if (glong < glongmax) and (glong > glongmin) and (logFl >= 0):
            flux.append(flS)
            lum.append(l)
        if logFl >= B2:
            numHiiRegions += 1
        index += 1

    print "There are " + str(numHiiRegions) + " regions in " + str(simulatedRegions[i])
    simulatedLum.append(lum)
    simulatedFlux.append(flux)
    i += 1
    
    ## BIN FLUX ##
    counts, bins, bars = plt.hist(flux, normed=False, bins=fluxBins, histtype='step', color='blue',linewidth=2)
    simulatedFlux_binned.append(counts)
#plt.clf()

#print knownFlux_binned
#print simulatedFlux_binned
plt.xscale('log')
plt.yscale('log')
plt.show()


######################
## PERFORM KS TESTS ##
######################

i = 0
while i < len(simulatedRegions):

    #ksTest = stats.ks_2samp(knownFlux[0],simulatedFlux[i])
    ksTest = stats.ks_2samp(knownFlux_binned[0],simulatedFlux_binned[i])

#print "############################"
    print "KS TEST FOR " + simulatedRegions[i]
    print "Statistic = " + str(ksTest[0])
    print "P-Value = " + str(ksTest[1])
    print "############################"
    i += 1



