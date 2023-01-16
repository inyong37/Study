# Section 2: Deep Learning and TensorFlow Fundamentals

## Date

2023-01-12-Thursday: ~ 8

2023-01-13-Friday: 9 ~ 16, 17 ~ 37

## Content

### 6. What is deep learning?

- Trandtional programming starts with inputs and rules and makes output. However, the machine learning algorithm starts with inputs and output, and figures out rules.

### 7. Why use deep learning?

- For a complex problem, can you think of all the rules?
- If you can build a simple rule-based system that doesn't require machine learning, do that. Google ML engineer rule 1.
  - Rules of Machine Learning
- What deep learning is good for
  - Problems with long list of rules
  - Continually changing environmnets
  - Discovering insights within large collections of data
- What deep learning is not good for
  - When you need explainability
  - When the tranditional approach is a better option
  - When errors are unacceptable
  - When you don't have much data
- Machine learning (shallow algorithm) fits structured data, whereas deep learning fits unstructured data

### 8. What are neural networks?

- Neural Networks
  - Inputs, Numerical encoding, Learns representation (pattern/feature/weights), Representation outputs, Outputs
- Anatomy
  - Input layer; data goes in here, Hidden layer(s); learns patterns in data, Output layer; outputs learned representation or prediction probabilites
- Types of Learning
  - Supervised Learning, Semi-supervised Learning, Unsupervised Learning, Transfer Learning

### 9. What is deep learning already being used for?

- Recommendation, Transloation, Speech recognition, Computer Vision (detection), Natural Language Processing (NLP)
  - seq2seq, classification/regression, AlphaFold

### 10. What is and why use TensorFlow?

- What
  - End-to-end platform for machine learning
  - Write fast deep learning code in Python/other accessible languages
  - Able to access many pre-built deep learning models
  - Whole stack: preprocess data, model data, deploy model in your application
  - Originally designed and used in-house by Google
- Why?
  - Easy model building, Robust ML production anywhere, Powerful experimentaion for research

### 11. What is a Tensor?

- numerical represenation of data
- https://youtu.be/f5liqUk0ZTw

### 12. What we're going to cover throughout the course

- Basic, preprocessing, build, using, fitting, prediction, evaluating, saving, loading, custom data
- A TensorFlow workflow

### 13. How to approach this course

- Write code, Explore & experiment, Ask questions, Do the exercises, Share your work
- Avoid: Overthinking the process, The "I can't learn it" mentally

### 14. Need A Refresher?

- https://zerotomastery.io/courses/machine-learning-and-data-science-bootcamp/

### 15. Creating your first tensors with TensorFlow and tf.constant()

- Colab
- https://www.tensorflow.org/api_docs/python/tf/constant

### 16. Creating tensors with TensorFlow and tf.Variable()

- Colab
- https://www.tensorflow.org/api_docs/python/tf/Variable

### 17. Creating random tensors with TensorFlow

- Colab
1. Initialize with random weights (only at beginning)
2. Show examples
3. Update representation outputs
4. Repeat with more examples

### 18. Shuffling the order of tensors

- Colab
- https://www.tensorflow.org/api_docs/python/tf/random/set_seed

### 19. Creating tensors from Numpy arrays

- Colab

### 20. Getting infromation from your tensors (tensor attributes)

- Colab

### 21. Indexing and expanding tensors

- Colab

### 22. Manipulating tensors with basic operations

- Colab

### 23. Matrix multiplication with tensors part 1

- Colab
- http://matrixmultiplication.xyz/
- https://www.mathsisfun.com/algebra/matrix-multiplying.html

### 24. Matrix multiplication with tensors part 2

- Colab

### 25. Matrix multiplication with tensors part 3

- Colab

### 26. Changing the datatype of tensors

- Colab
- https://www.tensorflow.org/guide/mixed_precision

### 27. Tensor aggregation (finding the min, max, mean & more)

- Colab

### 28. Tensor troubleshooting example (updating tensor datatypes)

- Colab

### 29. Finding the positional minimum and maximum of a tensor (argmin and argmax)

- Colab

### 30. Squeezing a tensor (removing all 1-dimension axes)

- Colab

### 31. One-hot encoding tensors

- https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/
- Colab

### 32. Trying out more tensor math operations

- Colab

### 33. Exploring TensorFlow and NumPy's compatibility

- https://numpy.org/
- Colab 

### 34. Making sure our tensor operations run really fast on GPUs

- Colab
- https://research.google.com/colaboratory/faq.html#gpu-availability

### 35. TensorFlow Fundamentals challenge, exercises & extra-...

- https://github.com/mrdbourke/tensorflow-deep-learning
- https://github.com/mrdbourke/tensorflow-deep-learning#-00-tensorflow-fundamentals-exercises
- https://github.com/mrdbourke/tensorflow-deep-learning/discussions

### 36. Monthly Coding Challenges, Free Resources and Guides

- https://zerotomastery.io/community/coding-challenges/
- https://zerotomastery.io/blog/
- https://zerotomastery.io/resources/

### 37. LinkedIn Endorsements

https://www.linkedin.com/groups/12121940/
https://www.linkedin.com/school/ztm-academy/
