import numpy as np
def get_manhattan_cost(node_1, node_2):

    idx_row_1 = node_1[0]
    idx_col_1 = node_1[1]

    idx_row_2 = node_2[0]
    idx_col_2 = node_2[1]

    squared_sum = 0;
    for idx in range(0,len(node_1)):
        squared_sum = squared_sum + (node_1[idx] - node_2[idx])**2;

    cost = squared_sum**0.5


    # dist_to_goal = np.array(node_2) - np.array(node_1)
    # cost = np.linalg.norm(dist_to_goal)

    # if ( idx_row_1!=idx_row_2 and idx_col_1!=idx_col_2 ):
    #     cost = 1.41
    # else:
    #     cost = 1

    return cost

