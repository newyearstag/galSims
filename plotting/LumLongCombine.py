import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import Rectangle # Used to make dummy legend

# Open CSV File from Simulation
datafileS = open('3DHiiRegions.csv', 'r')
csvFileS = []
for row in datafileS:
    csvFileS.append(row.strip().split(','))
# Save Galactic Radius Info from Simulation to new list
print len(csvFileS)
longS = list()
lumS = list()
indexS = 0
srcCount = 0
negFourBin = 0
negThreeBin = 0
negTwoBin = 0
negOneBin = 0
zeroBin = 0
oneBin = 0
twoBin = 0
threeBin = 0
fourBin = 0
fiveBin = 0
sixBin = 0
fluxMin = pow(10,-4)
fluxMax = pow(10,6)
while indexS < len(csvFileS) :
    lS = float(csvFileS[indexS][8])
    x = float(csvFileS[indexS][1])
    y = float(csvFileS[indexS][2])
    z = float(csvFileS[indexS][3])
    d2 = pow(x,2)+pow(y-8.5,2)+pow(z,2) # Distance from sun to source squared
    logFl = float(csvFileS[indexS][5])/4+47
    fl = pow(10,logFl)
    print logFl
    b = .9688 # Eq 7 Tremblin et al. Assume Te=10^4, freq=1.4 GHz
    flS = fl/(7.603*pow(10,46))*b/d2
#    if (flS > fluxMin) :
    if (logFl >= 48.25) and (lS < -20) and (lS > -85) :
#    if logFl == 47 :
#    if (flS > fluxMin) and (lS < 90) and (lS > 0) :
        longS.append(lS)
        lumS.append(flS)
        srcCount += 1
        if flS <= pow(10,-3) :
            negFourBin += 1
        elif flS <= pow(10,-2) :
            negThreeBin += 1
        elif flS <= pow(10,-1) :
            negTwoBin += 1
        elif flS <= pow(10,0) :
            negOneBin += 1
        elif flS <= pow(10,1) :
            zeroBin += 1           
        elif flS <= pow(10,2) :
            oneBin += 1
        elif flS <= pow(10,3) :
            twoBin += 1
        elif flS <= pow(10,4) :
            threeBin += 1
        elif flS <= pow(10,5) :
            fourBin += 1
        elif flS <= pow(10,6) :
            fiveBin += 1
            
    indexS += 1
    




# Open CSV File from Sumss Photometry
datafileSumss = open('ATCA_candidates_phot_sumss.csv', 'r')
csvFileSumss = []
for row in datafileSumss:
    csvFileSumss.append(row.strip().split(','))
# Save Galactic Radius Info from Simulation to new list
lumSumss = list()
indexSumss = 0
while indexSumss < len(csvFileSumss) :
    lSumss = float(csvFileSumss[indexSumss][2])
    if lSumss > 0 :
        lumSumss.append(lSumss)           
    indexSumss += 1


# Open CSV File from Known Regions
datafileKnown = open('ATCA_known_phot_sumss.csv', 'r')
csvFileKnown = []
for row in datafileKnown:
    csvFileKnown.append(row.strip().split(','))
# Save Galactic Radius Info from Simulation to new list
lumKnown = list()
indexKnown = 0
while indexKnown < len(csvFileKnown) :
    lKnown = float(csvFileKnown[indexKnown][2])
    if lKnown > 0 :
        lumKnown.append(lKnown)           
    indexKnown += 1


lumKnownAndSumss = list()
lumKnownAndSumss = lumSumss + lumKnown



print "Source Count : " + str(srcCount)

print "Sources with Luminosity in Neg Four Bin : " + str(negFourBin)
print "Sources with Luminosity in Neg Three Bin : " + str(negThreeBin)
print "Sources with Luminosity in Neg Two Bin : " + str(negTwoBin)
print "Sources with Luminosity in Neg one Bin : " + str(negOneBin)
print "Sources with Luminosity in Zero Bin : " + str(zeroBin)
print "Sources with Luminosity in One Bin : " + str(oneBin)
print "Sources with Luminosity in Two Bin : " + str(twoBin)
print "Sources with Luminosity in Three Bin : " + str(threeBin)
print "Sources with Luminosity in Four Bin : " + str(fourBin)
print "Sources with Luminosity in Five Bin : " + str(fiveBin)
print "Sources with Luminosity in Six Bin : " + str(sixBin)


# Produce histogram of data
plt.title("Continuum Flux versus Galactic Longitude across Galaxy (Simulated)")
plt.xlabel("Galactic Longitude (deg)")
plt.ylabel("Radio Coninuum Integrated Flux at 1.4 GHz (Jy)")
plt.scatter(longS,lumS,s=3,facecolor='0',lw=0)
plt.yscale('log')
plt.grid(True)
#plt.legend(loc='upper right')
#plt.xticks([-90,-75,-60,-45,-30,-15,0])
#plt.xticks([0,10,20,30,40,50,60,70,80,90])
plt.xticks([-180,-135,-90,-45,0,45,90,135,180])
plt.gca().invert_xaxis()
plt.savefig('FluxRecVsLongitude_Quadrant4.eps', format='eps', dpi=1000)
plt.show()


print "Total Regions In Search Area : " + str(srcCount)
print "Percent of Total Regions : " + str(srcCount*100/len(csvFileS))

TxtSize=18
LnWidth=3

# Produce histogram of data
plt.hist(lumS, bins=np.logspace(-3, 4, 50), histtype='step',color="red",linewidth=LnWidth)
plt.hist(lumKnown, bins=np.logspace(-3, 4, 50), histtype='step',color='#81DAF5',linewidth=LnWidth)
plt.hist(lumSumss, bins=np.logspace(-3, 4, 50), histtype='step',color='#2E9AFE',linewidth=LnWidth)
plt.hist(lumKnownAndSumss, bins=np.logspace(-3, 4, 50), histtype='step',color='#0101DF',linewidth=3)
#plt.title("Flux Distribution of HII Regions in 4th Quadrant (Galactic Sim)")
plt.ylim([pow(10,0),pow(10,4)])
plt.xlabel("Spectral Flux Density (Jy)",fontsize=TxtSize)
plt.ylabel("HII Region Count",fontsize=TxtSize)
plt.tick_params(which='both',width=LnWidth,labelsize=TxtSize)
plt.gca().xaxis.grid(True) #vertical axes
plt.gca().xaxis.grid(linewidth=2)
plt.xscale('log')
plt.yscale('log')


#Galactic Simulation Histogram Bin Values
simPos = 6500
#plt.annotate(negFourBin,xy = (2.5*pow(10,-4),simPos), color='red',fontsize=TxtSize)
plt.annotate(negThreeBin,xy = (2.5*pow(10,-3),simPos), color='red',fontsize=TxtSize)
plt.annotate(negTwoBin,xy = (2.5*pow(10,-2),simPos), color='red',fontsize=TxtSize)
plt.annotate(negOneBin,xy = (2.5*pow(10,-1),simPos), color='red',fontsize=TxtSize)
plt.annotate(zeroBin,xy = (2.5*pow(10,0),simPos), color='red',fontsize=TxtSize)
plt.annotate(oneBin,xy = (2.5*pow(10,1),simPos), color='red',fontsize=TxtSize)
plt.annotate(twoBin,xy = (2.5*pow(10,2),simPos), color='red',fontsize=TxtSize)
plt.annotate(threeBin,xy = (2.5*pow(10,3),simPos), color='red',fontsize=TxtSize)
#plt.annotate(fourBin,xy = (2.5*pow(10,4),simPos), color='red',fontsize=TxtSize)
#plt.annotate(fiveBin,xy = (2.5*pow(10,5),simPos), color='red',fontsize=TxtSize)
plt.annotate("Galactic Simulation",xy = (.25*pow(10,1),650), color='red',fontsize=TxtSize)

#Known Regions Histogram Bin Values
knownPos = 4500
#plt.annotate(0,xy = (2.5*pow(10,-4),knownPos), color='#81DAF5',fontsize=TxtSize)
plt.annotate(0,xy = (2.5*pow(10,-3),knownPos), color='#81DAF5',fontsize=TxtSize)
plt.annotate(2,xy = (2.5*pow(10,-2),knownPos), color='#81DAF5',fontsize=TxtSize)
plt.annotate(42,xy = (2.5*pow(10,-1),knownPos), color='#81DAF5',fontsize=TxtSize)
plt.annotate(77,xy = (2.5*pow(10,0),knownPos), color='#81DAF5',fontsize=TxtSize)
plt.annotate(74,xy = (2.5*pow(10,1),knownPos), color='#81DAF5',fontsize=TxtSize)
plt.annotate(3,xy = (2.5*pow(10,2),knownPos), color='#81DAF5',fontsize=TxtSize)
plt.annotate(0,xy = (2.5*pow(10,3),knownPos), color='#81DAF5',fontsize=TxtSize)
#plt.annotate(0,xy = (2.5*pow(10,4),knownPos), color='#81DAF5',fontsize=TxtSize)
#plt.annotate(0,xy = (2.5*pow(10,5),knownPos), color='#81DAF5',fontsize=TxtSize)
plt.annotate("Known Regions",xy = (.25*pow(10,1),450), color='#81DAF5',fontsize=TxtSize)

#SUMSS Candidates Histogram Bin Values
sumssPos =3000
#plt.annotate(0,xy = (2.5*pow(10,-4),sumssPos), color='#2E9AFE',fontsize=TxtSize)
plt.annotate(8,xy = (2.5*pow(10,-3),sumssPos), color='#2E9AFE',fontsize=TxtSize)
plt.annotate(52,xy = (2.5*pow(10,-2),sumssPos), color='#2E9AFE',fontsize=TxtSize)
plt.annotate(200,xy = (2.5*pow(10,-1),sumssPos), color='#2E9AFE',fontsize=TxtSize)
plt.annotate(209,xy = (2.5*pow(10,0),sumssPos), color='#2E9AFE',fontsize=TxtSize)
plt.annotate(71,xy = (2.5*pow(10,1),sumssPos), color='#2E9AFE',fontsize=TxtSize)
plt.annotate(2,xy = (2.5*pow(10,2),sumssPos), color='#2E9AFE',fontsize=TxtSize)
plt.annotate(0,xy = (2.5*pow(10,3),sumssPos), color='#2E9AFE',fontsize=TxtSize)
#plt.annotate(0,xy = (2.5*pow(10,4),sumssPos), color='#2E9AFE',fontsize=TxtSize)
#plt.annotate(0,xy = (2.5*pow(10,5),sumssPos), color='#2E9AFE',fontsize=TxtSize)
plt.annotate("SUMSS Candidates",xy = (.25*pow(10,1),300), color='#2E9AFE',fontsize=TxtSize)

#Candidates Plus Known Histogram Bin Values
cAndKPos =2000
#plt.annotate(0,xy = (2.5*pow(10,-4),cAndKPos), color='#0101DF',fontsize=TxtSize)
plt.annotate(8,xy = (2.5*pow(10,-3),cAndKPos), color='#0101DF',fontsize=TxtSize)
plt.annotate(54,xy = (2.5*pow(10,-2),cAndKPos), color='#0101DF',fontsize=TxtSize)
plt.annotate(242,xy = (2.5*pow(10,-1),cAndKPos), color='#0101DF',fontsize=TxtSize)
plt.annotate(286,xy = (2.5*pow(10,0),cAndKPos), color='#0101DF',fontsize=TxtSize)
plt.annotate(145,xy = (2.5*pow(10,1),cAndKPos), color='#0101DF',fontsize=TxtSize)
plt.annotate(5,xy = (2.5*pow(10,2),cAndKPos), color='#0101DF',fontsize=TxtSize)
plt.annotate(0,xy = (2.5*pow(10,3),cAndKPos), color='#0101DF',fontsize=TxtSize)
#plt.annotate(0,xy = (2.5*pow(10,4),cAndKPos), color='#0101DF',fontsize=TxtSize)
#plt.annotate(0,xy = (2.5*pow(10,5),cAndKPos), color='#0101DF',fontsize=TxtSize)
plt.annotate("Candidates and Known",xy = (.25*pow(10,1),200), color='#0101DF',fontsize=TxtSize)

plt.savefig('FluxBinned_LogCombine.eps', format='eps', dpi=1000)
plt.show()


