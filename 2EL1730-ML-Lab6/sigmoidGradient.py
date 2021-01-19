from numpy import *
from sigmoid import sigmoid

def sigmoidGradient(z):

    # SIGMOIDGRADIENT returns the gradient of the sigmoid function evaluated at z


    g = z*(1-z)
    # =========================== TODO ==================================
    # Instructions: Compute the gradient of the sigmoid function evaluated at
    #               each value of z.
    
    return g




