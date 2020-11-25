import numpy as np
from PIL import Image
# 定义图片格式
WIDTH = 64
HEIGHT = 64


def image_encoder(image):
    error_quantized = np.zeros([HEIGHT, WIDTH], dtype=np.float64)
    img_predicted = np.zeros([HEIGHT, WIDTH], dtype=np.float64)
    for j in range(WIDTH):
        # read row j from pixel j
        for i in range(j, WIDTH):
            if j == 0:  # for row 0
                if i == 0:  # for pixel 0 in row 0
                    prediction = 0
                else:  # for the remaining pixel i in row 1
                    prediction = img_predicted[0][i - 1]
            else:  # left +
                prediction = img_predicted[j][i - 1]
            error = image[j][i] - prediction
            error_quantized[j][i] = quantize(error)
            img_predicted[j][i] = prediction + error_quantized[j][i]
        # read column j from pixel j+1
        for i in range(j + 1, HEIGHT):
            prediction = img_predicted[i - 1][j]
            error = image[i][j] - prediction
            error_quantized[i][j] = quantize(error)
            img_predicted[i][j] = prediction + error_quantized[i][j]
    return error_quantized*32/256


def quantize(error):
    range_max = 256
    range_min = -256
    q = (range_max-range_min)/32
    i = 1
    while error >= range_min + q*i:
        i = i + 1
    return range_min + q*(i-1) + q/2


def main():
    image = np.array(Image.open("lena64.bmp"))
    error_quantized = image_encoder(image)
    np.savetxt('quantized_error.txt', error_quantized, fmt="%d", delimiter='\t')


if __name__ == '__main__':
    main()
