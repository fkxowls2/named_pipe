from named_pipe import NamedPipe
import cv2, time

n = NamedPipe()
n.server_build()
img = cv2.imread('img.bmp', cv2.IMREAD_GRAYSCALE)
img_byte = img.tobytes()
while True:
    n.write_byte(img_byte)
    time.sleep(1)