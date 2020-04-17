import cv2 as cv
import numpy as np
import operator


#function to display the image:
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html
def showImage(img):
	cv.imshow('Processing Images for COMP4102', img)
	cv.waitKey(0)
	cv.destroyAllWindows()


#Pre processing the image by the following steps:
	#1. blurring the image by cv.GaussianBlur with kernel size of 9x9
	#2. threshholding the image using cv.adaptiveThreshold which gives
		#better results over general threshholding
	#3. inverting the colour of the image using cv.bitwise_not
	#4. dilating the image to increase the thickness of lines to be more visible
def preProcessImg(image):
	blur = cv.GaussianBlur(img, (9,9), 0)
	thresh = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
	thresh = cv.bitwise_not(thresh, thresh)

	'''
	if not skipDilate:
		kernel = np.array([[0., 1., 0.], [1., 1., 1.], [0., 1., 0.]], np.uint8)
		thresh = cv.dilate(thresh, kernel)
	'''
	return thresh


#https://docs.python.org/3/library/operator.html
#operator.itemgetter returns a tuple of lookup values. For example: After f = itemgetter(2), the call f(r) returns r[2].
#to get the 4 corners of the puzzle, we did the following according to the position of the puzzle on the screen:
	#bRight is the bottom right corner and it has the biggest x and y coordinates
	#bLeft is the bottom left corner and it has the smallest x but biggest y coordinates
	#tRight is the top right corner and it has the biggest x and smallest y coordinates
	#tLeft is the top left corner and it has the smallest x and y coordinates
def cornersAndContours(processedImg):
	extContours, h = cv.findContours(processedImg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
	extContours = sorted(extContours, key = cv.contourArea, reverse = True)
	square = extContours[0]

	tLeft, _ = min(enumerate([pt[0][0] + pt[0][1] for pt in square]), key=operator.itemgetter(1))
	tRight, _ = min(enumerate([pt[0][0] - pt[0][1] for pt in square]), key=operator.itemgetter(1))
	bRight, _ = max(enumerate([pt[0][0] + pt[0][1] for pt in square]), key=operator.itemgetter(1))
	bLeft, _ = max(enumerate([pt[0][0] - pt[0][1] for pt in square]), key=operator.itemgetter(1))

	#return from tLeft to bLeft in clockwise
	return [square[tLeft][0], square[tRight][0], square[bRight][0], square[bLeft][0]]


#displaying points using the displayPoints function,
#the function was used in the following website:
#https://www.programcreek.com/python/example/70398/cv2.COLOR_GRAY2BGR
def displayPoints(processedImg, corners):
	radius = 9
	colour = (255, 0, 0)
	if len(colour) == 3:
		if len(processedImg.shape) == 2:
			processedImg = cv.cvtColor(processedImg, cv.COLOR_GRAY2BGR)
		elif processedImg.shape[2] == 1:
			processedImg = cv.cvtColor(processedImg, cv.COLOR_GRAY2BGR)

	for corner in corners:
		processedImg = cv.circle(processedImg, tuple(int(x) for x in corner), radius, colour, -1)
	showImage(processedImg)
	return processedImg


#we are cropping the image using two cv functions: getPerspectiveTransform
#and warpPerspective, examples on how to use them were found in:
#https://docs.opencv.org/3.1.0/da/d6e/tutorial_py_geometric_transformations.html
#calculated longest side to make the final puzzle picture same box size of that side
#that method along with the extractCells and showCells functions were
#used from https://medium.com/@neshpatel/solving-sudoku-part-ii-9a7019d196a2
def cropImg(processedImg, corners):

	def distance(p1, p2):
		return np.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))

	longestSide = max([
		distance(corners[0], corners[1]),
		distance(corners[1], corners[2]),
		distance(corners[2], corners[3]),
		distance(corners[0], corners[3])
	])

	#corners[0] = tLeft, corners[1] = tRight, corners[2] = bRight, corners[3] = bLeft
	src = np.float32([corners[0], corners[3], corners[2], corners[1] ])
	dst = np.float32([[0, 0], [longestSide - 1, 0], [longestSide - 1, longestSide - 1], [0, longestSide - 1]])

	M = cv.getPerspectiveTransform(src,dst)

	return cv.warpPerspective(processedImg, M, (int(longestSide), int(longestSide)))

#We would extract the cells from the cropped picture by
#slicing the cells by crop.shape[:1] and dividing that by 9 to get an indvidual cell
#we would then iterate over the cells using the nested for loop
def extractCells(crop):
	cells = []
	side = crop.shape[:1]
	side = side[0] / 9

	for i in range(9):
		for j in range(9):
			p1 = (i * side, j * side)
			p2 = ((i + 1) * side, (j + 1) * side)
			cells.append((p1, p2))
	return cells

#We would then show the grid in red using the following function
#we set the colour to red, convert the image again to grayscale as we did in displayPoints
#we would then iterate over the cells, drawing the grid using cv.rectangle:
#https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html
def showCells(crop, cells):
	colour = (0, 0, 255)
	if len(colour) == 3:
		if len(crop.shape) == 2:
			crop = cv.cvtColor(crop, cv.COLOR_GRAY2BGR)
		elif crop.shape[2] == 1:
			crop = cv.cvtColor(crop, cv.COLOR_GRAY2BGR)

	for cell in cells:
		crop = cv.rectangle(crop, tuple(int(x) for x in cell[0]), tuple(int(x) for x in cell[1]), colour, 5)
	showImage(crop)



# Main:
img = cv.imread("test3.jpg")
showImage(img)

#read image and convert to grayscale right away
img = cv.imread("test3.jpg", cv.IMREAD_GRAYSCALE)
processedImg = preProcessImg(img)
showImage(processedImg)

corners = cornersAndContours(processedImg)
displayPoints(processedImg, corners)

crop = cropImg(processedImg, corners)
showImage(crop)

cells = extractCells(crop)
showCells(crop, cells)
