# Listing 12.7 Multiple Perceptron Model for Boston House Problem.
# Listing: 12.2: Importing Classes and Functions
import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Listing 12.3: Load Dataset and Separate Into Input and Output Variables
# Load Dataset
dataframe = pandas.read_csv("housing.csv", delim_whitespace=True, header=None)
dataset = dataframe.values
# Split into Input (X) and Output (Y) Variables
X = dataset[:, 0:13]
Y = dataset[:, 13]

# Listing 12.4: Define and Compile a Baseline Neural Network Model.
# Define Base Model
def baseline_model():
    # Create Model
    model = Sequential()
    model.add(Dense(13, input_dim=13, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile Model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

# Listing 12.5: Initialize Random Number Generator and Prepare Model Wrapper for scikit-learn.
# Fix Random Seed for Reproducibility
seed = 7
numpy.random.seed(seed)
# Evaluate Model with Standardized Dataset
estimator = KerasRegressor(build_fn=baseline_model, epochs=100, batch_size=5, verbose=0)

# Listing 12.6: Evaluate Baseline Model.
kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(estimator, X, Y, cv=kfold)
print("Baseline: %.2f (%.2f) MSE" % (results.mean(), results.std()))

