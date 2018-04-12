# Binary Classification with Sonar Dataset: Baseline

# Listing 11.1: Import Classes and Functions.
import numpy
import pandas
from keras.models import Sequential
from keras.layers import  Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import  StandardScaler
from sklearn.pipeline import Pipeline

# Listing 11.2: Initialize The Random Number Generator.
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

# Listing 11.3: Load The Dataset And Separate Into Input and Output Variables.
# load dataset
dataframe = pandas.read_csv("sonar.csv", header=None)
dataset = dataframe.values
# split into input (X) and output (Y) variables
X = dataset[:, 0:60].astype(float)
Y = dataset[:, 60]

# Listing 11.4: Label Encode Output Variable.
# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)

# Listing 11.5: Define and Compile Baseline Model.
# baseline model
def create_baseline():
    # create model
    model = Sequential()
    # model.add(Dense(60, input_dim=60, init='normal', activation='relu'))
    model.add(Dense(60, input_dim=60, kernel_initializer='normal', activation='relu'))
    # model.add(Dense(1, init='normal', activation='sigmoid'))
    model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Listing 11.6: Fit And Evaluate Baseline Model.
# evaluate model with standardized dataset
# estimator = KerasClassifier(build_fn=create_baseline, nb_epoch=100, batch_size=5, verbose=0)
estimator = KerasClassifier(build_fn=create_baseline, epochs=100, batch_size=5, verbose=0)
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(estimator, X, encoded_Y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
