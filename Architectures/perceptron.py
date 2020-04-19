"""
Description : Implementation of simple perceptron
"""
import torch 
import torch.nn as nn

class Perceptron():
    def __init__(self, row, width):
        self.weights = torch.rand((row, width))
        self.bias = torch.rand((row, width))

    def forward(self, input):
        out = self.weights * input
        out += self.bias
        sig = nn.LogSigmoid()
        out = sig(out)
        return out


if __name__ == '__main__':
    neuron = Perceptron(3, 5)
    print (neuron.forward(2))