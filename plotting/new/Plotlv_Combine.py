import pylab as plt
import math
import numpy as np
from matplotlib.pyplot import Rectangle # Used to make dummy legend

markerScaling=25.
pointSize=3.

# Open CSV File
datafile = open('../MASTER_DISTRIBUTIONS/HIIregion_popSynthesis.csv', 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
ldata = list()
vdata = list()
index = 0
NlyLimit = 47.56
#NlyLimit = 48.0


while index < len(csvFile) :
    if (float(csvFile[index][5])) >= NlyLimit :
        ldata.append(float(csvFile[index][8]))
        vdata.append(float(csvFile[index][9]))
    index += 1

# Open CSV File for Wise Version 3
datafileW3 = open('../MASTER_DISTRIBUTIONS/wise_hii_V1.3_hrds.csv', 'r')
csvFileW3 = []
for row in datafileW3:
    csvFileW3.append(row.strip().split(','))

# Save x, y, and l Info from Simulated Data to new list
vDataW3 = list()
lDataW3 = list()
indexW3 = 1

while indexW3 < len(csvFileW3) :
    try :
        lW3 = float(csvFileW3[indexW3][2])
        vW3 = float(csvFileW3[indexW3][9])
        regType = str(csvFileW3[indexW3][1])
        #d = float(csvFile[index][32])
        if float(lW3) > 180 :
            lW3 = lW3-360
        else :
            lW3 = lW3
        if (regType == " K") or (regType == " C") :    
            lDataW3.append(lW3)
            vDataW3.append(vW3)
    except :
        pass
    indexW3 += 1


fig, (ax1,ax2) = plt.subplots(2, sharex=True, sharey=True)

ax1.scatter(ldata,vdata,s=pointSize, facecolors = 'black', edgecolors = 'none')
ax1.set_ylim([-200,200])
ax1.set_xlim([-180,180])
#ax1.set_xticks([-180,-120,-60,0,60,120,180])
ax1.invert_xaxis()

ax2.scatter(lDataW3,vDataW3,s=pointSize, facecolors = 'black', edgecolors = 'none')
ax2.set_ylim([-175,175])
ax2.set_xlim([-180,180])
#ax2.set_xticks([-180,-120,-60,0,60,120,180],[180,240,300,0,60,120,180])
ax2.invert_xaxis()



#ax1.plot([-90, -90], [-15, 15], '--', lw=2,alpha=0.7, color="black")
#ax1.plot([0, 0], [-15, 15], '--', lw=2,alpha=0.7, color="black")
#ax1.plot([90, 90], [-15, 15], '--', lw=2,alpha=0.7, color="black")
#ax2.plot([-90, -90], [-15, 15], '--', lw=2,alpha=0.7, color="black")
#ax2.plot([0, 0], [-15, 15], '--', lw=2,alpha=0.7, color="black")
#ax2.plot([90, 90], [-15, 15], '--', lw=2,alpha=0.7, color="black")

#ax2.text(45,15,"I", ha='center',va='center',color='black',fontsize=25)
#ax2.text(135,15,"II", ha='center',va='center',color='black',fontsize=25)
#ax2.text(-135,15,"III", ha='center',va='center',color='black',fontsize=25)
#ax2.text(-45,15,"IV", ha='center',va='center',color='black',fontsize=25)

#ax1.spines['right'].set_visible(False)
#ax1.spines['left'].set_visible(False)
#ax1.spines['top'].set_visible(False)
#ax1.spines['bottom'].set_visible(False)
ax1.xaxis.tick_top()
#ax1.yaxis.tick_right()
#ax1.yaxis.set_ticks_position('left')
#ax1.xaxis.set_ticks_position('top')
#ax1.yaxis.set_ticks_position('right')
ax1.xaxis.set_tick_params(width=2,labelsize=20)
ax1.yaxis.set_tick_params(width=2,labelsize=20)



#ax2.spines['right'].set_visible(False)
#ax2.spines['left'].set_visible(False)
#ax2.spines['top'].set_visible(False)
#ax2.spines['bottom'].set_visible(False)
ax2.xaxis.tick_bottom()
#ax2.yaxis.tick_right()
#ax1.yaxis.set_ticks_position('left')
#ax1.xaxis.set_ticks_position('bottom')
#ax1.yaxis.set_ticks_position('right')
ax2.xaxis.set_tick_params(width=2,labelsize=20)
ax2.yaxis.set_tick_params(width=2,labelsize=20)




plt.setp((ax1,ax2))

#plt.xticks([-180,-135,-90,-45,0,45,90,135,180],[r"$\/180^{\circ}$",r"$\/225^{\circ}$",r"$\/270^{\circ}$",r"$\/300^{\circ}$",r"$\/0^{\circ}$",r"$\/45^{\circ}$",r"$\/90^{\circ}$",r"$\/135^{\circ}$",r"$\/180^{\circ}$"])
plt.xticks([-180,-135,-90,-45,0,45,90,135,180],[r"$\/180^{\circ}$",r"$\/$",r"$\/270^{\circ}$",r"$\/$",r"$\/0^{\circ}$",r"$\/$",r"$\/90^{\circ}$",r"$\/$",r"$\/180^{\circ}$"])
plt.yticks([-150,-100,-50,0,50,100,150],[-150,-100,-50,0,50,100,150])

fig.text(0.93,0.33, "Observed", ha='center',va='center',color='black',rotation=90,fontsize=25)
fig.text(0.93,0.72,"Simulated", ha='center',va='center',color='black',rotation=90,fontsize=25)

fig.text(0.5, 0.04, "Galactic Longitude", ha='center',va='center',fontsize=35)
fig.text(0.03, 0.5, "LSR Velocity (km s$^{-1}$)", ha='center',va='center',rotation = 90,fontsize=35)

fig.set_size_inches(10,8)
fig.subplots_adjust(hspace=0,wspace=0)
fig.subplots_adjust(left=0.15,bottom=0.15)

fig.savefig('lv_Combine.eps', format='eps', dpi=1000)
fig.savefig('lv_Combine.pdf', format='pdf', dpi=1000)
fig.show()
