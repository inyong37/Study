# Section 4: Neural network classification in TensorFlow

## Date

2023-01-17-Tuesday: 69 ~ 74. -> 70 ~ 75.

2023-01-18-Wednesday: 74 ~ 79. -> 75 ~ 80.

2023-03-28-Tuesday: 81 ~ 85.

## Contents

https://github.com/mrdbourke/tensorflow-deep-learning/blob/main/02_neural_network_classification_in_tensorflow.ipynb

### 70. Introduction to neural network classification in TensorFlow

- https://github.com/mrdbourke/tensorflow-deep-learning/
- Binary classification, Multiclass classification, Multilabel classification (multiple label options per sample)

### 71. Example classification problems (and their inputs and outputs)

### 72. Input and output tensors of classification problems

- Input (batch_size, width, height, color_channels) -> Machine Learning Algorithm -> Output (prediction probabilities)
  - 32 is a very common batch size; 32 images at the time for memory size

### 73. Typical architecture of neural network classification models with TensorFlow

- Hyperparameters: Input layer shape, Hidden layer(s), Neurons per hidden layer, Output layer shape, Hidden activation, Output activation, Loss function, Optimizer
- http://karpathy.github.io/2019/04/25/recipe/
- Colab
- https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.68308&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false

### 74. Creating and viewing classifiation data to model

- Colab

### 75. Checking the input and output shapes of our classification data

- Colab

### 76. Building a not very good classification model with TensorFlow

- Colab
- https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryCrossentropy

### 77. Trying to improve our not very good classification model

- Colab
- https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense: `activation=None`

### 78. Creating a function to view our model's not so good predictions

- Colab
- https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html
- https://numpy.org/doc/stable/reference/generated/numpy.c_.html
- https://cs231n.github.io/neural-networks-case-study/
- https://github.com/GokuMohandas/Made-With-ML

### 79. Note: Updates for TensorFlow 2.7.0

- If you're using TensorFlow 2.7.0+ (default in Google Colab from November 2021), you might run into some shape errors when trying to fit a model (calling model.fit()).
  - This happened due to some changes in TensorFlow 2.7.0.
  - In short, TensorFlow no longer automatically upranks single dimension data from (batch_size, ) to (batch_size, 1).
  - `tf.keras.layers.Dense(100, input_shape=(None, 1)),`
  - `model_3.fit(tf.expand_dims(X_reg_train, axis=-1),`
  - https://github.com/mrdbourke/tensorflow-deep-learning/blob/main/02_neural_network_classification_in_tensorflow.ipynb
  - https://github.com/mrdbourke/tensorflow-deep-learning/discussions/278
  - https://colab.research.google.com/drive/1_dlrB_DJOBS9c9foYJs49I0YwN7LTakl?usp=sharing

### 80. Make our poor classification model work for a regression dataset

- Colab

### 81. Non-linearity part 1: Straight lines and non-straight lines

### 82. Non-linearity part 2: Building our first neural network with non-linearity

Linearity vs. non-leaarity

https://playground.tensorflow.org/

### 83. Non-linearity part 3: Upgrading our non-linear model with more...

### 84. Non-linearity part 4: Modeling our non-linear data once and for all

- https://stats.stackexchange.com/questions/218542/which-activation-function-for-output-layer
  - Regression: linear (because values are unbounded)
  - Classification: softmax (simple sigmoid works too but softmax works better)

### 85. Non-linearity part 5: Replicating non-linear activation functions from scratch

https://www.tensorflow.org/api_docs/python/tf/keras/activations/sigmoid

https://www.tensorflow.org/api_docs/python/tf/keras/activations/relu

https://www.tensorflow.org/api_docs/python/tf/keras/activations/linear

https://ml-cheatsheet.readthedocs.io/en/latest/activation_functions.html

### 86. Getting great results in less time by tweaking the learning rate

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
