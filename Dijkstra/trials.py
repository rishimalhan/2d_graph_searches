import time
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from get_neighbours import get_neighbours

strt_node = [95,95]
goal_node = [10,10]
# a = 2
# b = np.array([
#             [4,5,6],
#             [8,9,10]] , dtype=int)
# print (b*a)
# time.sleep(1)
# print (b*10)
# print ("Creating Grid\n")
# grid = np.array( [ [1, 1, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 0, 1, 1, 1, 1],
#                     [1, 1, 1, 0, 1, 1, 1, 1],
#                    [1, 1, 1, 0, 1, 1, 1, 1],
#                    [0, 0, 0, 0, 1, 0, 1, 1],
#                    [1, 1, 0, 0, 1, 0, 1, 1],
#                    [1, 1, 1, 1, 1, 1, 1, 1],] )
#
# print(grid)

basewidth = 100
im = Image.open("Grid_Resize2.png").convert("1")

# wpercent = (basewidth/float(im.size[0]))
# hsize = int((float(im.size[1])*float(wpercent)))
# img = im.resize((basewidth,hsize), Image.ANTIALIAS)
# img.save("C:\\Users\Rishi Malhan\PycharmProjects\Diijkstra_Grid\Grid_Resize3.png")

grid = np.array(im.getdata()).reshape(im.size[0], im.size[1])
for i in range(0, grid.shape[0]):
    for j in range(0, grid.shape[1]):
        if (grid[i][j] == 255):
            grid[i][j] = 1
        else:
            grid[i][j] = 0


for i in range(0,50):
    for j in [98,99,100]:
        neighbors = get_neighbours(np.array([i,j]))
        for k in range(0, neighbors.shape[0]):
            if (grid[neighbors[k][0]][neighbors[k][1]] not in [1,0]):
                grid[neighbors[k][0]][neighbors[k][1]] = 4


# PLOT MAP
grid[strt_node[0]][strt_node[1]] = 2
grid[goal_node[0]][goal_node[1]] = 3
grid_plot = plt.imshow(grid)
plt.show()


