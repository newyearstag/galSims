import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import Rectangle # Used to make dummy legend

# Open CSV File from Simulation
datafileS = open('../HIIregionFiles/3DHiiRegions.csv', 'r')
csvFileS = []
for row in datafileS:
    csvFileS.append(row.strip().split(','))
# Save Galactic Radius Info from Simulation to new list

##
## Set Search Space Parameters and Initialization
##

northMin = 18
northMax = 65
southMin = 275-360
southMax = 340-360

northCompleteness = pow(10,-2)
southCompleteness= pow(10,0.32)

northCandCSV = 'ATCA_candidates_phot_north.csv'
#northKnownCSV = 'ATCA_known_phot_north.csv'
northKnownCSV = 'wise_test_NEW_updated.csv'
southCandCSV = 'ATCA_candidates_phot_south.csv'
southKnownCSV = 'ATCA_known_phot_south.csv'

longN = list()
lumN = list()
longS = list()
lumS = list()

compN = list()
compS = list()

lumKnownNorth = list()
lumCandNorth = list()
lumKnownAndCandNorth = list()
indexS = 0
srcCountN = 0

lumKnownSouth = list()
lumCandSouth = list()
lumKnownAndCandSouth = list()
srcCountS = 0

logFlMin = 48

(negFourBinN,negThreeBinN,negTwoBinN,negOneBinN,zeroBinN,oneBinN,twoBinN,threeBinN,fourBinN,fiveBinN,sixBinN) = (0,0,0,0,0,0,0,0,0,0,0)
(negFourBinCN,negThreeBinCN,negTwoBinCN,negOneBinCN,zeroBinCN,oneBinCN,twoBinCN,threeBinCN,fourBinCN,fiveBinCN,sixBinCN) = (0,0,0,0,0,0,0,0,0,0,0)
(negFourBinKN,negThreeBinKN,negTwoBinKN,negOneBinKN,zeroBinKN,oneBinKN,twoBinKN,threeBinKN,fourBinKN,fiveBinKN,sixBinKN) = (0,0,0,0,0,0,0,0,0,0,0)
(negFourBinKCN,negThreeBinKCN,negTwoBinKCN,negOneBinKCN,zeroBinKCN,oneBinKCN,twoBinKCN,threeBinKCN,fourBinKCN,fiveBinKCN,sixBinKCN) = (0,0,0,0,0,0,0,0,0,0,0)

(negFourBinS,negThreeBinS,negTwoBinS,negOneBinS,zeroBinS,oneBinS,twoBinS,threeBinS,fourBinS,fiveBinS,sixBinS) = (0,0,0,0,0,0,0,0,0,0,0)
(negFourBinCS,negThreeBinCS,negTwoBinCS,negOneBinCS,zeroBinCS,oneBinCS,twoBinCS,threeBinCS,fourBinCS,fiveBinCS,sixBinCS) = (0,0,0,0,0,0,0,0,0,0,0)
(negFourBinKS,negThreeBinKS,negTwoBinKS,negOneBinKS,zeroBinKS,oneBinKS,twoBinKS,threeBinKS,fourBinKS,fiveBinKS,sixBinKS) = (0,0,0,0,0,0,0,0,0,0,0)
(negFourBinKCS,negThreeBinKCS,negTwoBinKCS,negOneBinKCS,zeroBinKCS,oneBinKCS,twoBinKCS,threeBinKCS,fourBinKCS,fiveBinKCS,sixBinKCS) = (0,0,0,0,0,0,0,0,0,0,0)

##
## Northern Regions
##

# Simulated Regions in Both the North and South
while indexS < len(csvFileS) :
    lS = float(csvFileS[indexS][8])
    x = float(csvFileS[indexS][1])
    y = float(csvFileS[indexS][2])
    z = float(csvFileS[indexS][3])
    d2 = pow(x,2)+pow(y-8.5,2)+pow(z,2) # Distance from sun to source squared
    logFl = float(csvFileS[indexS][5])/4+47
    fl = pow(10,logFl)
    b = .9688 # Eq 7 Tremblin et al. Assume Te=10^4, freq=1.4 GHz
    flS = fl/(7.603*pow(10,46))*b/d2
    if (logFl >= logFlMin) and (lS < northMax) and (lS > northMin) :
        longN.append(lS)
        lumN.append(flS)
        srcCountN += 1
        if flS <= pow(10,-3) :
            negFourBinN += 1
        elif flS <= pow(10,-2) :
            negThreeBinN += 1
        elif flS <= pow(10,-1) :
            negTwoBinN += 1
        elif flS <= pow(10,0) :
            negOneBinN += 1
        elif flS <= pow(10,1) :
            zeroBinN += 1           
        elif flS <= pow(10,2) :
            oneBinN += 1
        elif flS <= pow(10,3) :
            twoBinN += 1
        elif flS <= pow(10,4) :
            threeBinN += 1
        elif flS <= pow(10,5) :
            fourBinN += 1
        elif flS <= pow(10,6) :
            fiveBinN += 1

        if flS >= northCompleteness :
            compN.append(flS)
    elif (logFl >= logFlMin) and (lS < southMax) and (lS > southMin) :
        longS.append(lS)
        lumS.append(flS)
        if flS <= pow(10,-3) :
            negFourBinS += 1
        elif flS <= pow(10,-2) :
            negThreeBinS += 1
        elif flS <= pow(10,-1) :
            negTwoBinS += 1
        elif flS <= pow(10,0) :
            negOneBinS += 1
        elif flS <= pow(10,1) :
            zeroBinS += 1           
        elif flS <= pow(10,2) :
            oneBinS += 1
        elif flS <= pow(10,3) :
            twoBinS += 1
        elif flS <= pow(10,4) :
            threeBinS += 1
        elif flS <= pow(10,5) :
            fourBinS += 1
        elif flS <= pow(10,6) :
            fiveBinS += 1

        if flS >= southCompleteness :
            compS.append(flS)
    indexS += 1
    
# Open CSV File from Candidate Regions in North
datafileCandNorth = open(northCandCSV, 'r')
csvFileCandNorth = []
for row in datafileCandNorth:
    csvFileCandNorth.append(row.strip().split(','))
# Save Galactic Radius Info from Simulation to new list
lumCandNorth = list()
indexCandNorth = 0
while indexCandNorth < len(csvFileCandNorth) :
    lCandNorth = float(csvFileCandNorth[indexCandNorth][2])
    if lCandNorth > 0 :
        lumCandNorth.append(lCandNorth)
        if lCandNorth <= pow(10,-3) :
            negFourBinCN += 1
        elif lCandNorth <= pow(10,-2) :
            negThreeBinCN += 1
        elif lCandNorth <= pow(10,-1) :
            negTwoBinCN += 1
        elif lCandNorth <= pow(10,0) :
            negOneBinCN += 1
        elif lCandNorth <= pow(10,1) :
            zeroBinCN += 1           
        elif lCandNorth <= pow(10,2) :
            oneBinCN += 1
        elif lCandNorth <= pow(10,3) :
            twoBinCN += 1
        elif lCandNorth <= pow(10,4) :
            threeBinCN += 1
        elif lCandNorth <= pow(10,5) :
            fourBinCN += 1
        elif lCandNorth <= pow(10,6) :
            fiveBinCN += 1
    indexCandNorth += 1
    
# Open CSV File from Known Regions in North
datafileKnownNorth = open(northKnownCSV, 'r')
csvFileKnownNorth = []
for row in datafileKnownNorth:
    csvFileKnownNorth.append(row.strip().split(','))
# Save Galactic Radius Info from Simulation to new list
indexKnownNorth = 1
while indexKnownNorth < len(csvFileKnownNorth) :
    #lKnownNorth = float(csvFileKnownNorth[indexKnownNorth][2])
    lKnownNorth = float(csvFileKnownNorth[indexKnownNorth][89]) # For Zoltan's file
    if lKnownNorth > 0 :
        lumKnownNorth.append(lKnownNorth)
        if lKnownNorth <= pow(10,-3) :
            negFourBinKN += 1
        elif lKnownNorth <= pow(10,-2) :
            negThreeBinKN += 1
        elif lKnownNorth <= pow(10,-1) :
            negTwoBinKN += 1
        elif lKnownNorth <= pow(10,0) :
            negOneBinKN += 1
        elif lKnownNorth <= pow(10,1) :
            zeroBinKN += 1           
        elif lKnownNorth <= pow(10,2) :
            oneBinKN += 1
        elif lKnownNorth <= pow(10,3) :
            twoBinKN += 1
        elif lKnownNorth <= pow(10,4) :
            threeBinKN += 1
        elif lKnownNorth <= pow(10,5) :
            fourBinKN += 1
        elif lKnownNorth <= pow(10,6) :
            fiveBinKN += 1
    indexKnownNorth += 1

lumKnownAndCandNorth = lumCandNorth + lumKnownNorth
negFourBinKCN = negFourBinKN + negFourBinCN
negThreeBinKCN = negThreeBinKN + negThreeBinCN
negTwoBinKCN = negTwoBinKN + negTwoBinCN
negOneBinKCN = negOneBinKN + negOneBinCN
zeroBinKCN = zeroBinKN + zeroBinCN
oneBinKCN = oneBinKN + oneBinCN
twoBinKCN = twoBinKN + twoBinCN
threeBinKCN = threeBinKN + threeBinCN
fourBinKCN = fourBinKN + fourBinCN                                                                                                                          
fiveBinKCN = fiveBinKN + fiveBinCN                                                                                                                            
sixBinKCN = sixBinKN + sixBinCN

##
## Southern Regions
##

## NOTE : Simulated regions in South were already accounted for earlier.
    
# Open CSV File from Candidate Regions in South
datafileCandSouth = open(southCandCSV, 'r')
csvFileCandSouth = []
for row in datafileCandSouth:
    csvFileCandSouth.append(row.strip().split(','))
# Save Galactic Radius Info from Simulation to new list
lumCandSouth = list()
indexCandSouth = 0
while indexCandSouth < len(csvFileCandSouth) :
    lCandSouth = float(csvFileCandSouth[indexCandSouth][2])
    if lCandSouth > 0 :
        lumCandSouth.append(lCandSouth)
        if lCandSouth <= pow(10,-3) :
            negFourBinCS += 1
        elif lCandSouth<= pow(10,-2) :
            negThreeBinCS += 1
        elif lCandSouth <= pow(10,-1) :
            negTwoBinCS += 1
        elif lCandSouth <= pow(10,0) :
            negOneBinCS += 1
        elif lCandSouth <= pow(10,1) :
            zeroBinCS += 1           
        elif lCandSouth <= pow(10,2) :
            oneBinCS += 1
        elif lCandSouth <= pow(10,3) :
            twoBinCS += 1
        elif lCandSouth <= pow(10,4) :
            threeBinCS += 1
        elif lCandSouth <= pow(10,5) :
            fourBinCS += 1
        elif lCandSouth <= pow(10,6) :
            fiveBinCS += 1
    indexCandSouth += 1
    
# Open CSV File from Known Regions in North
datafileKnownSouth = open(southKnownCSV, 'r')
csvFileKnownSouth = []
for row in datafileKnownSouth:
    csvFileKnownSouth.append(row.strip().split(','))
# Save Galactic Radius Info from Simulation to new list
indexKnownSouth = 0
while indexKnownSouth < len(csvFileKnownSouth) :
    lKnownSouth = float(csvFileKnownSouth[indexKnownSouth][2])
    if lKnownSouth > 0 :
        lumKnownSouth.append(lKnownSouth)
        if lKnownSouth <= pow(10,-3) :
            negFourBinKS += 1
        elif lKnownSouth <= pow(10,-2) :
            negThreeBinKS += 1
        elif lKnownSouth <= pow(10,-1) :
            negTwoBinKS += 1
        elif lKnownSouth <= pow(10,0) :
            negOneBinKS += 1
        elif lKnownSouth <= pow(10,1) :
            zeroBinKS += 1           
        elif lKnownSouth <= pow(10,2) :
            oneBinKS += 1
        elif lKnownSouth <= pow(10,3) :
            twoBinKS += 1
        elif lKnownSouth <= pow(10,4) :
            threeBinKS += 1
        elif lKnownSouth <= pow(10,5) :
            fourBinKS += 1
        elif lKnownSouth <= pow(10,6) :
            fiveBinKS += 1
    indexKnownSouth += 1

lumKnownAndCandSouth = lumCandSouth + lumKnownSouth
negFourBinKCS = negFourBinKS + negFourBinCS
negThreeBinKCS = negThreeBinKS + negThreeBinCS
negTwoBinKCS = negTwoBinKS + negTwoBinCS
negOneBinKCS = negOneBinKS + negOneBinCS
zeroBinKCS = zeroBinKS + zeroBinCS
oneBinKCS = oneBinKS + oneBinCS
twoBinKCS = twoBinKS + twoBinCS
threeBinKCS = threeBinKS + threeBinCS
fourBinKCS = fourBinKS + fourBinCS                                                                                                                         
fiveBinKCS = fiveBinKS + fiveBinCS                                                                                                                           
sixBinKCS = sixBinKS + sixBinCS

print "--------------------"
print "--Northern Regions--"
print "Simulated : " + str(len(lumN))
print "Candidate : " + str(len(lumCandNorth))
print "Known : " + str(len(lumKnownNorth))
print "Known & Cand : " + str(len(lumCandNorth)+len(lumKnownNorth))
print "--------------------"
print "--Southern Regions--"
print "Simulated : " + str(len(lumS))
print "Candidate : " + str(len(lumCandSouth))
print "Known : " + str(len(lumKnownSouth))
print "Known & Cand : " + str(len(lumCandSouth)+len(lumKnownSouth))
print "--------------------"

##
## Here Starts Plotting
##

TxtSize = 16
LnWidth = 2
figWidth = 8
figHeight = 4.5
compColor = "#E6E6E6"
simColor = '#B40404'#'red'
knownColor = '#0174DF'#'#81DAF5'
candColor = '#2E9AFE'
cAndKColor = '#0101DF'

##
## Plotting Northern Data
##

# Produce histogram of data
#plt.title("Continuum Flux versus Galactic Longitude across Galaxy (Simulated)")
#plt.xlabel("Galactic Longitude (deg)")
#plt.ylabel("Radio Continuum Integrated Flux at 1.4 GHz (Jy)")
#plt.scatter(longS,lumS,s=3,facecolor='0',lw=0)
#plt.yscale('log')
#plt.grid(True)
#plt.legend(loc='upper right')
#plt.xticks([-90,-75,-60,-45,-30,-15,0])
#plt.xticks([0,10,20,30,40,50,60,70,80,90])
#plt.xticks([-180,-135,-90,-45,0,45,90,135,180])
#plt.gca().invert_xaxis()
#plt.savefig('FluxRecVsLongitude_FirstQuad.eps', format='eps', dpi=1000)
#plt.show()
#print "Total Regions In Search Area : " + str(srcCount)
#print "Percent of Total Regions : " + str(srcCount*100/len(csvFileS))

# Produce histogram of Northern Data
#Completeness Limit
fig, (ax1,ax2) = plt.subplots(1,2, sharex=True, sharey=True)
#ax1.hist(compN, bins=np.logspace(-2, 2, 47),histtype='bar',color=compColor,linewidth=0,alpha=0.5)
ax1.hist(lumN, bins=np.logspace(-3, 2, 59), histtype='step',color=simColor,linewidth=LnWidth+2)
ax1.hist(lumKnownNorth, bins=np.logspace(-3, 2, 59), histtype='step',color=knownColor,linewidth=LnWidth)
#ax1.hist(lumCandNorth, bins=np.logspace(-4,2, 47), histtype='step',color=candColor,linewidth=LnWidth)
#ax1.hist(lumKnownAndCandNorth, bins=np.logspace(-4, 2, 47), histtype='step',color=cAndKColor,linewidth=3)

ax1.tick_params(which='both',width=LnWidth,labelsize=TxtSize)
ax1.set_ylim([pow(10,0),pow(10,2)])
ax1.set_xlim([pow(10,-3),pow(10,2)])
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_title("Quadrant I (O9.5)",fontsize=TxtSize)
ax1.set_ylabel("HII Region Count",fontsize=TxtSize)
#ax1.set_xlabel("Integrated Flux Density",fontsize=TxtSize)
ax1.xaxis.grid(True)
ax1.xaxis.grid(linewidth=2)
#ax1.yaxis.grid(True)
#ax1.yaxis.grid(linewidth=2)

# Galactic Simulation Histogram Bin Values
#simPosN = pow(10,2.8)
#ax1.text(pow(10,-3.5),simPosN,negFourBinN, ha='center',color=simColor,fontsize=TxtSize)
#ax1.text(pow(10,-2.5),simPosN,negThreeBinN,ha='center', color=simColor,fontsize=TxtSize)
#ax1.text(pow(10,-1.5),simPosN,negTwoBinN,ha='center',color=simColor,fontsize=TxtSize)
#ax1.text(pow(10,-0.5),simPosN,negOneBinN,ha='center', color=simColor,fontsize=TxtSize)
#ax1.text(pow(10,0.5),simPosN,zeroBinN,ha='center',color=simColor,fontsize=TxtSize)
#ax1.text(pow(10,1.5),simPosN,oneBinN, ha='center',color=simColor,fontsize=TxtSize)
#ax1.text(pow(10,2.5),simPosN,twoBinN,ha='center',color=simColor,fontsize=TxtSize)
#ax1.text(pow(10,3.5),simPosN,threeBinN,ha='center', color=simColor,fontsize=TxtSize)
#ax1.text(pow(10,4.5),simPosN,fourBinN,ha='center', color=simColor,fontsize=TxtSize)
#ax1.text(pow(10,5.5),simPosN,fiveBinN,ha='center', color=simColor,fontsize=TxtSize)

# Known Regions Histogram Bin Values
#knownPosN = pow(10,2.65)
#ax1.text(pow(10,-3.5),knownPosN,negFourBinKN,ha='center', color=knownColor,fontsize=TxtSize)
#ax1.text(pow(10,-2.5),knownPosN,negThreeBinKN,ha='center',color=knownColor,fontsize=TxtSize)
#ax1.text(pow(10,-1.5),knownPosN,negTwoBinKN,ha='center',color=knownColor,fontsize=TxtSize)
#ax1.text(pow(10,-0.5),knownPosN,negOneBinKN,ha='center',color=knownColor,fontsize=TxtSize)
#ax1.text(pow(10,0.5),knownPosN,zeroBinKN,ha='center',color=knownColor,fontsize=TxtSize)
#ax1.text(pow(10,1.5),knownPosN,oneBinKN,ha='center',color=knownColor,fontsize=TxtSize)
#ax1.text(pow(10,2.5),knownPosN,twoBinKN,ha='center',color=knownColor,fontsize=TxtSize)
#ax1.text(pow(10,3.5),knownPosN,threeBinKN,ha='center',color=knownColor,fontsize=TxtSize)
#ax1.text(pow(10,4.5),knownPosN,fourBinKN,ha='center', color=knownColor,fontsize=TxtSize)
#ax1.text(pow(10,5.5),knownPosN,fiveBinKN,ha='center',color=knownColor,fontsize=TxtSize)

# Candidate Histogram Bin Values
#candPosN = pow(10,2.5)
#ax1.text(pow(10,-3.5),candPosN,negFourBinCN,ha='center',color=candColor,fontsize=TxtSize)
#ax1.text(pow(10,-2.5),candPosN,negThreeBinCN,ha='center',color=candColor,fontsize=TxtSize)
#ax1.text(pow(10,-1.5),candPosN,negTwoBinCN,ha='center',color=candColor,fontsize=TxtSize)
#ax1.text(pow(10,-0.5),candPosN,negOneBinCN,ha='center',color=candColor,fontsize=TxtSize)
#ax1.text(pow(10,0.5),candPosN,zeroBinCN,ha='center',color=candColor,fontsize=TxtSize)
#ax1.text(pow(10,1.5),candPosN,oneBinCN,ha='center',color=candColor,fontsize=TxtSize)
#ax1.text(pow(10,2.5),candPosN,twoBinCN,ha='center',color=candColor,fontsize=TxtSize)
#ax1.text(pow(10,3.5),candPosN,threeBinCN,ha='center',color=candColor,fontsize=TxtSize)
#ax1.text(pow(10,4.5),candPosN,fourBinCN,ha='center', color=candColor,fontsize=TxtSize)
#ax1.text(pow(10,5.5),candPosN,fiveBinCN,ha='center',color=candColor,fontsize=TxtSize)

# Candidates Plus Known Histogram Bin Values
#cAndKPosN = pow(10,2.35)
#ax1.text(pow(10,-3.5),cAndKPosN,negFourBinKCN, ha='center',color=cAndKColor,fontsize=TxtSize)
#ax1.text(pow(10,-2.5),cAndKPosN,negThreeBinKCN,ha='center',color=cAndKColor,fontsize=TxtSize)
#ax1.text(pow(10,-1.5),cAndKPosN,negTwoBinKCN,ha='center',color=cAndKColor,fontsize=TxtSize)
#ax1.text(pow(10,-0.5),cAndKPosN,negOneBinKCN,ha='center',color=cAndKColor,fontsize=TxtSize)
#ax1.text(pow(10,0.5),cAndKPosN,zeroBinKCN,ha='center',color=cAndKColor,fontsize=TxtSize)
#ax1.text(pow(10,1.5),cAndKPosN,oneBinKCN,ha='center',color=cAndKColor,fontsize=TxtSize)
#ax1.text(pow(10,2.5),cAndKPosN,twoBinKCN,ha='center',color=cAndKColor,fontsize=TxtSize)
#ax1.text(pow(10,3.5),cAndKPosN,threeBinKCN,ha='center',color=cAndKColor,fontsize=TxtSize)
#ax1.text(pow(10,4.5),cAndKPosN,fourBinKCN,ha='center', color=cAndKColor,fontsize=TxtSize)
#ax1.text(pow(10,5.5),cAndKPosN,fiveBinKCN,ha='center',color=cAndKColor,fontsize=TxtSize)

##
## Plotting Southern Data
##

# Produce histogram of Southern Data
#ax2.hist(compS, bins=np.logspace(-2, 2, 47),histtype='bar',color=compColor,linewidth=0,alpha=0.5)
ax2.hist(lumS, bins=np.logspace(-3, 2, 59), histtype='step',color=simColor,linewidth=LnWidth+2)
ax2.hist(lumKnownSouth, bins=np.logspace(-3, 2, 59), histtype='step',color=knownColor,linewidth=LnWidth)
#ax2.hist(lumCandSouth, bins=np.logspace(-4, 2, 47), histtype='step',color=candColor,linewidth=LnWidth)
#ax2.hist(lumKnownAndCandSouth, bins=np.logspace(-4, 2, 47), histtype='step',color=cAndKColor,linewidth=3)
ax2.tick_params(which='both',width=LnWidth,labelsize=TxtSize)
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_ylim([pow(10,0),pow(10,2)])
ax2.set_xlim([pow(10,-3),pow(10,2)])
ax2.set_title("Quadrant IV (O9.5)",fontsize=TxtSize)
#ax2.set_xlabel("Integrated Flux Density",fontsize=TxtSize)
ax2.xaxis.grid(True)
ax2.xaxis.grid(linewidth=2)
#ax2.yaxis.grid(True)
#ax2.yaxis.grid(linewidth=2)

# Galactic Simulation Histogram Bin Values
#simPosS = pow(10,2.8)
#ax2.text(pow(10,-3.5),simPosS,negFourBinS, ha='center',color=simColor,fontsize=TxtSize)
#ax2.text(pow(10,-2.5),simPosS,negThreeBinS,ha='center',color=simColor,fontsize=TxtSize)
#ax2.text(pow(10,-1.5),simPosS,negTwoBinS,ha='center',color=simColor,fontsize=TxtSize)
#ax2.text(pow(10,-0.5),simPosS,negOneBinS,ha='center',color=simColor,fontsize=TxtSize)
#ax2.text(pow(10,0.5),simPosS,zeroBinS,ha='center',color=simColor,fontsize=TxtSize)
#ax2.text(pow(10,1.5),simPosS,oneBinS,ha='center',color=simColor,fontsize=TxtSize)
#ax2.text(pow(10,2.5),simPosS,twoBinS,ha='center', color=simColor,fontsize=TxtSize)
#ax2.text(pow(10,3.5),simPosS,threeBinS,ha='center',color=simColor,fontsize=TxtSize)
#ax2.text(pow(10,4.5),simPosS,fourBinS,ha='center',color=simColor,fontsize=TxtSize)
#ax2.text(pow(10,5.5),simPosS,fiveBinS,ha='center',color=simColor,fontsize=TxtSize)
#ax2.text(pow(10,-3.5),simPosS,"Simulated Population", ha='center',color=simColor,fontsize=TxtSize)

# Known Regions Histogram Bin Values
#knownPosS = pow(10,2.65)
#ax2.text(pow(10,-3.5),knownPosS,negFourBinKS,ha='center', color=knownColor,fontsize=TxtSize)
#ax2.text(pow(10,-2.5),knownPosS,negThreeBinKS,ha='center',color=knownColor,fontsize=TxtSize)
#ax2.text(pow(10,-1.5),knownPosS,negTwoBinKS,ha='center', color=knownColor,fontsize=TxtSize)
#ax2.text(pow(10,-0.5),knownPosS,negOneBinKS,ha='center',color=knownColor,fontsize=TxtSize)
#ax2.text(pow(10,0.5),knownPosS,zeroBinKS,ha='center',color=knownColor,fontsize=TxtSize)
#ax2.text(pow(10,1.5),knownPosS,oneBinKS,ha='center',color=knownColor,fontsize=TxtSize)
#ax2.text(pow(10,2.5),knownPosS,twoBinKS,ha='center',color=knownColor,fontsize=TxtSize)
#ax2.text(pow(10,3.5),knownPosS,threeBinKS,ha='center', color=knownColor,fontsize=TxtSize)
#ax2.text(pow(10,4.5),knownPosS,fourBinKS,ha='center',color=knownColor,fontsize=TxtSize)
#ax2.text(pow(10,5.5),knownPosS,fiveBinKS,ha='center',color=knownColor,fontsize=TxtSize)
#ax2.text(pow(10,-3.5),knownPosS,"Known Regions",ha='center', color=knownColor,fontsize=TxtSize)

# Candidate Histogram Bin Values
#candPosS = pow(10,2.5)
#ax2.text(pow(10,-3.5),candPosS,negFourBinCS, ha='center',color=candColor,fontsize=TxtSize)
#ax2.text(pow(10,-2.5),candPosS,negThreeBinCS,ha='center',color=candColor,fontsize=TxtSize)
#ax2.text(pow(10,-1.5),candPosS,negTwoBinCS,ha='center',color=candColor,fontsize=TxtSize)
#ax2.text(pow(10,-0.5),candPosS,negOneBinCS,ha='center',color=candColor,fontsize=TxtSize)
#ax2.text(pow(10,0.5),candPosS,zeroBinCS,ha='center',color=candColor,fontsize=TxtSize)
#ax2.text(pow(10,1.5),candPosS,oneBinCS,ha='center',color=candColor,fontsize=TxtSize)
#ax2.text(pow(10,2.5),candPosS,twoBinCS,ha='center',color=candColor,fontsize=TxtSize)
#ax2.text(pow(10,3.5),candPosS,threeBinCS,ha='center',color=candColor,fontsize=TxtSize)
#ax2.text(pow(10,4.5),candPosS,fourBinCS,ha='center', color=candColor,fontsize=TxtSize)
#ax2.text(pow(10,5.5),candPosS,fiveBinCS,ha='center',color=candColor,fontsize=TxtSize)
#ax2.text(pow(10,-3.5),candPosS,"Candidate Regions",ha='center', color=candColor,fontsize=TxtSize)

#Candidates Plus Known Histogram Bin Values
#cAndKPosS = pow(10,2.35)
#ax2.text(pow(10,-3.5),cAndKPosS, negFourBinKCS,ha = 'center', color=cAndKColor,fontsize=TxtSize)
#ax2.text(pow(10,-2.5),cAndKPosS, negThreeBinKCS,ha = 'center',color=cAndKColor,fontsize=TxtSize)
#ax2.text(pow(10,-1.5),cAndKPosS,negTwoBinKCS,ha='center', color=cAndKColor,fontsize=TxtSize)
#ax2.text(pow(10,-0.5),cAndKPosS,negOneBinKCS,ha='center', color=cAndKColor,fontsize=TxtSize)
#ax2.text(pow(10,0.5),cAndKPosS,zeroBinKCS,ha='center', color=cAndKColor,fontsize=TxtSize)
#ax2.text(pow(10,1.5),cAndKPosS,oneBinKCS,ha='center',color=cAndKColor,fontsize=TxtSize)
#ax2.text(pow(10,2.5),cAndKPosS,twoBinKCS,ha='center',color=cAndKColor,fontsize=TxtSize)
#ax2.text(pow(10,3.5),cAndKPosS,threeBinKCS, ha='center',color=cAndKColor,fontsize=TxtSize)
#ax2.text(pow(10,4.5),cAndKPosS,fourBinKCS, ha='center',color=cAndKColor,fontsize=TxtSize)
#ax2.text(pow(10,5.5),cAndKPosS,fiveBinKCS, ha='center',color=cAndKColor,fontsize=TxtSize)
#ax2.text(pow(10,-3.5),cAndKPosS,"Known and Candidate", ha='center',color=cAndKColor,fontsize=TxtSize)

ax1.spines['right'].set_visible(False)
#ax1.spines['left'].set_visible(False)
#ax1.spines['top'].set_visible(False)
#ax1.spines['bottom'].set_visible(False)
ax1.yaxis.set_ticks_position('left')
#ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
#ax2.spines['top'].set_visible(False)
#ax2.spines['bottom'].set_visible(False)
ax2.yaxis.set_ticks_position('right')
simPosLabel = pow(10,1.65)
knownPosLabel = pow(10,1.5)
candPosLabel = pow(10,1.5)
cAndKPosLabel = pow(10,1.25)
#ax1.text(pow(10,1),simPosLabel,"Simulated",ha='center', color=simColor,fontsize=TxtSize)
#ax1.text(pow(10,1),knownPosLabel,"Known",ha='center',color=knownColor,fontsize=TxtSize)
#ax2.text(pow(10,-4),candPosLabel,"Candidate", ha='center',color=candColor,fontsize=TxtSize)
#ax2.text(pow(10,-4),cAndKPosLabel,"Known and", ha='center',color=cAndKColor,fontsize=TxtSize)
#ax2.text(pow(10,-4),pow(10,1.1),"Candidate", ha='center',color=cAndKColor,fontsize=TxtSize)
ax2.plot([pow(10,-3), pow(10,-3)], [pow(10,2), pow(10,0)], 'k-', lw=3)
#ax2.plot([pow(10,-2), pow(10,-2)], [pow(10,1.4), pow(10,0)], 'k-', lw=3)

# Showing completeness
#ax1.plot([2.7*pow(10,-2), 2.7*pow(10,-2)], [pow(10,2), pow(10,0)], 'k-', lw=4,alpha=0.7, color="#0B6138")
#ax2.plot([2.35*pow(10,-0.03), 2.35*pow(10,-0.03)], [pow(10,2), pow(10,0)], 'k-', lw=4,alpha=0.7,color="#0B6138")


##
## Combine North and South Panels into Same Figure
##

plt.setp((ax1,ax2), xticks=[pow(10,-2),pow(10,-1),pow(10,0),pow(10,1)])
fig.text(0.5, 0.04, 'Integrated Flux Density (Jy)', ha='center',fontsize=TxtSize)
fig.set_size_inches(figWidth,figHeight)
fig.subplots_adjust(hspace=0,wspace=0)
fig.subplots_adjust(bottom=0.15)

#Completeness Limits
#plt.line(1,1,1, 10)#, 'k-', lw=3)
#fig.plot([pow(10,0.5), pow(10,0.5)], [1.5*pow(10,1), pow(10,-1)], 'k-', lw=3)

fig.savefig('FluxBinned_FirstFourthQuads_O95.eps', format='eps', dpi=1000)
fig.show()

print "Simulated in 4th Quad : " + str(negFourBinS+negThreeBinS+negTwoBinS+negOneBinS+zeroBinS+oneBinS+twoBinS+threeBinS+fourBinS+fiveBinS+sixBinS)

print "Known in 4th Quad : " + str(negFourBinKS+negThreeBinKS+negTwoBinKS+negOneBinKS+zeroBinKS+oneBinKS+twoBinKS+threeBinKS+fourBinKS+fiveBinKS+sixBinKS)



