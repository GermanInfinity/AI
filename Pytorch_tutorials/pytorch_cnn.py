###############################################################################

"""Description: Simple CNN trained and tested on FashionMNIST dataset. 
             (Includes confusion Matrix for evaluating)
Acknowledgment: Deel Lizard Pytorch tutorial"""

###############################################################################

import torch #Top level pytorch package
import torch.nn as nn #Modules for NN building
import torch.optim as optim #Package with optimization operations
import torch.nn.functional as F #Typical NN functions

import torchvision #Access to image data
import torchvision.transforms as transforms #Image processing transforms

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

from sklearn.metrics import confusion_matrix
import pdb, itertools
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix
from plotcm import plot_confusion_matrix

train_set = torchvision.datasets.FashionMNIST(root='./data',train=True,download=True,transform=transforms.Compose([transforms.ToTensor()]))
train_loader = torch.utils.data.DataLoader(train_set,batch_size=1000,shuffle=True)

class Network(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5)
        self.conv2 = nn.Conv2d(in_channels=6, out_channels=12, kernel_size=5)
        
        self.fc1 = nn.Linear(in_features=12 * 4 * 4, out_features=120)
        self.fc2 = nn.Linear(in_features=120, out_features=60)
        self.out = nn.Linear(in_features=60, out_features=10)
    
    def forward(self, t):
        # (1) input layer
        t = t

        # (2) hidden conv layer
        t = self.conv1(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size=2, stride=2)

        # (3) hidden conv layer
        t = self.conv2(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size=2, stride=2)

        # (4) hidden linear layer
        t = t.reshape(-1, 12 * 4 * 4)
        t = self.fc1(t)
        t = F.relu(t)

        # (5) hidden linear layer
        t = self.fc2(t)
        t = F.relu(t)

        # (6) output layer
        t = self.out(t)
        #t = F.softmax(t, dim=1)

        return t
    
def get_all_preds(model, loader):
	all_preds = torch.tensor([])
    for batch in loader:
        images, labels = batch

        preds = model(images)
        all_preds = torch.cat(
            (all_preds, preds)
            ,dim=0
        )
    return all_preds

def get_num_correct(preds, labels):
	return preds.argmax(dim=1).eq(labels).sum().item()


if __name__ == "__main__":
    net = Network()
    train_loader = torch.utils.data.DataLoader(train_set, batch_size=100)
    optimizer = optim.Adam(net.parameters(), lr=0.01)

    train(optimizer, train_loader)

    #GET PREDICTIONS FROM MODEL
    with torch.no_grad():
        prediction_loader = torch.utils.data.DataLoader(train_set, batch_size=10000)
        train_preds = get_all_preds(net, prediction_loader)

    preds_correct = get_num_correct(train_preds, train_set.targets)
    cm = confusion_matrix(train_set.targets, train_preds.argmax(dim=1))
    names = (
    'T-shirt/top'
    ,'Trouser'
    ,'Pullover'
    ,'Dress'
    ,'Coat'
    ,'Sandal'
    ,'Shirt'
    ,'Sneaker'
    ,'Bag'
    ,'Ankle boot'
    )
    
    plt.figure(figsize=(10,10))
    plot_confusion_matrix(cm, names)