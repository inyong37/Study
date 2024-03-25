# Deep Learning

:bulb: My Definition of Deep Learning Framework and Library is a framework gives constraints and a guidance to developers, and in DL, to build a model, a developer needs to use some model and layer classes. It makes a code to subordinated to a library. Therefore, a DL library can be a DL framework also in many cases.

:bulb: I separate frameworks/libraries as three layers: top, middle, and bottom layer. The first top layer is the highest APIs such as callbacks, functions, optimizers, and losses. The second middle layer is the building models block such as models, and layers. The last bottom layer is a engine that can train the models as forwarding and back-propagation the values.

:key: So, the TensorFlow can cover all three layers, but specialize in bottle layer as a neural network engine. Keras uses TensorFlow, PyTorch, or JAX as a backend, so it can be regarded as frontend which covers middle and top layers. PyTorch also can cover all three but, is specialized in bottle and middle layer. However, PyTorch lightning only covers top layer. JAX fits to only bottle layers, and Flax and Haiku cover middle and top layers.

|Name|NN Engine|Model Building Modules|Extended Training Features|
|:--:|:-------:|:--------------------:|:------------------------:|
|TensorFlow1|O|O|O|
|TensorFlow2|O|Keras|O|
|Keras|TensorFlow, ~~Theano~~, PyTorch, JAX|O|O|
|PyTorch|O|O|O|
|Lightning|PyTorch|PyTorch|O|
|JAX|O|O|O|
|Flax|JAX|O|O|
|Haiku|JAX|O|O|

Caffe, CNTK, MXNet, Chainer, OpenVINO, ONNX

---

# :hammer_and_wrench: Frameworks and Libraries :books:

## :hammer_and_wrench: [Chainer](https://chainer.org/) | [GitHub](https://github.com/chainer/chainer)

A flexible framework of neural networks for deep learning.

* Modeling Blocks:
  * [chainer/links](https://github.com/chainer/chainer/tree/master/chainer/links)

### :books: ChainerCV | [GitHub](https://github.com/chainer/chainercv)

ChainerCV: a Library for Deep Learning in Computer Vision

This repository has been archived by the owner on Jul 2, 2021. It is now read-only.

### :books: ChainerRL | [GitHub](https://github.com/chainer/chainerrl)

ChainerRL is a deep reinforcement learning library built on top of Chainer.

## :hammer_and_wrench: HuggingFace

### :books: [timm (PyTorch Image Models)](https://huggingface.co/timm) | [GitHub](https://github.com/huggingface/pytorch-image-models)

PyTorch Image Models (timm) is a collection of image models, layers, utilities, optimizers, schedulers, data-loaders / augmentations, and reference training / validation scripts that aim to pull together a wide variety of SOTA models with ability to reproduce ImageNet training results.

### :books: [Transformers](https://huggingface.co/docs/transformers/en/index) | [GitHub](https://github.com/huggingface/transformers)

State-of-the-art Machine Learning for PyTorch, TensorFlow, and JAX.

Transformers provides APIs and tools to easily download and train state-of-the-art pretrained models. Using pretrained models can reduce your compute costs, carbon footprint, and save you the time and resources required to train a model from scratch. These models support common tasks in different modalities, such as:

* Natural Language Processing: text classification, named entity recognition, question answering, language modeling, summarization, translation, multiple choice, and test generation.
* Computer Vision: image classification, object detection, and segmentation.
* Audio: automatic speech recognition and audio classification.
* Multimodal: table question answering, optical character recognition, information extraction from scanned documents, video classification, and visual question answering.

Transformers support framework interoperability between PyTorch, TensorFlow, and JAX. This proivdes the flexibility to use a different framework at each stage of a model's life; train a model in three lines of code in one framework, and load it for inference in another. Models can also be exported to a format like ONNX and TorchScript for deployment in production environments.

## :hammer_and_wrench: JAX | [GitHub](https://github.com/google/jax) | Google

JAX is Autograd and XLA, brought together for high-performance numerical computing, including large-scale machine learning research.

* Modeling Blocks:
  * [stax](https://github.com/google/jax/blob/main/jax/example_libraries/stax.py)

### :books: [Flax](https://flax.readthedocs.io/en/latest/) | [GitHub](https://github.com/google/flax) | Google

Flax is a neural network library for JAX that is designed for flexibility.

* Modeling Blocks:
  * [flax/core/nn](https://github.com/google/flax/tree/main/flax/core/nn)

### :books: [Haiku](https://dm-haiku.readthedocs.io/en/latest/) | [GitHub](https://github.com/google-deepmind/dm-haiku) | DeepMind

JAX-based neural network library

* Modeling Blocks:
  * [haiku/_src](https://github.com/google-deepmind/dm-haiku/tree/main/haiku/_src)

## :hammer_and_wrench: [MXNet](https://mxnet.apache.org/versions/1.9.0/) | Apache | [Attic](https://attic.apache.org/projects/mxnet.html) - Deprecated

MXNet is a DL framework designed for both efficiency and flexibility. It allows you to mix the flavors of symbolic programming and imperative programming to maximize efficiency and productivity.

At its core is a dynamic dependency scheduler that automatically parallelizes both symbolic and imperative operations on-the-fly. A graph optimization layer on top of that makes symbolic execution fast and memory efficient. The library is portable and lightweight, and it scales to multiple GPUs and machines.

This project has retired. Apache MXNet moved into the Attic in 2023-09.

## :hammer_and_wrench: [MATLAB](https://www.mathworks.com/products/matlab.html)

MATLAB makes DL easy for engineers, scientists, and domain experts. With tools and functions for managing and labeling large data sets, MATLAB also offers specialized toolboxes for working with machine learning, neural networks, computer vision, and automated driving. With just a few lines of code, MATLAB allows you to create and visualize models, and deploy models to servers and embedded devices without being an expert. MATLAB also enables users to automatically generate high performance CUDA code for DL and vision applications from MATLAB code.

## :hammer_and_wrench: PyTorch

### :books: [PyTorch Ignite](https://pytorch-ignite.ai/) | [GitHub](https://github.com/pytorch/ignite)

High-level library to help with training and evaluating neural networks in PyTorch flexibly and transparently.

### :books: [fastai](https://docs.fast.ai/)

fastai simplifies training fast and accurate neural nets using modern best practices.

### :books: [PyTorch Lightning](https://lightning.ai/docs/pytorch/stable/) | [GitHub](https://github.com/Lightning-AI/pytorch-lightning)

PyTorch Lightning is the deep learning framework for professional AI researchers and machine learning engineers who need maximal flexibility without sacrificing performance at scale. Lightning evolves with you as your projects go from idea to paper/production.

* [trainer.py](https://github.com/Lightning-AI/pytorch-lightning/blob/master/src/lightning/pytorch/trainer/trainer.py):
  * fit: Runs the full optimization routine.
  * validate: Perform one evaluation epoch over the validation set.
  * test: Perform one evaluation epoch over the test set. It's separated from fit to make sure you never run on your test set until you want to.
  * predict: Run inference on your data. This will call the model forward function to compute predictions. Useful to perform distributed and batched predictions. Logging is disabled in the predict hooks.
* [Callbacks](https://lightning.ai/docs/pytorch/stable/extensions/callbacks.html):
  * BackboneFinetuning
  * BaseFinetuning
  * BasePredictionWriter
  * BatchSizeFinder
  * Callback
  * DeviceStatsMonitor
  * EarlyStopping
  * GradientAccumulationScheduler
  * LambdaCallback
  * LearningRateFinder
  * LearningRateMonitor
  * ModelCheckpoint
  * ModelPruning
  * ModelSummary
  * ProgressBar
  * RichModelSummary
  * RichProgressBar
  * StochasticWeightAveraging
  * Timer
  * TQDMProgressBar
* [Accelerator](https://lightning.ai/docs/pytorch/stable/extensions/accelerator.html):
  * Accelerator
  * CPUAccelerator
  * CUDAAccelerator
  * MPSAccelerator
  * XLAAccelerator
* [Strategy](https://lightning.ai/docs/pytorch/stable/extensions/strategy.html)

* [PyTorch Lightning Tutorials (University of Amsterdam)](https://lightning.ai/docs/pytorch/stable/tutorials.html)
  * [Tutorial 1: Introduction to PyTorch](https://lightning.ai/docs/pytorch/stable/notebooks/course_UvA-DL/01-introduction-to-pytorch.html)
  * [Tutorial 2: Activation Functions](https://lightning.ai/docs/pytorch/stable/notebooks/course_UvA-DL/02-activation-functions.html) - Sigmoid, Tanh, ReLU, LeakyReLU, ELU, Swish
  * [Tutorial 3: Initialization and Optimization](https://lightning.ai/docs/pytorch/stable/notebooks/course_UvA-DL/03-initialization-and-optimization.html) - xavier, kaiming, and SGD, SGDMomentum, Adam
  * [Tutorial 4: Inception, ResNet and DenseNet](https://lightning.ai/docs/pytorch/stable/notebooks/course_UvA-DL/04-inception-resnet-densenet.html)
  * [Tutorial 5: Transformers and Multi-Head Attention](https://lightning.ai/docs/pytorch/stable/notebooks/course_UvA-DL/05-transformers-and-MH-attention.html)
  * [Tutorial 6: Basics of Graph Neural Networks](https://lightning.ai/docs/pytorch/stable/notebooks/course_UvA-DL/06-graph-neural-networks.html)
  * [Tutorial 7: Deep Energy-Based Generative Models](https://lightning.ai/docs/pytorch/stable/notebooks/course_UvA-DL/07-deep-energy-based-generative-models.html)
  * [Tutorial 8: Deep Autoencoders](https://lightning.ai/docs/pytorch/stable/notebooks/course_UvA-DL/08-deep-autoencoders.html)
  * [Tutorial 9: Normalizing Flows for image Modeling](https://lightning.ai/docs/pytorch/stable/notebooks/course_UvA-DL/09-normalizing-flows.html)
  * [Tutorial 10: Autoregressive Image Modeling](https://lightning.ai/docs/pytorch/stable/notebooks/course_UvA-DL/10-autoregressive-image-modeling.html)
  * [Tutorial 11: Vision Transformers](https://lightning.ai/docs/pytorch/stable/notebooks/course_UvA-DL/11-vision-transformer.html)
  * [PyTorch Lightning CIFAR10 ~94% Baseline Tutorial](https://lightning.ai/docs/pytorch/stable/notebooks/lightning_examples/cifar10-baseline.html)
  * [PyTorch Lightning DataModules](https://lightning.ai/docs/pytorch/stable/notebooks/lightning_examples/datamodules.html)
  * [Fine-Tuning Scheduler](https://lightning.ai/docs/pytorch/stable/notebooks/lightning_examples/finetuning-scheduler.html)

---

## Comparison

[PyTorch vs TensorFlow 2023](https://www.assemblyai.com/blog/pytorch-vs-tensorflow-in-2023/)
1. Model Availability: With the domain of Deep Learning expanding every year and models becoming bigger in turn, training State-of-the-Art (SOTA) models from scratch is simply not feasible anymore. There are fortunately SOTA models publicly available, and it is important to utilize them where possible.
2. Deployment Infrastructure: Training well-performing models is pointless if they can't be put to use. Lowering time-to-deploy is paramount, especially with the growing popularity of microservice business models; and efficient deployment has the potential to make-or-break many business that center on Machine Learning.
3. Ecosystems: No longer is Deep Learning relegated to specific use cases in highly contrlled environments. AI is injecting new power into a litany of industries, so a framework that sits within a larger ecosystem which facilitates development for mobile, local, and server applications is important. Also, the advent of specialized Machine Learning hardware, such as Google's Edge TPU, means that successful practitioners need to work with a framework that can integrate well with this hardware.
* What if I'm in Industry?: TensorFlow
* What if I'm a Researcher?: PyTorch
* What if I'm a Professor?: TensorFlow and/or PyTorch
* What if I'm a Hobbyist?: TensorFlow or PyTorch
* What if I'm a Total Beginner?: Keras-TensorFlow-PyTorch

[PyTorch vs PyTorch Lightning](https://towardsdatascience.com/from-pytorch-to-pytorch-lightning-a-gentle-introduction-b371b7caaf09)

[2024 Jax vs. PyTorch](https://www.newhorizons.com/resources/blog/jax-vs-pytorch-comparing-two-deep-learning-frameworks)

---

### Reference
- fastai, https://docs.fast.ai/, 2022-01-15-Sat.
- PyTorch vs TensorFlow 2023, https://www.assemblyai.com/blog/pytorch-vs-tensorflow-in-2023/, 2023-12-14-Thu.
- PyTorch vs PyTorch Lightning, https://towardsdatascience.com/from-pytorch-to-pytorch-lightning-a-gentle-introduction-b371b7caaf09, 2024-02-03-Sat.
- MATLAB, https://www.mathworks.com/products/matlab.html, 2024-02-08-Thu.
- Apache MXNet, https://mxnet.apache.org/versions/1.9.0/, 2024-02-08-Thu.
- Apache MXNet Attic, https://attic.apache.org/, 2024-02-08-Thu.
- PyTorch Lightning GitHub, https://github.com/Lightning-AI/pytorch-lightning, 2024-02-15-Thu.
- JAX GitHub, https://github.com/google/jax, 2024-02-20-Tue.
- JAX vs PyTorch, https://www.newhorizons.com/resources/blog/jax-vs-pytorch-comparing-two-deep-learning-frameworks, 2024-02-02-Tue.
- HuggingFace Transformers, https://huggingface.co/docs/transformers/en/index, 2024-02-14-Wed.
- HuggingFace Transformers GitHub, https://github.com/huggingface/transformers, 2024-02-14-Wed.
- Flax, https://flax.readthedocs.io/en/latest/, 2024-02-20-Tue.
- Flax GitHub, https://github.com/google/flax, 2024-02-20-Tue.
- Haiku, https://dm-haiku.readthedocs.io/en/latest/, 2024-02-20-Tue.
- Haiku GitHub, https://github.com/google-deepmind/dm-haiku, 2024-02-20-Tue.
- Haiku Modeling Blocks, haiku/_src](https://github.com/google-deepmind/dm-haiku/tree/main/haiku/_src, 2024-02-20-Tue.
- Chainer, https://chainer.org/, 2024-02-22-Thu.
- Chainer GitHub, https://github.com/chainer/chainer, 2024-02-22-Thu.
- ChainerCV GitHub, https://github.com/chainer/chainercv, 2024-02-22-Thu.
- ChainerRL GitHub, https://github.com/chainer/chainerrl, 2024-02-22-Thu.
- PyTorch Ignite, https://pytorch-ignite.ai/, 2024-02-25-Sun.
- PyTorch Ignite GitHub, https://github.com/pytorch/ignite, 2024-02-25-Sun.
- HuggingFace timm, https://huggingface.co/timm, 2024-02-27-Tue.
- PyTorch Image Models GitHub, https://github.com/huggingface/pytorch-image-models, 2024-02-27-Tue.
- PyTorch Lightning Tutorials, https://lightning.ai/docs/pytorch/stable/tutorials.html, 2024-03-25-Mon.
