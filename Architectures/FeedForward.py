"""
Description : Implementation of Feed Forward Neural Network Architecture
Detail: Feed forward networks are simple neural networks that have one layer
		in between the input and outputt layer. The process of creating one, 
		starts with initializing the general architecture with linear and non-linear
		functions, defining the loss,  and a process of which to optimize the loss. 
		While we train, we alter the parameters in the loss function to 
		produce a lower loss, we do this by ensuring a reduction in the gradient
		as we train per epoch. To include GPU processing, put model and input 
		tensor on GPU 

"""
import torch 
import torch.nn as nn

class FeedForward(nn.Module):
	def __init__(self, input_size, hidden_size, output_size):
		super(FeedForward, self).__init__()
		self.fc1 = nn.Linear(input_size, hidden_size)
		self.sigmoid = nn.Sigmoid()
		self.fc2 = nn.Linear(hidden_size, output_size)

	def forward(self, x): 
		out = self.fc1(x)
		out = self.sigmoid(out)
		out = self.fc2(out)
		return out 

	def train(self, input_data, output_data, criterion, optimizer, num_epochs):
		target = output_data #Actual results

		for epoch in range(num_epochs):
			#Clear gradients
			optimizer.zero_grad()
			#Get output from model
			output = self.forward(input_data)
			#Find loss
			loss = criterion(output, target)
			#Get gradients
			loss.backward()
			#Update parameters 
			optimizer.step()

	def eval(self, data):
		return net.forward(data)
			
if __name__=='__main__':
	input_dim = 8 #Input features
	hidden_dim = 136
	output_dim = 11

	inp = torch.tensor([ [100000,1,5,26,5,5,3,4],
						[20000,0,2,32,4,3,5,5],
						[87000,0,4,28,4,3,1,2],
						[65000,1,3,30,4,2,3,4],
						[40000,1,1,29,2,3,4,5],
						[24500,1,1,37,0,5,3,2],
						[77230,1,5,45,0,4,2,1],
						[5000,1,2,19,2,4,4,5],
						[0,0,5,23,5,3,5,5],
						[11500,0,2,21,3,4,3,5],
						[30000,1,3,28,1,1,3,5],
						[50000,1,4,55,4,2,2,5],
						[88000,0,5,27,5,1,2,1],
						[12000,1,1,34,5,5,4,3],
						[49500,1,3,67,5,3,4,4],
						[31230,0,2,20,2,5,5,5],
						[72500,1,5,48,1,5,4,3] ]).float()
	out = torch.tensor([[9],[10],[3],[5],[8],[2],[3],[8],[10],
						[7],[4],[6],[2],[9],[8],[10],[5]])
	out = out.squeeze(1)


	#Model
	net = FeedForward(input_dim, hidden_dim, output_dim)
	#Loss
	loss = nn.CrossEntropyLoss()
	#Optimizer
	lr = 0.01
	optimizer = torch.optim.SGD(net.parameters(), lr=lr)


	#Train
	net.train(inp, out, loss, optimizer, 10)
	#Evaluate
	print (net.eval(torch.tensor([100000,1,5,26,5,5,3,4]).float()))