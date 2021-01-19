import numpy as np

def randInitializeWeights(layers):

    num_of_layers = len(layers)
    epsilon = 0.12
        
    Theta = []
    for i in range(num_of_layers-1):
        # ====================== TODO ======================
        # Instructions: Initialize W randomly so that we break the symmetry while
        #               training the neural network.
        #
        W = 2 * epsilon *np.random.rand(layers[i+1], layers[i]+1) - epsilon
        Theta.append(W)
                
    return Theta
            
