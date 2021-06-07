import pylab as p
from matplotlib.pyplot import Rectangle # Used to make dummy legend
import matplotlib
import matplotlib.font_manager as font_manager

dcol = str('#FF0000')
bcol = str('#5FB404')
rcol = str('#086A87')
scol = str('black')

# Open CSV File
datafile = open('3DHiiRegions.csv', 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
xdata = list()
ydata = list()
regNum = list()
index = 0
while index < len(csvFile) :
    xdata.append(float(csvFile[index][1]))
    ydata.append(float(csvFile[index][2]))

    # Distributed
    if (csvFile[index][10] == str(1)) :
        regNum.append(dcol)
    # Bar
    elif csvFile[index][10] == str(2) :
        regNum.append(bcol)
    # Ring    
    elif csvFile[index][10] == str(4) :
        regNum.append(rcol)
    # Spirals & 3kpc Arm 
    else :
        regNum.append(scol)
    
    index += 1


p.scatter(xdata,ydata,s=5,facecolor=regNum, lw = 0)
font_prop = font_manager.FontProperties(size=20)
p.xlabel("X (kpc)", fontproperties=font_prop)
p.ylabel("Y (kpc)", fontproperties=font_prop)
p.yticks(fontproperties=font_prop)
p.xticks(fontproperties=font_prop)
#p.title('3D HII Region Simulation - Face On View')
prox1 = Rectangle((0, 0), 1, 1, fc=dcol)
prox2 = Rectangle((0, 0), 1, 1, fc=bcol)
prox3 = Rectangle((0, 0), 1, 1, fc=rcol)
prox4 = Rectangle((0, 0), 1, 1, fc=scol)
p.legend([prox1, prox2,prox3,prox4], ["Distributed", "Bar", "Ring", "Spiral Arms"], loc='upper right', prop=font_prop)
#p.title('8000 Regions - Only Spiral and Diffuse Shown')
p.savefig('FaceOnPlot.eps', format='eps', dpi=1000)
p.show()
