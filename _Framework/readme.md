# :hammer_and_wrench: Framework | [Nvidia](https://developer.ibm.com/articles/compare-deep-learning-frameworks/) | [IBM](https://developer.ibm.com/articles/compare-deep-learning-frameworks/)

Deep Learning (DL) frameworks offer building blocks for designing, training, and validating deep neural networks through a high-level programming interface. Widely-used DL frameworks, such as PyTorch, TensorFlow, PyTorch Geometric, DGL, and others, rely on GPU-accelerated libraries, such as cuDNN, NCCL, and DALI to deliver high-performance, multi-GPU-accelerated training.

### Framework vs. Library | [Reference](https://martinfowler.com/bliki/InversionOfControl.html) | [Reference](https://www.c-sharpcorner.com/uploadfile/a85b23/framework-vs-library/)

Inversion of Control is a key part of what makes a framework different to a library. A library is essentially a set of functions that you can call, these days usually organized into classes. Each call does some work and returns control to the client.

A framework embodies some abstract design, with more behavior built in. In order to use it you need to insert your behavior into various places in the framework either by subclassing or by plugging in your own classes. The framework's code then calls your code at these points.

Both of them define an API for programmers to use. To put those together, we can think of a library as a certain function of an application, a framework as the skeleton of the application, and an API as a connector to put those together. A typical development process normally starts with a framework and fills out functions defined in libraries using the API.

## :hammer: [OpenCV](https://opencv.org/) | [GitHub](https://github.com/opencv/opencv)

OpenCV was started at Intel in 1999 by Gary Bradsky, and the first release came out in 2000. Vadim Pisarevsky joined Gary Bradsky to manage Intel's Russian software OpenCV team. In 2005, OpenCV was used on Stanley, the vehicle that won the 2005 DARPA Grand Challenge. Later, its active development continued under the support of Willow Garage with Gary Bradsky and Vadim Pisarevsky leading the project. OpenCV now supports a multitud of algorithms related to Computer Vision and Machine Learning and is expanding day by day.

OpenCV supports a wide variety of programming languages such as C++, Python, Java, etc., and is available on different platforms including Windows, Linux, OS X, Android, and iOS. Interfaces for high-speed GPU operations based on CUDA and OpenCL are also under active development. OpenCV-Python is the Python API for OpenCV, combining the best qualities of the OpenCV C++ API and the Python language.

Open Source Computer Vision Library[Ref]

OpenCV is built with CMake, cpp, and h.

## :hammer: [TensorFlow](https://www.tensorflow.org/) | [GitHub](https://github.com/tensorflow/tensorflow) | [Model Garden](https://github.com/tensorflow/models) | [tensorflow/python/keras](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python/keras)

TensorFlow is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries, and community resources that lets researchs push the state-of-the-art in ML and developers easily build and deploy ML-powered applications.

TensorFlow was originally developed by researchers and engineers working on the Google Brain team within Google's Machine Intelligence Research organiztion to conduct machine learning and deep nural networks research. The system is general enough to be applicable in a wide variety of other domains, as well.

TensorFlow provides stable Python and C++ APIs, as well as non-guaranted backward compatible API for other languages. [Ref]

[Get started with tensorflow-metal](https://developer.apple.com/metal/tensorflow-plugin/)

[Set up your environment to take the TensorFlow Developer Certificate Exam](https://www.tensorflow.org/extras/cert/Setting_Up_TF_Developer_Certificate_Exam.pdf)

[Python venv: How To Create, Activate, Deactivate, And Delete](https://python.land/virtual-environments/virtualenv)

### [TensorFlow Documentation](https://github.com/tensorflow/docs)

TensorFlow:
* [Low Level Introduction](https://github.com/tensorflow/docs/blob/master/site/en/r1/guide/low_level_intro.md)
  * Building the computational graph: `tf.Graph`
    * The nodes of the graph (ops): `tf.Operation`
    * The edges in the graph: `tf.Tensor`
  * Running the computational graph: `tf.Session`
* [Architecture](https://github.com/tensorflow/docs/blob/master/site/en/r1/guide/extend/architecture.md)

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
- [What's new in TensorFlow and Keras](https://blog.tensorflow.org/2023/05/google-io-2023-whats-new-in-tensorflow-and-keras.html)

### [TensorBoard](https://www.tensorflow.org/tensorboard)

TensorFlow's visualization toolkit. TensorBoard provides the visualization and tooling needed for machine learning experimentation: Tracking and visualizing metrics such as loss and accuracy. Visualizing the model graph (ops and layers). Viewing histograms of weights, biases, or other tensors as they change over time. Projecting embedding to a lower dimensional space. Displaying images, text, and audio data. Profiling TensorFlow programs. And much more.

[TensorBoardX](https://tensorboardx.readthedocs.io/en/latest/tensorboard.html) | [GitHub](https://github.com/lanpa/tensorboardX)

### [Keras](https://keras.io/) | [GitHub](https://github.com/keras-team/keras) | [keras/layers](https://github.com/keras-team/keras/tree/master/keras/layers) [keras/models](https://github.com/keras-team/keras/tree/master/keras/models)

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

[Backend](https://keras.io/getting_started/): `export KERAS_BACKEND="tensorflow"` or `import os; os.environ["KERAS_BACKEND"] = "tensorflow"; import keras`
* [Customizing `fit()` with TensorFlow](https://keras.io/guides/custom_train_step_in_tensorflow/)
* [Customizing `fit()` with PyTorch](https://keras.io/guides/custom_train_step_in_torch/)
* [Customizing `fit()` with JAX](https://keras.io/guides/custom_train_step_in_jax/)

[model.py](https://github.com/keras-team/keras/blob/master/keras/models/model.py):
* `Model.{fit, predict, evalute, train_on_batch, test_on_batct, predict_on_batch}.__doc__`
* `base_trainer.Trainer.{fit, predict, evalute, train_on_batch, test_on_batct, predict_on_batch}.__doc__`

[trainer.py](https://github.com/keras-team/keras/blob/master/keras/trainers/trainer.py):
* compile: Configures the model for training.
* fit: Trains the model for a fixed number of epochs (dataset iterations).
* evaluate: Returns the loss value & metrics values for the model in test mode.
* predict: Generates output predictions for the input samples.
* train_on_batch: Runs a single gradient update on a single batch of data.
* test_on_batch: Test the model on a single batch of samples.
* predict_on_batch: Returns predictions for a single batch of samples.

[Callbacks](https://keras.io/api/callbacks/):
* Base Callback class
* [ModelCheckpoint](https://keras.io/api/callbacks/model_checkpoint/): Callback to save the Keras model or model weights at some frequency. It is used in conjuction with training using `model.fit()` to save a model or weights (in a checkpoint file) at some interval, so the model or weights can be loaded later to continue the training from the state saved.
* BackupAndRestore
* TensorBoard
* EarlyStopping
* LearningRateScheduler
* ReduceLROnPlateau
* RemoteMonitor
* LambdaCallback
* TerminateOnNaN
* CSVLogger
* ProgbarLogger

[Multiple Devices](https://keras.io/guides/distribution/):
* [Distributed training with Keras3](https://keras.io/guides/distribution/)
* [Distributed training with TensorFlow](https://keras.io/guides/distributed_training_with_tensorflow/)
* [Distributed training with PyTorch](https://keras.io/guides/distributed_training_with_torch/)
* [Distributed training with JAX](https://keras.io/guides/distributed_training_with_jax/)

Created by [François Chollet](https://fchollet.com/)

## :hammer: [PyTorch](https://pytorch.org/) | [GitHub](https://github.com/pytorch/pytorch) | [Tutorial](https://pytorch.org/tutorials/) | [Tutorial (KR)](https://tutorials.pytorch.kr/) | [Model Zoo](https://pytorch.org/serve/model_zoo.html) | [torch/nn](https://github.com/pytorch/pytorch/tree/main/torch/nn)

Tensors and Dynamic neural networks in Python with strong GPU acceleration[Ref]

PyTorch is built with submodule or bazel.

Papers:
* [Automatic differenctiation in PyTorch](https://openreview.net/pdf?id=BJJsrmfCZ)
* [PyTorch: an imperative style, high-performance deep learning library NIPS 2019](https://dl.acm.org/doi/10.5555/3454287.3455008)

[PyTorch Distributed Overview](https://pytorch.org/tutorials/beginner/dist_overview.html): `torch.distributed`
* Distributed Data-Parallel Training (DDP) is a widely adopted single-program multiple-data training paradigm. With DDP, the model is replicated on every process, and every model replica will be fed with a different set of input data samples. DDP takes care of gradient communiation to keep model replicas synchronized and overlaps it with the gradient computations to speed up training.
* RPC-Based Distributed Training (RPC) supports general training structures that cannot fit into data-parallel training such as distributed pipeline parallelism, parameters server paradigm, and combinations of DDP with other training paradigms. It helps manage remote object lifetime and extends the autograd engine beyond machine boundaries.
* Collective Communication (c10d) library supports sending tensors across processes within a group. It offers both collective communication APIs (e.g., all_reduce and all_gather) and P2P communication APIs (e.g., send and isend). DDP and RPC (ProcessGroup Backend) are built on c10d, where the former uses collective communications and the latter uses P2P communications. Usually, developers do not need to directly use this raw communication API, as the DDP and RPC APIs can serve many distributed training scenarios. However, there are use cases where this API is still helpful. One example would be distributed parameter averaging, where applications would like to compute the average values of all model parameters after the backward pass instead of using DDP to communicate gradients. This can decouple communications from computations and allow finer-grain control over what to communicate, but on the other hand, it also gives up the performance optimizations offered by DDP. Writing Distributed Applications with PyTorch shows examples of using c10d communication APIs.

[Distributed and Parallel Training Tutorials](https://pytorch.org/tutorials/distributed/home.html):
* Distributed Data Parallel (DDP)
* Fully Sharded Data Parallel (FSDP)
* Device Mesh
* Remote Procedure Call (RPC) distributed training
* Custom Extensions

[Distributed Communication Packages - torch.distributed](https://pytorch.org/docs/stable/distributed.html)

[Distributed Data Parallel (Single Node) | Blog (KR)](https://csm-kr.tistory.com/47)

[Distributed Data Parallel (Multi Nodes) | Blog (KR)](https://csm-kr.tistory.com/89)

## :hammer: [Caffe](https://caffe.berkeleyvision.org/) | [GitHub](https://github.com/BVLC/caffe)

Caffe is a deep learning framework made with expression, speed, and modularity in mind. It is developed by Berkeley AI Research (BAIR) and by community contributors. Yangqing Jia created the project during his PhD at UC Berkeley. Caffe is released under the BSD 2-Clause license.[Ref]

Caffe is built with CMake and Docker.

### [Caffe2](https://caffe2.ai/)

Caffe2 is now a part of PyTorch.

## :hammer: [Theano](http://www.deeplearning.net/software/theano/) | [GitHub](https://github.com/Theano/Theano) - Deprecated

Theano is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently. It can use GPUs and perform efficient symbolic differentiation.[Ref]

[MILA will stop developing Theano.](https://groups.google.com/forum/#!msg/theano-users/7Poq8BZutbY/rNCIfvAEAwAJ)

## :hammer: [CNTK](https://docs.microsoft.com/ko-kr/cognitive-toolkit/) | [GitHub](https://github.com/microsoft/CNTK) - Deprecated

The Microsoft Cognitive Toolkit (CNTK) is an open-source toolkit for commercial-grade distributed deep learning. It describes neural networks as a series of computational steps via a directed graph. CNTK allows the user to easily realize and combine popular model types such as feed-forward DNNs, convolutional neural networks (CNNs) and recurrent neural networks (RNNs/LSTMs). CNTK implements stochastic gradient descent (SGD, error backpropagation) learning with automatic differentiation and parallelization across multiple GPUs and servers.[Ref]

[CNTK is no longer actively developed.](https://docs.microsoft.com/en-us/cognitive-toolkit/releasenotes/cntk_2_7_release_notes)

### [OpenVINO](https://software.intel.com/content/www/us/en/develop/tools/openvino-toolkit.html) | [Docs](https://docs.openvinotoolkit.org/latest/index.html) | [Open Model Zoo](https://github.com/openvinotoolkit/open_model_zoo)

OpenVINO toolkit is a comprehensive toolkit for quickly developing applications and solutions that solve a variety of tasks including emulation of human vision, automatic speech recognition, natural language processing, recommendation systems, and many others. Based on latest generations of artificial neural networks, including Convolutional Neural Networks (CNNs), recurrent and attention-based networks, the toolkit extends computer vision and non-vision workloads across Intel® hardware, maximizing performance. It accelerates applications with high-performance, AI and deep learning inference deployed from edge to cloud.

### [Weights & Biases](https://wandb.ai/site)

The Weights & Biases MLOps platform helps AI developers streamline their ML workflow from end-to-end.

### [ONNX: Open Neural Network Exchange](https://onnx.ai/) | [GitHub](https://github.com/onnx/onnx) | [Model Zoo](https://github.com/onnx/models)

ONNX is an open format built to represent machine learning models. ONNX defines a common set of operators - the building blocks of machine learning and deep learning models - and a common file format to enable AI developers to use models with a variety of frameworks, tools, runtimes, and compilers.

Key Benefits:
* Interoperability: Develop in your preferred framework without worrying about downstream inferencing implications. ONNX enables you to use your preferred framework with your chosen inference engine.
* Hardware Access: ONNX makes it easier to access hardware optimizations. Use ONNX-compatible runtimes and libraries designed to maximize performance across hardware.

`Some of Computer Vision Frameworks and Libraries (OpenMMLab, and PaddlePaddle) have moved to the _ComputerVision Folder/Directory.`

`Machine Learning Frameworks and Libraries (AutoSklearn, H2Oai, SciPy, and ScikitLearn) have moved to the _MachineLearning Folder/Directory.`

`Some of Deep Learning Frameworks and Libraries (MXNet, MATLAB, PaddlePaddle, JAX, and Chain have moved to the _DeepLearning Folder/Directory.`

`Reinforcement Learning Frameworks and Libraries (Acme, Gym, Gymnasium, and KerasRL) have moved to the _ReinforcementLearning Folder/Directory.`

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
- TensorFlow Certificate Program, https://www.tensorflow.org/certificate, 2022-10-18-Tue.
- DeepLearning.AI TensorFlow Developer Professional Certificate Coursera, https://www.coursera.org/professional-certificates/tensorflow-in-practice, 2022-10-18-Tue.
- Intro to TensorFlow for Deep Learning Udacity, https://www.udacity.com/course/intro-to-tensorflow-for-deep-learning--ud187, 2022-10-18-Tue.
- Get started with tensorflow-metal, https://developer.apple.com/metal/tensorflow-plugin/, 2023-08-25-Fri.
- Set up your environment to take the TensorFlow Developer Certificate Exam, https://www.tensorflow.org/extras/cert/Setting_Up_TF_Developer_Certificate_Exam.pdf, 2023-08-25-Fri.
- Python venv: How To Create, Activate, Deactivate, And Delete, https://python.land/virtual-environments/virtualenv, 2023-08-25-Fri.
- ONNX, https://onnx.ai/, 2023-12-14-Thu.
- Nvidia Deep Learning Frameworks, https://developer.nvidia.com/deep-learning-frameworks, 2024-02-08-Thu.
- IBM Deep Learning Frameworks, https://developer.ibm.com/articles/compare-deep-learning-frameworks/, 2024-02-08-Thu.
- Caffe2, https://caffe2.ai/, 2024-02-15-Thu.
- PyTorch NIPS 2019, https://dl.acm.org/doi/10.5555/3454287.3455008, 2024-02-15-Thu.
- SciKit-Learn JMLR 2011, https://www.jmlr.org/papers/v12/pedregosa11a.html, 2024-02-15-Thu.
- PyTorch NIPS 2017, https://openreview.net/pdf?id=BJJsrmfCZ, 2024-02-15-Thu.
- Configuring your backend Keras, https://keras.io/getting_started/, 2024-02-15-Thu.
- Customizing fit() with TensorFlow Keras, https://keras.io/guides/custom_train_step_in_tensorflow/, 2024-02-15-Thu.
- Customizing fit() with PyTorch Keras, https://keras.io/guides/custom_train_step_in_torch/, 2024-02-15-Thu.
- Customizing fit() with JAX Keras, https://keras.io/guides/custom_train_step_in_jax/, 2024-02-15-Thu.
- François Chollet, https://fchollet.com/, 2024-03-04-Mon.
- Low Level Introduction GitHub, https://github.com/tensorflow/docs/blob/master/site/en/r1/guide/low_level_intro.md, 2024-03-05-Tue.
- Architecture GitHub, https://github.com/tensorflow/docs/blob/master/site/en/r1/guide/extend/architecture.md, 2024-03-05-Tue.
- What's new in TensorFlow and Keras, https://blog.tensorflow.org/2023/05/google-io-2023-whats-new-in-tensorflow-and-keras.html, 2024-03-05-Tue.
- Keras ModelCheckpoint, https://keras.io/api/callbacks/model_checkpoint/, 2024-03-27-Wed.
- PyTorch Distributed Overview, https://pytorch.org/tutorials/beginner/dist_overview.html, 2024-03-29-Fri.
- Distributed and Parallel Training Tutorials, https://pytorch.org/tutorials/distributed/home.html, 2024-03-29-Fri.
- Distributed Communication Package - torch.distributed, https://pytorch.org/docs/stable/distributed.html, 2024-03-29-Fri.
- Distributed Data Parallel Single Node Blog KR, https://csm-kr.tistory.com/47, 2024-04-01-Mon.
- Distributed Data Parallel Multi Nodes Blog KR, https://csm-kr.tistory.com/89, 2024-04-01-Mon.
- TensorBoard, 2024-04-08-Mon.
- TensorBoardX, https://tensorboardx.readthedocs.io/en/latest/tensorboard.html, 2024-04-23-Tue.
- TensorBoardX GitHub, https://github.com/lanpa/tensorboardX, 2024-04-23-Tue.
