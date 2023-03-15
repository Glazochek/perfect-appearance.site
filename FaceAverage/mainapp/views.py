import random
from pathlib import Path

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
import os
from pathlib import Path
import cv2
import matplotlib.pyplot as plt
from django.template.loader import render_to_string
from perfect_appearance.Facer.facer import facer

like_list = ['']


def delete(request):
    like_list[0] = ''
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def main(request):
    delete(request)
    return render(request, 'mainapp/index.html')


def face_average(request, gender, id):
    path = f'D:/Documents/programming/Neuronet Python/FaceAverage/FaceAverage/static/face_images/{gender}/'
    folders = [str(img) for img in Path(path).glob('*/')]
    img_list = []
    for f in folders:
        files = sorted([str(j) for j in Path(f).glob('*.J*')], key=lambda x: x.split('\\')[-2])
        if files:
            img_list.append(str(files[0]))
    if id >= len(img_list): id = 0

    context = {
        'img': img_list[id].split('\\')[-2]+'/'+img_list[id].split('\\')[-1],
        'name': img_list[id].split('\\')[-2],
        'gender': gender,
        'id': str(id),
        'next': id+1,
        'befor': id-1,
        'like_list': like_list,
        'like_list_int': [i for i in like_list[0].split('$') if i.isalnum()],
        'n': len(list(set(like_list[0].split('$')[1:]))),
        'last': id == len(img_list)-1,
        'first': id == 0,
        'ln':len(img_list)-1,
    }
    return render(request, 'mainapp/pictures.html', context)


def face_average_gender(request, gender):
    context = {
        'gender': gender,
        'id': 0,
        'img': '0',
        'n': len(list(set(like_list[0].split('$')[1:]))),
        'like_list_int': [i for i in like_list[0].split('$') if i.isalnum()],
        'like_list': like_list[0],
    }
    return render(request, 'mainapp/pictures.html', context)


def like(request, gender, id):
    if str(id) not in like_list[0]:
        like_list[0] += '$' + str(id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def create_img_face(request, gender, ids):
    size = '1000&1500'
    rn = random.randint(0, 1000000)
    img = f'D:/Documents/programming/Neuronet Python/FaceAverage/FaceAverage/static/average_face/face_average_{rn}.jpeg'
    likes = list(set(ids[2:-2].split('$')[1:]))
    path = f'D:/Documents/programming/Neuronet Python/FaceAverage/FaceAverage/static/face_images/{gender}/'
    img_list = sorted([str(img) for img in Path(path).glob('*/*.*')])
    folders_list = [str(img) for img in Path(path).glob('*/')]
    imgs_like_list = []
    peoples = []
    for id in likes:
        peoples.append(folders_list[int(id)].split('\\')[-1])
    for p in set(peoples):
        for b in img_list:
            if p in b:
                imgs_like_list.append(b.replace('\\', '/'))
    path_to_images = 'perfect_appearance/face_images'
    images = facer.load_images(path_to_images, files=imgs_like_list)
    landmarks, faces = facer.detect_face_landmarks(images)
    facer.create_average_face(faces, landmarks, save_image=True, output_file=img, output_dims=map(int, size.split('&')))
    like_list[0] = ''
    context = {'name_img': f'average_face/face_average_{rn}.jpeg',
               'peoples': list(set(peoples)),
               'last': list(set(peoples))[-1]
               }
    return context


def create_img(request, gender, ids):
    return render(request, 'mainapp/create_img.html', create_img_face(request, gender, ids))


