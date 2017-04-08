import numpy as np
import cv2
import os
import re
from shutil import copyfile


def resize_with_longer_side(img, sidewidth):
    height, width = img.shape[:2]
    ratio = sidewidth * 1.0 / np.maximum(height, width)
    height_new = int(ratio * height)
    width_new = int(ratio * width)
    img_resized = cv2.resize(img, (width_new, height_new))
    return img_resized

roots = ['examples/segmentation', 'examples/input', 'examples/style']
for root in roots:
    for fname in os.listdir(root):
        if 'jpg' in fname or 'png' in fname:
            print("Processing {}".format(fname))
            full_file = os.path.join(root, fname)
            img = cv2.imread(full_file)
            img_resize = resize_with_longer_side(img, 700)
            cv2.imwrite(full_file,  img_resize)
