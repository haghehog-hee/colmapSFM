import cv2
import os
from tqdm import tqdm
import numpy as np


from panorama import panorama_to_plane

frame_width = 500
frame_height = 500
image_path = "images\\"
save_path = "images2\\"
check = True




for deg in tqdm(np.arange(0, 360, 20)):
    beta = 0.8
    alpha = 0.01
    paths = os.listdir(image_path)
    if check:
        check = False
        for i in range(0, len(paths)-1, 10):
            print(deg)
            print(check)
            print(i)

            path_ = paths[i]
            path = image_path + path_
            savepath = save_path + path_
            image = cv2.imread(path)
            savepath = path_.removesuffix('.jpg')
            x, y, z = image.shape
            newX = y // 2
            newY = x // 2
            down_points = (y // 2, x // 2)
            image = cv2.resize(image, dsize=down_points)
            output_image = panorama_to_plane(path, 90, (frame_width, frame_height), deg, 90)
            pix = np.array(output_image)
            pix = cv2.convertScaleAbs(pix, alpha, beta)
            cv2.imwrite(save_path + format(deg, '03d') + format(i, '03d')  + savepath  + '.jpg', pix)
    else:

        check = True
        for i in range(len(paths)-1, 0, -10):
            print(deg)
            print(check)
            print("i= " + str(len(paths)-i))

            path_ = paths[i]
            path = image_path + path_
            savepath = save_path + path_
            image = cv2.imread(path)
            image = cv2.convertScaleAbs(image, alpha, beta)
            savepath = path_.removesuffix('.jpg')
            x, y, z = image.shape
            newX = y // 2
            newY = x // 2
            down_points = (y // 2, x // 2)
            image = cv2.resize(image, dsize=down_points)
            output_image = panorama_to_plane(path, 90, (frame_width, frame_height), deg, 90)
            pix = np.array(output_image)
            pix = cv2.convertScaleAbs(pix, alpha, beta)

            cv2.imwrite(save_path + format(deg, '03d') + format(len(paths)-i, '03d')   + savepath +  '.jpg', pix)
