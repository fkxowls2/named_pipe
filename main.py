from named_pipe import NamedPipe
import cv2
import matplotlib.pyplot as plt
import numpy as np

n = NamedPipe()
idx = 1
while True:
    n.read_byte()
    img_arr = n.get_img_arr()
    cv2.imwrite(f'{str(idx)}.bmp', img_arr)
    idx += 1