from imread import imread

image = imread('simple-dataset/building05.jpg')

from matplotlib import pyplot as plt

plt.imshow(image)
plt.show()
