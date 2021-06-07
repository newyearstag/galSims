import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3

# Open CSV File
datafile = open('3DHiiRegions.csv', 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
xdata = list()
ydata = list()
zdata = list()
index = 0
while index < len(csvFile) :
    xdata.append(float(csvFile[index][1]))
    ydata.append(float(csvFile[index][2]))
    zdata.append(float(csvFile[index][3]))
    index += 1

fig=p.figure()
ax = p3.Axes3D(fig)
ax.scatter(xdata, ydata, zdata, s=3, facecolor='0', lw = 0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
fig.add_axes(ax)
p.show()
