# Section 3: Neural network regression with TensorFlow

## Date

2023-01-13-Friday 38 ~ 40

2023-01-14-Saturday 41 ~ 47, 48 ~ 49

## Contents

### 38. Introduction to Neural Network Regression with TensorFlow

- https://github.com/mrdbourke/tensorflow-deep-learning
- Predict numbers
  - How much/many
  - Detected box

### 39. Inputs and outputs of a neural network regression model

- Input (independent variable/predictors)
  - shape = [3]
  - bedroom, bathroom, garage
- Output (dependent/outcome variable)
  - shape = [1]
  - house price = [939700]

### 40. Anatomy and architecture of a neural network regression model

- Hyperparameters

### 41. Creating sample regression data (so we can model it)

- Colab

### 42. Note: Code update for upcoming lecture(s) for TensorFlow 2.7.0+ fix

- `model.fit(X, y, epochs=5) # this will break with TensorFlow 2.7.0+`
- `model.fit(tf.expand_dims(X, axis=-1), y, epochs=5) # <- updated line`
- https://github.com/mrdbourke/tensorflow-deep-learning/discussions/256#discussioncomment-1618168
- https://colab.research.google.com/drive/1i4i5wtC50p_FDdKXTWfNpX165I9dbw91?usp=sharing
- https://github.com/mrdbourke/tensorflow-deep-learning/blob/main/01_neural_network_regression_in_tensorflow.ipynb

### 43. The major steps in modelling with TensorFlow

1. Get the day ready (trun into tensors)
2. Build or pick a pretrained model (to suit your problem)
3. Fir the model to the data and make a prediction
4. Evaluate the model
5. Improve through experimentation
6. Save and reload your trained model
- Colab

### 44. Steps in improving a model with TensorFlow part 1

- Colab

### 45. Steps in improving a model with TensorFlow part 2

- Colab: epochs

### 46. Steps in improving a model with TensorFlow part 3

- Colab
- model
  - adding layers
  - increase the number of hidden units
  - change the activation functions
  - change the optimizer function
  - change the "learning rate"
  - fitting on more data
  - fitting for longer

### 47. Evaluating a TensorFlow model part 1 ("visualise, visualise, visualise")

- Colab

### 48. Evaluating a TensorFlow model part 2 (the three datasets)

- Colab
- Three datasets
  - Course materials (training set)
  - Practice exame (validation set)
  - Final exam (test set)
- Generalization: The ability for a machine learning model to perform well on data it hasn't seen before.

### 49. Evaluating a TensorFlow model part 3 (getting a model summary)

- Colab
- http://introtodeeplearning.com/

### 50. Evaluating a TensorFlow model part 4 (visualising a model's layers)

### 51. Evaluating a TensorFlow model part 5 (visualising a model's ...

### 52. Evaluating a TensorFlow model part 6 (common regression...

### 53. Evaluating a TensorFlow regression model part 7 (mean...

### 54. Evaluating a TensorFlow regression model part 7 (mean...

### 55. Setting up TensorFlow modelling experiments part 1 (start with a...

### 56. Setting up TensorFlow modelling experiments part 2 (increasing...

### 57. Comparing and tracking your TensorFlow modelling experiments

### 58. How to save a TensorFlow model

### 59. How to load and use a saved TensorFLow model

### 60 (Optional) How to save and download files from Google Colab

### 61. Putting together what we've learned part 1 (preparing a dataset)

### 62. Putting together what we've learned part 2 (building a regression...

### 63. Putting together what we've learned part 3 (improving our...

### 64. Preprocessing data with feature scaling part 1 (what is feature...

### 65. Preprocessing data with feature scaling part 2 (normalising our data)

### 66. Preprocessing data with feature scaling part 3 (fitting a model on...

### 67. TensorFlow Regression challenge, exercises & extra-curriculum

### 68. Learning Guideline

