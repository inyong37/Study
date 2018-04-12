# Listing 13.2: Serialize Model To JSON Format.
# MLP for Pima Indians Dataset Serialize to JSON and HDF5
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy
import os

# Fix Random Seed for Reproducibility
seed = 7
numpy.random.seed(seed)

# Load Pima Indians Dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")

# Split into Input (X) and Output (Y) Variables
X = dataset[:, 0:8]
Y = dataset[:, 8]

# Create Model
model = Sequential()
model.add(Dense(12, input_dim=8, kernel_initializer='uniform', activation='relu'))
model.add(Dense(8, kernel_initializer='uniform', activation='relu'))
model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))

# Compile Model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the Model
model.fit(X, Y, epochs=150, batch_size=10, verbose=0)

# Evaluate the Model
scores = model.evaluate(X, Y, verbose=0)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# Serialize Model to JSON
model_json = model.to_json()
with open("model.json", 'w') as json_file:
    json_file.write(model_json)

# Serialize Weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")

# Load JSON and Create Model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# Load Weights into New Model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# Evaluate Loaded Model on Test Data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
score = loaded_model.evaluate(X, Y, verbose=0)
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))
