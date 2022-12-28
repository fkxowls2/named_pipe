from named_pipe import NamedPipe
import cv2, time

n = NamedPipe()
n.client_build()
while True:
    # n.read_byte(byte_length=248160000)
    n.read_byte()
    # img_arr = n.get_img_arr(info_length=0)
    img_arr = n.get_img_arr()
    print(img_arr.shape)
    # time.sleep(1)