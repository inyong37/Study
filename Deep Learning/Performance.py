from keras import backend as k

'''
# Function
k.clip(x=, min_value=, max_value=)
: Sharpen the edges except the max and min values.
k.round(x=)
: Rounds x.
'''
'''
# Table
-----------------------------------------------------
|                   |                          Real |
|                   ---------------------------------
|                   |      Positive |      Negative |
-----------------------------------------------------
|Prediction|Positive|  True Positive| False Positive|
|          |Negative| False Negative|  True Negative|
-----------------------------------------------------
'''
'''
# Value
True = True Positive + True Negative
Real Positive = True Positive + False Negative
Prediction Positive = True Positive + False Positive
All = True Positive + False Positive + False Negative + True Negative

Recall(Sensitivity)
= True Positive / Real Positive
= True Positive / (True Positive + False Negative)
Precision(Positive Predictive Value, PPV)
= True Positive / Prediction Positive
= True Positive / (Ture Positive + False Positive)
Accuracy
= True / All
= (True Positive + True Negative) / (True Positive + False Positive + False Negative + True Negative) 
True Negative(Specificity)
= True Negative / True
= True Negative / (True Positive + True Negative)
F Measure
= 1 / {a * (1 / precision) + (1 - a) * (1 / recall)}
= {(b^2 + 1) * precision * recall} / {(b^2) * precision + recall}
F1 Score(F1 Measure)
= (precision * recall) / (precision + recall)
'''


def func_recall(y_target, y_pred):
    y_target = k.round(k.clip(y_target, 0, 1))
    y_pred = k.round(k.clip(y_pred, 0, 1))
    tp = k.sum(y_target * y_pred)
    rp = k.sum(y_target)
    value = tp / (rp + k.epsilon())
    return value


def func_precision(y_target, y_pred):
    y_target = k.round(k.clip(y_target, 0, 1))
    y_pred = k.round(k.clip(y_pred, 0, 1))
    tp = k.sum(y_target * y_pred)
    rp = k.sum(y_pred)
    value = tp / (rp + k.epsilon())
    return value


def f1score(y_target, y_pred):
    _recall = func_recall(y_target, y_pred)
    _precision = func_precision(y_target, y_pred)
    value = (2 * _recall * _precision) / (_recall + _precision + k.epsilon())
    return value
