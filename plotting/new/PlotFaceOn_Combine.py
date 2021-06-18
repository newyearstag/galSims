import pylab as p
from matplotlib.pyplot import Rectangle # Used to make dummy legend
import matplotlib
import matplotlib.font_manager as font_manager
import math
import numpy


# Open CSV File
datafile = open(r'C:\Users\newye\OneDrive\Documents\GitHub\galSims\misc\wise_hii_V1.3_hrds.csv', 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))
print (len(csvFile))

# Save Galactic Radius Info from CSV to new list
xdataW = list()
ydataW = list()
sizedataW = list()
index = 1

while index < len(csvFile) :
    try:
        regType = str(csvFile[index][1])
        KDAR = str(csvFile[index][31])
        d = float(csvFile[index][32])
        if ((KDAR==" (T)") or (KDAR==" T")):
            d = float(csvFile[index][27])
        elif d == 0 :
           d = float(csvFile[index][38])
        else :
            pass
        l = (float(csvFile[index][2])+90)*math.pi/180
        b = math.pi/2-float(csvFile[index][3])*math.pi/180
        if (d != 0) and ((regType == " K") or (regType == " C")) :#\
 #       and ((KDAR!=" (T)") and (KDAR!=" T")) :
 #       and ((KDAR==" (N)") or (KDAR==" N")) \
 #       or ((KDAR==" (F)") or (KDAR==" F")) :
 #       or ((KDAR==" (T)") or (KDAR==" T")) :
            xdataW.append(d*math.sin(b)*math.cos(l))
            ydataW.append(d*math.sin(b)*math.sin(l)-8.4)
            sizedataW.append(float(csvFile[index][4])/3600.*math.pi/180.*d*1000.*2.)
    except:
        pass
    index += 1
'''
# Open CSV File
datafile = open('../MASTER_DISTRIBUTIONS/wise_hii_V2.0_hrds.csv', 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
xdataW = list()
ydataW = list()
sizedataW = list()
index = 1

while index < len(csvFile) :
    try:
        regType = str(csvFile[index][2])
        KDAR = str(csvFile[index][39])
        d = float(csvFile[index][40])
        if ((KDAR==" (T)") or (KDAR==" T")):
            d = float(csvFile[index][35])
        elif d == 0 :
            d = float(csvFile[index][49])
        else :
            pass
        l = (float(csvFile[index][3])+90)*math.pi/180
        b = math.pi/2-float(csvFile[index][4])*math.pi/180
        if (d != 0) and ((regType == " K") or (regType == " C")) :#\
        #       and ((KDAR!=" (T)") and (KDAR!=" T")) :
            #       and ((KDAR==" (N)") or (KDAR==" N")) \
            #       or ((KDAR==" (F)") or (KDAR==" F")) :
            #       or ((KDAR==" (T)") or (KDAR==" T")) :
            xdataW.append(d*math.sin(b)*math.cos(l))
            ydataW.append(d*math.sin(b)*math.sin(l)-8.4)
            sizedataW.append(float(csvFile[index][5])/3600.*math.pi/180.*d*1000.*2.)
    except:
        pass
index += 1
'''



NlyLimit = 47.56
#NlyLimit = 48.0


# Open CSV File
datafile = open(r'C:\Users\newye\OneDrive\Documents\GitHub\galSims\misc\HIIregion_popSynthesis_test.csv', 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
xdataS = list()
ydataS = list()
sizedataS = list()
index = 0

while index < len(csvFile) :
    if float(csvFile[index][5]) >= NlyLimit :
        xdataS.append(float(csvFile[index][1]))
        ydataS.append(float(csvFile[index][2]))
        sizedataS.append(4.*float(csvFile[index][7])*2.)
    index += 1



fig, (ax1,ax2) = p.subplots(1,2, sharex=True, sharey=True)



ax1.scatter(xdataS,ydataS,s=sizedataS,facecolors='none', edgecolors='black')
ax1.set_ylim([-20,20])
ax1.set_xlim([-20,20])
ax1.axis('off')
ax1.plot([-20,20], [-8.4,-8.4], 'k-', lw=2)
ax1.plot([0,0], [-20,20], 'k-', lw=2)
ax1.text(-17,-7,"I", va='center',ha='center',color='black',fontsize=24)
ax1.text(-17,-10,"II", va='center',ha='center',color='black',fontsize=24)
ax1.text(17,-10,"III", va='center',ha='center',color='black',fontsize=24)
ax1.text(17,-7,"IV", va='center',ha='center',color='black',fontsize=24)
#ax1.plot([8,9], [-15,-15], 'k-', lw=3)
ax1.plot([18,19], [14.25,14.25], 'k-', lw=2)
#ax1.text(9.5,-15,r"$1\/kpc$", va='center',ha='left',color='black',fontsize=24)
ax1.text(-0.11,-8.32,r"$\star$", va='center',ha='center',color='red',fontsize=60)

ax2.scatter(xdataW,ydataW,s=sizedataW,facecolors='none', edgecolors='black')
ax2.set_ylim([-20,20])
ax2.set_xlim([-20,20])
ax2.axis('off')
ax2.plot([-20,20], [-8.4,-8.4], 'k-', lw=2)
ax2.plot([0,0], [-20,20], 'k-', lw=2)
ax2.text(-17,-7,"I", va='center',ha='center',color='black',fontsize=24)
ax2.text(-17,-10,"II", va='center',ha='center',color='black',fontsize=24)
ax2.text(17,-10,"III", va='center',ha='center',color='black',fontsize=24)
ax2.text(17,-7,"IV", va='center',ha='center',color='black',fontsize=24)
#ax2.plot([8,9], [-15,-15], 'k-', lw=3)
#ax2.text(9.5,-15,r"$1\/kpc$", va='center',ha='left',color='black',fontsize=24)
ax2.text(-0.11,-8.32,r"$\star$", va='center',ha='center',color='red',fontsize=60)


#print len(sizedataS)
#x=numpy.arange(0.,1.05,0.05)
#y1=numpy.sin(2*numpy.pi*x)
#y2=y1+0.2

#eta=1e-6
#y1positive=(y1+eta)>=0
#y1negative=(y1-eta)<=0

#plt.plot(x,y1,'-r',label='y1')
#plt.plot(x,y2,'-g',label='y2')
#plt.plot(x,x*0,'--k')
#lt.fill_between(x,y2,y1,where=y1positive,color='green',alpha=0.5,interpolate=False)
#plt.fill_between(x,y2,y1,where=y1negative,color='red',alpha=0.5,interpolate=False)


#a = numpy.arange(0, 100, .1)
#galCent1 = -4*a
#galCent2 = 4*a
#ax2.fill_between(a, galCent2, galCent1, hatch = '/')



p.setp((ax1,ax2))


fig.text(0.375, 0.12, 'Simulated', ha='left',fontsize=24)
fig.text(0.775, 0.12, 'Observed', ha='left',fontsize=24)
#fig.plot([.46,.50], [.9,.9], 'k-', lw=3)
fig.text(.49,0.77,"1 kpc", va='center',ha='left',color='black',fontsize=24)
#fig.text(0.5, 0.15, r"$1\/kpc$", ha='center',fontsize=24)
fig.set_size_inches(15,7)
fig.subplots_adjust(hspace=0,wspace=0.1)
#fig.subplots_adjust(bottom=0.15)

    
fig.savefig('FaceOnPlot_Combine.eps', format='eps', dpi=1000)
fig.savefig('FaceOnPlot_Combine.pdf', format='pdf', dpi=1000)
fig.show()
