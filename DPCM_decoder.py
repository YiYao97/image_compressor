import numpy as np
from PIL import Image
WIDTH = 64
HEIGHT = 64


def image_decoder(quantized_error):
    image = np.zeros([HEIGHT, WIDTH], dtype=np.float64)
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
            image[j][i] = prediction + quantized_error[j][i]
            img_predicted[j][i] = prediction + quantized_error[j][i]
        # read column j from pixel j+1
        for i in range(j + 1, HEIGHT):
            prediction = img_predicted[i - 1][j]
            image[i][j] = prediction + quantized_error[i][j]
            img_predicted[i][j] = prediction + quantized_error[i][j]
    return image


def main():
    quantized_error = np.loadtxt('quantized_error.txt', delimiter='\t')
    image = image_decoder(quantized_error*256/32)
    image = image.astype(np.uint8)
    result = Image.fromarray(image)
    result.save('lena64_out.bmp')


if __name__ == '__main__':
    main()
