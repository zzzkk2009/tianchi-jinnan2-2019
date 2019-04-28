# -*- coding: utf-8 -*-

import json
import random
import os

datasets_path = '../data/jinnan2_round1_train_20190305/'

f = open('{}train_no_poly.json'.format(datasets_path) ,encoding='utf-8')
gt = json.load(f)

print(gt['info'])
print(gt['licenses'])

print('categories:{}'.format(len(gt['categories'])))
print('images:{}'.format(len(gt['images'])))
print('annotations:{}'.format(len(gt['annotations'])))


train = dict()

train['info'] = gt['info']
train['licenses'] = gt['licenses']
train['categories'] = gt['categories']
train['images'] = []
train['annotations'] = []


val = dict()

val['info'] = gt['info']
val['licenses'] = gt['licenses']
val['categories'] = gt['categories']
val['images'] = []
val['annotations'] = []

train_image_size = int(len(gt['images']) * 0.9)

print('train_img_num:{}'.format(train_image_size))
print('val_img_num:{}'.format(len(gt['images']) - train_image_size))


random.shuffle(gt['images'])

for img_info in gt['images']:

    if len(train['images']) < train_image_size:

        train['images'].append(img_info)


        for anno in gt['annotations']:
            if anno['image_id'] == img_info['id']:
                train['annotations'].append(anno)

    else:
        val['images'].append(img_info)

        for anno in gt['annotations']:
            if anno['image_id'] == img_info['id']:
                val['annotations'].append(anno)
                
                
                
def save_train_val_datesets():
    with open("{}jinnan_round1_train.json".format(datasets_path), 'w', encoding='utf-8') as json_file:
        json.dump(train, json_file, ensure_ascii=False)

    with open("{}jinnan_round1_val.json".format(datasets_path), 'w', encoding='utf-8') as json_file:
        json.dump(val, json_file, ensure_ascii=False)
    print('process success!')
    