from create_map import create_grid
import numpy as np

def get_neighbours(node_id):
    grid = np.array(create_grid())
    grid_rows = grid.shape[0]
    grid_cols = grid.shape[1]

    idx_row = node_id[0]
    idx_col = node_id[1]

    neighbors = []
    for i in [0,1,-1]:
        for j in [0,1,-1]:
            neigh_row = idx_row + i
            neigh_col = idx_col + j
            if ( (neigh_row>=grid_rows) or (neigh_col>=grid_cols) or (neigh_row<0) or (neigh_col<0) ):
                continue
                pass
            if (neigh_row==idx_row and neigh_col==idx_col):
                continue
                pass
            else:
                if (collision_check(grid,[neigh_row,neigh_col])==False):
                    neighbors.append([neigh_row,neigh_col])

    # neighbor Search ends
    return np.array(neighbors)

def collision_check(grid,index):
    collision = False
    if (grid[index[0],index[1]]==0):
        collision=True
    return collision