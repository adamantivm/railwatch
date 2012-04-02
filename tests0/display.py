import cv

WIN = "win-0"
WIN_X = "win-x"
WIN_Y = "win-y"
DATA_DIR = "../runtime"

cv.NamedWindow( WIN)
im_prev = cv.LoadImageM("%s/seq-1.jpg" % DATA_DIR)

velx = cv.CreateMat( im_prev.rows, im_prev.cols, cv.CV_32FC1)
vely = cv.CreateMat( im_prev.rows, im_prev.cols, cv.CV_32FC1)

im_prev_8 = cv.CreateMat( im_prev.rows, im_prev.cols, cv.CV_8UC1)
im_curr_8 = cv.CreateMat( im_prev.rows, im_prev.cols, cv.CV_8UC1)

for i in range(2,300):
    im_curr = cv.LoadImageM("%s/seq-%d.jpg" % (DATA_DIR,i))

    cv.CvtColor( im_prev, im_prev_8, cv.CV_BGR2GRAY)
    cv.CvtColor( im_curr, im_curr_8, cv.CV_BGR2GRAY)
    cv.CalcOpticalFlowHS( im_prev_8, im_curr_8, 0, velx, vely, 0.0001, (cv.CV_TERMCRIT_ITER, 10, 0))

    cv.ShowImage( WIN_X, velx)
    cv.ShowImage( WIN_Y, vely)
    cv.ShowImage( WIN, im_curr_8)
    cv.WaitKey( 200)
    im_prev = im_curr
