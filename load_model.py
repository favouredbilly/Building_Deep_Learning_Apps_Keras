import pandas as pd
from keras.models import load_model

model = load_model('trained_model.h5')

X = pd.read_csv("proposed_data2.csv").values
prediction = model.predict(X)

# Grab just the first element of the first prediction (since we only have one)
prediction = prediction[0][0]

# Re-scale the data from the 0-to-1 range back to dollars
# These constants are from when the data was originally scaled down to the 0-to-1 range
prediction = prediction + 0.009122
prediction = prediction / 0.0000531842

print("nextdaylow Prediction for Proposed day data - ${}".format(prediction))

