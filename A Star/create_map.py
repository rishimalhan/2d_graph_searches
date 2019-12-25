import numpy as np
from PIL import Image

def create_grid():
    # grid = np.array([[1, 1, 1, 1, 1, 1, 1, 1],
    #                  [1, 0, 0, 0, 1, 1, 1, 1],
    #                  [1, 1, 1, 0, 1, 1, 1, 1],
    #                  [1, 1, 1, 0, 1, 1, 1, 1],
    #                  [0, 0, 0, 0, 0, 0, 1, 1],
    #                  [1, 1, 0, 0, 1, 0, 1, 1],
    #                  [1, 1, 1, 1, 1, 1, 1, 1], ])
    #
    # im = Image.open("Grid_Resize2.png").convert("1")
    # grid = np.array(im.getdata()).reshape(im.size[0], im.size[1])
    #
    # for i in range(0, grid.shape[0]):
    #     for j in range(0, grid.shape[1]):
    #         if (grid[i][j] == 255):
    #             grid[i][j] = 1
    #         else:
    #             grid[i][j] = 0

    grid = np.ones((100,100))
    return grid