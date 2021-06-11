import matplotlib.pyplot as plt
import argparse
import matplotlib
import matplotlib.font_manager as font_manager
import numpy as np
import math

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()

wise_color = 'black'
sim_color = 'red'


northMin = 18
northMax = 65

# Open CSV File from Simulation
#datafileS = open('../MASTER_DISTRIBUTIONS/3DHiiRegions.csv', 'r')
datafileS = open('../MASTER_DISTRIBUTIONS/HIIregion_popSynthesis.csv', 'r')
csvFileS = []
for row in datafileS:
    csvFileS.append(row.strip().split(','))
# Save Galactic Radius Info from Simulation to new list
(R_gal_sim,x_sim,y_sim,z_sim,mass_sim,N_ly_sim,age_sim,rad_sim,l_sim,vR_sim,regNum_sim,b_sim,flux_sim,dist_sim,rad_wise_angular,rad_sim_angular) = (list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list())
indexS = 0
while indexS < len(csvFileS) :
    long = float(csvFileS[indexS][8])
    if (long>northMin) and (long<northMax):
        x=float(csvFileS[indexS][1])
        y=float(csvFileS[indexS][2])
        z=float(csvFileS[indexS][3])
        dist=float(pow(x**2+(y-8.4)**2+z**2,.5))
        rad_pc = float(csvFileS[indexS][7])*2.
        rad_angular = rad_pc/dist/1000.*3600.*180./math.pi/60. #in arcmin
        
        R_gal_sim.append(float(csvFileS[indexS][0]))
        x_sim.append(x)
        y_sim.append(y)
        z_sim.append(z*1000)
        mass_sim.append(float(csvFileS[indexS][4]))
        N_ly_sim.append(float(csvFileS[indexS][5]))
        age_sim.append(float(csvFileS[indexS][6]))
        rad_sim.append(rad_pc*2)
        rad_sim_angular.append(rad_angular*2)
        l_sim.append(float(csvFileS[indexS][8]))
        vR_sim.append(float(csvFileS[indexS][9]))
        regNum_sim.append(float(csvFileS[indexS][10]))
        b_sim.append(float(csvFileS[indexS][11]))
        flux_sim.append(float(csvFileS[indexS][12]))
        dist_sim.append(dist)
    indexS += 1

# Open CSV File from WISE
'''
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
'''
# WISE CATALOG, VERSION 1.3
'''
datafileW = open('../MASTER_DISTRIBUTIONS/wise_hii_V1.3_hrds.csv', 'r')
csvFileW = []
for row in datafileW:
    csvFileW.append(row.strip().split(','))
# Save Galactic Radius Info from WISE data to new list
(R_gal_wise,x_wise,y_wise,z_wise,mass_wise,N_ly_wise,age_wise,rad_wise,l_wise,vR_wise,regNum_wise,b_wise,flux_wise,dist_wise) = (list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list())
indexW = 1
while indexW < len(csvFileW) :
    rad_wise.append(float(csvFileW[indexW][4]))
    l_wise.append(float(csvFileW[indexW][2]))

    dist = float(csvFileW[indexW][32])
    if (dist > 0):
        z_wise.append(float(csvFileW[indexW][34]))
        dist_wise.append(dist)
        R_gal_wise.append(float(csvFileW[indexW][29]))
    indexW += 1
'''
# WISE CATALOG, VERSION 2
datafileW = open('../MASTER_DISTRIBUTIONS/wise_hii_V2.0_hrds.csv', 'r')
csvFileW = []
for row in datafileW:
    csvFileW.append(row.strip().split(','))
# Save Galactic Radius Info from WISE data to new list
(R_gal_wise,x_wise,y_wise,z_wise,mass_wise,N_ly_wise,age_wise,rad_wise,l_wise,vR_wise,regNum_wise,b_wise,flux_wise,dist_wise) = (list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list())
indexW = 1
while indexW < len(csvFileW) :
    long = float(csvFileW[indexW][3])
    if (long>northMin) and (long<northMax):
        dist = float(csvFileW[indexW][40])
        rad_arcsec = float(csvFileW[indexW][5])
        rad_wise_angular.append(rad_arcsec/60.) # in arcmin
        rad_pc = rad_arcsec/3600*3.14159/180.*dist*1000

        if rad_pc > 0. :
            rad_wise.append(rad_pc)
        l_wise.append(float(csvFileW[indexW][3]))

        if (dist > 0):
            z_wise.append(float(csvFileW[indexW][45]))
            dist_wise.append(dist)
            R_gal_wise.append(float(csvFileW[indexW][37]))
        '''
        if (str(csvFileW[indexW][1]) == (" K")) or (str(csvFileW[indexW][1]) == (" G")) or (str(csvFileW[indexW][1]) == (" C")):
            z_wise.append(float(csvFileW[indexW][2]))
            dist_wise.append(float(csvFileW[indexW][32]))
            R_gal_wise.append(float(csvFileW[indexW][29]))
        '''
    indexW += 1





## R_Gal Histogram ##
n_bins = 100
ax0.hist(R_gal_sim, n_bins, normed=1, range=[0,20], histtype='bar', color = sim_color, label = '')
ax0.hist(R_gal_wise, n_bins, normed=1, range=[0,20], histtype='step', color = wise_color, label = '')
#ax0.legend(prop={'size': 10})
ax0.set_xlabel('Galactocentric Radius (kpc)')

#ax0.cdf(R_gal_sim, n_bins, normed=1, range=[0,16], color = sim_color, label = '')




## Heliocentric Distance ##
n_bins = 100
ax1.hist(dist_sim, n_bins, normed=1, range=[0,30], histtype='bar', color = sim_color, label = '')
ax1.hist(dist_wise, n_bins, normed=1, range=[0,30], histtype='step', color = wise_color, label = '')
ax1.set_xlabel('Heliocentric Distance (kpc)')


    
## z Height ##
n_bins = 100
ax2.hist(z_sim*1000, n_bins, range=[-100,100], normed=1, histtype='bar', color = sim_color, label = '')
ax2.hist(z_wise, n_bins, range=[-100,100], normed=1, histtype='step', color = wise_color, label = '')
ax2.set_xlabel('z-Height (pc)')

'''
## Size ##
# MAKE SURE THIS IS REALLY DIAMETER
# NOTE: In one version of the simulation code, all sizes are 1
n_bins = 100
ax3.hist(rad_sim, n_bins, range=[0,25], normed=1, histtype='bar', color = sim_color, label = '')
ax3.hist(rad_wise, n_bins, range=[0,25], normed=1, histtype='step', color = wise_color, label = '')
ax3.set_title('Diameter (pc)')
'''

## Size (arcmin) ##
# MAKE SURE THIS IS REALLY DIAMETER
# NOTE: In one version of the simulation code, all sizes are 1
n_bins = 100
ax3.hist(rad_sim_angular, n_bins, range=[0,10], normed=1, histtype='bar', color = sim_color, label = '')
ax3.hist(rad_wise_angular, n_bins, range=[0,10], normed=1, histtype='step', color = wise_color, label = '')
ax3.set_xlabel('Angular Diameter (arcmin)')



fig.tight_layout()
plt.show()
fig.savefig('PropertyHistograms.eps', format='eps', dpi=1000)
fig.savefig('PropertyHistograms.png', format='png', dpi=1000)



'''
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
'''




