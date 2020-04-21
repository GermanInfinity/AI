"""
Description : Implementation of Feed Forward Neural Network Architecture
Detail: Is able to determine linear serparability in multi-dim data
Action: Regression task for NN model 
"""
import torch 
import torch.nn as nn
from layer import Layer

class FeedForward():
	def __init__(self, input_shape, row, col):
		#One layer between input and output 
		self.inp_layer = Layer(row,col)
		self.hidden_layer = Layer(col, 1)
		self.out = 0 #no function on output layer 


	def forward(self, input):
		out = self.inp_layer.forward(input, set_bias=True)
		self.out = self.hidden_layer.forward(out, set_bias=True)

		return self.out 

	def train(self):
		

	def print(self):
		print (self.out)

if __name__ == '__main__':
	data_row = 4
	data_col = 2

	inp = torch.tensor([[0,0],[0,1],[1,0],[1,1]]).float()

	FF_net = FeedForward(data_row, 2, 1)
	FF_net.forward(inp)

	FF_net.print()