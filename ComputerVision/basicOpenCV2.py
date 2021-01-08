import cv2

img = cv2.imread('src/ppl1.jpg')

while True:
    cv2.imshow('Ppl1', img)

    # if we waited at least 1 ms AND we've press
    # the Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()