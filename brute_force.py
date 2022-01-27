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

meltratePar =       [0.8,0.6,0.4,0.2 ,0]
atmoloss =          [0.8,0.6,0.4,0.2 ,0]
seepageProportion = [0.8,0.6,0.4,0.2 ,0]
templaps =          [0.8,0.6,0.4,0.2 ,0]
infil  =            [0.8,0.6,0.4,0.2 ,0]

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
            for p in range(0,5):
                for m in range (0,5):
                    old_time = new_time
                    new_time = time.time()
                    counter +=1
                    print((new_time - old_time))
                  
                    print(counter)
                    myModel = MyFirstModel(melt=meltratePar[i] , 
                                atmospericLoss= atmoloss [j],
                                seepage= seepageProportion[k],
                                templap= templaps[p],
                                infil= infil[m]
                                )
                    dynamicModel = DynamicFramework(myModel,1461)
                    dynamicModel.setQuiet()
                    dynamicModel.run()
                    data = myModel.simulation
                    like = mae(evaluation(), data[366:])
