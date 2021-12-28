# Framework

### Framework vs. Library | [Reference](https://martinfowler.com/bliki/InversionOfControl.html) | [Reference](https://www.c-sharpcorner.com/uploadfile/a85b23/framework-vs-library/)
Inversion of Control is a key part of what makes a framework different to a library. A library is essentially a set of functions that you can call, these days usually organized into classes. Each call does some work and returns control to the client.

A framework embodies some abstract design, with more behavior built in. In order to use it you need to insert your behavior into various places in the framework either by subclassing or by plugging in your own classes. The framework's code then calls your code at these points.

Both of them define an API for programmers to use. To put those together, we can think of a library as a certain function of an application, a framework as the skeleton of the application, and an API as a connector to put those together. A typical development process normally starts with a framework and fills out functions defined in libraries using the API.

## [OpenCV](https://opencv.org/) | [GitHub](https://github.com/opencv/opencv)
OpenCV was started at Intel in 1999 by Gary Bradsky, and the first release came out in 2000. Vadim Pisarevsky joined Gary Bradsky to manage Intel's Russian software OpenCV team. In 2005, OpenCV was used on Stanley, the vehicle that won the 2005 DARPA Grand Challenge. Later, its active development continued under the support of Willow Garage with Gary Bradsky and Vadim Pisarevsky leading the project. OpenCV now supports a multitud of algorithms related to Computer Vision and Machine Learning and is expanding day by day.

OpenCV supports a wide variety of programming languages such as C++, Python, Java, etc., and is available on different platforms including Windows, Linux, OS X, Android, and iOS. Interfaces for high-speed GPU operations based on CUDA and OpenCL are also under active development. OpenCV-Python is the Python API for OpenCV, combining the best qualities of the OpenCV C++ API and the Python language.

Open Source Computer Vision Library[Ref]

(with CMake, cpp, h)

## [TensorFlow](https://www.tensorflow.org/) | [GitHub](https://github.com/tensorflow/tensorflow)
TensorFlow is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries, and community resources that lets researchs push the state-of-the-art in ML and developers easily build and deploy ML-powered applications.

TensorFlow was originally developed by researchers and engineers working on the Google Brain team within Google's Machine Intelligence Research organiztion to conduct machine learning and deep nural networks research. The system is general enough to be applicable in a wide variety of other domains, as well.

TensorFlow provides stable Python and C++ APIs, as well as non-guaranted backward compatible API for other languages. [Ref]

### [TensorFlow Hub](https://tfhub.dev/)
The TensorFlow Hub lets you search and discover hundreds of trained, ready-to-deploy machine learning models in one place.

- Text Problem Domains: Embedding | Language model | Preprocessing | ...
- Image Problem Domains: Classification | Feature vector | Object detection | ...
- Video Problem Domains: Classification | Generation | Audio text | ...
- Audio Problem Domains: Speech-to-Text | Embedding | Speech synthesis | ... 

## [Keras](https://keras.io/) | [GitHub](https://github.com/keras-team/keras)
Keras is a deep learning API written in Python, running on top of the machine learning platform TensorFlow.

Multi-backend Keras has been discontinued. At this time, we recommend that Keras users who use multi-backend Keras with the TensorFlow backend switch to tf.keras in TensorFlow 2.0.

Keras 2.2.5 was the last release of Keras implementing the 2.2.* API. It was the last release to only support TensorFlow 1 (as well as Theano and CNTK).[Ref]

Install `pip install keras`

Setup(TensorFlow >=2.0) `from tensorflow import keras`

## [PyTorch](https://pytorch.org/) | [GitHub](https://github.com/pytorch/pytorch) | [Tutorial](https://pytorch.org/tutorials/) | [Tutorial (KR)](https://tutorials.pytorch.kr/)
Tensors and Dynamic neural networks in Python with strong GPU acceleration[Ref]

(with submodule or bazel)

## [Caffe](https://caffe.berkeleyvision.org/) | [GitHub](https://github.com/BVLC/caffe)
Caffe is a deep learning framework made with expression, speed, and modularity in mind. It is developed by Berkeley AI Research (BAIR) and by community contributors. Yangqing Jia created the project during his PhD at UC Berkeley. Caffe is released under the BSD 2-Clause license.[Ref]

(with CMake and docker)

## [Theano](http://www.deeplearning.net/software/theano/) | [GitHub](https://github.com/Theano/Theano)
Theano is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently. It can use GPUs and perform efficient symbolic differentiation.[Ref]

[MILA will stop developing Theano.](https://groups.google.com/forum/#!msg/theano-users/7Poq8BZutbY/rNCIfvAEAwAJ)

## [CNTK](https://docs.microsoft.com/ko-kr/cognitive-toolkit/) | [GitHub](https://github.com/microsoft/CNTK)
The Microsoft Cognitive Toolkit (CNTK) is an open-source toolkit for commercial-grade distributed deep learning. It describes neural networks as a series of computational steps via a directed graph. CNTK allows the user to easily realize and combine popular model types such as feed-forward DNNs, convolutional neural networks (CNNs) and recurrent neural networks (RNNs/LSTMs). CNTK implements stochastic gradient descent (SGD, error backpropagation) learning with automatic differentiation and parallelization across multiple GPUs and servers.[Ref]

## [OpenVINO](https://software.intel.com/content/www/us/en/develop/tools/openvino-toolkit.html) | [Docs](https://docs.openvinotoolkit.org/latest/index.html)
OpenVINO toolkit is a comprehensive toolkit for quickly developing applications and solutions that solve a variety of tasks including emulation of human vision, automatic speech recognition, natural language processing, recommendation systems, and many others. Based on latest generations of artificial neural networks, including Convolutional Neural Networks (CNNs), recurrent and attention-based networks, the toolkit extends computer vision and non-vision workloads across Intel® hardware, maximizing performance. It accelerates applications with high-performance, AI and deep learning inference deployed from edge to cloud.

#### Reference
- TensorFlow GitHub, https://github.com/tensorflow/tensorflow, 2020-07-16-Thu.
- TensorFlow Hub, https://tfhub.dev/, 2021-12-28-Tue.
- Keras, https://keras.io/, 2020-07-16-Thu.
- Keras GitHub, https://github.com/keras-team/keras, 2020-07-16-Thu.
- OpenCV, https://opencv.org/, 2020-07-16-Thu.
- OpenCV GitHub, https://github.com/opencv/opencv, 2020-07-16-Thu.
- PyTorch, https://pytorch.org/, 2020-07-16-Thu.
- PyTorch GitHub, https://github.com/pytorch/pytorch, 2020-07-16-Thu.
- PyTorch Tutorial, https://pytorch.org/tutorials/, 2021-10-25-Mon.
- PyTorch Tutorial KR, https://tutorials.pytorch.kr/, 2021-10-25-Mon.
- Caffe, https://caffe.berkeleyvision.org/, 2020-07-16-Thu.
- Caffe GitHub, https://github.com/BVLC/caffe, 2020-07-16-Thu.
- Theano, http://www.deeplearning.net/software/theano/, 2020-07-16-Thu.
- Theano GitHub, https://github.com/Theano/Theano, 2020-07-16-Thu.
- CNTK, https://docs.microsoft.com/ko-kr/cognitive-toolkit/, 2020-07-16-Thu.
- CNTK GitHub, https://github.com/microsoft/CNTK, 2020-07-16-Thu.
- Introduction to OpenCV-Python Tutorials, https://docs.opencv.org/master/d0/de3/tutorial_py_intro.html, 2020-11-25-Wed.
- OpenVINO, https://software.intel.com/content/www/us/en/develop/tools/openvino-toolkit.html, 2020-12-10-Thu.
- OpenVINO Docs, https://docs.openvinotoolkit.org/latest/index.html, 2020-12-10-Thu.
- Inveresion of Control, https://martinfowler.com/bliki/InversionOfControl.html, 2021-08-10-Tue.
- Framework vs. Library, https://www.c-sharpcorner.com/uploadfile/a85b23/framework-vs-library/, 2021-08-10-Tue.
