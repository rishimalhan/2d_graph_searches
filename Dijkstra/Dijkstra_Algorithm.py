from create_grid import create_grid
import numpy as np
import matplotlib.pyplot as plt
from queue import PriorityQueue
from get_neighbours import get_neighbours
from get_manhattan_cost import get_manhattan_cost
from create_node import create_node
from create_node import create_key
import time
from initial_nodes import *
from pandas import DataFrame

# INITIALIZE CODE
queue = PriorityQueue(maxsize=0)
grid = np.array(create_grid())
Nodes = {}
terminate = False

curr_node = create_node(strt_node,None,0,True,False)
Nodes[curr_node.map_key] = curr_node
queue.put([curr_node.cost, curr_node.map_key])

count = 1
t0 = time.clock()

# DIIJKSTRA ALGORITHM
print("Running Diijkstra.....")
while queue.empty()==False:
    curr_node = Nodes[queue.get()[1]]
    Nodes[curr_node.map_key].is_open = False
    Nodes[curr_node.map_key].is_closed = True

    if (count%500)==0:
        print("Iteration Number:  ",count)

    neighbors = get_neighbours(curr_node.id)
    for i in range(0,neighbors.shape[0]):

        cost = get_manhattan_cost(curr_node.id, neighbors[i]) + curr_node.cost
        #Check if the Node already exits
        node_exists = create_key(neighbors[i]) in Nodes.keys()

        if ( node_exists==False ):
            count += 1
            neighbr_node = create_node(neighbors[i],curr_node.id,cost,True,False)
            Nodes[neighbr_node.map_key] = neighbr_node
            queue.put([neighbr_node.cost, neighbr_node.map_key])
            grid[neighbors[i][0]][neighbors[i][1]] = 3

        elif ( (node_exists==True) ):
            if( cost < (Nodes[create_key(neighbors[i])].cost - 0.0001 ) ):
                Nodes[create_key(neighbors[i])].cost = cost
                Nodes[create_key(neighbors[i])].parent_id = curr_node.parent_id
                Nodes[create_key(neighbors[i])].is_closed = False
                Nodes[create_key(neighbors[i])].is_open = True
                queue.put([ Nodes[create_key(neighbors[i])].cost, Nodes[create_key(neighbors[i])].map_key ])
                grid[neighbors[i][0]][neighbors[i][1]] = 3

    # grid_plot = plt.imshow(grid)
    # plt.show()

t1 = time.clock()

print("\nGenerating Path")
# Generate Path
path = []
path_complete = False
parent = Nodes[create_key(goal_node)].parent_id
while path_complete==False:
    path.append(Nodes[create_key(parent)].id)
    parent = Nodes[create_key(parent)].parent_id
    if (parent==None):
        path_complete = True

path = np.array(path[:][:])
tot_cost = 0
for i in range(0,len(path)):
    # print([ path[i][0],path[i][1] ])
    grid[path[i][0],path[i][1]] = 4
    tot_cost += Nodes[create_key([ path[i][0],path[i][1] ])].cost

# PLOT MAP
grid[strt_node[0]][strt_node[1]] = 2
grid[goal_node[0]][goal_node[1]] = 2

for i in range(0,grid.shape[0]):
    for j in range(0,grid.shape[1]):
        if(grid[i][j]!=0):
            grid[i][j] = Nodes[create_key([i,j])].cost
        else:
            grid[i][j] = 500

df = DataFrame(grid)
df.to_csv("Grid_2_FMM.csv",index_label=False,header=False,index=False)

grid_plot = plt.imshow(grid)
print("Total Time: ", (round((t1-t0)*10000))/10000, " seconds")
print("Total Cost:  ",tot_cost)
plt.show()
