import os
from pathlib import Path
import cv2
from Facer.facer import facer
import matplotlib.pyplot as plt


path_to_images = "./face_images/boys"
like_imgs = []

for file in Path(path_to_images).glob('*.j*'):
    img = cv2.imread(f'{path_to_images}/{file.name}')
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    # answer = input()
    # if answer in '1yesYES2344':
    like_imgs.append(f'{path_to_images}/{file.name}')

images = facer.load_images(path_to_images, files=like_imgs)
landmarks, faces = facer.detect_face_landmarks(images)
average_face = facer.create_average_face(faces, landmarks, save_image=True)
plt.imshow(average_face)
plt.show()
