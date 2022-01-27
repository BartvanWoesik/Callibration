from spotpy.parameter import Uniform, Normal
from spotpy.objectivefunctions import mae
from runoff import MyFirstModel
import os
from pcraster import *
from pcraster.framework import *

class spot_setup(object):
    meltratePar = Uniform(low = 0.0001, high = 0.021)
    atmoloss = Uniform(low=0.000025, high = 0.021)
    seepageProportion = Uniform(low = 0.005, high = 0.21)
    templaps = Uniform(low = 0.0005, high = 0.01)
    infil  = Uniform(low = 0.0001, high = 0.05)

    def __init__(self,obj_func=None):
        #Find Path to Hymod on users system
        self.owd = os.path.dirname(os.path.realpath('C:\Bewaar\Data_Science\Spatial data analysis\Week 7\d'))
        self.hymod_path = self.owd+os.sep+'runoff.py'
        self.trueObs = []

        with open(self.owd+os.sep+'streamflow.txt') as flow:
            for line in flow:
                strflw = line.split()[1]
                self.trueObs.append(float(strflw))
                
    def simulation(self,x):
        #Here the model is actualy started with a unique parameter combination that it gets from spotpy for each time the model is called
        print(x)
        myModel = MyFirstModel( x[0] , x[1] , x[2] , x[3], x[4])
        
        dynamicModel = DynamicFramework(myModel,1461)
        dynamicModel.setQuiet()
        dynamicModel.run()
        data = myModel.simulation
        sim=[]
        for val in data:
            sim.append(val)
        #The first year of simulation data is ignored (warm-up)
        print(len(sim))
        return sim[366:]

    def evaluation(self):
        #The first year of simulation data is ignored (warm-up)

        return self.trueObs[366:]

    def objectivefunction(self,simulation,evaluation, params=None):
        
        like = mae(evaluation, simulation)
        print(like)
 
        return (like)
      
