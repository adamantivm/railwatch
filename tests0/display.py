import cv, time

win = "win-0"
im = cv.LoadImageM("seq-1.jpg")
print im
cv.NamedWindow( win)
cv.ShowImage( win, im)
cv.WaitKey( 0)
