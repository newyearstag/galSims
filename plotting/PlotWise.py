import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3
import math

# Open CSV File
datafile = open('wise_hii_V1.0.csv', 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
xdata = list()
ydata = list()
zdata = list()
errdata = list()
index = 1

# GLong in column 2
# GLat in column 3
# Distance in Column 13

while index < len(csvFile) :
    try:
        d = float(csvFile[index][13])
        l = (float(csvFile[index][2])+90)*math.pi/180
        b = math.pi/2 - float(csvFile[index][3])*math.pi/180
        err = float(csvFile[index][14])
        
        xdata.append(d*math.sin(b)*math.cos(l))
        ydata.append(d*math.sin(b)*math.sin(l)-8.4)
        zdata.append(d*math.cos(b))
        errdata.append(err)
        
    except:
        pass
    index += 1

fig=p.figure()
ax = p3.Axes3D(fig)
ax.scatter(xdata, ydata, zdata, s=errdata*2, facecolor='0', lw = 0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
fig.add_axes(ax)
p.show()
