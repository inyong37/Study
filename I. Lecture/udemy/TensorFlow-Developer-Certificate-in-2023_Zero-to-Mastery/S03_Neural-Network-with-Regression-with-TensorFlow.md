# Section 3: Neural network regression with TensorFlow

## Date

2023-01-13-Friday: 38 ~ 40

2023-01-14-Saturday: 41 ~ 47, 48 ~ 49

2023-01-15-Sunday: 50

2023-01-16-Monday: 51 ~ 56, 57 ~ 68

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

- Colab
- https://www.tensorflow.org/api_docs/python/tf/keras/utils

### 51. Evaluating a TensorFlow model part 5 (visualising a model's ...

- Colab

### 52. Evaluating a TensorFlow model part 6 (common regression...

- Colab
- Regression Metrics:
  - Mean absolute error (MAE)
  - Mean square error (MSE): when larger errors are more significant than smaller errors.
  - Huber: combination of MSE and MAE, less sensitive to outliers than MSE.

### 53. Evaluating a TensorFlow regression model part 7 (mean absolute error

- Colab

### 54. Evaluating a TensorFlow regression model part 7 (mean square error

- Colab

### 55. Setting up TensorFlow modelling experiments part 1 (start with a...

- Colab 

### 56. Setting up TensorFlow modelling experiments part 2 (increasing...

- Colab

### 57. Comparing and tracking your TensorFlow modelling experiments

- Colab
- https://www.tensorflow.org/tensorboard
- https://wandb.ai/site

### 58. How to save a TensorFlow model

- Colab
- SavedModel format
- HDF5 format

### 59. How to load and use a saved TensorFLow model

### 60 (Optional) How to save and download files from Google Colab

### 61. Putting together what we've learned part 1 (preparing a dataset)

- https://www.kaggle.com/datasets/mirichoi0218/insurance
- https://github.com/stedy/Machine-Learning-with-R-datasets
- https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv
- one-hot encoding: https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html

### 62. Putting together what we've learned part 2 (building a regression...

- Colab: `COMMAND/CONTROL` + `m` + `-`
- https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

### 63. Putting together what we've learned part 3 (improving our...

- Colab
- https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/EarlyStopping

### 64. Preprocessing data with feature scaling part 1 (what is feature...

- Colab
1. Turn all data into numbers (neural networks can't handle strings)
2. Make sure all of your tensors are the right shape
3. Scale features (normalize or standardize, neural networks tend to prefer normalization)
- Feature scaling
  - Scale (also referred to as normalization)
  - Standardization
- https://towardsdatascience.com/scale-standardize-or-normalize-with-scikit-learn-6ccc7d176a02

### 65. Preprocessing data with feature scaling part 2 (normalising our data)

- Colab

### 66. Preprocessing data with feature scaling part 3 (fitting a model on...

- Colab

### 67. TensorFlow Regression challenge, exercises & extra-curriculum

- https://github.com/mrdbourke/tensorflow-deep-learning
- https://github.com/mrdbourke/tensorflow-deep-learning/blob/main/README.md#-01-neural-network-regression-with-tensorflow-exercises
- https://github.com/mrdbourke/tensorflow-deep-learning/discussions

### 68. Learning Guideline

- https://zerotomastery.io/career-paths/
