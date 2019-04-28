# 环境安装
## 要求
- 操作系统：Ubuntu 16.04
- CUDA 版本： 9.0.176
- Nvidia Drive： 396.18
- CUDNN版本： 7.0.5
- python：3.7.2
- miniconda： 4.6.8
- GCC >= 4.9
- jupyter notebook

## 安装步骤
1. 创建并进入python虚拟环境
	- `conda create -n fastai_jinnan python=3.7`
	- `conda activate fastai_jinnan`
2. 安装必要的依赖包
	- `conda install -c pytorch pytorch-nightly cuda90`
	- `conda install -c fastai torchvision-nightly`
	- `conda install -c fastai fastai`
	- `pip install opencv-python`
3. 下载本工程项目代码
	- 假设本工程路径为： `$JINNAN_ROOT`
	- `cd $JINNAN_ROOT/classify`

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

## 启动juypter notebook环境

## 数据集预处理
1. 准备训练数据集
	- `打开并运行 $JINNAN_ROOT/classify/process_data_tianchi_annotations.ipynb文件`

## 训练
	- `打开并运行 $JINNAN_ROOT/classify/train_tianchi.ipynb文件`

## 预测
1. 分类测试a数据集：
	`打开并运行 $JINNAN_ROOT/classify/predict_tianchi_test_a.ipynb文件`
2. 分类测试b数据集：
	`打开并运行 $JINNAN_ROOT/classify/predict_tianchi_test_b.ipynb文件`
3. 将当前目录下生成的288tianchi_result_testa.txt和288tianchi_result100_testb.txt拷贝到$JINNAN_ROOT/code目录下

## 下载本人训练完成的权重文件
1.  [百度网盘下载(228_best_100.pkl)](https://pan.baidu.com/s/1GzgpGvVOJYSU9xwoHA_0qA "228_best_100.pkl")
提取码： 5kao
2. 将下载的权重文件拷贝到$JINNAN_ROOT/classify目录下