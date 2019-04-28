# 安装说明
	本项目采用的是分类+检测的方法：先使用二分类网络对训练集中的normal和restrict图片进行训练，将normal视为负类，restrict视为正类，使用数据扩充增加了restrict样本，使得正负样本数量基本一致；训练完成后先对测试集进行预测，将测试集分为包含和未包含限制品的两类图片进行label，最后检测过程基于分类结果，只对包含限制品的图片进行检测，标注出限制品的具体位置坐标信息。

## 分类（可选）
1. 安装部署过程请参考[README_restricted_classify.md](https://github.com/zzzkk2009/tianchi-jinnan2-2019/blob/master/round1/README_restricted_classify.md)文档。

## 检测
1. 安装部署过程请参考[README_restricted_detection.md](https://github.com/zzzkk2009/tianchi-jinnan2-2019/blob/master/round1/README_restricted_detection.md)文档。

## 注
1. 分类结果文件已生成并保存在code目录下，可以直接用于检测任务
