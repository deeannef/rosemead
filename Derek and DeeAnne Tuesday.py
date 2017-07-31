#    Derek and DeeAnne.

import matplotlib.pyplot as plt
import os.path
import numpy as np  # "as" lets us use standard abbreviations
   
#    Read the image data'''
#    Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 

#    Build an absolute filename from directory + filename
filename = os.path.join(directory, 'batman.jpg')
#    Read the image data into an array
img = plt.imread(filename)
img1 = plt.imread(filename)
  
#   Create and assign two variables "fig" and "ax"
#    Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)
#    Show the image data in a subplot. There is only 1 at the moment

height = len(img)    #  This sets the bounds of the portion to be manupilated
width = len(img[0])  #  This uses a list of array
for r in range(168):    #   For loop named "r" in range 168, the whole width
    for c in range(width):  #   For loop named "c" for range all height
        if sum(img[r][c])>200 and sum(img[r][c])<350: #    change middle color to below 
            img[r][c]=[4,30,66]                     # Cal Bear offical blue
        if sum(img[r][c])<25:                       # change black to below
            img[r][c]=[255, 199, 44]                # Cal Bear offical yellow
        rgb = img[r][c]                             # variable equal to image
        if rgb[0] < 15 or rgb[1] < 15 or rgb[2] <15: # filter to make low colors blacker
            rgb = [0, 0, 0]                         # color black
            

ax[1].imshow(img, interpolation='none')
ax[0].imshow(img1, interpolation='none')
# Show the figure on the screen
fig.show()