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

---

### Reference
- PyTorch vs TensorFlow 2023, https://www.assemblyai.com/blog/pytorch-vs-tensorflow-in-2023/, 2023-12-14-Thu.
- PyTorch vs PyTorch Lightning, https://towardsdatascience.com/from-pytorch-to-pytorch-lightning-a-gentle-introduction-b371b7caaf09, 2024-02-03-Sat.
