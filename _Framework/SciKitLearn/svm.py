# Title: SVM Tutorial
# Author: Inyong Hwang
# Date: 2021-12-17-Fri.
# Reference: https://www.datacamp.com/community/tutorials/svm-classification-scikit-learn-python


from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics


cancer = datasets. load_breast_cancer()

print('Features: ', cancer.feature_names)
print('Labels: ', cancer.target_names)
print(cancer.data.shape)
print(cancer.data[0:5])
print(cancer.target)

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3, random_state=109)

clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print('Accuracy: ', metrics.accuracy_score(y_test, y_pred))
print('Precision: ', metrics.precision_score(y_test, y_pred))
print('Recall: ', metrics.recall_score(y_test, y_pred))

'''
Tuning Hyper-parameters
- Kernel: The main function of the kernel is to transform the given dataset input data into the required form. There are 
various types of functions such as linear, polynomial, and radial basis function (RBF). Polynomial and RBF are useful
for non-linear hyperplane. Polynomial and RBF kernels compute the separation line in the higher dimension. In some of
the applications, it is suggested to use a more complex kernel to separate the classes that are curved or nonlinear.
This transformation can lead to more accurate classifiers.
- Regularization: Regularization parameter in python's scikit-learn C parameter used to maintain regularization. Here
C is the penalty parameter, which represents miss-classification or error term. The miss-classification or error term 
tells the SVM optimization how mush error os bearable. This is how you can control the trade-off between decision 
boundary and miss-classification term. A smaller value of C creates a small-margin hyperplane and a larger value or C
creates a larger-margin hyperplane.
- Gamma: A lower value of Gamma will loosely fit the training dataset, whereas a higher value of gamma will exactly fit
the training dataset, which causes over-fitting. In other words, you can say a low value of gamma considers only nearby
points in calculating the separation line, while the a value of gamma considers all the data points in the calculation
of the separation line.

Advantages
SVM Classifier offer good accuracy and perform faster prediction compared to Naive Bayes algorithm. They also use less
memory because they use a subset of training points in the decision phase. SVM works well with a clear margin of
separation and with high dimensional space.

Disadvantage
SVM is not suitable for large datasets because of its high training time and it also takes more time in training 
compared to Naive Bayes. It works poorly with overlapping classes and is also sensitive to the type of kernel used. 
'''
