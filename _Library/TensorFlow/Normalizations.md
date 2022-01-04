# Normalization | [TensorFlow](https://www.tensorflow.org/addons/tutorials/layers_normalizations)
- Group Normalization (TensorFlow Addons)
- Instance Normalization (TensorFlow Addons)
- Layer Normalization (TensorFlow Core)

The basic idea behind these layers is to normalize the output of an activation layer to improve the convergence during training. In contrast to batch normalization these normalizations do not work on batches, instead they normalize the activations of a single sample, making them suitable for recurrent neural networks as well.

Typically the normalization is performed by calculating the mean and the standard deviation of a subgroup in your input tensor. It is also possible to apply a scale and an offset factor to this as well.

y[i] = gamma * (x[i] - mu) / sigma + beta

y: Output

x: Input

gamma: Scale factor

mu: mean

sigma: standard deviation

beta: Offset factor

The following image demonstrates the difference between these techniques. Each subplot shows an input tensor, with N as the batch axis, C as the channel axis, and (H, W) as the spatial axes (Heigth and Width of a picture for example). The pixels in blue are normalized by the same mean and variance, computed by aggregating the values of these pixels.

<img width="1069" alt="norm" src="https://user-images.githubusercontent.com/20737479/141724968-9279ebef-0e81-49a3-9386-33cb5aeaf870.png">

The weights gamma and beta are trainable in all normalization layers to compensate for the possible lost of representational ability. You can activate these factors by setting the center or the flag to Ture. Of course you can use initializers, constraints and regularizer for beta and gamma to tune these values during the training process.

## Group Normalization Tutorial
### Introduction
Groupd Normalization(GN) divides the channels of your inputs into smaller sub groups and normalizes these values based on their mean and variance. Since GN works on a single example this technique is batchsize independent.

GN experimentally scored closed to batch normalization in image classification tasks. It can be beneficial to use GN instead of Batch Normalization in case your overall batch_size is low, which would lead to bad performace of batch normalization

### Example
Splitting 10 channels after a Conv2D layer into 5 subgroups in a standard "channels last" setting:
```Python
model = tf.keras.models.Sequential([
  # Reshape into "channels last" setup.
  tf.keras.layers.Reshape((28, 28, 1), input_shape=(28, 28)),
  tf.keras.layers.Conv2D(filters=10, kernel_size(3, 3), data_format="channels_last"),
  # Groupnorm Layer
  tfa.layers.GroupNormalization(groups=5, axis=3),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu')m
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_test, y_test)
```

## Instance Normalization Tutorial
### Introduction
Instance Normalization is special case of group normalization where the group size is the same size as the channel size (or the axis size).

Experimental results show that instance normalization performs well on style transfer when replacing batch normalization. Recently, instance normalization has also been used as a replacement for batch normalization in GANs.

### Example
Applying InstanceNormalization after a Conv2D Layer and using a uniformed initialized scale and offset factor.
```Python
model = tf.keras.models.Sequential([
  # Reshape into "channels last" setup.
  tf.keras.layers.Reshape((28, 28, 1), input_shape=(28, 28)),
  tf.keras.layers.Conv2D(filters=10, kernel_size=(3, 3), data_format="channels_last")
  # LayerNorm Layer
  tfa.layers.InstanceNormalization(axis=3,
                                   center=True,
                                   scale=True,
                                   beta_initializer="random_uniform",
                                   gamma_initializer="random_uniform")
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_test, y_test)
```

## Layer Normalization Tutorial
### Introduction
Layer Normalization is special case of group normalization where the group size is 1. The mean and standard deviation is calculated from all activations of a single sample.

Experimental results show that Layer normalization is well suited for Recurrent Neural Networks, since it works batchsize independently.

### Example
Applying Layernormalization after a Conv2D Layer and using a scale and offset factor.
```Python
model = tf.keras.models.Sequential([
  # Reshape into "channels last" setup.
  tf.keras.layers.Reshape((28, 28, 1), input_shape=(28, 28)),
  tf.keras.layers.Conv2D(filters=10, kernel_size=(3, 3), data_format="channels_last"),
  # LayerNorm Layer
  tf.keras.layers.LayerNormalization(axis=3, center=True, scale=True),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])
model.complie(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_test, y_test)
```

#### Reference
- Normalization TensorFlow, https://www.tensorflow.org/addons/tutorials/layers_normalizations, 2021-11-15-Mon.
