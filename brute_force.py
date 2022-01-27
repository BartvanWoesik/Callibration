from runoff import MyFirstModel
import os
from spotpy.objectivefunctions import mae
from spotpy.parameter import Uniform, Normal
from spotpy.objectivefunctions import mae
from runoff import MyFirstModel
import os
from pcraster import *
from pcraster.framework import *

import time

import pandas as pd

meltratePar =       [0.008,0.005,0.003,0.002 ,0.001]
atmoloss =          [0.008, 0.004,0.004,0.002,0.001 ]
seepageProportion = [0.12,0.08,0.06,0.04 ,0.02]
infil  =            [0.08,0.06,0.0432,0.02 ,0.01]

outcomes = []

# Change path on new device!!
owd = os.path.dirname(os.path.realpath('C:\Bewaar\Data_Science\Spatial data analysis\Week 7\d'))
hymod_path = owd+os.sep+'runoff.py'
trueObs = []

with open(owd+os.sep+'streamflow.txt') as flow:
    for line in flow:
        strflw = line.split()[1]
        trueObs.append(float(strflw))

def evaluation():
    #The first year of simulation data is ignored (warm-up)
    return trueObs[366:]
counter = 0 
new_time = time.time()
tot_run = 5^5
for i in range(0,5):
    for j in range (0,5):
        for k in range (0,5):
                for m in range (0,5):
                    old_time = new_time
                    new_time = time.time()
                    counter +=1
                    print((new_time - old_time))
                  
                    print(counter)
                    myModel = MyFirstModel(melt=meltratePar[i] , 
                                atmospericLoss= atmoloss [j],
                                templap=0.005,
                                seepage= seepageProportion[k],
                                infil= infil[m]
                                )
                    dynamicModel = DynamicFramework(myModel,1461)
                    dynamicModel.setQuiet()
                    dynamicModel.run()
                    data = myModel.simulation
                    like = mae(evaluation(), data[366:])
                    outcomes.append([i,j,k,m,like])
                  
textfile = open("a_file.txt", "w")
textfile.write("Brute Force results: MAE 3 years")
for element in outcomes:
    textfile.write(str(element) + "\n")
textfile.close()