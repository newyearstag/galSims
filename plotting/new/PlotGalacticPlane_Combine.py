import pylab as plt
import math
import numpy as np
from matplotlib.pyplot import Rectangle # Used to make dummy legend

markerScaling=25.

# Open CSV File
datafile = open(r'C:\Users\newye\OneDrive\Documents\GitHub\galSims\misc\HIIregion_popSynthesis_test.csv', 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
ldata = list()
bdata = list()
sizedata = list()
index = 0
NlyLimit = 47.56
#NlyLimit = 48.0


while index < len(csvFile) :
    if (float(csvFile[index][5])) >= NlyLimit :
        ldata.append(float(csvFile[index][8]))
        bdata.append(float(csvFile[index][11])*180./3.14159)
        x = float(csvFile[index][1])
        y = float(csvFile[index][2])
        z = float(csvFile[index][3])
        d2 = pow(x,2.)+pow(y-8.5,2.)+pow(z,2.) # Distance from sun to source squared
        dist_kpc =float(pow(d2,0.5))
        dist_pc = dist_kpc*1000.
        radius_pc = float(csvFile[index][7])
        sizedata.append(radius_pc/dist_pc*3600.*180./math.pi/markerScaling*2*2)
    index += 1

print (len(sizedata))

# Open CSV File for Wise Version 3
datafileW3 = open(r'C:\Users\newye\OneDrive\Documents\GitHub\galSims\misc\wise_hii_V1.3_hrds.csv', 'r')
csvFileW3 = []
for row in datafileW3:
    csvFileW3.append(row.strip().split(','))

# Save x, y, and l Info from Simulated Data to new list
bDataW3 = list()
lDataW3 = list()
sizedataW3 = list()
indexW3 = 1

while indexW3 < len(csvFileW3) :
    try :
        bW3 = float(csvFileW3[indexW3][3])
        lW3 = float(csvFileW3[indexW3][2])
        regType = str(csvFileW3[indexW3][1])
        #d = float(csvFile[index][32])
        if float(lW3) > 180 :
            lW3 = lW3-360
        else :
            lW3 = lW3
        if (bW3 < 10) and (bW3 > -10) and ((regType == " K") or (regType == " C")) :    
            lDataW3.append(lW3)
            bDataW3.append(bW3)
            sizedataW3.append(float(csvFileW3[indexW3][4])/markerScaling)
            #sizedataW3.append(float(csvFileW3[indexW3][4])*d/100)
    except :
        pass
    indexW3 += 1


fig, (ax1,ax2) = plt.subplots(2, sharex=True, sharey=True)

ax1.scatter(ldata,bdata,s=sizedata, facecolors = 'none', edgecolors = 'black')
ax1.set_ylim([-15,15])
ax1.set_xlim([-180,180])
#ax1.set_xticks([-180,-120,-60,0,60,120,180])
ax1.invert_xaxis()

ax2.scatter(lDataW3,bDataW3,s=sizedataW3, facecolors = 'none', edgecolors = 'black')
ax2.set_ylim([-15,15])
ax2.set_xlim([-180,180])
#ax2.set_xticks([-180,-120,-60,0,60,120,180],[180,240,300,0,60,120,180])
ax2.invert_xaxis()



ax1.plot([-90, -90], [-15, 15], '--', lw=2,alpha=0.7, color="black")
ax1.plot([0, 0], [-15, 15], '--', lw=2,alpha=0.7, color="black")
ax1.plot([90, 90], [-15, 15], '--', lw=2,alpha=0.7, color="black")
ax2.plot([-90, -90], [-15, 15], '--', lw=2,alpha=0.7, color="black")
ax2.plot([0, 0], [-15, 15], '--', lw=2,alpha=0.7, color="black")
ax2.plot([90, 90], [-15, 15], '--', lw=2,alpha=0.7, color="black")

ax2.text(45,15,"I", ha='center',va='center',color='black',fontsize=25)
ax2.text(135,15,"II", ha='center',va='center',color='black',fontsize=25)
ax2.text(-135,15,"III", ha='center',va='center',color='black',fontsize=25)
ax2.text(-45,15,"IV", ha='center',va='center',color='black',fontsize=25)

ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.xaxis.tick_top()
#ax1.yaxis.tick_right()
#ax1.yaxis.set_ticks_position('left')
#ax1.xaxis.set_ticks_position('top')
#ax1.yaxis.set_ticks_position('right')
ax1.xaxis.set_tick_params(width=2,labelsize=25)
ax1.yaxis.set_tick_params(width=2,labelsize=25)



ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.xaxis.tick_bottom()
#ax2.yaxis.tick_right()
#ax1.yaxis.set_ticks_position('left')
#ax1.xaxis.set_ticks_position('bottom')
#ax1.yaxis.set_ticks_position('right')
ax2.xaxis.set_tick_params(width=2,labelsize=25)
ax2.yaxis.set_tick_params(width=2,labelsize=25)




plt.setp((ax1,ax2))

#plt.xticks([-180,-135,-90,-45,0,45,90,135,180],[r"$\/180^{\circ}$",r"$\/225^{\circ}$",r"$\/270^{\circ}$",r"$\/300^{\circ}$",r"$\/0^{\circ}$",r"$\/45^{\circ}$",r"$\/90^{\circ}$",r"$\/135^{\circ}$",r"$\/180^{\circ}$"])
plt.xticks([-180,-135,-90,-45,0,45,90,135,180],[r"$\/180^{\circ}$",r"$\/$",r"$\/270^{\circ}$",r"$\/$",r"$\/0^{\circ}$",r"$\/$",r"$\/90^{\circ}$",r"$\/$",r"$\/180^{\circ}$"])
plt.yticks([-10,-5,0,5,10],[r"$-10^{\circ}$",r"$-5^{\circ}$",r"$\/0^{\circ}$",r"$\/5^{\circ}$",r"$\/10^{\circ}$"])

fig.text(0.93,0.33, "Observed", ha='center',va='center',color='black',rotation=90,fontsize=25)
fig.text(0.93,0.72,"Simulated", ha='center',va='center',color='black',rotation=90,fontsize=25)

fig.text(0.5, 0.04, "Galactic Longitude", ha='center',va='center',fontsize=35)
fig.text(0.03, 0.5, "Galactic Latitude", ha='center',va='center',rotation = 90,fontsize=35)

fig.set_size_inches(10,8)
fig.subplots_adjust(hspace=0,wspace=0)
fig.subplots_adjust(left=0.15,bottom=0.15)

fig.savefig('GalacticPlanePlot_Combine.eps', format='eps', dpi=1000)
fig.savefig('GalacticPlanePlot_Combine.pdf', format='pdf', dpi=1000)
fig.show()
