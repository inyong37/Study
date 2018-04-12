# Listing 12.12: Evaluate the Larger Neural Network Model.
# Regression Example with Boston Dataset: Standardized and Larger
import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Load Dataset
dataframe = pandas.read_csv("housing.csv", delim_whitespace=True, header=None)


dataset = dataframe.values
# Split into Input (X) and Output (Y) Variables
X = dataset[:, 0:13]
Y = dataset[:, 13]

# Define Larger Model
def larger_model():
    # Create Model
    model = Sequential()
    model.add(Dense(13, input_dim=13, kernel_initializer='normal', activation='relu'))
    model.add(Dense(6, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile Model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

# Fix Random Seed for Reproducibility
seed = 7
numpy.random.seed(seed)
# Evaluate Model with Standardized Dataset
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasRegressor(build_fn=larger_model, epochs=50, batch_size=5, verbose=0)))
pipeline = Pipeline(estimators)

kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(pipeline, X, Y, cv=kfold)
print("Larger: %.2f (%.2f) MSE" % (results.mean(), results.std()))

