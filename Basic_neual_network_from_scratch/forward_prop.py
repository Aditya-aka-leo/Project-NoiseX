import numpy as np
from random import random
class MLP(object):
#--------------------------------------------------------------------------------------------------------------------
    #defining the initial constructor
    def __init__(self,num_inputs=3,num_hidden=[3,3],num_outputs=2):
        #num_input is the total number of inputs/neurons we are giving to the network
        '''
        hidden_layers is the number of layers , here 3 means number of neurons in 2nd layer
        and 5 means number of neurons in 2nd layer 
        so total we have total of two layers as there are two items in the list provide
    '''
#-------------------------------------------------------------  -------------------------------------------------------
        #num_output is the last layer of the network which is the output we want from the network
        self.num_inputs = num_inputs
        self.num_hidden = num_hidden
        self.num_outputs = num_outputs
        layers = [self.num_inputs] + self.num_hidden + [self.num_outputs]
#--------------------------------------------------------------------------------------------------------------------
        #creating weights or initiating random weights
        self.weights = []
        for i in range (len(layers)-1):
            w=np.random.rand(layers[i],layers[i+1])
            self.weights.append(w)
        #self.weights = weights ( Maybe be used in future for returning the weight matrix not usefull but !)
#--------------------------------------------------------------------------------------------------------------------
        #Creating empty actiavation vector to store the actiavation for generating the gradients desecent
        activations = []
        for i in range (len(layers)):
            a = np.zeros(layers[i])
            activations.append(a)
            self.activations = activations
            
#--------------------------------------------------------------------------------------------------------------------
        #creating empty derivatives for calculating the derivatives for the caluclation of the gradients desecnt 
        derivatives = []
        for i in range (len(layers)-1):
            d = np.zeros((layers[i],layers[i+1]))
            derivatives.append(d)
            self.derivatives=derivatives


#--------------------------------------------------------------------------------------------------------------------
        #creating a forward progration funstion to calculate the activation
    def forward_propagate(self,inputs):

        activations = inputs
        self.activations[0] = inputs
        for i, w in enumerate(self.weights):
            net_inputs = np.dot(activations,w)
            activations = self._sigmoid(net_inputs)  
            self.activations[i+1]= activations
        return activations      





#--------------------------------------------------------------------------------------------------------------------
    #creating back progration for model traning

    def back_propagate(self,error,verbose=False):
        
        for i in reversed(range(len(self.derivatives))):
            activations = self.activations[i+1]
            delta = error * self._sigmoid_derivative(activations)
            delta_reshaped = delta.reshape(delta.shape[0],-1).T
            current_activations = self.activations[i]
            current_activations_reshaped=current_activations.reshape(current_activations.shape[0],-1)
            self.derivatives[i] =np.dot(current_activations_reshaped,delta_reshaped)
            error=np.dot(delta,self.weights[i].T)
            if verbose:
                print("Derivatives For W{}: {}".format(i,self.derivatives[i]))
        return error
#--------------------------------------------------------------------------------------------------------------------
    #Creating the derivative function to solve the derivative of error to weigts to get gradient decent

    def _sigmoid_derivative(self,x):
        return x * (1.0-x)

#---------------------------------------------------------------------------------------------------------------------
    #creating sigmoid function
    def _sigmoid(self, x):
        return 1/(1+np.exp(-(x)))
#---------------------------------------------------------------------------------------------------------------------
    #creating a function to generate gradient decent
    def gradient_descent(self, learningRate=1):
        """Learns by descending the gradient
        Args:
            learningRate (float): How fast to learn.
        """
        # update the weights by stepping down the gradient
        for i in range(len(self.weights)):
            weights = self.weights[i]
            derivatives = self.derivatives[i]
            weights += derivatives * learningRate

#---------------------------------------------------------------------------------------------------------------------
    #creating a function to train the model 
    def train(self, inputs, targets, epochs, learning_rate):
        """Trains model running forward prop and backprop
        Args:
            inputs (ndarray): X
            targets (ndarray): Y
            epochs (int): Num. epochs we want to train the network for
            learning_rate (float): Step to apply to gradient descent
        """
        # now enter the training loop
        for i in range(epochs):
            sum_errors = 0

            # iterate through all the training data
            for j, input in enumerate(inputs):
                target = targets[j]

                # activate the network!
                output = self.forward_propagate(input)

                error = target - output

                self.back_propagate(error)

                # now perform gradient descent on the derivatives
                # (this will update the weights
                self.gradient_descent(learning_rate)

                # keep track of the MSE for reporting later
                sum_errors += self._mse(target, output)

            # Epoch complete, report the training error
            print("Error: {} at epoch {}".format(sum_errors / len(items), i+1))

        print("Training complete!")
        print("=====")

#---------------------------------------------------------------------------------------------------------------------
    #Creating Mean square root for calculating the loss function
    def _mse(self,target,output):
        return np.average((target-output)**2)


if __name__ == "__main__":
 # create a dataset to train a network for the sum operation
    items = np.array([[random()/2 for _ in range(2)] for _ in range(1000)])
    targets = np.array([[i[0] + i[1]] for i in items])

    # create a Multilayer Perceptron with one hidden layer
    mlp = MLP(2, [5], 1)

    # train network
    mlp.train(items, targets, 50, 0.1)

    # create dummy data
    input = np.array([.2,.2])
    #target = np.array([.3])

    # get a prediction
    output = mlp.forward_propagate(input)

    print()
    print("Our network believes that {} + {} is equal to {}".format(input[0], input[1], output[0]))
