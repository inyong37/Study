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

* Padding using Numpy

```Python
array_padded_1_dim = np.pad(array_org_1dim, (int(left), int(right), 'constant', constant_values=0)
array_padded_2_dim = np.pad(array_org_2dim, ((int(up), int(down)), (int(left), int(right)), 'constant', constant_values=0)
```
* Normalize

```Python
audio_norm = np.max(np.abs(audio_org), axis=0) # Audio Org: -1 ~ +1
image_norm = image_org * 255./image_org.max()  # Image Org: 0 ~ 255
```

---

### Reference
- Make a Same Size Numpy Array, Stackoverflow, https://stackoverflow.com/questions/35967907/how-to-make-a-new-numpy-array-same-size-as-a-given-array-and-fill-it-with-a-scal, 2023-08-22-Tue.
- Numpy Calculation Blog KR, https://eunguru.tistory.com/215, 2023-08-22-Tue.
- tf.keras.layers.Bidirectional, https://www.tensorflow.org/api_docs/python/tf/keras/layers/Bidirectional, 2023-08-22-Tue.
- tf.keras.losses.BinaryCrossentropy, https://www.tensorflow.org/api_docs/python/tf/keras/losses/BinaryCrossentropy, 2023-08-22-Tue.
- tf.keras.optimizers.Adam, https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adam, 2023-08-22-Tue.
- np.pad Blog KR, https://m.blog.naver.com/wideeyed/221665256911, 2023-08-23-Wed.
- np.pad to images Blog KR, https://hanstar4.tistory.com/19, 2023-08-23-Wed.
- Normalize Stackoverflow, https://stackoverflow.com/questions/1735025/how-to-normalize-a-numpy-array-to-within-a-certain-range, 2023-08-23-Wed.
