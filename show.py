

import spotpy
from spot_setup import spot_setup
from matplotlib import *
import sys
from pylab import *

spot_setup  = spot_setup()

results = spotpy.analyser.load_csv_results('SA_model')

#spotpy.analyser.plot_parametertrace(results)  
fig= plt.figure(1,figsize=(9,5))
plt.plot(results['like1'])
plt.ylabel('MAE')
plt.xlabel('Iteration')
plt.grid(color = 'gray' , linestyle = '-')
plt.title('SCUEA objective function')
fig.savefig('SCEUA_objectivefunctiontrace.png',dpi=300)

bestindex,bestobjf = spotpy.analyser.get_minlikeindex(results)
best_model_run = results[bestindex]
fields=[word for word in best_model_run.dtype.names if word.startswith('sim')]
best_simulation = list(best_model_run[fields])
fig= plt.figure(figsize=(9,5))
ax = plt.subplot(1,1,1)
ax.plot(best_simulation,color='red',linestyle='solid', label='Best objf.='+str(bestobjf))
ax.plot(spot_setup.evaluation(),'r.', color = 'blue', linestyle = 'solid',markersize=3, label='Observation data')
plt.xlabel('Number of Observation Points')
plt.ylabel ('Discharge [l s-1]')
plt.legend(loc='upper right')
plt.title('SCUEA best model run')
plt.grid(color = 'gray' , linestyle = '-')
fig.savefig('SCEUA_best_modelrun.png',dpi=300)