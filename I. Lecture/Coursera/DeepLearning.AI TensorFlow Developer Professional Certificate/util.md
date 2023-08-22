## Keras

* `tf.keras.layers.Bidirectional`

```Python
tf.keras.layers.Bidirectional(
    layer,
    merge_mode='concat',
    weights=None,
    backward_layer=None,
    **kwargs
)
```

* `tf.keras.losses.BinaryCrossEntropy`

```Python
tf.keras.losses.BinaryCrossentropy(
    from_logits=False,
    label_smoothing=0.0,
    axis=-1,
    reduction=losses_utils.ReductionV2.AUTO,
    name='binary_crossentropy'
)
```

* `tf.keras.optimizers.Adam`

```Python
tf.keras.optimizers.Adam(
    learning_rate=0.001,
    beta_1=0.9,
    beta_2=0.999,
    epsilon=1e-07,
    amsgrad=False,
    weight_decay=None,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    jit_compile=True,
    name='Adam',
    **kwargs
)
```

## Util

* Make a Same Size Numpy Array

```Python
array_new = np.full_like(array_org, 1)
```

```Python
array_new = np.ones_like(array_org)
```

* Numpy Calculation

```Python
# Add
array_a = array_foo + array_bar
array_b = np.add(array_foo, array_bar)
# array_a == array_b

# Subtract
array_a = array_foo - array_bar
array_b = np.subtract(array_foo, array_bar)
# array_a == array_b

# Multiply
array_a = array_foo * array_bar
array_b = np.multiply(array_foo, array_bar)
# array_a == array_b

# Divide
array_a = array_foo / array_bar
array_b = np.divide(array_foo, array_bar)
# array_a == array_b
```

* Remove Stop Words

```Python
words = line.split()
words_without_stop_words = [word for word in words if word not in stop_words]
line = " ".join(words_without_stop_words)
```

---

### Reference
- Make a Same Size Numpy Array, Stackoverflow, https://stackoverflow.com/questions/35967907/how-to-make-a-new-numpy-array-same-size-as-a-given-array-and-fill-it-with-a-scal, 2023-08-22-Tue.
- Numpy Calculation Blog KR, https://eunguru.tistory.com/215, 2023-08-22-Tue.
- tf.keras.layers.Bidirectional, https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional, 2023-08-22-Tue.
- tf.keras.losses.BinaryCrossentropy, https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryCrossentropy, 2023-08-22-Tue.
- tf.keras.optimizers.Adam, https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adam, 2023-08-22-Tue.
