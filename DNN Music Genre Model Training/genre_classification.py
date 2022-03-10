from cProfile import label
import json
import re
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras
import matplotlib.pyplot as plt
DATASET_PATH = "Music Genre Classification Code Base\data1.json"


#loading data 
def load_data(dataset_path):
    with open(dataset_path, 'r') as fp:
        data = json.load(fp)
    #convert lists into numpy arrays for putting it in the nn
    inputs = np.array(data["mfcc"])
    targets = np.array(data["labels"])
    return inputs, targets

def plot_history(history):

    figure , axs = plt.subplots(2)
    #accuracy subplot
    axs[0].plot(history.history["accuracy"],label="train accuracy")
    axs[0].plot(history.history["val_accuracy"],label="Test accuracy")
    axs[0].set_ylabel("Accuracy")
    axs[0].legend(loc="lower right")
    axs[0].set_title("Accuracy eval")
    #error

    axs[1].plot(history.history["loss"],label="train error")
    axs[1].plot(history.history["val_loss"],label="Test error")
    axs[1].set_ylabel("Error")
    axs[1].set_xlabel("Epoch")
    axs[1].legend(loc="upper right")
    axs[1].set_title("Error eval")
    plt.show()

if __name__ == "__main__":
    #loading data 
    inputs,targets = load_data(DATASET_PATH)
    #spliting the data into train and test sets
    inputs_train,inputs_test,targets_train,targets_test =train_test_split(inputs,targets,test_size=0.3)
    #build network
    model = keras.Sequential([
        #input layer
        keras.layers.Flatten(input_shape=(inputs.shape[1],inputs.shape[2])),
        #1st hidden layer
        keras.layers.Dense(512,activation="relu",kernel_regularizer=keras.regularizers.l2(0.001)),
        keras.layers.Dropout(0.3),
        #2nd hidden layer
        keras.layers.Dense(256,activation="relu",kernel_regularizer=keras.regularizers.l2(0.001)),
        keras.layers.Dropout(0.3),
        #3rd hidden layer
        keras.layers.Dense(64,activation="relu",kernel_regularizer=keras.regularizers.l2(0.001)),
        keras.layers.Dropout(0.3),
        #output layer
        keras.layers.Dense(10,activation="softmax")
    ])
    #compile network
    optimizer = keras.optimizers.Adam(learning_rate = 0.0001)
    model.compile(optimizer=optimizer,loss = "sparse_categorical_crossentropy",metrics = ["accuracy"])
    model.summary()
    #train network
    history = model.fit(inputs_train,targets_train,validation_data = (inputs_test,targets_test),epochs=50,batch_size=10)
    #plot the accuracy and error of the epoch
    plot_history(history)




    
