import pylab as p
from matplotlib.pyplot import Rectangle # Used to make dummy legend
import matplotlib
import matplotlib.font_manager as font_manager

# Open CSV File
datafile = open('../MASTER_DISTRIBUTIONS/HIIregion_popSynthesis.csv', 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))

NlyLimit = 47.56
#NlyLimit = 48.0

# Save Galactic Radius Info from CSV to new list
xdata = list()
ydata = list()
sizedata = list()
regNum = list()
index = 0
while index < len(csvFile) :
    if float(csvFile[index][5]) >= NlyLimit :
        xdata.append(float(csvFile[index][1]))
        ydata.append(float(csvFile[index][2]))
        sizedata.append(4.*float(csvFile[index][7])*2.)
    index += 1


p.scatter(xdata,ydata,s=sizedata,facecolors='none', edgecolors='black')
p.ylim([-18,18])
p.xlim([-18,18])
p.axis('off')

p.plot([-18,18], [-8.4,-8.4], 'k-', lw=2)
p.plot([0,0], [-18,18], 'k-', lw=2)
p.text(-14,-7,r"$I$", va='center',ha='center',color='black',fontsize=24)
p.text(-14,-10,r"$II$", va='center',ha='center',color='black',fontsize=24)
p.text(14,-10,r"$III$", va='center',ha='center',color='black',fontsize=24)
p.text(14,-7,r"$IV$", va='center',ha='center',color='black',fontsize=24)

p.plot([8,9], [-15,-15], 'k-', lw=3)
p.text(9.5,-15,r"$1\/kpc$", va='center',ha='left',color='black',fontsize=24)

p.text(-0.11,-8.32,r"$\star$", va='center',ha='center',color='red',fontsize=60)

#p.scatter(0,-8.4,s=300.0,marker='*',color='red')

#font_prop = font_manager.FontProperties(size=20)
#p.xlabel("X (kpc)", fontproperties=font_prop)
#p.ylabel("Y (kpc)", fontproperties=font_prop)
#p.yticks(fontproperties=font_prop)
#p.xticks(fontproperties=font_prop)
#p.title('3D HII Region Simulation - Face On View')
#prox1 = Rectangle((0, 0), 1, 1, fc=dcol)
#prox2 = Rectangle((0, 0), 1, 1, fc=bcol)
#prox3 = Rectangle((0, 0), 1, 1, fc=rcol)
#prox4 = Rectangle((0, 0), 1, 1, fc=scol)
#p.legend([prox1, prox2,prox3,prox4], ["Distributed", "Bar", "Ring", "Spiral Arms"], loc='upper right', prop=font_prop)
#p.title('8000 Regions - Only Spiral and Diffuse Shown')
fig = p.gcf()
fig.set_size_inches(8,8)
#p.savefig('FaceOnPlot_Sim.eps', format='eps', dpi=1000)
p.savefig('FaceOnPlot_Sim.png', format='png', dpi=1000)
p.show()
