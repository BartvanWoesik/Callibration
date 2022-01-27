from pcraster import *
from pcraster.framework import *

import spotpy
from spot_setup import spot_setup
from matplotlib import *
import sys
from pylab import *

spot_setup  = spot_setup()



rep = 5000
sampler = spotpy.algorithms.sceua(spot_setup, dbname='SA_model', dbformat='csv') 
sampler.sample(rep)
