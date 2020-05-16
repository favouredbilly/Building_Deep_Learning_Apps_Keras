import pandas as pd
from keras.models import Sequential
from keras.layers import *

training_data_df = pd.read_csv("nextdaylow_training_scaled.csv")

X = training_data_df.drop('nextdaylow', axis=1).values
Y = training_data_df[['nextdaylow']].values

for i in range(50,51):
    for j in range(1,2):
        # Define the model
        model = Sequential()
        model.add(Dense(i, input_dim=5, activation='relu'))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(50, activation='relu'))
        model.add(Dense(1, activation='linear'))
        model.compile(loss='mean_squared_error', optimizer='adam')

        # Train the model
        model.fit(
            X,
            Y,
            epochs=50,
            shuffle=True,
            verbose=2
        )

        # Load the separate test data set
        test_data_df = pd.read_csv("nextdaylow_testing_scaled.csv")

        X_test = test_data_df.drop('nextdaylow', axis=1).values
        Y_test = test_data_df[['nextdaylow']].values

        test_error_rate = model.evaluate(X_test, Y_test, verbose=0)
        print("The mean squared error (MSE) for the test data set is: {}".format(test_error_rate))
        print(f"value of i is {i} and j is {j}")
       # if 0.001 < test_error_rate < 0.0023:
           # break

    #if 0.001 < test_error_rate < 0.0023:
       # break

# Save the model to disk
model.save("trained_model.h5")
print("Model saved to disk.")

