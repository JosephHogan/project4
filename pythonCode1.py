#Set up a docker environment for this code, and don't try to include superfluous packages!
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import random

blackblankimage = random.randint(0, 255) * np.ones(shape=[512, 512, 3], dtype=np.uint8)

cv.putText(blackblankimage, "You did it!", (100, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255))
cv.rectangle(blackblankimage, pt1=(200,200), pt2=(300, 300), color=(0,0,255), thickness=-1)
plt.axis('off')
plt.imshow(blackblankimage)

plt.savefig("./pythonCode1Image.png")

#modify this code so that it also generates self signed certificate and keys
