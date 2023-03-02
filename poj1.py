import numpy as np
import pandas as pd


data = pd.DataFrame(pd.read_csv("FCCdata.csv"))

#print(data.head)

search1 = data[data['geography_type'].str.contains("State")]
state1= search1[search1['geography_desc'].str.contains("New York")]

#cop res,bis,cable res,cab biz,

coppercol=state1.columns[4:112:7]
cablecol=state1.columns[5:112:7]
print(state1[coppercol.values].values)
res=coppercol[::2]
biz=coppercol[1::2]

#print(res)
#print(state1[coppercol])

types=["copper"," cable"," fiber"," gso_satellite"," ngso_satellite"," unlicensed_tfw"," licensed_tfw"," other"] #," mobile_voice"," 3g"," 4g"," 5g"]" lbr_tfw",
building=["Residential",'Business']

test = [state1[res],state1[biz]]
#tester = pd.DataFrame(test,index=building,columns=types)
#print(tester)
#print(state1['t1_s1_r'],state1['t1_s1_b'])

