# 环境部署

## 要求
- 操作系统：Ubuntu 16.04
- CUDA 版本： 9.0.176
- Nvidia Drive： 396.18
- CUDNN版本： 7.0.5
- pytorch： 1.0 nightly
- python：3.7.2
- miniconda： 4.6.8
- GCC >= 4.9

## 安装步骤
1. 创建并进入python虚拟环境
	- `conda create -n tc_jinnan python=3.7` 
	- `conda activate tc_jinnan`
2. 安装必要的依赖包
	- `pip install ninja yacs cython matplotlib tqdm`
	- `pip install opencv-python`
3. 安装PyTorch
	- `conda install -c pytorch pytorch-nightly torchvision cudatoolkit=9.0`
4. 下载本工程项目代码
	- 假设本工程路径为： `$JINNAN_ROOT`
	- `cd $JINNAN_ROOT/code`
5. 安装cocoapi和maskrcnn-benchmark库
	- `export INSTALL_DIR=$PWD`
	- `cd $INSTALL_DIR`
	- `cd cocoapi/PythonAPI`
	- `python setup.py build_ext install`
	- `cd $INSTALL_DIR/maskrcnn-benchmark`
	- `rm -rf build`（清除缓存）
	- `python setup.py build develop`
	- `unset INSTALL_DIR`

## 数据准备
1. 将下载的津南数据集解压并存入`$JINNAN_ROOT/data`目录下
2. 整套代码目录结构如下：
		classify/
		code/
		data/
				jinnan2_round1_train_20190305/
				jinnan2_round1_test_a_20190306/
				jinnan2_round1_test_b_20190326/
		submit/
		README.md
		README_restricted_classify.md
		README_restricted_detection.md

## 准备预训练权重
1. [点此链接下载X-101-32x8d-FPN预训练权重文件](https://dl.fbaipublicfiles.com/detectron/36761843/12_2017_baselines/e2e_mask_rcnn_X-101-32x8d-FPN_1x.yaml.06_35_59.RZotkLKI/output/train/coco_2014_train%3Acoco_2014_valminusminival/generalized_rcnn/model_final.pkl "X-101-32x8d_FPN")
2. 将下载的权重模型文件存入 `$JINNAN_ROOT/code/models/`目录下
3. 重命名文件：
	`cd $JINNAN_ROOT/code`
	`mv ./models/model_final.pkl  ./models/X-101-32x8d_FPN.pkl`
4. 移除模型权重的最后一层：
	`cd $JINNAN_ROOT/code`
	`python trim_detectron_model.py`

## 数据集预处理
1. 拆分训练数据集
	- `python split_datasets.py`

## 训练
 `cd $JINNAN_ROOT/code`
1. 单GPU训练：
	- `python train_net_1x.py`
	注：默认使用第0块GPU进行训练，可以在train_net_2x.py中第29行自行指定使用其他GPU
2. 两块GPU训练
	`export NGPUS=2`
	`python -m torch.distributed.launch --nproc_per_node=$NGPUS train_net_2x.py`
	注：默认使用第0,1两块GPU进行训练，可以在train_net_2x.py中第29行自行指定使用其他GPU

## 成绩提交
 `cd $JINNAN_ROOT/code`
1. 提交测试a数据集成绩：
	`python submit_a.py`
2. 提交测试b数据集成绩：
	`python submit_b.py`

## 下载本人训练完成的权重文件
1. [百度网盘下载(model_0030000.pth)](https://pan.baidu.com/s/1O-Xw7EnuMmHuBJWmNaRA6A "model_0030000.pth")
提取码： 9ka8
2. 将下载的权重文件存入$JINNAN_ROOT/code/models/目录下