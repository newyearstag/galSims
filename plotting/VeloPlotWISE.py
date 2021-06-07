import pylab as p

# Open CSV File
datafile = open('wise_hii_V1.0.csv', 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))

# Save Galactic Radius Info from CSV to new list
ldata = list()
vdata = list()
index = 1

while index < len(csvFile):
    try:
        vdata.append(float(csvFile[index][9]))
        if float(csvFile[index][2]) > 180 :
            ldata.append(float(csvFile[index][2])-360)
        else :
            ldata.append(float(csvFile[index][2]))
    except:
        pass
    index += 1

p.scatter(ldata,vdata,s=3,facecolor="g", lw = 1)
p.xlabel('Galactic Longitude (deg)')
p.ylabel('VLSR (km/s)')
p.title('Longitude-Velocity Plot for WISE HII Regions')
p.savefig('WISE Longitude-Velocity Plot')
p.show()
