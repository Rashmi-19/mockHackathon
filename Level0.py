import json
import math

#read the json file level0
file = open('level0.json','r')
data = json.loads(file.read())

#List to store the neighbourhoods
neighbourhoods = []
for i in data['neighbourhoods']:
    neighbourhoods.append(i)
rest_incl = ['r0'] + neighbourhoods

# To store the distance from one restaurant to another
distances = []
restaurant_dist = [0]+data['restaurants']['r0']['neighbourhood_distance']

distances.append(restaurant_dist)
index = 0
for i in neighbourhoods:
	temp = [data['restaurants']['r0']['neighbourhood_distance'][index]]+data['neighbourhoods'][i]['distances']
	distances.append(temp)
	index += 1
#print(distances)
    
def solve_tsp_nearest(distances):
    no_of_neighbourhood = len(distances)
    visited = [False] *  no_of_neighbourhood
    tour = []
    all_neighbourhood_visited_dist=[]
    total_distance = 0
    
    # Start at the first neighbourhood
    current_neighbourhood = 0
    tour.append(current_neighbourhood)
    all_neighbourhood_visited_dist.append(rest_incl[0])
    visited[current_neighbourhood] = True
    
    
    # Repeat until all neighbourhoods have been visited
    while len(tour) <  no_of_neighbourhood:
        nearest_neighbourhood = None
        nearest_distance = math.inf

        # Find the nearest unvisited neighbourhood
        for i in range( no_of_neighbourhood):
            if not visited[i]:
                distance = distances[current_neighbourhood][i]
                if distance < nearest_distance:
                    nearest_neighbourhood = i
                    nearest_distance = distance

        # Move to the nearest neighbourhood
        current_neighbourhood = nearest_neighbourhood
        tour.append(current_neighbourhood)
        all_neighbourhood_visited_dist.append(rest_incl[current_neighbourhood])
        visited[current_neighbourhood] = True
        total_distance += nearest_distance

    # Complete the tour by returning to the starting city
    tour.append(0)
    all_neighbourhood_visited_dist.append(rest_incl[0])
    total_distance += distances[current_neighbourhood][0]

    return all_neighbourhood_visited_dist, total_distance

tour,total_distance = solve_tsp_nearest(distances)

temp_dict = dict(path = tour)
result = dict(v0 = temp_dict)
print(result)

with open('level0_output.json','w') as outputFile:
     json.dump(result,outputFile)
