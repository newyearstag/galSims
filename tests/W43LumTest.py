import matplotlib.pyplot as plt
import numpy as np

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
zeroBin = 0
oneBin = 0
twoBin = 0
threeBin = 0
fourBin = 0
fiveBin = 0
sixBin = 0
fluxMin = pow(10,0)
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
    if (flS > fluxMin) and (lS < 0) and (lS > -90) :
#    if (flS < fluxMax) :#and (lS < -25) and (lS > -90) :
#    if logFl == 47 :
#    if (flS > fluxMin) and (lS < 90) and (lS > 0) :
        longS.append(lS)
        lumS.append(flS)
        srcCount += 1
        if flS <= pow(10,0) :
            zeroBin += 1
        elif flS <= pow(10,1) :
            oneBin += 1
        elif flS <= pow(10,2) :
            twoBin += 1
        elif flS <= pow(10,3) :
            threeBin += 1
        elif flS <= pow(10,4) :
            fourBin += 1
        elif flS <= pow(10,5) :
            fiveBin += 1
        elif flS <= pow(10,6) :
            sixBin += 1
            
    indexS += 1
    


print "Source Count : " + str(srcCount)

print "Sources with Luminosity in Zero Bin : " + str(zeroBin)
print "Sources with Luminosity in One Bin : " + str(oneBin)
print "Sources with Luminosity in Two Bin : " + str(twoBin)
print "Sources with Luminosity in Three Bin : " + str(threeBin)
print "Sources with Luminosity in Four Bin : " + str(fourBin)
print "Sources with Luminosity in Five Bin : " + str(fiveBin)
print "Sources with Luminosity in Six Bin : " + str(sixBin)


# Produce histogram of data
plt.title("Continuum Flux versus Galactic Longitude in 4th Quadrant (Sim)")
plt.xlabel("Galactic Longitude (deg)")
plt.ylabel("Radio Coninuum Integrated Flux at 1.4 GHz (Jy)")
plt.scatter(longS,lumS,s=3,facecolor='0',lw=0)
plt.yscale('log')
plt.grid(True)
#plt.legend(loc='upper right')
plt.xticks([-90,-75,-60,-45,-30,-15,0])
#plt.xticks([0,10,20,30,40,50,60,70,80,90])
#plt.xticks([-180,-135,-90,-45,0,45,90,135,180])
plt.gca().invert_xaxis()
plt.savefig('FluxRecVsLongitude_Quadrant4.eps', format='eps', dpi=1000)
plt.show()


print "Total Regions In Search Area : " + str(srcCount)
print "Percent of Total Regions : " + str(srcCount*100/len(csvFileS))

# Produce histogram of data
plt.hist(lumS, bins=np.logspace(0.1, 6.0, 50), histtype='step')
plt.title("Flux Distribution of HII Regions in 4th Quadrant (Sim)")
plt.xlabel("Flux (Jy)")
plt.ylabel("HII Region Count")
plt.xscale('log')
#plt.tick_params(\
#    axis='x',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off') # labels along the bottom edge are off
plt.savefig('FluxBinnedHIIRegions_Quadrant4.eps', format='eps', dpi=1000)
plt.show()


