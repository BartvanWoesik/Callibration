
import pandas as pd
import numpy as np

object_F = []
meltrate = []
atmoshpericloss = []
seepage = []
infil = []

with open("a_file.txt", 'r') as f:
    line_count = 0
    for lines in f:
        if line_count >=1:
            lines = lines[1: (len(lines)-2)]
            line = lines.split(',')
            object_F.append(line[4])
            meltrate.append(line[0])
            atmoshpericloss.append(line[1])
            seepage.append(line[2])
            infil.append(line[3])
            
        line_count+=1
data = {
    'object_':object_F,
    'meltrate': meltrate,
    'athmosperic': atmoshpericloss,
    'seepage': seepage,
    'infil': infil
}
df = pd.DataFrame(data)

meltratePar =       [0.008,0.005,0.003,0.002 ,0.001]
atmoloss =          [0.008, 0.004,0.004,0.002,0.001 ]
seepageProportion = [0.12,0.08,0.06,0.04 ,0.02]
infil  =            [0.08,0.06,0.0432,0.02 ,0.01]
results = df.iloc[87,]
print("Meltrate value is", meltratePar[int(results['meltrate'])])
print("Athomosperic Loss value is", atmoloss[int(results['athmosperic'])])
print("seepage value is", seepageProportion[int(results['seepage'])])
print("Infiltration value is", infil[int(results["infil"])])


