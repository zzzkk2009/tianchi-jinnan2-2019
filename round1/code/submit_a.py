# -*- coding: utf-8 -*-

import os
import time


# from PIL import Image
import torch
import json
import cv2
import tqdm
import os
from maskrcnn_benchmark.config import cfg
from predictor import COCODemo

def mkdir_if_not_exist(path):
    if not os.path.exists(os.path.join(*path)):
        os.makedirs(os.path.join(*path))

os.environ["CUDA_VISIBLE_DEVICES"] = "1"
date = time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) 
load_epoch = '0030000'

config_file = './configs/e2e_mask_rcnn_X_101_32x8d_FPN_1x_caffe2.yaml'
test_path = '../data/jinnan2_round1_test_a_20190306'

filename = os.listdir(test_path)
print('test file len:{}'.format(len(filename)))

# update the config options with the config file
cfg.merge_from_file(config_file)
print('cfg.MODEL.WEIGHT={}'.format(cfg.MODEL.WEIGHT))
# manual override some options
cfg.merge_from_list(["MODEL.DEVICE", "cuda"])

confidence_threshold = 0.7

coco_demo = COCODemo(
    cfg,
    min_image_size=800,
    confidence_threshold=confidence_threshold,
)

results = []

img2label = {}
p_num = 0
n_num = 0
with open('288tianchi_result_testa.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip() # 去掉每行头尾空白
        items = line.split() # 按空白符分割
        label = int(items[1])
        img2label[items[0]] = label
        if label != 0:
            p_num += 1
        else:
            n_num += 1

print('test positive img num: {}'.format(p_num))
print('test negative img num: {}'.format(n_num))

print(img2label)
print('img2label len={}'.format(img2label.keys()))
        
save_pred_img = False
save_pred_img_dir = '../submit/model_{}_{}_{}'.format(load_epoch, date, confidence_threshold)
for file in tqdm.tqdm(filename) :
    label = img2label[file]
    print(file + '=' + str(label))
    img_path = os.path.join(test_path,file)
    img = cv2.imread(img_path)
    
    if label != 0:
        rects, result_img = coco_demo.predict(img, save_pred_img)
    else:
        rects = []
        result_img = img
    
    if save_pred_img:
        mkdir_if_not_exist(save_pred_img_dir.split('/'))
        cv2.imwrite(save_pred_img_dir + '/' + file, result_img)

    result = dict()
    result['filename'] = file
    result['rects'] = []
    result['rects'].extend(rects)

    results.append(result)
    print(rects)
    print('results.len={}'.format(len(results)))

a = dict()
a['results'] = results


with open("../submit/submit_{}_{}_{}.json".format(load_epoch, date, confidence_threshold), 'w', encoding='utf-8') as json_file:
    json.dump(a, json_file, ensure_ascii=False)

print('process success!')
