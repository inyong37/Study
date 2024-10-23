# Cross Validation: evaluating estimator performance

Learning the parameters of a prediction function and testing it on the same data is a methodological mistake: a model that would just repeat the labels of the samples that it has just seen would have a perfect score but would fail to predict anything useful on yet-unseen data. This situation is called overfitting. To avoid it, it is common practice when performing a (supervised) machine learning experiment to hold out part of the available data as a test set X_test, y_test. Note that the word "experiment" is not intended to denote academic use only, because even in commercial settings machine learning usually starts out experimentally.

# KFold

K-Fold cross-validator provides train/test indices to split data in train/test sets. Split dataset into K consecutive folds (without shuffling by default). Each fold is then used once as a validation while the k-1 remaining folds form the training set.

```Python
from sklearn.model_selection import KFold
kf = KFold(n_splits=2)
kf.get_n_splits(X)
```

---

### Reference
- Cross Validation, https://scikit-learn.org/stable/modules/cross_validation.html, 2024-10-23-Wed.
- KFold, https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html, 2024-10-23-Wed.
