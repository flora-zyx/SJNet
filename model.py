import torch
import torch.nn as nn
import torch.nn.functional as F

# Tutorial for building a neural network in pytorch: https://towardsdatascience.com/building-neural-network-using-pytorch-84f6e75f9a

class SJNet(nn.Module):  # inherits from nn.Module
    def __init__(self):
        super().__init__()  # constructor for base class
        # define all the layers here
    
    def forward(self, x):
        # pass input x through all stages
        # in our case, we will be passing Anchor(A), Positive(P), and Negative(N) images through the network
        

