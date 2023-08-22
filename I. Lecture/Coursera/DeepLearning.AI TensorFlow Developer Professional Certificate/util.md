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

---

### Reference
- Make a Same Size Numpy Array, Stackoverflow, https://stackoverflow.com/questions/35967907/how-to-make-a-new-numpy-array-same-size-as-a-given-array-and-fill-it-with-a-scal, 2023-08-22-Tue.
- Numpy Calculation Blog KR, https://eunguru.tistory.com/215, 2023-08-22-Tue.
