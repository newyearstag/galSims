#!/usr/bin/python

from scipy.stats import cauchy
import random
import math
import csv
import numpy as np
#import netCDF4 as nc
import argparse
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#import plotly.plotly as py
#import plotly.graph_objs as go


#####################################################
## TAKE IN NUMBER OF HII REGIONS FROM COMMAND LINE ##
#####################################################

parser = argparse.ArgumentParser()
parser.add_argument("numberRegions", type=int,
                    help="Number of HII Regions to Populate in Model")
args = parser.parse_args()
numRegions = args.numberRegions # Prompt User for number of Hii regions



############
## SETUP  ##
############


useTremblin = False # Use the Tremblin 2014 model to determine HII region sizes
plot3D = False # Use Plotly to create interactive 3D plots of the HII region distribution

if useTremblin == True :
    import netCDF4 as nc
    ff=nc.Dataset('/Users/Marvin/Research/Projects/GalSims/3D/larson_radius_hypercube.ncdf') # Import data cube from Tremblin et. al. 2014

region = 1 # Start count of regions from 1 to NumRegions
HiiList = [] # Initialize list to store Hii data
(galRad,xRot,yRot,z,mass,lum,age,radius)=(0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)
(diffLum,barLum,ThreekpcLum,sprLum,totLum)=(0.0,0.0,0.0,0.0,0.0)
(diffCount,barCount,ThreekpcCount,sprCount,totCount)=(0,0,0,0,0)


###############################################
## TURN ON / OFF VARIOUS GALACTIC STRUCTURES ##
###############################################

# The following definitions determine which structures will
# be present in the galaxy and what their relative proportion is.
# See Hughes et al. ApJ April 2013 for relative proportion in M51
diffuse = True
bar = True
ThreekpcArm = True
spiral = True
diffusePercent = 25
barPercent = 10
ThreekpcArmPercent = 10
spiralPercent = 100 - (diffusePercent + barPercent +
                       ThreekpcArmPercent)

###########################
## STRUCTURAL PARAMETERS ##
###########################

extentOfBar = 4.4 # Length of bar in kiloparsecs.
                  # See Benjamin et al. ApJ Sept 2005.
cutoff = 3.41#4.1 # Looking to (cutoff)x the bar length.
              # Max value ~6.86 due to model limitation (Tremblin, below)
galRange = extentOfBar*cutoff
sunPos = 8.4 # Distance of Sun from GC
sunHeight = 0.02 # Distance of Sun above galactic plane (kpc) (Humphreys 1995)
circRot = 220 # Solar circular rotation speed. Carroll & Ostlie (24.36)
v0 = 0 # Initial velocity of source. Only relevant to 3kpc arm.
galRot = 44.0*math.pi/180.0 # Rotates entire galaxy by (x) degrees.
                            # See Benjamin et al. ApJ Sept 2005.
random.seed( 1 ) # Seed random number generator. (ARBITRARY)
numSpirals = 4 # Determines Number of Spiral arms
pitchAngle =  12.*math.pi/180. # Determines curvature of arms
    # 7.3 deg --> See Wu et al. A&A April 2014 for pitch angle estimate in Sagitarrius arm
    # Vallee 2014 gives pitch angle of 12 deg.
warpParam = math.pi/2 # Determines degree of Galactic warp
    # DEFINE/CONVERT TO AS ANGLE?
warpHeight = 0.08 # BY INSPECTION
maxSpiralRevolutions = 1.25 # Range for number of spiral revs. (ARBITRARY)
maxCluster = 2 # Maximum number of regions in a given cluster (ARBITRARY)
avgCluster = 1 # Most commonly found number of regions in cluster (ARBITRARY)
clusterRange = 20/1000 # Sets clustered regions to be within (x) pc of each other
                       # See Motte et al. ApJ 2002
sigma = 0.8/2.35 # Sets FWHM of spiral arms to (x) kpc
            # 200 pc See Wu et al. A&A April 2014 for deviation
            # from spiral estimate in Sagitarrius arm.
            # Vallee 2014 gives width of 400 pc "from mid arm to dust lane"
            # Therefore, FWHM would be 800 pc and sigma = .800/2.35
zmax = .15/5 # Sets max height in z as +/- (x) kpc
gamma =0# 0.01365 # Sets spread of Cauchy-Lorentz Z-distribution of regions
alpha = 0 # Sets HII region drop off as r^-alpha(after bar)

# Mass Limits, In Units of Stellar Mass. Sets lower bound for ionizing star
#(lowerMass, upperMass) = (10, 90)
(lowerMass, upperMass) = (9, 90)

while region <= numRegions :

    ########################
    ## RESET INDICES, ETC ##
    ########################
    
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
                                     + ThreekpcArmPercent
                                     + spiralPercent, 1)
        # Determines location of one individual region.

    ##################
    ## DIFFUSE HALO ##
    ##################

    # HII Region will be randomly populated in Galaxy, but will not be
    # be placed in central region (within bar radius).
    
    if (whereIsRegion <= diffusePercent) and (diffuse == True) : 
        while i != 0 : # This loop forces an Hii region to be populated diffusely
            x = random.gauss(0,galRange/2) # Sets diffuse population to have
                                           # FWHM of galRange/2
            y = random.gauss(0,galRange/2)
            theta = math.atan(x/y)
            galRad = pow(pow(x,2)+pow(y,2),.5)# Region's distance from center
            if galRad > 11 :
                galWarp = ((galRad-11)/6)*math.sin(theta)+0.3*(((galRad-11)/6)**2)*(1-math.cos(2*theta))
            else :
                galWarp = 0
            zpos = cauchy.rvs(loc=0,scale=zmax,size=1,random_state=None)[0]
            z = zpos + galWarp # Produces Cauchy-Lorentz z distribution
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
   
    ##################
    ## GALACTIC BAR ##
    ##################

    elif (whereIsRegion > diffusePercent) \
    and (whereIsRegion <= (diffusePercent + barPercent)) \
    and (bar == True) :
        while i != 0 : # This loop forces an Hii region to be populated in bar
            x = random.uniform(-extentOfBar,extentOfBar)+ random.gauss(0,sigma) # Returns random number between (-extentOfBar,extentOfBar)
            y = random.gauss(0,sigma) # Sets thickness of bar to (sigma) kpc
            theta = math.atan(x/y)
            galRad = pow(pow(x,2)+pow(y,2),.5)# Region's distance from center
            galWarp = 0 # No warp assigned within R_Gal = 11 kpc
            zPos = cauchy.rvs(loc=0,scale=zmax,size=1,random_state=None)[0]
            z = galWarp + zPos
                # Produces Cauchy-Lorentz z distribution
            galRad = pow(pow(x,2)+pow(y,2),.5) # Region's distance from center
            i += 1
            if (selectionParam < galRad/(extentOfBar)) \
            and (galRad < galRange) :
                region += numClusterTot # Increase region count
                i = 0 # Escape loop
                # Note: Distribution was slightly higher than observed. Dropped with 0.9 factor.


    ######################
    ## 3 KILOPARSEC ARM ##
    ######################

    elif (whereIsRegion > (diffusePercent + barPercent)) \
    and (whereIsRegion <= (diffusePercent + barPercent + ThreekpcArmPercent)) \
    and (ThreekpcArm == True) :
        yInt = extentOfBar/2
        ySign = random.randrange(-1,1)
        while i != 0 : # This loop forces an Hii region to be populated in 3 kpc arm
            xCart = random.uniform(-extentOfBar,extentOfBar)
            yCart = math.copysign(yInt*pow(1-pow(xCart,2)/pow(extentOfBar,2),.5),ySign) # Produces 3 kpc arm structure
            x = xCart + random.gauss(0, sigma) # Gaussian distribution around 3 kpc arm
            y = yCart + random.gauss(0, sigma)
            theta = math.atan(x/y)
            zPos = cauchy.rvs(loc=0,scale=zmax,size=1,random_state=None)[0]
            galWarp = 0 # No warp assigned within R_Gal = 11 kpc
            z = galWarp + zPos # EDIT TO Produces Cauchy-Lorentz z distribution
            galRad = pow(pow(x,2)+pow(y,2),.5) # Region's distance from center
            i += 1
            if (selectionParam < galRad/extentOfBar) \
            and (galRad < galRange) :
                v0 = 53 # Expansion of 3kpc arm
                region += numClusterTot # Increase region count
                i = 0 # Escape loop

    #################
    ## SPIRAL ARMS ##
    #################

    elif (whereIsRegion > (diffusePercent + barPercent + ThreekpcArmPercent)) \
    and (whereIsRegion <= (diffusePercent + barPercent + ThreekpcArmPercent + spiralPercent)) \
    and (spiral == True):
        while i != 0 : # This loop forces an Hii region to be populated in arms
            whichArm = random.randint(0,numSpirals-1)
            theta = random.uniform(0,2*np.pi*maxSpiralRevolutions)
            r = extentOfBar*math.exp(pitchAngle*(1 + 0.5*math.floor(whichArm/2))*theta) # (.2 ARBITRARY)
            xCart = r*math.cos(theta + np.pi*math.fmod(whichArm,2))
            yCart = r*math.sin(theta + np.pi*math.fmod(whichArm,2))
            x = xCart + random.gauss(0,sigma) # Gaussian distribution around spiral
            y = yCart + random.gauss(0,sigma)
            #theta = math.atan(x/y)
            galRad = pow(pow(x,2)+pow(y,2),.5)# Region's distance from center
            if galRad > 11 :
                galWarp = ((galRad-11)/6)*math.sin(theta)+0.3*(((galRad-11)/6)**2)*(1-math.cos(2*theta))
            else :
                galWarp = 0
            zPos = cauchy.rvs(loc=0,scale=zmax,size=1,random_state=None)[0]
            z = galWarp + zPos
            galRad = pow(pow(x,2)+pow(y,2),.5) # Region's distance from center in kpc
            i += 1
            if (galRad < galRange) \
            and (selectionParam < pow(extentOfBar,alpha)/pow(galRad,alpha)) :  
                region += numClusterTot # Increase region count
                i = 0 # Escape Loop


    ############################################
    ## DETERMINE INDIVIDUAL REGION PARAMETERS ##
    ############################################

    while (i == 0) and (numCluster <= numClusterTot) :
        
        #######################################
        ## UPDATE REGION POSITION / DISTANCE ##
        #######################################
        
        # Rotate galaxy to match Milky Way's rotation
        xRot = x*math.cos(galRot) - y*math.sin(galRot)
        yRot = x*math.sin(galRot) + y*math.cos(galRot)
        
        # Determine Distance and Galactic Coordinates
        dist = pow(pow(xRot,2)+pow(yRot-sunPos,2),0.5)
        l = math.copysign(math.acos((pow(dist,2)+pow(sunPos,2)-pow(galRad,2))/(2*sunPos*dist))*180/math.pi,xRot)
        b = math.atan((z-sunHeight)/dist)
        
        # Set velocity of source
        omega = circRot/galRad # Assume flat rotation curve.
        omega0 = circRot/sunPos
        vR = (omega - omega0)*sunPos*math.sin(l*math.pi/180)+v0*math.cos(theta)
        
        
        ######################
        ## AGE DISTRIBUTION ##
        ######################
        
        # Set Age Distribution
        timeParam = random.randint(0,99)
        age = timeParam*.127 # Age in Myr (12.7 Myr limit) in Trebmlin model


        ##########################
        ## ELECTRON TEMPERATURE ##
        ##########################

        # Set Electron Temperature Distribution
        # Relationship taken from Balser et.al. 2011, put in range accepted by Tremblin model
        # Tremblin model ranges from 5000 K to 15000 K in 1000 K increments
        T_e = 5756 + 303*random.uniform(-1,1) + galRad*(299 + 31*random.uniform(-1,1))
        # T_e = 6080 + galRad*378 # Averaged value suggested in Tremblin 2014
        TeParam = int(round(T_e,-3)/1000 - 5)
        
        
        ###################################
        ## NEUTRAL HYDROGEN DISTRIBUTION ##
        ###################################
        
        # Set Neutral Hydrogen Density Distribution
        # Tremblin model ranges from 1700 cm-3 to 5100 cm-3 in 340 cm-3 increments
        densityParam = random.randint(0,10)


        #######################
        ## MASS DISTRIBUTION ##
        #######################

        # Set Host Star Mass Distribution
        massParam = random.random() # Used in forcing powerlaw fit
        
        while massParam > 0. :
            mass = random.randrange(lowerMass,upperMass)
            IMF = pow(lowerMass,2.35)*pow(mass,-2.35)
            lifetime = 10000.*pow(mass,-2.5) # 10 billion years for Sun, less for higher mass stars
            # L~M^3.5. Lifetime ~ M/L ~ M^(1-3.5) ~ M^(-2.5)
            #print str(mass) + " : " + str(massParam) + " <? " + str(IMF) + " : " + str(age) + " <? " + str(lifetime)
            if (massParam < IMF) :#and (age < lifetime) : # Makes power law fit
                massParam = 0. # Escape loop

                

        #########################
        ## IONIZING LUMINOSITY ##
        #########################

        '''
        lumPowerLaw = 3.5 # Used 1.94 previously (WHY?)
        lumMin = math.log10(pow(lowerMass,lumPowerLaw))
        lumMax = math.log10(pow(upperMass,lumPowerLaw))
        lumParam = int(round((math.log10(pow(mass,lumPowerLaw))-lumMin)/(lumMax-lumMin)*16,0)) # Use this line to access all values of Lum from 10^47 - 10^51
        # fluxParam = int(round((math.log10(pow(mass,1.94))-fluxMin)/(fluxMax-fluxMin)*12,0)+4)
        '''

        # Set Host Star Ionizing Luminosity Distribution
        # Tremblin model ranges from 10^47 to 10^51 in quarter-dec increments
        # In practice these are given as 47 to 51 in steps of 0.25
        # B-star mass ranges come from Silaj et. al 2014 and Armentrout et al. 2017
        # O-star mass ranges comes from Loren Anderson's Thesis (Eq 6.1, Boston University 2009)
        if mass < 9.11 :
            N_ly = 45.57 # B2
        elif mass < (13.21+9.11)/2. :
            N_ly = 46.1 # B1.5
        elif mass < 13.21 :
            N_ly = 46.5 # B1
        elif mass < 16.27 :
            N_ly = 46.95 # B0.5 (This matches up the fit from Anderson with numbers from Silaj)
        else :
            N_ly = 46.95*math.pow(mass-16.27,7./500.) # Fit to Sternberg 2003 by Anderson 2010

        # Conform ionizing luminosities to fit Tremblin model
        # Round ionizing luminosities to the nearsest quarter dec
        if N_ly < 47 :
            lumParam = 47
        else :
            lumParam = round(4.*N_ly)/4

        freq_GHz = 10
        regionLum = pow(10,N_ly)*pow(T_e,0.45)*pow(freq_GHz,-0.1)/(6.3*pow(10,52)) # Derived from Eq. 4 in Armentrout et al. 2017
        regionFlux = regionLum/(4*math.pi*dist**2) # UNITS?
                                                         
        ####################
        ## SIZE OF REGION ##
        ####################

        # From Distributions, Determine HII Region Radius
        if useTremblin == True :
            # Using Pascal Tremblin's hypercube data
            # TESTING. TAKE THESE OUT.
            timeParam=2
            lumParam = 47.25
            TeParam = int(round((5756 + 303*random.uniform(-1,1)) + galRad*(299 + 31*random.uniform(-1,1)),-3)/1000 - 5)
            densityParam = 2
            radius = ff.variables['radius'][timeParam,lumParam,TeParam,densityParam]
        else :
            alpha_h = 3.*pow(10.,-13.)
            n_e = 10.**3.
            age_sec = age*10**6.*3.154*10**7.
            soundSpeed = 20000 # in cm/s (0.2 km/s) Tremblin 14
            rad_initial = pow(3.*pow(10.,N_ly)/(4.*math.pi*alpha_h*pow(n_e,2.)),(1./3.)) #radius in cm
            radius= rad_initial*pow(1+7*age_sec*soundSpeed/(4*rad_initial),4./7.)*3.24*pow(10,-19.) #radius in pc, time evolution from Spitzer 1968
            

        #############
        ## TESTING ##
        #############

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
        and (whereIsRegion <= (diffusePercent + barPercent + ThreekpcArmPercent + spiralPercent)) \
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
        
        #print region
        

        #####################
        ## APPEND TO ARRAY ##
        #####################

        HiiList.append([galRad,xRot,yRot,z,mass,N_ly,age,radius,l,vR,regNum,b,regionFlux])
        numCluster += 1


######################
## PLOT DATA POINTS ##
######################

if plot3D == True :
    i = 0
    (xlist,ylist,zlist)=(list(),list(),list())
    while i < len(HiiList):
        xlist.append(HiiList[i][1])
        ylist.append(HiiList[i][2])
        zlist.append(HiiList[i][3])
        i+=1
    trace = go.Scatter3d(x=xlist,y=ylist,z=zlist,mode='markers',marker=dict(size=5,line=dict(color='rgba(217,217,217,0.14)',width=0.5),opacity=0.8))
    data=[trace]
    layout = go.Layout(margin=dict(l=0,r=0,b=0,t=0))
    fig = go.Figure(data=data,layout=layout)
    py.iplot(fig,filename='3dscatter')

###################
## WRITE TO FILE ##
###################

with open("HIIregion_popSynthesis.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(HiiList)
'''    
print "Diffuse Luminosity : " + str(diffLum*100/totLum) + "% (" + str(diffCount) + " Regions)"
print "Bar Luminosity : " + str(barLum*100/totLum) + "% (" + str(barCount) + " Regions)"
print "3 kpc Arm Luminosity : " + str(ThreekpcLum*100/totLum) + "% ("+ str(ThreekpcCount) + " Regions)"
print "Spiral Luminosity : " + str(sprLum*100/totLum) + "% (" + str(sprCount) + " Regions)"
print "Total Luminosity : " + str((barLum+ThreekpcLum+sprLum+diffLum)*100/totLum) + "% (" + str(barCount+ThreekpcCount+sprCount+diffCount) + " Regions)"
'''
