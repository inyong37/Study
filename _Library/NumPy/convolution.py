# 2021-12-10-Fri.
# Inyong Hwang
# Reference: https://medium.com/analytics-vidhya/2d-convolution-using-python-numpy-43442ff5f381

import numpy as np


# 2D Convolution 
def conv2D(image, kernel, padding=0, strides=1):
  # apply cross correlation to kernel and this can be done using NumPy very easily through just flipping the matrix horizontally then vertically.
  kernel = np.flipud(np.fliplr(kernel))
  
  # output_features = ((input_features + 2 * padding_size - kernel_size) / stride_size) + 1
  # this must be implemented in each dimension (x, y).
  x_kernel_shape = kernel.shape[0]
  y_kernel_shape = kernel.shape[1]
  x_image_shape = image.shape[0]
  y_image_shape = image.shape[1]
  x_output = int(((x_image_shape - x_kernel_shape + 2 * padding) / strides) + 1)
  y_output = int(((y_image_shape - y_kernel_shape + 2 * padding) / strides) + 1)
  
  # create a fresh matrix with the deduced dimenstions.
  output = np.zeros((x_output, y_output))

  if padding != 0:
    # create a fresh array of zeros with the padded dimensions.
    # multiply the padding by 2 because we are applying even padding on all sides so a padding of 1 would increase the dimension of the padded image by 2.
    image_padded = np.zeros((image.shape[0] + padding * 2, image.shape[1] + padding * 2))
    # replace the inner portiong of the padded iamge with the actual image.
    image_padded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image
  else:
    # if there is no padding, make the padded image equal to the image.
    image_padded = image
  
  # iterate through the image and apply element wise multiplication and then sum it and set it equal to the respective element in the output array.
  for y in range(image.shape[1]):
    # check if we are at the end of the image in the y direction.
    # It will exit the complete convolution once we to reach the very bottom right of the image matrix
    if y > image.shape[1] - y_kernel_shape:
      break
    if y % strides == 0:
      for x in range(image.shape[0]):
        if x > image.shape[0] - x_kernel_shape:
          break
        # main convolution operator that applies a convolution, sums the elements, and appends it to the output matrix.
        try:
          if x % strides == 0:
            output[x, y] = (kernel * image_padded[x:x + x_kernel_shape, y:y + y_kernel_shape]).sum()
        except:
          break
  return output
  
