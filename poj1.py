import numpy as np
import pandas as pd


data = pd.DataFrame(pd.read_csv("FCCdata.csv"))

#print(data.head)

search1 = data[data['geography_type'].str.contains("State")]
state1= search1[search1['geography_desc'].str.contains("New York")]

#cop res,bis,cable res,cab biz,

coppercol=state1.columns[4:112:7]
cablecol=state1.columns[5:112:7]
#print(state1[coppercol.values].values)
#print(coppercol.values)
res=coppercol[::2]
biz=coppercol[1::2]
#print(state1[res].values)

#print(res)
#print(state1[coppercol])

types=["copper"," cable"," fiber"," gso_satellite"," ngso_satellite"," unlicensed_tfw"," licensed_tfw"," other"] #," mobile_voice"," 3g"," 4g"," 5g"]" lbr_tfw",
building=["Residential",'Business']

test = [state1[res].values[0].tolist(),state1[biz].values[0].tolist()]
#print(test)
tester = pd.DataFrame(test,index=building,columns=types)
#print(tester)
#print(state1['t1_s1_r'],state1['t1_s1_b'])
speedselect = {
    1:state1.columns[4:112:7],
    2:state1.columns[5:112:7],
    3:state1.columns[6:112:7],
    4:state1.columns[7:112:7],
    5:state1.columns[8:112:7],
    6:state1.columns[9:112:7]
}
print(speedselect[6])
state=input("Please Enter the State Name in full ex:New York,Texas: ")
speed=input("PLs enter the speed to search, .2,")
def states(state):
    
    #getting all states
    search2 = data[data['geography_type'].str.contains("State")]
    #get pecific state
    state2= search2[search2['geography_desc'].str.contains(state)]
    
    #get the data for each 
    coppercol=state2.columns[4:112:7]
    cablecol=state2.columns[5:112:7]
    #!!!!! need to change to request speed type
    
    speedselect={
        1:state2.columns[4:112:7],
        2:state2.columns[5:112:7],
        3:state2.columns[6:112:7],
        4:state2.columns[7:112:7],
        5:state2.columns[8:112:7],
        6:state2.columns[9:112:7]
    }
    speedselect[1]

    def speed(speed):
        speedselect={
        1:state2.columns[4:112:7],
        2:state2.columns[5:112:7],
        3:state2.columns[6:112:7],
        4:state2.columns[7:112:7],
        5:state2.columns[8:112:7],
        6:state2.columns[9:112:7],
    }


    #sseprating by residentail and business
    res=coppercol[::2]
    biz=coppercol[1::2]
    #types of conections
    types=["copper"," cable"," fiber"," gso_satellite"," ngso_satellite"," unlicensed_tfw"," licensed_tfw"," other"] #," mobile_voice"," 3g"," 4g"," 5g"]" lbr_tfw",
    building=["Residential",'Business']
    
    #table info
    test = [state2[res].values[0].tolist(),state2[biz].values[0].tolist()]
    tester = pd.DataFrame(test,index=building,columns=types)
    print(tester)