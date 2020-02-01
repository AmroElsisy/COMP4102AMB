# COMP4102 AMB
Title: Sudoko Solver Proposal

Group Name: AMB

Group Members: 

Amro Elsisy - 100917564

Menna Mohsen - 101007934

Bill Creber - 100884250

## Introduction:
Our team will be working on the sudoko solver project. We are planning to work with the sudoko solver algorithm and implement it on pictures captured from sudoko puzzles printed on paper. 

## The Challenge:
We shall be taking either a real-time snapshot via a phone camera or a scanned image of a potential sudoku puzzle page.
OpenCV has edge detection that we could use to find the game board, though we would have to determine the location of the discrete input boxes from the edges as well as the different line thickness for the unique groups. This is doubly important for variants where the 1-N character groups are not always a uniform box (ie. Jigsaw).

 We will have to interface with an OCR (Optical Character Recognition) engine like [Tesseract](https://opensource.google/projects/tesseract) to determine which unique character is where on the game grid (for both answers and clues) to then be passed to the solving algorithm(s).


## Goals and Deliverables: 
Our main goal is start with the default 9x9 puzzle and that is going to be our main focus when implementing the project. If we have time we will aim to solve the more elaborate variants of the much loved game like [Overlapping Grids](https://en.wikipedia.org/wiki/Glossary_of_Sudoku#Sudoku_variants), [Killer Sudoku](https://en.wikipedia.org/wiki/Killer_sudoku), or [Jigsaw](https://en.wikipedia.org/wiki/Nonomino).

The project should be able to outcome a recognizable puzzle with the unique characters that are on the sudoko grid. These recognized characters should then be used to solve the problem we have at hand using our suduko solver algorithm. We believe that these results are acheivable in the time frame that we have been provided our research indicates that there are a lot available resources and examples of image detection applied on a sudoko print outs. 


## Schedule:
From February 1st till March 31st, we would have around 8 weeks to finish our project.
 ### Weeks:
 * 1 and 2: We would be working on the sudoko solver algorithm.
 
 * 3 and 4: Implement thresholding techniques, blob extraction algorithms and Hough transform algorithms in OpenCV on images to try and detect the puzzle's edges.
 
 * 5: We will implement perspective transform on the puzzle we extracted to change it into a 2D quadrilateral using OpenCV built-in functions.
 
 * 6 and 7: Extract and recognise the numbers; using blob extraction to distinguish between empty and full boxes. Then we will use different OCR techniques and check which one works best.
 
 * 8: Implement the sudoko solver algorithm on the extracted puzzles and get everything ready for our demo.


A few of the resources that our team have looked at are: 
* http://sudokugrab.blogspot.com/2009/07/how-does-it-all-work.html
* https://en.wikipedia.org/wiki/Thresholding_%28image_processing%29
* https://en.wikipedia.org/wiki/Connected-component_labeling
* https://en.wikipedia.org/wiki/Hough_transform
* http://www.robots.ox.ac.uk/%7Evgg/presentations/bmvc97/criminispaper/
* https://en.wikipedia.org/wiki/Optical_character_recognition
* https://en.wikipedia.org/wiki/Pattern_recognition
* https://en.wikipedia.org/wiki/Artificial_neural_network
