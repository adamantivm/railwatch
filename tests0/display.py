import cv

WIN = "win-0"
DATA_DIR = "../runtime"

cv.NamedWindow( WIN)
im_prev = cv.LoadImageM("%s/seq-1.jpg" % DATA_DIR)
im_diff = cv.CreateMat( im_prev.rows, im_prev.cols, im_prev.type)
for i in range(2,300):
    im_cur = cv.LoadImageM("%s/seq-%d.jpg" % (DATA_DIR,i))
    cv.AbsDiff( im_prev, im_cur, im_diff)
    cv.ShowImage( WIN, im_diff)
    cv.WaitKey( 200)
    im_prev = im_cur
