import cv, numpy

WIN = "win-0"
WIN_X = "win-x"
WIN_Y = "win-y"
DATA_DIR = "../runtime"
MASK_COORDINATES = (0, 168, 368, 258)  # Apparently it's x0, y0, width, height

cv.NamedWindow( WIN)
im_prev = cv.LoadImageM("%s/seq-1.jpg" % DATA_DIR)
im_prev = cv.GetSubRect( im_prev, MASK_COORDINATES)

velx = cv.CreateMat( im_prev.rows, im_prev.cols, cv.CV_32FC1)
vely = cv.CreateMat( im_prev.rows, im_prev.cols, cv.CV_32FC1)

im_prev_8 = cv.CreateMat( im_prev.rows, im_prev.cols, cv.CV_8UC1)
im_curr_8 = cv.CreateMat( im_prev.rows, im_prev.cols, cv.CV_8UC1)

#for i in range(2,300):
for i in range(90,120):
    im_curr = cv.LoadImageM("%s/seq-%d.jpg" % (DATA_DIR,i))
    im_curr = cv.GetSubRect( im_curr, MASK_COORDINATES)

    # Calculate optical flow. Produces and X and Y matrices of velocities
    cv.CvtColor( im_prev, im_prev_8, cv.CV_BGR2GRAY)
    cv.CvtColor( im_curr, im_curr_8, cv.CV_BGR2GRAY)
    cv.CalcOpticalFlowHS( im_prev_8, im_curr_8, 0, velx, vely, 0.0001, (cv.CV_TERMCRIT_ITER, 10, 0))
    
    # Calculate average velocity vector
    mean_x = cv.Avg( velx)[0]
    mean_y = cv.Avg( vely)[0]
    mean_p = numpy.sqrt(numpy.square(mean_x)+numpy.square(mean_y))
    mean_r = numpy.degrees( numpy.arctan2( mean_x, mean_y))
    print "%i: X,Y | (p,r) = %.2f,%.2f (%.2f,%d)" % (i, mean_x, mean_y, mean_p, mean_r)

    #cv.ShowImage( WIN_X, velx)
    #cv.ShowImage( WIN_Y, vely)
    cv.ShowImage( WIN, im_curr_8)
    cv.WaitKey( 100)
    im_prev = im_curr
