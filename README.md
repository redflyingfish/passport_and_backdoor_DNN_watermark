# passport_and_backdoor_DNN_watermark
## 描述

该项目为本人实践的信息隐藏期末大作业，主要目的为对基于护照和后门的深度神经网络数字水印技术进行学习、理解和实践，并对自己的一些想法进行实践。该项目主要功能为给一个深度神经网络嵌入护照和后门，以实现数字水印机制，并提供了一些攻击模块以评估其性能。

## 如何运行

本项目使用时基于的环境为 `python 3.10` 和`pytorch 1.13.1. 同时, 可以根据 `requirements.txt` 或者Dockerfile` 检查所需的环境配置。

### 训练一个没有水印的普通模型

运行以下指令：

```
python train_v1.py
```

### 训练一个含有护照层和后门的模型

运行以下指令：(其中path/to/pretrained.pth为预训练的模型的存储路径)

```
python train_v23.py --pretrained-path path/to/pretrained.pth
```

## 攻击

本项目设置了三种攻击方式，分别为`passport_attack_1.py`, `passport_attack_2.py`, 和`passport_attack_3.py`，可以根据--help的提示，按照自己的需求运行他们。攻击的结果可以基于test.py得到。
