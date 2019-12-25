from initial_nodes import *
from create_map import create_grid
import numpy as np
import matplotlib.pyplot as plt
from queue import PriorityQueue
from neighborhood import get_neighbours
from get_cost import get_Cost
from node_prop import create_node
from node_prop import create_key
import time


# INITIALIZE CODE
queue = PriorityQueue(maxsize=0)
grid = np.array(create_grid())
Nodes = {}
goal_reached = False
curr_node = create_node(strt_node,None,0,True,False)
Nodes[curr_node.map_key] = curr_node
queue.put([curr_node.cost, curr_node.map_key])

count = 1
t0 = time.clock()

# AStar ALGORITHM
print("Running A-Star Search.....")
while (goal_reached==False and queue.empty!=False):
    curr_node = Nodes[queue.get()[1]]
    Nodes[curr_node.map_key].is_open = False
    Nodes[curr_node.map_key].is_closed = True

    if (count%500)==0:
        print("Iteration Number:  ",count)

    neighbors = get_neighbours(curr_node.id)
    for i in range(0,neighbors.shape[0]):

        cost = get_Cost(curr_node.id, neighbors[i]) + curr_node.cost
        #Check if the Node already exits
        node_exists = create_key(neighbors[i]) in Nodes.keys()
        # Check if Goal has been Reached
        if ( np.array_equal(neighbors[i],np.array(goal_node))):
            print("Goal Reached!")
            neighbr_node = create_node(np.array(goal_node), curr_node.id, cost, False, True)
            Nodes[neighbr_node.map_key] = neighbr_node
            goal_reached = True

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
                queue.put([Nodes[create_key(neighbors[i])].cost, Nodes[create_key(neighbors[i])].map_key])
                grid[neighbors[i][0]][neighbors[i][1]] = 3


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
grid_plot = plt.imshow(grid)
print("Total Time: ", (round((t1-t0)*10000))/10000, " seconds")
print("Total Cost:  ",tot_cost)
plt.show()
