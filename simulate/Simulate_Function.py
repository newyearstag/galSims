#!/usr/bin/python

from scipy.stats import cauchy
import random
import math
import csv
import numpy as np
import netCDF4 as nc
import argparse

import lvDiagram

'''
parser = argparse.ArgumentParser()
parser.add_argument("numberRegions", type=int,
                    help="Number of HII Regions to Populate in Model")
args = parser.parse_args()
numRegions = args.numberRegions # Prompt User for number of Hii regions
'''

def defaults():

    ff=nc.Dataset('/Users/Marvin/Research/data/larson_radius_hypercube.ncdf') # Import data cube from Tremblin et. al. 2014
    region = 1 # Start count of regions from 1 to NumRegions
    HiiList = [] # Initialize list to store Hii data

    # The following definitions determine which structures will
    # be present in the galaxy and what their relative proportion is.
    # See Hughes et al. ApJ April 2013 for relative proportion in M51
    diffuse = True
    bar = True
    ThreekpcArm = True
    ring = True
    spiral = True
    diffusePercent = 25
    barPercent = 10
    ThreekpcArmPercent = 10
    ringPercent = 10
    spiralPercent = 100 - (diffusePercent + barPercent +
                           ThreekpcArmPercent + ringPercent)
        
    numRegions = 10000
    # Determine Structure of Galaxy
    extentOfBar = 4.4 # Length of bar in kiloparsecs.
    # See Benjamin et al. ApJ Sept 2005.
    cutoff = 3.41#4.1 # Looking to (cutoff)x the bar length.
    # Max value ~6.86 due to model limitation (Tremblin, below)
    galRange = extentOfBar*cutoff
    sunPos = 8.4 # Distance of Sun from GC
    sunHeight = 0.02 # Distance Sun is above galactic plane (kpc) CITE SOURCE!
    circRot = 220 # Solar circular rotation speed. Carroll & Ostlie (24.36)
    v0 = 0 # Initial velocity of source. Only relevant to 3kpc arm.
    galRot = 44.0*math.pi/180.0 # Rotates entire galaxy by (x) degrees.
    # See Benjamin et al. ApJ Sept 2005.
    random.seed( 1 ) # Seed random number generator. (ARBITRARY)
    numSpirals = 4 # Determines Number of Spiral arms
    pitchAngle =  11*math.pi/180 # Determines curvature of arms
    # 7.3 --> See Wu et al. A&A April 2014 for pitch angle estimate in Sagitarrius arm
    warpParam = math.pi/2 # Determines degree of galactic warp
    # DEFINE/CONVERT TO AS ANGLE?
    warpHeight = 0.08 # BY INSPECTION
    maxSpiralRevolutions = 1 # Range for number of spiral revs. (ARBITRARY)
    maxCluster = 10 # Maximum number of regions in a given cluster (ARBITRARY)
    avgCluster = 4 # Most commonly found number of regions in cluster (ARBITRARY)
    clusterRange = 20/1000 # Sets clustered regions to be within (x) pc of each other
    # See Motte et al. ApJ 2002
    sigma = 0.3 # Sets FWHM of spiral arms to (x) kpc
    # 0.2 See Wu et al. A&A April 2014 for deviation
    # from spiral estimate in Sagitarrius arm.
    zmax = .15 # Sets max height in z as +/- (x) kpc
    gamma =0# 0.01365 # Sets spread of Cauchy-Lorentz Z-distribution of regions
    alpha = 0 # Sets HII region drop off as r^-alpha(after bar)

    # Determine Mass of Individual Regions
    # In Units of Stellar Mass. Sets lower bound for ionizing star
    lowerMass = 16
    upperMass = 90

    barAngle=0 # THIS IS NOT USED IN THE CODE. IT DEFINES THE SUN'S STARTING POSITION

    # Output parameters
    (galRad,xRot,yRot,z,mass,lum,age,radius)=(0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)
    (diffLum,barLum,ThreekpcLum,ringLum,sprLum,totLum)=(0.0,0.0,0.0,0.0,0.0,0.0)
    (diffCount,barCount,ThreekpcCount,ringCount,sprCount,totCount)=(0,0,0,0,0,0)

def Simulate(numRegions=numRegions, alpha=alpha, pitchAngle=pitchAngle, numSpirals=numSpirals, extentOfBar=extentOfBar, \
             barAngle=barAngle, scaleHeight=gamma, warpHeight=warpHeight):
    '''
        
        
        
        
        To display the default values for all parameters, call >> help(defaults)
        
        
    '''


    while region <= numRegions :

        v0 = 0
        i = 1
        # Reset i each time to force a region to be populated
        # if all requirements are met.

        selectionParam = random.random()
        # Determines if Hii region is kept or thrown away.
        # Forces population of regions to follow linear trend
        # to end of bar and power law drop-off after bar.

        numCluster = 1
        numClusterTot = random.randrange(1,maxCluster,1)
    
   
        whereIsRegion = random.randrange(1, diffusePercent + barPercent
                                         + ringPercent + ThreekpcArmPercent
                                         + spiralPercent, 1)
        # Determines location of one individual region.

        # HII Region will be randomly populated in Galaxy, but will not be
        # be placed in central region (within bar radius).
        if (whereIsRegion <= diffusePercent) and (diffuse == True) :
            while i != 0 : # This loop forces an Hii region to be populated diffusely
                x = random.gauss(0,galRange/2) # Sets diffuse population to have
                                           # FWHM of galRange/2
                y = random.gauss(0,galRange/2)
                theta = math.atan(x/y)
                galWarp = warpHeight*math.tan(x/galRange*warpParam)*math.cos(y/galRange*warpParam)
                # Models galactic warp with Tan(x)*Cos(y)
                zPos = random.uniform(-zmax,zmax)
                z = galWarp + zPos
                # Produces Cauchy-Lorentz z distribution
                galRad = pow(pow(x,2)+pow(y,2),.5) # Region's distance from center
                i += 1
                if (abs(x) > extentOfBar + random.gauss(0,sigma)) \
                and (galRad < galRange + random.gauss(0,sigma)) \
                and (selectionParam < pow(extentOfBar,alpha)/pow(galRad,alpha)):
                    region += numClusterTot # Increase region count
                    i = 0 # Escape loop
                elif (abs(x) < extentOfBar + random.gauss(0,sigma)) \
                and (extentOfBar < galRad < galRange + random.gauss(0,sigma)) \
                and (selectionParam < pow(extentOfBar,alpha)/pow(galRad,alpha)):
                    region += numClusterTot # Increase region count
                    i = 0 # Escape loop
   
        # Populate in Bar
        elif (whereIsRegion > diffusePercent) \
        and (whereIsRegion <= (diffusePercent + barPercent)) \
        and (bar == True) :
            while i != 0 : # This loop forces an Hii region to be populated in bar
                x = random.uniform(-extentOfBar,extentOfBar) # Returns random number between (-extentOfBar,extentOfBar)
                y = random.gauss(0,sigma) # Sets thickness of bar to (sigma) kpc
                theta = math.atan(x/y)
                galWarp = warpHeight*math.tan(x/galRange*warpParam)*math.cos(y/galRange*warpParam)
                # Models galactic warp with Tan(x)*Cos(y)
                zPos = random.uniform(-zmax,zmax)
                z = galWarp + zPos
                # Produces Cauchy-Lorentz z distribution
                galRad = pow(pow(x,2)+pow(y,2),.5) # Region's distance from center
                i += 1
                if (selectionParam < galRad/extentOfBar) \
                and (galRad < galRange) :
                    region += numClusterTot # Increase region count
                    i = 0 # Escape loop

        # Populate in 3 Kiloparsec Arm
        elif (whereIsRegion > (diffusePercent + barPercent)) \
        and (whereIsRegion <= (diffusePercent + barPercent + ThreekpcArmPercent)) \
        and (ThreekpcArm == True) :
            yRingInt = extentOfBar/2
            ySign = random.randrange(-1,1)
            while i != 0 : # This loop forces an Hii region to be populated in ring
                xCart = random.uniform(-extentOfBar,extentOfBar)
                yCart = math.copysign(yRingInt*pow(1-pow(xCart,2)/pow(extentOfBar,2),.5),ySign) # Produces ring structure
                x = xCart + random.gauss(0, sigma) # Gaussian distribution around ring
                y = yCart + random.gauss(0, sigma)
                theta = math.atan(x/y)
                zPos = random.uniform(-zmax,zmax)
                galWarp = warpHeight*math.tan(x/galRange*warpParam)*math.cos(y/galRange*warpParam) # Models galactic warp with Tan(x)*Cos(y)
                z = galWarp + zPos # EDIT TO Produces Cauchy-Lorentz z distribution
                galRad = pow(pow(x,2)+pow(y,2),.5) # Region's distance from center
                i += 1
                if (selectionParam < galRad/extentOfBar) \
                and (galRad < galRange) :
                    v0 = 56 # Expansion of 3kpc arm
                    region += numClusterTot # Increase region count
                    i = 0 # Escape loop

        # Populate in Ring
        elif (whereIsRegion > (diffusePercent + barPercent + ThreekpcArmPercent)) \
        and (whereIsRegion <= (diffusePercent + barPercent + ThreekpcArmPercent + ringPercent)) \
        and (ring == True) :
            yRingInt = extentOfBar
            ySign = random.randrange(-1,1)
            while i != 0 : # This loop forces an Hii region to be populated in ring
                xCart = random.uniform(-extentOfBar,extentOfBar)
                yCart = math.copysign(yRingInt*pow(1-pow(xCart,2)/pow(extentOfBar,2),.5),ySign) # Produces ring structure
                x = xCart + random.gauss(0, sigma) # Gaussian distribution around ring
                y = yCart + random.gauss(0, sigma)
                theta = math.atan(x/y)
                zPos = random.uniform(-zmax,zmax)
                galWarp = warpHeight*math.tan(x/galRange*warpParam)*math.cos(y/galRange*warpParam) # Models galactic warp with Tan(x)*Cos(y)
                z = galWarp + zPos
                galRad = pow(pow(x,2)+pow(y,2),.5) # Region's distance from center
                i += 1
                if (selectionParam < galRad/extentOfBar) \
                and (galRad < galRange) :
                    region += numClusterTot # Increase region count
                    i = 0 # Escape loop

        # Populate in One of Spirals
        elif (whereIsRegion > (diffusePercent + barPercent + ThreekpcArmPercent + ringPercent)) \
        and (whereIsRegion <= (diffusePercent + barPercent + ThreekpcArmPercent + ringPercent + spiralPercent)) \
        and (spiral == True):
            while i != 0 : # This loop forces an Hii region to be populated in arms
                whichArm = random.randint(0,numSpirals-1)
                theta = random.uniform(0,2*np.pi*maxSpiralRevolutions)
                r = extentOfBar*math.exp(pitchAngle*(1 - .3*math.floor(whichArm/2))*theta) # (.2 ARBITRARY)
                xCart = r*math.cos(theta + np.pi*math.fmod(whichArm,2))
                yCart = r*math.sin(theta + np.pi*math.fmod(whichArm,2))
                x = xCart + random.gauss(0,sigma) # Gaussian distribution around spiral
                y = yCart + random.gauss(0,sigma)
                galWarp = warpHeight*math.tan(x/galRange*warpParam)*math.cos(y/galRange*warpParam) # Models galactic warp with Tan(x)*Cos(y)
                zPos = random.uniform(-zmax,zmax)
                z = galWarp + zPos
                galRad = pow(pow(x,2)+pow(y,2),.5) # Region's distance from center in kpc
                i += 1
                if (galRad < galRange) \
                and (selectionParam < pow(extentOfBar,alpha)/pow(galRad,alpha)) :
                    region += numClusterTot # Increase region count
                    i = 0 # Escape Loop
                
        # Determine individual region parameters and write to list
        while (i == 0) and (numCluster <= numClusterTot) :
            # Set Time Distribution
            timeParam = random.randint(0,99)
            age = timeParam*.127 # Age in Myr (12.7 Myr limit) in Trebmlin model

            # Set Host Star Mass Distribution
            massParam = random.random() # Used in forcing powerlaw fit
            while massParam != 0 :
                mass = random.randrange(lowerMass,upperMass)
                IMF = pow(lowerMass,2.35)*pow(mass,-2.35)
                lifetime = pow(lowerMass,.935)*pow(mass,-.935)
                numHiiRegions = IMF*lifetime
                if numHiiRegions > massParam : # Makes power law fit
                    massParam = 0 # Escape loop

            # Set Host Star Flux Distribution
            fluxMin = math.log10(pow(lowerMass,1.94))
            fluxMax = math.log10(pow(upperMass,1.94))
            fluxParam = int(round((math.log10(pow(mass,1.94))-fluxMin)/(fluxMax-fluxMin)*16,0)) # Use this line to access all values of Lum from 10^47 - 10^51
#           fluxParam = int(round((math.log10(pow(mass,1.94))-fluxMin)/(fluxMax-fluxMin)*12,0)+4)
            lum = fluxParam
        
            # Set Electron Temperature Distribution
            # Relationship taken from Balser et.al. 2011, put in range accepted by Tremblin model
            TeParam = int(round((5756 + 303*random.uniform(-1,1)) + galRad*(299 + 31*random.uniform(-1,1)),-3)/1000 - 5)

            # Set Neutral Hydrogen Density Distribution
            densityParam = random.randint(0,10)

            # From Distributions, Determine HII Region Radius
            # Using Pascal Tremblin's hypercube data
            radius = ff.variables['radius'][timeParam,fluxParam,TeParam,densityParam]

            # Rotate galaxy
            xRot = x*math.cos(galRot) - y*math.sin(galRot)
            yRot = x*math.sin(galRot) + y*math.cos(galRot)
 
            # Set velocity of source
            omega = circRot/galRad # Assume flat rotation curve.
            omega0 = circRot/sunPos
            dist = pow(pow(xRot,2)+pow(yRot-sunPos,2),0.5)
            l = math.copysign(math.acos((pow(dist,2)+pow(sunPos,2)-pow(galRad,2))/(2*sunPos*dist))*180/math.pi,xRot)
            b = math.atan((z-sunHeight)/dist)
            vR = (omega - omega0)*sunPos*math.sin(l*math.pi/180)+v0*math.cos(theta)

            # This section allows the user to test various parameters for easy
            # output to terminal (e.g. luminosity of various features, counts
            # of regions in spiral versus bar, etc.)
            if (whereIsRegion <= diffusePercent) \
            and (diffuse == True) :
                diffLum = diffLum + lum
                diffCount += 1
                regNum = 1
            elif (whereIsRegion > diffusePercent) \
            and (whereIsRegion <= (diffusePercent + barPercent)) \
            and (bar == True) :
                barLum = barLum + lum
                barCount += 1
                regNum = 2
            elif (whereIsRegion > (diffusePercent + barPercent)) \
            and (whereIsRegion <= (diffusePercent + barPercent + ThreekpcArmPercent)) \
            and (ThreekpcArm == True) :
                ThreekpcLum = ThreekpcLum + lum
                ThreekpcCount += 1
                regNum = 3
            elif (whereIsRegion > (diffusePercent + barPercent + ThreekpcArmPercent)) \
            and (whereIsRegion <= (diffusePercent + barPercent + ThreekpcArmPercent + ringPercent)) \
            and (ring == True) :
                ringLum = ringLum + lum
                ringCount += 1
                regNum = 4
            elif (whereIsRegion > (diffusePercent + barPercent + ThreekpcArmPercent + ringPercent)) \
            and (whereIsRegion <= (diffusePercent + barPercent + ThreekpcArmPercent + ringPercent + spiralPercent)) \
            and (spiral == True):
                sprLum = sprLum + lum
                sprCount += 1
                if whichArm == 0 :
                    regNum = 5
                elif whichArm == 1 :
                    regNum = 6
                elif whichArm == 2 :
                    regNum = 7
                elif whichArm == 3 :
                    regNum = 8
            totLum = totLum + lum

            # Append information to CSV file
            HiiList.append([galRad,xRot,yRot,z,mass,lum,age,radius,l,vR,regNum,b])

            numCluster += 1
    
    with open("3DHiiRegions.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(HiiList)
    
    print "Diffuse Luminosity : " + str(diffLum*100/totLum) + "% (" + str(diffCount) + " Regions)"
    print "Bar Luminosity : " + str(barLum*100/totLum) + "% (" + str(barCount) + " Regions)"
    print "3 kpc Arm Luminosity : " + str(ThreekpcLum*100/totLum) + "% ("+ str(ThreekpcCount) + " Regions)"
    print "Ring Luminosity : " + str(ringLum*100/totLum) + "% ("+ str(ringCount) + " Regions)"
    print "Spiral Luminosity : " + str(sprLum*100/totLum) + "% (" + str(sprCount) + " Regions)"
    print "Total Luminosity : " + str((barLum+ThreekpcLum+ringLum+sprLum+diffLum)*100/totLum) + "% (" + str(barCount+ThreekpcCount+ringCount+sprCount+diffCount) + " Regions)"


def main(numRegions=numRegions, alpha=alpha, pitchAngle=pitchAngle, numSpirals=numSpirals, extentOfBar=extentOfBar, \
         barAngle=barAngle, scaleHeight=gamma, warpHeight=warpHeight):

    defaults()
    # This will not work as expected. It will use all values from the defaults() function
    Simulate(numRegions=numRegions, alpha=alpha, pitchAngle=pitchAngle, numSpirals=numSpirals, extentOfBar=extentOfBar, \
             barAngle=barAngle, scaleHeight=gamma, warpHeight=warpHeight)
    # UPDATE PLOTS
    lvDiagram.lvDiagram()

main()
