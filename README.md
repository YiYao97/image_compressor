# DPCM压缩
## 工程介绍
DPCM压缩是基于python的图片压缩程序, 可以将一张64 * 64的灰度图片进行DPCM（差分预测编码调制）编码，再对编码进行重建
## 使用说明
### 环境要求
1. Windows
2. 确保DPCM_encoder.exe, DPCM_decoder.exe, lena64.bmp在同一文件夹下
### 运行步骤
1. 运行DPCM_encoder.exe, 生成quantized_error.txt和lena64_error.bmp两个文件
2. 运行DPCM_decoder.exe, 生成lena64_out.bmp文件
## 算法描述
### 图像编码
DPCM_encoder.py为图像编码程序，该程序读取lena64.bmp灰度图存入像素范围[0, 255]的二维矩阵。将
### 图像解码
DPCM_decoder.py为图像解码程序，该程序读取quantized_error.txt中的
## 算法评估
DPCM
