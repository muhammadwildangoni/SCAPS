from torch import nn
from jcopdl.layers import linear_block
from torchvision.models import shufflenet_v2_x2_0


class Shufflenet_V2_X2_0(nn.Module):
    def __init__(self):
        super().__init__()
        self.mnet = shufflenet_v2_x2_0(pretrained=True)
        self.freeze()
        self.mnet.classifier = linear_block(2048, 8, activation="lsoftmax")
            
    def forward(self, x):
        return self.mnet(x)
    
    def freeze(self):
        for param in self.mnet.parameters():
            param.requires_grad = True
            
    def unfreeze(self):
        for param in self.mnet.parameters():
            param.requires_grad = True