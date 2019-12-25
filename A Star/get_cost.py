import numpy as np
from initial_nodes import *

def get_Cost(node_1, node_2):
    idx_row_1 = node_1[0]
    idx_col_1 = node_1[1]

    idx_row_2 = node_2[0]
    idx_col_2 = node_2[1]

    dist_to_goal = np.array(goal_node) - np.array(node_1)
    dist = np.linalg.norm(dist_to_goal)
    d_cost = dist
    if ( idx_row_1!=idx_row_2 and idx_col_1!=idx_col_2 ):
        cost = 1.41 + d_cost
    else:
        cost = 1 + d_cost
    return cost

