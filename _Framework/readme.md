# Framework

## [TensorFlow](https://www.tensorflow.org/) | [GitHub](https://github.com/tensorflow/tensorflow)
TensorFlow is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries, and community resources that lets researchs push the state-of-the-art in ML and developers easily build and deploy ML-powered applications.

TensorFlow was originally developed by researchers and engineers working on the Google Brain team within Google's Machine Intelligence Research organiztion to conduct machine learning and deep nural networks research. The system is general enough to be applicable in a wide variety of other domains, as well.

TensorFlow provides stable Python and C++ APIs, as well as non-guaranted backward compatible API for other languages. [Ref]

(with bazel, starlark)

## [Keras](https://keras.io/) | [GitHub](https://github.com/keras-team/keras)
Keras is a deep learning API written in Python, running on top of the machine learning platform TensorFlow.

Multi-backend Keras has been discontinued. At this time, we recommend that Keras users who use multi-backend Keras with the TensorFlow backend switch to tf.keras in TensorFlow 2.0.

Keras 2.2.5 was the last release of Keras implementing the 2.2.* API. It was the last release to only support TensorFlow 1 (as well as Theano and CNTK).[Ref]

(using TensorFlow)

## [OpenCV](https://opencv.org/) | [GitHub](https://github.com/opencv/opencv)
Open Source Computer Vision Library

(with CMake, cpp, h)

## [PyTorch](https://pytorch.org/) | [GitHub](https://github.com/pytorch/pytorch)
Tensors and Dynamic neural networks in Python with strong GPU acceleration

(with submodule or bazel)

## [Caffe](https://caffe.berkeleyvision.org/) | [GitHub](https://github.com/BVLC/caffe)
Caffe is a deep learning framework made with expression, speed, and modularity in mind. It is developed by Berkeley AI Research (BAIR) and by community contributors. Yangqing Jia created the project during his PhD at UC Berkeley. Caffe is released under the BSD 2-Clause license.

(with CMake and docker)

## [Theano](http://www.deeplearning.net/software/theano/) | [GitHub](https://github.com/Theano/Theano)
Theano is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently. It can use GPUs and perform efficient symbolic differentiation.[Ref]

[MILA will stop developing Theano.](https://groups.google.com/forum/#!msg/theano-users/7Poq8BZutbY/rNCIfvAEAwAJ)

## [CNTK](https://docs.microsoft.com/ko-kr/cognitive-toolkit/) | [GitHub](https://github.com/microsoft/CNTK)
The Microsoft Cognitive Toolkit (CNTK) is an open-source toolkit for commercial-grade distributed deep learning. It describes neural networks as a series of computational steps via a directed graph. CNTK allows the user to easily realize and combine popular model types such as feed-forward DNNs, convolutional neural networks (CNNs) and recurrent neural networks (RNNs/LSTMs). CNTK implements stochastic gradient descent (SGD, error backpropagation) learning with automatic differentiation and parallelization across multiple GPUs and servers.[Ref]

#### Reference
- TensorFlow GitHub, https://github.com/tensorflow/tensorflow, 2020-07-16-Thu.
- Keras, https://keras.io/, 2020-07-16-Thu.
- Keras GitHub, https://github.com/keras-team/keras, 2020-07-16-Thu.
- OpenCV, https://opencv.org/, 2020-07-16-Thu.
- OpenCV GitHub, https://github.com/opencv/opencv, 2020-07-16-Thu.
- PyTorch, https://pytorch.org/, 2020-07-16-Thu.
- PyTorch GitHub, https://github.com/pytorch/pytorch, 2020-07-16-Thu.
- Caffe, https://caffe.berkeleyvision.org/, 2020-07-16-Thu.
- Caffe GitHub, https://github.com/BVLC/caffe, 2020-07-16-Thu.
- Theano, http://www.deeplearning.net/software/theano/, 2020-07-16-Thu.
- Theano GitHub, https://github.com/Theano/Theano, 2020-07-16-Thu.
- CNTK, https://docs.microsoft.com/ko-kr/cognitive-toolkit/, 2020-07-16-Thu.
- CNTK GitHub, https://github.com/microsoft/CNTK, 2020-07-16-Thu.

## Build

### [Bazel](https://www.bazel.build/) | [Wiki (Kor)](https://ko.wikipedia.org/wiki/%EB%B0%94%EC%A0%A4_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4)) | [GitHub](https://github.com/bazelbuild/bazel)
Basel is an open source tool that enables software build and test automation. Google used and built Blaze, a build tool internally, and released and released part of the Blaze tool with Bazel, named Blaze's anagram. Bazel was first released in March 2015 and was beta tested until September 2015.

Similar to build tools like Make, Apache Ant, or Apache Maven, Bazel uses a set of rules to build application software from source code. Rules and macros are written in the Skylark language, a subset of Python. There are basic rules for writing software written in Java, C, C++, Python, Objective-C and Bourne shell script programming languages. Bazel can create application software packages suitable for distribution for Android and iOS operating systems.

When designing Bazel, we focused on build speed, accuracy and reproducibility. This tool uses parallelism to accelerate parts of the build process. Includes Bazel Query language that can be used to analyze build dependencies in complex build graphs.[Ref]

### [Starlark Language](https://docs.bazel.build/versions/2.0.0/skylark/language.html) | [GitHub](https://github.com/bazelbuild/starlark)
Starlark (formerly known as Skylark) is a language intended for use as a configuration language. It was designed for the Bazel build system, but may be useful for other projects as well. This repository is where Starlark features are proposed, discussed, and specified. It contains information about the language, including the specification. There are multiple implementations of Starlark.

Starlark is a dialect of Python. Like Python, it is a dynamically typed language with high-level data types, first-class functions with lexical scope, and garbage collection. Independent Starlark threads execute in parallel, so Starlark workloads scale well on parallel machines. Starlark is a small and simple language with a familiar and highly readable syntax. You can use it as an expressive notation for structured data, defining functions to eliminate repetition, or you can use it to add scripting capabilities to an existing application.

A Starlark interpreter is typically embedded within a larger application, and the application may define additional domain-specific functions and data types beyond those provided by the core language. For example, Starlark was originally developed for the Bazel build tool. Bazel uses Starlark as the notation both for its BUILD files (like Makefiles, these declare the executables, libraries, and tests in a directory) and for its macro language, through which Bazel is extended with custom logic to support new languages and compilers.[Ref]

### [Make]() | [Wiki (Kor)](https://ko.wikipedia.org/wiki/Make_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4)) |

### [CMake](https://cmake.org/) | [Wiki (Kor)](https://ko.wikipedia.org/wiki/CMake) | [GitLab](https://gitlab.kitware.com/cmake/cmake)
CMake is an open-source, cross-platform family of tools designed to build, test and package software. CMake is used to control the software compilation process using simple platform and compiler independent configuration files, and generate native makefiles and workspaces that can be used in the compiler environment of your choice. The suite of CMake tools were created by Kitware in response to the need for a powerful, cross-platform build environment for open-source projects such as ITK and VTK.[Ref]

### [Ninja](https://ninja-build.org/) | [Wiki (Kor)](https://ko.wikipedia.org/wiki/%EB%8B%8C%EC%9E%90_(%EB%B9%8C%EB%93%9C_%EC%8B%9C%EC%8A%A4%ED%85%9C)) | [GitHub](https://github.com/ninja-build/ninja)
Ninja is a small build system with a focus on speed. It differs from other build systems in two major respects: it is designed to have its input files generated by a higher-level build system, and it is designed to run builds as fast as possible.

### [GYP]() | [Wiki (Kor)](https://ko.wikipedia.org/wiki/GYP_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4)) | 

### [GN](https://www.chromium.org/developers/gn-build-configuration) | [Wiki (Kor)](https://ko.wikipedia.org/wiki/GN_(%EB%B9%8C%EB%93%9C_%EC%8B%9C%EC%8A%A4%ED%85%9C)) | [Google Source](https://gn.googlesource.com/gn/)
GN is a meta-build system that generates build files for Ninja.

#### Reference
- Bazel, https://www.bazel.build/, 2020-07-16-Thu.
- Bazel wiki, https://ko.wikipedia.org/wiki/%EB%B0%94%EC%A0%A4_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4), 2020-07-16-Thu.
- Bazel GitHub, https://github.com/bazelbuild/bazel, 2020-07-16-Thu.
- Starlark GitHub, https://github.com/bazelbuild/starlark, 2020-07-16-Thu.
- Make, 2020-07-16-Thu.
- Make Wiki(kor), https://ko.wikipedia.org/wiki/Make_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4), 2020-07-16-Thu.
- CMake, https://cmake.org/, 2020-07-16-Thu.
- CMake Wiki, https://ko.wikipedia.org/wiki/CMake, 2020-07-16-Thu.
- CMake GitLab, https://gitlab.kitware.com/cmake/cmake, 2020-07-16-Thu.
- Ninja, https://ninja-build.org/, 2020-07-16-Thu.
- Ninja Wiki, https://ko.wikipedia.org/wiki/%EB%8B%8C%EC%9E%90_(%EB%B9%8C%EB%93%9C_%EC%8B%9C%EC%8A%A4%ED%85%9C), 2020-07-16-Thu.
- Ninja GitHub, https://github.com/ninja-build/ninja, 2020-07-16-Thu.
- GYP Wiki, https://ko.wikipedia.org/wiki/GYP_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4), 2020-07-16-Thu. 
- GN, https://www.chromium.org/developers/gn-build-configuration, 2020-07-16-Thu.
- GN Wiki, https://ko.wikipedia.org/wiki/GN_(%EB%B9%8C%EB%93%9C_%EC%8B%9C%EC%8A%A4%ED%85%9C), 2020-07-16-Thu.
- GN Google Source, https://gn.googlesource.com/gn/, 2020-07-16-Thu.

