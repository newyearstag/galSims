import matplotlib.pyplot as plt
import argparse

'''parser = argparse.ArgumentParser()
parser.add_argument("parameter", type=str,
                    help="Options : mass, age, radius, lum, velo, long")
parser.add_argument("numberBins", type=int,
                    help="Set number of bins for histogram")
args = parser.parse_args()
param = args.parameter # Prompt User for plotting parameter
numBins = args.numberBins()''' # Prompt User for number of bins
param = "mass"
numBins = 50

# Open CSV File
datafile = open(r'C:\Users\newye\OneDrive\Documents\GitHub\galSims\misc\3DHiiRegions.csv', 'r')
csvFile = []
for row in datafile:
    csvFile.append(row.strip().split(','))

if param == "mass" :
    # Save Galactic Radius Info from CSV to new list
    data = list()
    index = 0
    while index < len(csvFile) :
        data.append(float(csvFile[index][4]))
        index += 1

    # Produce histogram of data    
    plt.hist(data, bins=numBins, histtype='step')
    plt.title("Mass Binned HII Regions in 3D Galaxy Simulation")
    plt.xlabel("HII Region Mass (In Solar Units)")
    plt.ylabel("HII Region Count")
    plt.yscale('log')
    plt.show()

elif param == "age" :
    # Save Galactic Radius Info from CSV to new list
    data = list()
    index = 0
    while index < len(csvFile) :
        data.append(float(csvFile[index][6]))
        index += 1
    # Produce histogram of data    
    plt.hist(data, bins=numBins, histtype='step')
    plt.title("Age Binned HII Regions in 3D Galaxy Simulation")
    plt.xlabel("HII Region Age (In Myr)")
    plt.ylabel("HII Region Count")
    plt.show()

elif param == "radius" :
    # Save Galactic Radius Info from CSV to new list
    data = list()
    index = 0
    while index < len(csvFile) :
        data.append(float(csvFile[index][7]))
        index += 1

    # Produce histogram of data    
    plt.hist(data, bins=numBins, histtype='step')
    plt.title("Radius Binned HII Regions in 3D Galaxy Simulation")
    plt.xlabel("HII Region Radius (parsecs)")
    plt.ylabel("HII Region Count")
    plt.show()    

elif param == "lum" :
    # Save Galactic Radius Info from CSV to new list
    galRad = list() #Use this to tell us flux from various directions? Useful?
    lum = list()
    index = 0
    while index < len(csvFile) :
        galRad.append(float(csvFile[index][0]))
        lum.append(float(csvFile[index][5]))
        index += 1
    # Produce histogram of data
    plt.hist(lum, bins=numBins, histtype='step')
    plt.title("Luminosity Function for HII Regions in 3D Galaxy Simulation")
    plt.xlabel("HII Region Integrated Luminosity at Given Radius")
    plt.ylabel("HII Region Count")
    plt.yscale('log')
    plt.show()

elif param == "velo" :
    # Save Galactic Radius Info from CSV to new list
    data = list()
    index = 0
    while index < len(csvFile) :
        data.append(float(csvFile[index][9]))
        index += 1

    # Produce histogram of data    
    plt.hist(data, bins=numBins, histtype='step')
    plt.title("Velocity Binned HII Regions in 3D Galaxy Simulation")
    plt.xlabel("HII Region Velocity (km/s)")
    plt.ylabel("HII Region Count")
    plt.show()

elif param == "long" :
    # Save Galactic Radius Info from CSV to new list
    data = list()
    index = 0
    while index < len(csvFile) :
        data.append(float(csvFile[index][8]))
        index += 1

    # Produce histogram of data    
    plt.hist(data, bins=numBins, histtype='step')
    plt.title("Longitude Binned HII Regions in 3D Galaxy Simulation")
#    plt.title("8000 Regions - Only Spiral and Diffuse Shown")
    plt.xlabel("HII Region Longitude (deg)")
    plt.ylabel("HII Region Count")
    plt.show()

else :
    print ("Invalid Parameter")
    quit
