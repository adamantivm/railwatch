import cv, time

win = "win-0"
im1 = cv.LoadImageM("seq-1.jpg")
im2 = cv.LoadImageM("seq-2.jpg")
diff = cv.CreateMat( im1.rows, im1.cols, im1.type)
cv.AbsDiff( im1, im2, diff)
cv.NamedWindow( win)
cv.ShowImage( win, diff)
cv.WaitKey( 0)
