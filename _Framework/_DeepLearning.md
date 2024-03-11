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
