import cv2
from numpy import *

WIN = "win-0"
WIN_X = "win-x"
WIN_Y = "win-y"
DATA_DIR = "../runtime"
MASK_COORDINATES = (0, 168, 368, 258)  # Apparently it's x0, y0, width, height

im_prev = cv2.imread("%s/seq-1.jpg" % DATA_DIR)
im_prev = cv2.cvtColor( im_prev,cv2.COLOR_RGB2GRAY)
im_prev = cv2.GaussianBlur( im_prev, (0,0), 2)

#for i in range(2,300):
for i in range(90,120):
    im_curr = cv2.imread("%s/seq-%d.jpg" % (DATA_DIR,i))
    im_curr = cv2.cvtColor( im_curr, cv2.COLOR_RGB2GRAY)
    im_curr = cv2.GaussianBlur( im_curr, (0,0), 2)  

    # Calculate difference vector
    im_diff = cv2.absdiff( im_prev, im_curr)
    #im_diff = im_prev - im_curr
    
    # Display calculated diff
    cv2.imshow( WIN, im_diff)
   
    cv2.waitKey( 200)
    im_prev = im_curr
