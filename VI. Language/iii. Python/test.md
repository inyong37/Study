# Test

### [doctest](https://docs.python.org/3.7/library/doctest.html)

The doctest module searches for pieces of next that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. There are several common ways to use doctest:

* To check that a module's docstrings are up-to-date by verifying that all interactive examples still work as documented.
* To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
* To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of "literate testing" or "executable documentation". `python test.py -v`

### [pytest](https://docs.pytest.org/en/8.2.x/)

The pytest framework makes it easy to write small, readable tests, and can sacle to support complex functional testing for applications and libraries. pytest requires: Python 3.8+ or PyPy3. `pytest {test_directory}`

### [unittest](https://docs.python.org/3/library/unittest.html)

The unittest unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.

[pytest vs unittest](https://www.browserstack.com/guide/pytest-vs-unittest)

## TensorFlow

[tensorflow/python/framework/test_util.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/framework/test_util.py)

## PyTorch

[torch/testing/_internal/common_utils.py](https://github.com/pytorch/pytorch/blob/main/torch/testing/_internal/common_utils.py)

## Ray

[python/ray/tests/test_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/tests/test_utils.py)

---

### Reference
- pytest, https://docs.pytest.org/en/stable/, 2021-02-15-Mon.
- doctest, https://docs.python.org/3.7/library/doctest.html, 2021-03-19-Fri.
- unittest, https://docs.python.org/3/library/unittest.html, 2024-06-19-Wed.
- pytest vs unittest, https://www.browserstack.com/guide/pytest-vs-unittest, 2024-07-09-Tue.
- torch/testing/_internal/common_utils.py, https://github.com/pytorch/pytorch/blob/main/torch/testing/_internal/common_utils.py, 2024-07-09-Tue.
- expecttest, https://github.com/ezyang/expecttest, 2024-07-09-Tue.
- tensorflow/python/framework/test_util.py, https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/framework/test_util.py, 2024-07-09-Tue.
- python/ray/tests/test_utils.py, https://github.com/ray-project/ray/blob/master/python/ray/tests/test_utils.py, 2024-07-09-Tue.
