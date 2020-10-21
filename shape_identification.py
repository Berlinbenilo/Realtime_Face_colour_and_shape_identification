import cv2
from tkinter.filedialog import askopenfilename

filename = askopenfilename(filetypes=[("all files","*.*")])
input_image = cv2.imread(filename)
img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)

_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)

_, contours, _ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
font = cv2.FONT_HERSHEY_COMPLEX

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    cv2.drawContours(img,[approx],0,(0),5)

    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 3:
        cv2.putText(input_image,"Triangle",(x,y),font,1,(0))
    elif len(approx) == 4:

        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        # print(ar)
        if ar >= 0.95 and ar <= 1.05:
            cv2.putText(input_image,"square",(x,y),font,1,(0))
        else:
            cv2.putText(input_image, "Rectangle", (x, y), font, 1, (0))

    elif len(approx) == 5:
        cv2.putText(input_image,"Pentagon",(x,y),font,1,(0))
    elif 6 < len(approx) < 15:
        cv2.putText(input_image,"Elipse",(x,y),font,1,(0))
    elif len(approx) > 15:
        cv2.putText(input_image,"Circle",(x,y),font,1,(0))
cv2.imshow("shapes", img)
cv2.imshow("threshold",threshold)
cv2.imshow("Orginal image",input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()