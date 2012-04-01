import cv, time

win = "win-0"
cv.NamedWindow( win)
im_prev = cv.LoadImageM("seq-1.jpg")
im_diff = cv.CreateMat( im_prev.rows, im_prev.cols, im_prev.type)
for i in range(2,300):
    im_cur = cv.LoadImageM("seq-%d.jpg" % i)
    cv.AbsDiff( im_prev, im_cur, im_diff)
    cv.ShowImage( win, im_diff)
    cv.WaitKey( 200)
    im_prev = im_cur
