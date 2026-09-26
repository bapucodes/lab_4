import cv2
import matplotlib.pyplot as plt
import numpy as np

#function to display images

def show_comparison(original,blur3,blur5,blur7):
  plt.figure(figsize=(12,10))

  #original image
  plt.subplot(2,2,1)
  plt.imshow(original,cmap='gray')
  plt.title("Original Grayscale Image")
  plt.axis('off')

  #3*3 kernel
  plt.subplot(2,2,2)
  plt.imshow(blur3,cmap='gray')
  plt.title("Average Filter (3*3)")
  plt.axis('off')

  #5*5 kernel
  plt.subplot(2,2,3)
  plt.imshow(blur5,cmap='gray')
  plt.title("Average Filter (5*5)")
  plt.axis('off')

  #7*7 kernel
  plt.subplot(2,2,4)
  plt.imshow(blur7,cmap='gray')
  plt.title("Average Filter (7*7)")
  plt.axis('off')

  plt.tight_layout()
  plt.show()

#1.read the image in grayscale
#replace 'input_image.jpg' with your filename
img=cv2.imread('moun.png',0)

if img is None:
  print("Error:image not found. Make sure 'anime.jpg' is in the /content/ directory.")
else:
  #2.define averaging kernels of different sizes(3*3,5*5,7*7)

  #A kernel is a matrix of ones normalized by the number of elements
  kernel_3x3=np.ones((3,3),dtype=np.float32)/9
  kernel_5x5=np.ones((5,5),dtype=np.float32)/25
  kernel_7x7=np.ones((7,7),dtype=np.float32)/49

  #3. apply each kernel to the image using 2d convolution
  #cv2.filter2d performs the convolution operation
  blur_3x3=cv2.filter2D(img, -1,kernel_3x3)
  blur_5x5=cv2.filter2D(img, -1,kernel_5x5)
  blur_7x7=cv2.filter2D(img, -1,kernel_7x7)

  #4.display the original and blurred images
  show_comparison(img,blur_3x3,blur_5x5,blur_7x7)