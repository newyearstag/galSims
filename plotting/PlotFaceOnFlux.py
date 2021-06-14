import pylab as p
from matplotlib.pyplot import Rectangle # Used to make dummy legend
import matplotlib as mpl
import matplotlib.font_manager as font_manager
import math
from pylab import subplot

dcol = str('#FF0000')
bcol = str('#5FB404')
rcol = str('#086A87')
scol = str('black')

# Open CSV File
datafile = open(r'C:\Users\newye\OneDrive\Documents\GitHub\galSims\misc\3DHiiRegions.csv', 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))
print (len(csvFile))

# Save Galactic Radius Info from CSV to new list
thetadata = list()
rdata = list()
fluxdata = list()
index = 0
galRot = math.pi
while index < len(csvFile) :
    x = float(csvFile[index][1])
    y = float(csvFile[index][2])
    z = float(csvFile[index][3])
    xRot = x*math.cos(galRot) - y*math.sin(galRot)
    yRot = x*math.sin(galRot) + y*math.cos(galRot)
    d2 = pow(x,2)+pow(y-8.5,2)+pow(z,2) # Distance from sun to source squared
    logFl = float(csvFile[index][5])/4+47
    fl = pow(10,logFl)
    b = .9688 # Eq 7 Tremblin et al. Assume Te=10^4, freq=1.4 GHz
    flS = fl/(7.63*pow(10,46))*b/d2
    logFlS = math.log10(flS)
    theta = math.atan((yRot+8.5)/xRot)
    r=pow((pow(xRot,2)+pow(yRot+8.5,2)),0.5)

    if logFl >=48.25 :
        if xRot > 0 :
            thetadata.append(theta)
            rdata.append(r)
            fluxdata.append(logFlS)
        else :
            thetadata.append(theta+math.pi)
            rdata.append(r)
            fluxdata.append(logFlS)
    
    index += 1

ax = p.subplot(111, polar=True)
c = p.scatter(thetadata, rdata, c=fluxdata, s=5, norm=mpl.colors.SymLogNorm(linthresh=10,vmin=-3,vmax=3),lw=0)
c.set_alpha(0.75)

#p.scatter(xdata,ydata,c=fluxdata,s=5,norm=mpl.colors.SymLogNorm(linthresh=10,vmin=-3,vmax=3),lw=0)
p.colorbar(ticks=[-3,-2,-1,0,1,2,3],label="Log of Received Flux (Log[Jy])")

#[r'$10^{-3}$',r'$10^{-2}$',r'$10^{-1}$',r'$10^{0}$',r'$10^{1}$',r'$10^{2}$',r'$10^{3}$']
#font_prop = font_manager.FontProperties(size=16)
#p.xlabel("X (kpc)", fontproperties=font_prop)
#p.ylabel("Y (kpc)", fontproperties=font_prop)
#p.yticks(fontproperties=font_prop)
#p.xticks(fontproperties=font_prop)
#fig.add_axes(rect, polar=True, frameon=False)
#fig.set_rticklabels([5,10,15,20])
#p.title('3D HII Region Simulation - Face On View')
#prox1 = Rectangle((0, 0), 1, 1, fc=dcol)
#prox2 = Rectangle((0, 0), 1, 1, fc=bcol)
#prox3 = Rectangle((0, 0), 1, 1, fc=rcol)
#prox4 = Rectangle((0, 0), 1, 1, fc=scol)
#p.legend([prox1, prox2,prox3,prox4], ["Distributed", "Bar", "Ring", "Spiral Arms"], loc='upper right', prop=font_prop)
#p.title('8000 Regions - Only Spiral and Diffuse Shown')
#p.savefig('FaceOnPlotLum.eps', format='eps', dpi=1000)
p.show()
