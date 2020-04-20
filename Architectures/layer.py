"""
Description : Implementation of Layer module for architecutes
Detail: This layer module has a sigmoid activation function
"""

import torch 
import torch.nn as nn

class Layer():
    def __init__(self, row, col):
        self.weights = torch.rand((row, col))

    def init_bias(self, row, col):
        self.bias = torch.rand((row, col))

    def forward(self, input, set_bias=False):
        out = torch.matmul(input, self.weights)

        if set_bias: 
            self.init_bias(out.size()[0], out.size()[1])   

        out += self.bias

        sig = nn.LogSigmoid()
        out = sig(out)
        return out

    def weights(self):
        return self.weights

    def bias(self): 
        return self.bias

    def print(self):
        print (self.weights)


