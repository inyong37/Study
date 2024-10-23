# Grid Search Cross Validation

Exhaustive search over specified parameter values for an estimator. Important members are fit, predict. GridSearchCV implements a "fit" and a "score" method. It also implements "score_samples", "predict", "predict_proba", "decision_function", "transform" and "inverse_transform" if they are implemented in the estimator used. The parameters of the estimator used to apply these methods are optimized by cross-validated grid-search over a parameter grid.

# Randomized Search Cross Validation

Randomized search on hyper parameters. RandomizedSearchCV implements a "fit" and a "score" method. It also implements "score_samples", "predict", "predict_proba", "decision_function", "transform" and "inverse_transform" if they are implemented in the estimator used. The parameters of the estimator used to apply these methods are optimized by cross-validated search over parameter settings. In contrast to GridSearchCV, not all parameter values are tried out, but rather a fixed number of parameter settings is sampled from the specified distributions. The number of parameter settings that are tried is given by n_iter. If all parameteres are presented as a list, sampling without replacement is performed. If at least one parameter is given as a distribution, sampling with replacement is used. It is highly recommended to use continuous distributions for continuous parameters.

---

### Reference
- Grid Search, https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html, 2024-10-23-Wed.
- Randomized Search, https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html, 2024-10-23-Wed.
