# Machine Learning

---

# :hammer_and_wrench: Frameworks and Libraries :books:

## :hammer_and_wrench: [auto-sklearn](https://automl.github.io/auto-sklearn/master/) | [GitHub](https://github.com/automl/auto-sklearn)

auto-sklearn is an automated machine learning toolkit and a drop-in replacement for a scikit-learn estimator.

## :hammer_and_wrench: [H2O.ai](https://h2o.ai/) | [GitHub](https://github.com/h2oai)

## :hammer_and_wrench: [SciPy](https://scipy.org/) | [GitHub](https://github.com/scipy/scipy)

Fundamental algorithms for scientific computing in Python.

## :hammer_and_wrench:  [Scikit-learn](https://scikit-learn.org/stable/): Machine Learning in Python | [GitHub](https://github.com/scikit-learn/scikit-learn)

- Simple and efficient tools for perdictive data analysis
- Accessible to everybody, and reusable in various contexts
- Built on NumPy, SciPy, and matplotlib
- Open source, commercially usable - BSD license

scikit-learn is a Python module for machine learning built on top of SciPy and is distributed under the 3-Clause BSD license. The project was started in 2007 by David Cournapeau as a Google Summer of Code project, and since then many volunteers have contributed. It is currently maintained by a team of volunteers.

[[2011] Scikit-learn: Machine Learning in Python (JMLR)](https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html)

### [I. Classification](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)

Identifying which category an object belongs to.

Applications: Spam detections, image recognition.

Algorithms: Gradient boosting, [nearest neighbors](https://scikit-learn.org/stable/modules/neighbors.html), [random forest](https://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees), logistic regression, [SVM](https://scikit-learn.org/stable/modules/svm.html), and more...

### [II. Regression](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)

Prediciton a continuous-valued atttribute assicated with an object.

Applications: Drug response, Stock prices.

Algorithms: Gradient boosting, [nearest neighbors](https://scikit-learn.org/stable/modules/neighbors.html), [random forest](https://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees), ridege, SVR, and more...

### [III. Clustering](https://scikit-learn.org/stable/modules/clustering.html#clustering)

Automatic grouping of similar objects into sets.

Applications: Customer segmentation, Grouping experiment outcomes.

Algorithms: k-Means, HDBSCAN, hierarchical clustering, spectral clustering, mean-shift, and more...

### [IV. Dimensionality reduction](https://scikit-learn.org/stable/modules/decomposition.html)

Reducing the number of random variables to consider.

Applications: Visualization, Increased efficiency.

Algorithms: PCA, feature selection, non-negative matrix factorization, and more...

### [V. Model selection](https://scikit-learn.org/stable/model_selection.html)

Comparing, validating, and choosing parameters and models.

Applications: Improved accuracy via parameter tuning.

Algorithms: grid search, cross validation, metrics, and more...

### [VI. Preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)

Feature extraction and normalization.

Applications: Transforming input data such as text for use with machine learning algorithms.

Algorithms: preprocessing, feature extraction, and more...

### [1. Supervised learning](https://scikit-learn.org/stable/supervised_learning.html)

1. Linear Models
2. Linear and Quadratic Discriminant Analysis
3. Kernel ridge regression
4. Support Vector Machines
5. Stochastic Gradient Descent
6. Nearest Neighbors
7. Gaussian Processes
8. Cross decomposition
9. Naive Bayes
10. Decision Trees
11. Ensembles: Gradient boosting, random forests, bagging, voting, stacking
12. Multiclass and multioutput algorithms
13. Feature selection
14. Semi-supervised learning
15. Isotonic regression
16. Probability calibration
17. Neural network models (supervised)

### [2. Unsupervised learning](https://scikit-learn.org/stable/unsupervised_learning.html)

1. Gaussian mixture models
2. Manifold learning
3. Clustering < [III. Clustering](https://scikit-learn.org/stable/modules/clustering.html#clustering)
4. Biclustering
5. Decomposing signals in components (matrix factorization problems) < [IV. Dimensionality reduction](https://scikit-learn.org/stable/modules/decomposition.html)
6. Covariance estimation
7. Novelty and Outlier Detection
8. Density Estimation
9. Neural network models (unsupervised)

## :hammer_and_wrench: [XGBoost](https://xgboost.readthedocs.io/en/stable/)

XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. It implements machine learning algorithms under the Gradient Boosting framework. XGBoost provides a parallel tree boosting (also known as GBDT, GBM) that solve many data science problems in a fast and accurate way. The same code runs on major distributed environment (Hadoop, SGE, MPI) and can solve problems beyond billions of examples.

## :hammer_and_wrench: [CatBoost](https://catboost.ai/)

CatBoost is a high-performance open source library for gradient boosting on decision trees..

Features:
1. Great quality without parameter tuning: Reduce time spent on parameter tuning, because CatBoost provides great results with default parameters.
2. Categorical features support: Improve your training results with CatBoost that allows you to use non-numeric factors, instead of having to pre-process your data or spend time and effort turning it to numbers.
3. Fast and scalable GPU version: Train your model on a fast implementation of gradient-boosting algorithm for GPU. Use a multi-card configuration for large datasets.
4. Improved accuracy: Reduce overfitting when constructing your models with a novel gradient-boosting scheme.
5. Fast prediction: Apply your trained model quickly and efficiently even to latency-critical tasks using CatBoost's model applier.

## :hammer_and_wrench: [LightGBM](https://lightgbm.readthedocs.io/en/stable/)

LightGBM is a gradient boosting framework that uses tree based learning algorithms. It is designed to be distributed and efficient with the following advantages:
* Faster training speed and higher efficiency.
* Lower memory usage.
* Better accuracy.
* Support of parallel, distributed, and GPU learning.
* Capable of handling large-scale data.

## :hammer_and_wrench: [Prophet](https://facebook.github.io/prophet/)

Prophet is a forecasting procedure implemented in R and Python. It is fast and provides completely automated forecasts that can be tuned by hand by data scientists and analysts.

# Tunning

## :hammer_and_wrench: [Ray Tune](https://docs.ray.io/en/latest/tune/index.html)

Tune is a Python library for experiment execution and hyperparameter tuning at any scale. You can tune your favorite machine learning framework (PyTorch, XGBoost, TensorFlow and Keras, and more) by running state of the art algorithms. Tune further integrates with a wide range of additional hyperparameter optimization tools, including Ax, BayesOpt, BOHB, Nevergrad, and Optuna.

## :hammer_and_wrench: [Hyperopt](https://hyperopt.github.io/hyperopt/) | [GitHub](https://github.com/hyperopt/hyperopt)

Hyperopt is a Python library for serial and parallel optimization over awkward search spaces, which may include real-valued, discrete, and conditional dimensions.

---

### Reference
- scikit-learn, https://scikit-learn.org/stable/, 2021-12-17-Fri.
- Supervised Learning, https://scikit-learn.org/stable/supervised_learning.html#supervised-learning, 2021-12-17-Fri.
- Support Vector Machines, https://scikit-learn.org/stable/modules/svm.html, 2021-12-17-Fri.
- Nearest Neighors, https://scikit-learn.org/stable/modules/neighbors.html, 2021-12-17-Fri.
- Random Forests, https://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees, 2021-12-17-Fri.
- Clustering, https://scikit-learn.org/stable/modules/clustering.html#clustering, 2021-12-17-Fri.
- scikit-learn GitHub, https://github.com/scikit-learn/scikit-learn, 2024-02-02-Fri.
- Supervised learning, https://scikit-learn.org/stable/supervised_learning.html, 2024-02-02-Fri.
- Unsupervised learning, https://scikit-learn.org/stable/unsupervised_learning.html, 2024-02-02-Fri.
- auto-sklearn, https://automl.github.io/auto-sklearn/master/, 2024-02-28-Wed.
- auto-sklearn GitHub, https://github.com/automl/auto-sklearn, 2024-02-28-Wed.
- H2O.ai, https://h2o.ai/, 2024-02-28-Wed.
- H2O.ai GitHub, https://github.com/h2oai, 2024-02-28-Wed.
- SciPy, https://scipy.org/, 2024-02-28-Wed.
- SciPy GitHub, https://github.com/scipy/scipy, 2024-02-28-Wed.
- XGBoost, https://xgboost.readthedocs.io/en/stable/, 2024-10-22-Tue.
- CatBoost, https://catboost.ai/, 2024-10-22-Tue.
- LightGBM, https://lightgbm.readthedocs.io/en/stable/, 2024-10-22-Tue.
- Prophet, https://facebook.github.io/prophet/, 2024-10-31-Thu.
- Ray Tune, https://docs.ray.io/en/latest/tune/index.html, 2024-10-31-Thu.
- Hyperopt, https://hyperopt.github.io/hyperopt/, 2024-10-31-Thu.
- Hyperopt GitHub, https://github.com/hyperopt/hyperopt, 2024-10-31-Thu.
