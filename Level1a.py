import json
import math

#read the json file level0
file = open('level1a.json','r')
data = json.loads(file.read())

#List to store the neighbourhoods
neighbourhoods = []
for i in data['neighbourhoods']:
    neighbourhoods.append(i)
#rest_incl = ['r0'] + neighbourhoods
#print(neighbourhoods)

#list to store the capacity

capacity=[]
for i in neighbourhoods:
    capacity.append(data['neighbourhoods'][i]['order_quantity'])
#print(capacity)

# To store the distance from one restaurant to another
distances = []
restaurant_dist = [0]+data['restaurants']['r0']['neighbourhood_distance']

distances.append(restaurant_dist)
index = 0
for i in neighbourhoods:
	temp = [data['restaurants']['r0']['neighbourhood_distance'][index]]+data['neighbourhoods'][i]['distances']
	distances.append(temp)
	index += 1
    
def solve_tsp_nearest(capacity):
    c=0
    no_of_neighbourhood=len(capacity)
    currCapacity=0 
    visited = [False] *  no_of_neighbourhood
    maxCapacity=data['vehicles']['v0']['capacity']
    totPaths=[]
    
    while c < 20:
        path=['r0']
        while currCapacity <= maxCapacity:
            
            minCapacity = min(capacity)
            if minCapacity+currCapacity > maxCapacity:
                 break
            index1=capacity.index(minCapacity)
            visited[index1]=True
            currCapacity += capacity[index1]
            path.append(neighbourhoods[index1])
            capacity[index1]=math.inf
            c+=1
        path = path+['r0']
        totPaths.append(path)
        path=['r0']
        currCapacity=0
        
    return totPaths
         
tour=solve_tsp_nearest(capacity)
temp_dict=dict()
for i in range(len(tour)):
   pathI='path'+str(i+1)
   temp_dict[pathI]=tour[i]
result = dict(v0 = temp_dict)
#print(result)

with open('level1a_output.json','w') as outputFile:
     json.dump(result,outputFile)

