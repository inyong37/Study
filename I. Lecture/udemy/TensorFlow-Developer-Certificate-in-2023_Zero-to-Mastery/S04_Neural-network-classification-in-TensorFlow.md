# Section 4: Neural network classification in TensorFlow

## Date

2023-01-17-Tuesday: 69 ~ 74.

2023-01-18-Wednesday: 74 ~ 79.

## Contents

### 69. Introduction to neural network classification in TensorFlow

- https://github.com/mrdbourke/tensorflow-deep-learning/
- Binary classification, Multiclass classification, Multilabel classification (multiple label options per sample)

### 70. Example classification problems (and their inputs and outputs)

### 71. Input and output tensors of classification problems

- Input (batch_size, width, height, color_channels) -> Machine Learning Algorithm -> Output (prediction probabilities)
  - 32 is a very common batch size; 32 images at the time for memory size

### 72. Typical architecture of neural network classification models with...

- Hyperparameters: Input layer shape, Hidden layer(s), Neurons per hidden layer, Output layer shape, Hidden activation, Output activation, Loss function, Optimizer
- http://karpathy.github.io/2019/04/25/recipe/
- Colab
- https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.68308&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false

### 73. Creating and viewing classifiation data to model

- Colab

### 74. Checking the input and output shapes of our classification data

- Colab

### 75. Building a not very good classification model with TensorFlow

- Colab
- https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryCrossentropy

### 76. Trying to improve our not very good classification model

- Colab
- https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense: `activation=None`

### 77. Creating a function to view our model's not so good predictions

- Colab
- https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html
- https://numpy.org/doc/stable/reference/generated/numpy.c_.html
- https://cs231n.github.io/neural-networks-case-study/
- https://github.com/GokuMohandas/Made-With-ML

### 78. Note: Updates for TensorFlow 2.7.0

- If you're using TensorFlow 2.7.0+ (default in Google Colab from November 2021), you might run into some shape errors when trying to fit a model (calling model.fit()).
  - This happened due to some changes in TensorFlow 2.7.0.
  - In short, TensorFlow no longer automatically upranks single dimension data from (batch_size, ) to (batch_size, 1).
  - `tf.keras.layers.Dense(100, input_shape=(None, 1)),`
  - `model_3.fit(tf.expand_dims(X_reg_train, axis=-1),`
  - https://github.com/mrdbourke/tensorflow-deep-learning/blob/main/02_neural_network_classification_in_tensorflow.ipynb
  - https://github.com/mrdbourke/tensorflow-deep-learning/discussions/278
  - https://colab.research.google.com/drive/1_dlrB_DJOBS9c9foYJs49I0YwN7LTakl?usp=sharing

### 79. Make our poor classification model work for a regression dataset

- Colab

### 80. Non-linearity part 1: Straight lines and non-straight lines

### 81. Non-linearity part 2: Building our first neural network with non-linearity

### 82. Non-linearity part 3: Upgrading our non-linear model with more...

### 83. Non-linearity part 4: Modeling our non-linear data once and for all

### 84. Non-linearity part 5: Replicating non-linear activation functions fro...

### 85. Getting great results in less time by tweaking the learning rate

### 86.

### 87.

### 88.

### 89.

### 90.

### 91.

### 92.

### 93.

### 94.

### 95.

### 96.

### 97.

### 98.

### 99.

### 100.

### 101.

### 102.

### 103.