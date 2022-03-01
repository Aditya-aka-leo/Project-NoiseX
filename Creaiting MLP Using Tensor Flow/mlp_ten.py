import numpy as np 
import tensorflow as tf
from random import random
from sklearn.model_selection import train_test_split

def generate_dataset(num_samples,test_sizee=0.33):
    x = np.array([[random()/2 for _ in range(2)] for _ in range(num_samples)])
    y = np.array([[i[0] + i[1]] for i in x])
    #for automatically spliting the data set into training and testing from sickit learn lib
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=test_sizee)
    return x_train, x_test, y_train,y_test

if __name__ == "__main__":
    x_train,x_test,y_train,y_test = generate_dataset(5000,0.3)
    
    #Building The Neural Network
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(5,input_dim=2,activation="sigmoid"),
        tf.keras.layers.Dense(1,activation="sigmoid")
    ])
    optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)

    model.compile(optimizer=optimizer,loss="MSE") 
    
    #Training The Model
    model.fit(x_train, y_train,epochs=50,batch_size=1)
    #Lets Evaluate The Neural Network
    print("\nModel evaluation : ")
    model.evaluate(x_test, y_test, verbose=1,batch_size = 1)
    #Make Predictions
    data = np.array([[0.1,0.2],[0.2,0.2]])
    predictions = model.predict(data)
    print("\nSome Predictions : ")
    for d , p in zip(data, predictions):
        print("{} + {} = {}".format(d[0],d[1],p[0]))
        














