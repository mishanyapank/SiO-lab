from skimage import io
img = io.imread('image.jpg')
import matplotlib.pyplot as plt
plt.imshow(img)
plt.title('My Plot')
plt.show()