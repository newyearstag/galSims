# galSims
3D population synthesis modeling of HII regions in the Milky Way


Galactic HII Region Simulations - Read Me File

———

Dr. William P. Armentrout
Dr. Loren D. Anderson
West Virginia University

———

## GENERAL FUNCTIONALITY ##

—

Simulate.py (NumberOfRegions)

e.g. : python Simulate.py 2000

Includes a model for distributing HII regions throughout a galaxy. Initial population studies were
based on surveys given in the Bradley et al. (______) paper discussing extragalactic HII surveys.
Also included in this simulation is a model by Pascal Tremblin for determining the size of an HII
region based on age, location in galaxy, and neutral hydrogen density.

Takes as input the number of regions you wish to populate in your sample galaxy.

Produces the output file “3DHiiRegions.csv”.

—

NEEDS FIXED - ClusterNearby.py (clusterIterations)

e.g. : python ClusterNearby.py 4

Groups overlapping and engulfed HII regions together to simulate our inability to
resolve distant HII regions in close proximity. The “clusterIterations” parameter determines
how many times the clustering algorithm is performed (i.e. clustering clusters).

Produces the output file “3DHiiRegionsCombine.csv”.

—

## DATA VISUALIZATION ##

—

Plot.py

e.g. : python Plot.py

Displays a 3D rendering of your simulated galaxy, which can be rotated and zoomed in on.

—

PlotCompare.py

e.g. : python PlotCompare.py

Displays a 3D rendering of your simulated galaxy overlaid with the galaxy clustered into
nearby regions, which can be rotated and zoomed in on. Individual region size on the plot
corresponds to their relative radial size.

—

LongitudeHist.py (gc, sun) (numberBins) (minDistance) (maxDistance)

e.g. : python RadialHist.py sun 30 17 24

Displays a histogram of number of HII regions for a given longitude. The search area
can either be centered on the Sun or Galactic Center.

In addition to your location in the galaxy (gc, sun) number of histogram bins is also
an input parameter. You must also set what range you want to search in the galaxy. For
instance, if you would only like to display distant HII regions, you could input 17 24 as the
final two parameters, which would only return regions between 17 kpc and 24 kpc from your
location.

—

ParamHist.py (age, mass, lum, radius) (numberBins)

e.g. : python ParamHist.py radius 30

Displays a histogram of various HII region parameters (including age, mass, luminosity, and
radius). The displayed plot is for all samples within your simulated galaxy.

Takes as the first input the parameter of interest (age, mass, lum, rad) and as the second
input number of histogram bins.

—

RadialLogHistGC.py (numberBins)

Displays a histogram of HII regions binned by distance from the galactic center as well as
a power law fit to the distribution beyond the galactic bar.

Displays to the terminal the exponent associated to two power law fits.

—

ThetaLnRGals.py

Displays a plot of Theta versus Log(R). A spiral galaxy should display sloped lines across the plot when visualized in this way.

—


