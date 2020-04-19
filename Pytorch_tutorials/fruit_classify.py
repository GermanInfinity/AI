###############################################################################

"""Description: Simple CNN trained and tested on fruit dataset. 
             (Includes confusion Matrix for evaluating)
"""

###############################################################################

import torch #Top level pytorch package
import torch.nn as nn #Modules for NN building
import torch.optim as optim #Package with optimization operations
import torch.nn.functional as F #Typical NN functions
from torchvision import transforms, datasets

import torchvision #Access to image data
import torchvision.transforms as transforms #Image processing transforms

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

import pdb, itertools
import matplotlib.pyplot as plt

from plotcm import plot_confusion_matrix
from PIL import Image

data_transform = transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
fruit_train_dataset = datasets.ImageFolder(root='../fruit_data/train',
                                           transform=data_transform)
dataset_loader = torch.utils.data.DataLoader(fruit_train_dataset,
                                             batch_size=4, shuffle=True,
                                             num_workers=4)


class Network(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=10, kernel_size=5)
        #self.conv2 = nn.Conv2d(in_channels=18, out_channels=36, kernel_size=5)
        
        self.fc1 = nn.Linear(in_features=18, out_features=18)
        #self.fc2 = nn.Linear(in_features=120, out_features=60)
        self.out = nn.Linear(in_features=18, out_features=3)
    
    def forward(self, t):
        # (1) input layer
        t = t

        # (2) hidden conv layer
        print (t.size())
        print ("Convolve now")
        t = self.conv1(t)
        print (t.size())
        print ("ReLu now")
        t = F.relu(t)
        return
        t = F.max_pool2d(t, kernel_size=2, stride=2)

        # (3) hidden conv layer
        #t = self.conv2(t)
        #t = F.relu(t)
        #t = F.max_pool2d(t, kernel_size=2, stride=2)

        # (4) hidden linear layer
        t = t.reshape(-1, 12 * 4 * 4)
        t = self.fc1(t)
        t = F.relu(t)

        # (5) hidden linear layer
        #t = self.fc2(t)
        #t = F.relu(t)

        # (6) output layer
        t = self.out(t)
        #t = F.softmax(t, dim=1)

        return t

if __name__=="__main__":
	net = Network() 

	img = Image.open("../fruit_data/train/apples/apple1.png")
	img2 = Image.open("../fruit_data/train/apples/apple3.png")

	pil2tensor = transforms.ToTensor()
	tensor2pil = transforms.ToPILImage()
	rgb_img = pil2tensor(img)
	rgb_img2 = pil2tensor(img2)

	c = torch.stack((rgb_img, rgb_img2), dim=0)

	print (c.size())
	print ("Before forward pass")
	net.forward(c)

	