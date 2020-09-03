import matplotlib.pyplot as plt
import numpy as np 

map: int = [[]]; 
grid_bits = { "clean": 0, "dirty": 1, "obstacle": 2, "unchecked" : -1 }


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
		i = int(grid[0])
		j = int(grid[1])
		map [i][j] = type


def main():
	global map
	global grid_bits
	inpt = input("Enter number of rows and cols\n").split()
	
	if len(inpt) > 2:
		exit()

	rows = int(inpt[0])
	cols = int(inpt[1])

	# limiting to 9 x 9 grids
	if rows > 9 or cols > 9:
		exit()
	

	generate_and_initialize(rows, cols)
	
	dirty_grids = input("Enter dirty grids").split()
	obstacle_grids = input("Enter Obstacle grids").split()

	if len(dirty_grids) > rows * cols or len(obstacle_grids) > rows * cols: 
		exit()

	assign_bits(grid_bits["dirty"], dirty_grids)
	assign_bits(grid_bits["obstacle"], obstacle_grids)

	fig = plt.figure()
	ax = fig.add_subplot(1,2,1)
	ax.set_title('Initial') 
	ax.set_aspect('equal')
	ax.set_xticklabels([])
	ax.set_yticklabels([])
	plt.xticks(np.arange(0.5, rows + 1, step = 1))
	plt.yticks(np.arange(0.5, cols + 1, step = 1))
	plt.grid(True, which="both")
	im = plt.imshow(map)
	plt.colorbar(im, orientation='vertical')
	

	explore(0, 0, rows, cols)
	
	ax = fig.add_subplot(1,2,2)
	ax.set_title('Cleaned') 
	ax.set_aspect('auto')
	plt.xticks(np.arange(0.5, rows+1, step = 1))
	plt.yticks(np.arange(0.5, cols+1, step = 1))
	plt.imshow(map)
	plt.grid(True, which="both")
	ax.set_xticklabels([])
	ax.set_yticklabels([])
	im = plt.imshow(map)
	plt.colorbar(im, orientation='vertical')


	plt.show()

if __name__ == '__main__':
	main()