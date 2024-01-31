# :hammer_and_wrench: Framework

### Framework vs. Library | [Reference](https://martinfowler.com/bliki/InversionOfControl.html) | [Reference](https://www.c-sharpcorner.com/uploadfile/a85b23/framework-vs-library/)

Inversion of Control is a key part of what makes a framework different to a library. A library is essentially a set of functions that you can call, these days usually organized into classes. Each call does some work and returns control to the client.

A framework embodies some abstract design, with more behavior built in. In order to use it you need to insert your behavior into various places in the framework either by subclassing or by plugging in your own classes. The framework's code then calls your code at these points.

Both of them define an API for programmers to use. To put those together, we can think of a library as a certain function of an application, a framework as the skeleton of the application, and an API as a connector to put those together. A typical development process normally starts with a framework and fills out functions defined in libraries using the API.

## :hammer: [OpenCV](https://opencv.org/) | [GitHub](https://github.com/opencv/opencv)

OpenCV was started at Intel in 1999 by Gary Bradsky, and the first release came out in 2000. Vadim Pisarevsky joined Gary Bradsky to manage Intel's Russian software OpenCV team. In 2005, OpenCV was used on Stanley, the vehicle that won the 2005 DARPA Grand Challenge. Later, its active development continued under the support of Willow Garage with Gary Bradsky and Vadim Pisarevsky leading the project. OpenCV now supports a multitud of algorithms related to Computer Vision and Machine Learning and is expanding day by day.

OpenCV supports a wide variety of programming languages such as C++, Python, Java, etc., and is available on different platforms including Windows, Linux, OS X, Android, and iOS. Interfaces for high-speed GPU operations based on CUDA and OpenCL are also under active development. OpenCV-Python is the Python API for OpenCV, combining the best qualities of the OpenCV C++ API and the Python language.

Open Source Computer Vision Library[Ref]

OpenCV is built with CMake, cpp, and h.

## :hammer: [TensorFlow](https://www.tensorflow.org/) | [GitHub](https://github.com/tensorflow/tensorflow)

TensorFlow is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries, and community resources that lets researchs push the state-of-the-art in ML and developers easily build and deploy ML-powered applications.

TensorFlow was originally developed by researchers and engineers working on the Google Brain team within Google's Machine Intelligence Research organiztion to conduct machine learning and deep nural networks research. The system is general enough to be applicable in a wide variety of other domains, as well.

TensorFlow provides stable Python and C++ APIs, as well as non-guaranted backward compatible API for other languages. [Ref]

[Get started with tensorflow-metal](https://developer.apple.com/metal/tensorflow-plugin/)

[Set up your environment to take the TensorFlow Developer Certificate Exam](https://www.tensorflow.org/extras/cert/Setting_Up_TF_Developer_Certificate_Exam.pdf)

[Python venv: How To Create, Activate, Deactivate, And Delete](https://python.land/virtual-environments/virtualenv)

### [TensorFlow Hub](https://tfhub.dev/)

The TensorFlow Hub lets you search and discover hundreds of trained, ready-to-deploy machine learning models in one place.

- Text Problem Domains: Embedding | Language model | Preprocessing | ...
- Image Problem Domains: Classification | Feature vector | Object detection | ...
- Video Problem Domains: Classification | Generation | Audio text | ...
- Audio Problem Domains: Speech-to-Text | Embedding | Speech synthesis | ...

### [TensorFlow Certification](https://www.tensorflow.org/certificate)

Resources:

- [DeepLearning.AI TensorFlow Developer Professional Certificate](https://www.coursera.org/professional-certificates/tensorflow-in-practice)
- [Intro To TensorFlow for Deep Learning](https://www.udacity.com/course/intro-to-tensorflow-for-deep-learning--ud187)

## :hammer: [Keras](https://keras.io/) | [GitHub](https://github.com/keras-team/keras) | Merged to TensorFlow

Keras is a deep learning API written in Python, running on top of the machine learning platform TensorFlow. It was developed with a focus on enabling fast experimentation. Being able to go from idea to result as fast as possible is key to doing good research.

Keras is:

- Simple -- but not simplistic. Keras reduces developer cognitive load to free you to focus on the parts of the problem that really matter.
- Flexible -- Keras adopts the principle of progressive disclosure of complexity: simple workflows should be quick and easy, while arbitrarily advanced workflows should be possible via a clear path that builds upon what you've already learned.
- Powerful -- Keras provides industry-strength performance and scalability: it is used by organizations and companies including NAS, YouTube, or Waymo.

Multi-backend Keras has been discontinued. At this time, we recommend that Keras users who use multi-backend Keras with the TensorFlow backend switch to tf.keras in TensorFlow 2.0.

Keras 2.2.5 was the last release of Keras implementing the 2.2.* API. It was the last release to only support TensorFlow 1 (as well as Theano and CNTK).[Ref]

Install-TensorFlow < 2.0: `pip install keras`.

Import-TensorFlow < 2.0: `import keras`, TensorFlow >=2.0: `from tensorflow import keras`.

Merged into TensorFlow

## :hammer: [PyTorch](https://pytorch.org/) | [GitHub](https://github.com/pytorch/pytorch) | [Tutorial](https://pytorch.org/tutorials/) | [Tutorial (KR)](https://tutorials.pytorch.kr/)

Tensors and Dynamic neural networks in Python with strong GPU acceleration[Ref]

PyTorch is built with submodule or bazel.

### :hammer: [PyTorch](https://lightning.ai/docs/pytorch/stable/)

PyTorch Lightning is the deep learning framework for professional AI researchers and machine learning engineers who need maximal flexibility without sacrificing performance at scale. Lightning evolves with you as your projects go from idea to paper/production.

## :hammer: [Caffe](https://caffe.berkeleyvision.org/) | [GitHub](https://github.com/BVLC/caffe)

Caffe is a deep learning framework made with expression, speed, and modularity in mind. It is developed by Berkeley AI Research (BAIR) and by community contributors. Yangqing Jia created the project during his PhD at UC Berkeley. Caffe is released under the BSD 2-Clause license.[Ref]

Caffe is built with CMake and Docker.

## :hammer: [Theano](http://www.deeplearning.net/software/theano/) | [GitHub](https://github.com/Theano/Theano) Deprecated

Theano is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently. It can use GPUs and perform efficient symbolic differentiation.[Ref]

[MILA will stop developing Theano.](https://groups.google.com/forum/#!msg/theano-users/7Poq8BZutbY/rNCIfvAEAwAJ)

## :hammer: [CNTK](https://docs.microsoft.com/ko-kr/cognitive-toolkit/) | [GitHub](https://github.com/microsoft/CNTK) Deprecated

The Microsoft Cognitive Toolkit (CNTK) is an open-source toolkit for commercial-grade distributed deep learning. It describes neural networks as a series of computational steps via a directed graph. CNTK allows the user to easily realize and combine popular model types such as feed-forward DNNs, convolutional neural networks (CNNs) and recurrent neural networks (RNNs/LSTMs). CNTK implements stochastic gradient descent (SGD, error backpropagation) learning with automatic differentiation and parallelization across multiple GPUs and servers.[Ref]

[CNTK is no longer actively developed.](https://docs.microsoft.com/en-us/cognitive-toolkit/releasenotes/cntk_2_7_release_notes)

## :hammer: [OpenVINO](https://software.intel.com/content/www/us/en/develop/tools/openvino-toolkit.html) | [Docs](https://docs.openvinotoolkit.org/latest/index.html)

OpenVINO toolkit is a comprehensive toolkit for quickly developing applications and solutions that solve a variety of tasks including emulation of human vision, automatic speech recognition, natural language processing, recommendation systems, and many others. Based on latest generations of artificial neural networks, including Convolutional Neural Networks (CNNs), recurrent and attention-based networks, the toolkit extends computer vision and non-vision workloads across Intel® hardware, maximizing performance. It accelerates applications with high-performance, AI and deep learning inference deployed from edge to cloud.

[PyTorch vs TensorFlow 2023](https://www.assemblyai.com/blog/pytorch-vs-tensorflow-in-2023/)
1. Model Availability: With the domain of Deep Learning expanding every year and models becoming bigger in turn, training State-of-the-Art (SOTA) models from scratch is simply not feasible anymore. There are fortunately SOTA models publicly available, and it is important to utilize them where possible.
2. Deployment Infrastructure: Training well-performing models is pointless if they can't be put to use. Lowering time-to-deploy is paramount, especially with the growing popularity of microservice business models; and efficient deployment has the potential to make-or-break many business that center on Machine Learning.
3. Ecosystems: No longer is Deep Learning relegated to specific use cases in highly contrlled environments. AI is injecting new power into a litany of industries, so a framework that sits within a larger ecosystem which facilitates development for mobile, local, and server applications is important. Also, the advent of specialized Machine Learning hardware, such as Google's Edge TPU, means that successful practitioners need to work with a framework that can integrate well with this hardware.

---

### [Weights & Biases](https://wandb.ai/site)

### [fastai](https://docs.fast.ai/)

fastai simplifies training fast and accurate neural nets using modern best practices.

### [FAIR Detectron](https://github.com/facebookresearch/Detectron)

Detectron is Facebook AI Research's software system that implements state-of-the-art object detection algorithms, including Mask R-CNN. It is written in Python and powered by the Caffe2 deep learning framework.

Detectron is deprecated. Please see detectron2, a ground-up rewrite of Detectron in PyTorch.

### [FAIR Detectron2](https://github.com/facebookresearch/detectron2)

Detectron2 is Facebook AI Research's next generation library that provides state-of-the-art detection and segmentation algorithms. It is the successor of Detectron and maskrcnn-benchmark. It supports a number of computer vision research projects and production applications in Facebook.

### [OpenMMLab MMDetection](https://github.com/open-mmlab/mmdetection)

MMDetection is an open source object detection toolbox based on PyTorch. It is a part of the OpenMMLab project.

### [ONNX: Open Neural Network Exchange](https://onnx.ai/) | [GitHub](https://github.com/onnx/onnx)

ONNX is an open format built to represent machine learning models. ONNX defines a common set of operators - the building blocks of machine learning and deep learning models - and a common file format to enable AI developers to use models with a variety of frameworks, tools, runtimes, and compilers.

Key Benefits:
* Interoperability: Develop in your preferred framework without worrying about downstream inferencing implications. ONNX enables you to use your preferred framework with your chosen inference engine.
* Hardware Access: ONNX makes it easier to access hardware optimizations. Use ONNX-compatible runtimes and libraries designed to maximize performance across hardware.

---

### Reference
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
- Weights & Biases, https://wandb.ai/site, 2022-01-05-Wed.
- fastai, https://docs.fast.ai/, 2022-01-15-Sat.
- Detectron, https://github.com/facebookresearch/Detectron, 2022-02-16-Wed.
- detectron2, https://github.com/facebookresearch/detectron2, 2022-02-16-Wed.
- MMDetection, https://github.com/open-mmlab/mmdetection, 2022-02-16-Wed.
- TensorFlow Certificate Program, https://www.tensorflow.org/certificate, 2022-10-18-Tue.
- DeepLearning.AI TensorFlow Developer Professional Certificate Coursera, https://www.coursera.org/professional-certificates/tensorflow-in-practice, 2022-10-18-Tue.
- Intro to TensorFlow for Deep Learning Udacity, https://www.udacity.com/course/intro-to-tensorflow-for-deep-learning--ud187, 2022-10-18-Tue.
- Get started with tensorflow-metal, https://developer.apple.com/metal/tensorflow-plugin/, 2023-08-25-Fri.
- Set up your environment to take the TensorFlow Developer Certificate Exam, https://www.tensorflow.org/extras/cert/Setting_Up_TF_Developer_Certificate_Exam.pdf, 2023-08-25-Fri.
- Python venv: How To Create, Activate, Deactivate, And Delete, https://python.land/virtual-environments/virtualenv, 2023-08-25-Fri.
- PyTorch vs TensorFlow 2023, https://www.assemblyai.com/blog/pytorch-vs-tensorflow-in-2023/, 2023-12-14-Thu.
- ONNX, https://onnx.ai/, 2023-12-14-Thu.
