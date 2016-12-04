import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#all
csv_OUT = r"C:\...\Improving Foster Care Placements\out.csv"
#small
#csv_CYF_Merged = r"C:\...\Improving Foster Care Placements\CYF Merged_small.csv"
df_OUT = pd.read_csv(csv_OUT)

#add GoodBad column
df_OUT["GoodBad"] = ""


#import Lookup table
df_GoodBad_lookup = pd.read_csv(r"C:\...\Improving Foster Care Placements\Placement Exit - Spell - Reason Values - JS.csv", header=None)

#match Good/Bad value from judgement doc to Placement info in the data
for index_0, row_0 in df_OUT.iterrows():
    GB = row_0["Placement.Exit.Reason"]
    for index_1, row_1 in df_GoodBad_lookup.iterrows():
        if row_1[0] == GB:
            print row_1[0] == GB
            df_OUT.set_value(index_0, "GoodBad", row_1[1])

#exit
with open(r"C:\....\Improving Foster Care Placements\outGB.csv", 'a') as f:
    df_OUT.to_csv(f, header=True)  
