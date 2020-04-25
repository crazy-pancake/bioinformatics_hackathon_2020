import keras, pandas
import tensorflow
import numpy
from keras.regularizers import l2
from keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
file = "simplified_only_benign_and_pathogenic.csv"
original_data = pandas.read_csv(file)
print(original_data.head())
data = original_data[:800]
data = data.drop(columns=["Unnamed: 0"])
print(data.head())
X = data.drop(columns=["simplified.significance"])
Y = data["simplified.significance"]

scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(X)

x_train, x_test, y_train, y_test = train_test_split(rescaledX, Y)

model = keras.models.Sequential()
model.add(Dense(100, activation = "relu", input_dim=3, kernel_regularizer=l2(0.01)))
model.add(Dense(1, activation="sigmoid"))
model.summary()
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])



check_point = keras.callbacks.ModelCheckpoint("checkpoint2.h5", monitor='val_loss', verbose=1, save_best_only=True,
                                                     save_weights_only=False, mode='auto', period=1)
early_callback = keras.callbacks.EarlyStopping(monitor='loss', mode='auto', min_delta=0.001, patience=5,
                                                      verbose=1)
callbacks_list = [check_point, early_callback]

info = model.fit(x_train, y_train, batch_size=32, epochs=100, verbose=1, callbacks=callbacks_list, validation_data=(x_test, y_test), shuffle=True)
print("Training Accuracy ", numpy.mean(info.history['accuracy']))
print("Validation Accuracy ", numpy.mean(info.history['val_accuracy']))

test_data = original_data[800:]
test_data = test_data.drop(columns=["Unnamed: 0"])
X_eval = test_data.drop(columns=["simplified.significance"])
Y_eval = test_data["simplified.significance"]
result = model.evaluate(X_eval, Y_eval, batch_size=128)
print('test loss, test acc:', result)
