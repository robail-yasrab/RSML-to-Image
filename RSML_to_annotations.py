# Put RSML and dateset images to same file 
import cv2
import numpy as np
from rsml import RSMLParser
from glob import glob
import os

rsml = glob("./..*.rsml") #give path to RSML dirc.
i= len(rsml)
print i
for x in range (0, i):
	rsml_file = rsml[x]
	name = os.path.basename(rsml_file)
	name = name[:-5]
	print name

	img = cv2.imread(rsml_file[:-4]+'tif', 0) #change for .jpg/.png
	height, width = img.shape
	print height, width

# Create from RSML and round all points
	plants = RSMLParser.parse(rsml_file, round_points = True)
	# RSML supports multiple plants in a list, select the first (and only) one
	#plant = plants[0]

	line_thickness = 4

	# Create blank image
	im = np.zeros((height,width,3), dtype=np.uint8)

	# The pairwise function in Root iterates through each pair of points so you can draw a line
	# E.g if a root has points [a, b, c, d] the pairwise produces
	# [(a,b), (b,c), (c,d)]
	# If you don't want to do that, just iterate through root.points

	# Draw lateral roots
	for plant in plants:
		for r in plant.lateral_roots():
			for p in r.pairwise():
				cv2.line(im, p[0], p[1], (255,0,0), line_thickness)

		# Draw primary roots
		for r in plant.primary_roots():
			for p in r.pairwise():
				cv2.line(im, p[0], p[1], (0,255,0), line_thickness)
		############################################################################Primery tip circle ######
		# Just for example:
		# Draw primary root tip circles
		for r in plant.primary_roots():
			for p in r.pairwise():
				cv2.ellipse(im, r.end, (2,2), 0.0, 0.0, 360.0, (0,255,255), line_thickness//2)
		########################################################################################################

		for r in plant.lateral_roots():
			for p in r.pairwise():
				cv2.ellipse(im, r.end, (2,2), 0.0, 0.0, 360.0, (255,0,255), line_thickness//2)
		# Draw seed location circle
		cv2.ellipse(im, plant.seed, (2,2), 0.0, 0.0, 360.0, (255,255,255), line_thickness//2)

	# Save mask
	cv2.imwrite('./../'+name+'.png',im) # add path for output


	# for real time display 
	#cv2.imwrite('mask.png',im)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
