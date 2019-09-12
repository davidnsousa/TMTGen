from tkinter import *
from shutil import copyfile
import random
import math

root = Tk()

f = open('config')
lines = f.read().splitlines()
container_size =[int(lines[0]), int(lines[1])]
node_size = int(lines[2])
n_phases = int(lines[3])
node_sequence = []
for l in lines[4:4+n_phases]:
	node_sequence.append(l.split(" "))

OUTPUT_NAME = lines[4+2*n_phases+1]
f.close()
copyfile('config', OUTPUT_NAME)

midW = root.winfo_screenwidth()/2
midH = root.winfo_screenheight()/2
x0 = midW-container_size[0]/2
y0 = midH-container_size[1]/2
x1 = midW+container_size[0]/2
y1 = midH+container_size[1]/2
coordinates = [x0, y0, x1, y1]

pos = [[0, 0]]
with open(OUTPUT_NAME, 'a') as f:
	for level in node_sequence:
		for tag in level:
			while True:
				x = random.randint(coordinates[0]+node_size, coordinates[2]-node_size)
				y = random.randint(coordinates[1]+node_size, coordinates[3]-node_size)
				if not any(math.sqrt((x-p[0])**2+(y-p[1])**2) <= 2*node_size for p in pos):
					break
			pos.append([x, y])
			out = ' '.join(str(e) for e in [x, y])
			f.write("%s\n" % out)
		pos = [[0, 0]]

f.close()
