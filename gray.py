import cv2
import numpy as np
import matplotlib.pyplot as plt
def process_and_show_image_slices():
  rmin = 100
  rmax = 200

  img = cv2.imread("/content/dead.jpg", 0)
  if img is None:
      print("Error: Could not load image from /content/dead.jpg")
      return

  # Initialize slices based on the original logic's intent
  slice_with_bg = img.copy() # Keeps original image, but pixels in range will be set to 255
  slice_without_bg = np.zeros(img.shape, dtype=np.uint8) # Binary image for pixels in range

  for i in range(img.shape[0]):
    for j in range(img.shape[1]):
      pixel_value = img[i,j]
      if rmin <= pixel_value <= rmax:
        slice_with_bg[i,j] = 255  # Max out pixels within range in this slice
        slice_without_bg[i,j] = 255 # Set to white for binary slice
      else:
        # slice_with_bg[i,j] remains its original value from img.copy()
        slice_without_bg[i,j] = 0 # Set to black for binary slice

  # Display the results
  plt.figure(figsize=(15, 5))

  plt.subplot(1, 3, 1)
  plt.imshow(img, cmap='gray')
  plt.title('Original Image')
  plt.axis('off')

  plt.subplot(1, 3, 2)
  plt.imshow(slice_with_bg, cmap='gray')
  plt.title(f'Slice with Background (range [{rmin},{rmax}] pixels maxed)')
  plt.axis('off')

  plt.subplot(1, 3, 3)
  plt.imshow(slice_without_bg, cmap='gray')
  plt.title(f'Slice Without Background (range [{rmin},{rmax}] only)')
  plt.axis('off')

  plt.tight_layout()
  plt.show()

# Call the function without arguments, as it handles image loading internally
process_and_show_image_slices()
