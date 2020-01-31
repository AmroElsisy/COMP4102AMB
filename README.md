# COMP4102 AMB
Title: Sudoko Solver Proposal

Group Name: AMB

Group Members: 

Amro Elsisy - 100917564

Menna Mohsen - 101007934

Bill Creber - 100884250


Our team will be working on the sudoko solver project. We are planning to work with the sudoko solver algorithm and implement it on pictures captured from sudoko puzzles printed on paper. 

A few of the resources that our team have looked at are: 
* http://sudokugrab.blogspot.com/2009/07/how-does-it-all-work.html
* https://en.wikipedia.org/wiki/Thresholding_%28image_processing%29
* https://en.wikipedia.org/wiki/Connected-component_labeling
* https://en.wikipedia.org/wiki/Hough_transform

## The Challenge:
We shall be taking either a real-time snapshot via a phone camera or a scanned image of a potential sudoku puzzle page.
OpenCV has edge detection that we could use to find the game board, though we would have to determine the location of the discrete input boxes from the edges as well as the different line thickness for the unique groups. This is doubly important for variants where the 1-N character groups are not always a uniform box (ie. Jigsaw).

We will have to interface with an OCR (Optical Character Recognition) engine like [Tesseract](https://opensource.google/projects/tesseract) to determine which unique character is where on the game grid (for both answers and clues) to then be passed to the solving algorithm(s).

## Goals and Deliverables: 
Our main goal is start with the default 9x9 puzzle and that is going to be our main focus when implementing the project. If we have time we will aim to solve the more elaborate variants of the much loved game like [Overlapping Grids](https://en.wikipedia.org/wiki/Glossary_of_Sudoku#Sudoku_variants), [Killer Sudoku](https://en.wikipedia.org/wiki/Killer_sudoku), or [Jigsaw](https://en.wikipedia.org/wiki/Nonomino).


# Default README Below
Background: If your ideas coming from existing research you should refer to the publications and describe what you are doing differently.

Notes: If your project involves taking advantage of computational speedups available on your iOS device - such as box filters, inverse composition in the LK algorithm, NEON intrinsics, OpenGL ES, Accelerate Framework, binary descriptors such as FAST and BRIEF, etc. - describe their application and why they are necessary in more detail. If your project involves something around using your device in a mobile fashion - for example virtually rendering an object in your room - then describe what components of your solution are unique to a mobile device (the high-speed camera, GPS, IMU, Gyro?).
1

The Challenge: Describe in a few sentences why the problem is challeng- ing. Could you solve your problem using just a few pre-existing functions in OpenCV? Try to state explicitly what you are hoping to learn by doing this project? A flow chart or visual depiction of what you are trying to do would be good here.

Goals and Deliverables: Describe the deliverables or goals of your project.
• In a couple of sentences separate your goals into what you PLAN TO ACHIEVE (what you believe you must get done to have a successful project and get the grade you expect) and an extra goal or two that you HOPE TO ACHIEVE if the project goes really well and you get ahead of schedule.

• Describe what success looks like and how it can be evaluated. For example, if your project is to measure the velocity of a baseball being thrown in front of an iOS device, how will you validate that it works? Screen shots of the App in action? A speed benchmark run across a variety of videos? A live video of the app in action? It will NOT be enough to simply provide the Xcode project - you will need to provide evidence that you have achieved your goal.

• How realistic is it for your team to get what it needs to get done within the allotted time? Remember you only have a few weeks to get this project completed.

Schedule: Produce a schedule for your project. Your schedule should have at least one item to do per week per participant. List what your plan to get done each week from February 1st until the 10th of April deadline. You would present your projects in the class in the last week of the semester. You should have some results by March 31.
