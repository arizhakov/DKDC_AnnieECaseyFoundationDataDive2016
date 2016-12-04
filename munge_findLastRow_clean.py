import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#all
csv_CYF_Merged = r"C:\...\Improving Foster Care Placements\CYF Merged.csv"
#small
#csv_CYF_Merged = r"C:\...\Improving Foster Care Placements\CYF Merged_small.csv"
df_CYF_Merged = pd.read_csv(csv_CYF_Merged)

### Write to csv
header = df_CYF_Merged.columns
df = pd.DataFrame()
df = df.append([header.T], ignore_index=True)

## TODO ASSUMPTION: this may be the reason for having n-1 unique clients 
final_index = df_CYF_Merged.shape[0] - 1

## ASSUMPTION: 'CL_ID' and 'HOME_RMVL_SEQ_NBR' are sorted(increasing) 
for index, row in df_CYF_Merged.iterrows():
    if index == 0:
        child = row['CL_ID']
    elif index == final_index:
        r = df_CYF_Merged.iloc[index].values
        df = df.append([r], ignore_index=True)
    else:    
        if (row['CL_ID'] != child): 
            r = df_CYF_Merged.iloc[index-1].values
            df = df.append([r], ignore_index=True)
            child = row['CL_ID']
            print "index-1", index-1
'''
Note the above for loop is not efficient. 
In 
Line 29: df = df.append([r], ...)
this step is a major bottleneck. Problem is memory allocation. 
At every call of line 29, a new memory allocation step is performed. 
SO articles are helpful to solve the problem.
Find memory preallocation with "df.append" on search.

Also, the pandas command: df.drop_duplicates()
may be very useful and efficient instead of the manual approach above.
'''

            
with open(r"C:\...\Improving Foster Care Placements\out.csv", 'a') as f:
    df.to_csv(f, header=False)     
