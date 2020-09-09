import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np 

map: int = [[]]; 
grid_bits = { "clean": 0, "dirty": 1, "obstacle": 2, "unchecked" : -1 }
fig = plt.figure()


def generate_and_initialize(rows: int, cols: int):
	global map
	map = [[-1 for i in range(rows)] for j in range(cols)]
	pass


def explore(x: int, y: int, rows: int, cols: int):
	global grid_bits
	global map
	if (x < 0 or y < 0 or x >= rows or y >= rows or 
		map[x][y] == grid_bits["obstacle"] or map[x][y] == grid_bits["clean"]):
		return
	
	map[x][y] = 0

	explore(x+1, y  , rows, cols)
	explore(x-1, y  , rows, cols)
	explore(x  , y+1, rows, cols)
	explore(x  , y-1, rows, cols)
	
	
	
	pass


def assign_bits(type, grids):
	global map # reference global map
	
	for grid in grids:
		if len(grid):
			pos = grid.split()
			i = int(pos[0])
			j = int(pos[1])
			map [i][j] = type


def draw(position: int, title: str, rows: int, cols: int):
	ax = fig.add_subplot(1,2,position)
	ax.set_title(title) 
	ax.set_aspect('auto')
	ax.set_xticklabels([])
	ax.set_yticklabels([])
	plt.xticks(np.arange(0.5, rows + 1, step = 1))
	plt.yticks(np.arange(0.5, cols + 1, step = 1))
	plt.grid(True, which="both")
	im = plt.imshow(map)
	colors = im.cmap(im.norm(np.unique(map)))
	labels=list(grid_bits.keys())

	patches = [ mpatches.Patch(color=colors[i], label="{}".format(labels[i])) for i in range(len(colors)) ]
	
	plt.legend(handles=patches, bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0. , fontsize="large")
	# plt.colorbar(im, orientation='vertical')
	pass

def main():
	global map
	global grid_bits
	inpt = input("Enter number of rows and cols\n").split()
	
	if len(inpt) > 2:
		exit()

	rows = int(inpt[0])
	cols = int(inpt[1])


	generate_and_initialize(rows, cols)
	
	dirty_grids = input("Enter dirty grids\n").split(';')
	obstacle_grids = input("Enter Obstacle grids\n").split(';')

	if len(dirty_grids) > rows * cols or len(obstacle_grids) > rows * cols: 
		exit()

	assign_bits(grid_bits["dirty"], dirty_grids)
	assign_bits(grid_bits["obstacle"], obstacle_grids)

	
	draw(1, "Initial", rows, cols)

	explore(0, 0, rows, cols)
	
	draw(2, "Final", rows, cols)


	plt.show()

if __name__ == '__main__':
	main()