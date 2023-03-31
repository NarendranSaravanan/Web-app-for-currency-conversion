import pandas as pd

import glob

import os, sys

path = "N:/amba_naren" # enter the path of folder of all csv files for filling missing data

  
# csv files in the path
files = glob.glob(path + "/*.csv")
for fname in files:
        print(fname)
        df = pd.read_csv(fname)
        
        df = df[df['REGIONID'] == 'TAS1']
        print(df)
        df.loc[df['PEAKRRP'].isnull(),'PEAKRRP'] = df['AVGRRP']
        print(df)
        df.to_csv(fname, index=False)
