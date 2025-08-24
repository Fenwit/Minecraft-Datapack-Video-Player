# I DID NOT MAKE THIS CODE, I copied it from somewhere but I can't for the life of me find the source because I made this at 4am so if you can find the original website it came from please let me know.

import cv2
import os
import math

# Read the video from specified path
cam = cv2.VideoCapture(input("filename: "))

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')

# frame
currentframe = 0
count = 0
# fps = input("What is the video's fps?: ")
# target = input("What is your target fps?: ")
# scaler = math.ciel(fps/target)

while(True):
    # reading from frame
    ret,frame = cam.read()

    if ret and count % 2 == 0:
        # if video is still left continue creating images
        name = 'data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    elif count % 2 != 0:
        pass
    else:
        break
    count +=1

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
