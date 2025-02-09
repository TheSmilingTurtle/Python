import torch

class Kernel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.c1 = torch.nn.Conv2d(6, 12, 9, padding=4, padding_mode="reflect")
        self.c2 = torch.nn.Conv2d(12, 24, 7, padding=3, padding_mode="reflect")
        self.c3 = torch.nn.Conv2d(24, 12, 5, padding=2, padding_mode="reflect")
        self.c4 = torch.nn.Conv2d(12, 6, 3, padding=1, padding_mode="reflect")

        self.r = torch.nn.ReLU()
    
    def forward(self, x):
        _x = self.r(self.c1(x))
        _x = self.r(self.c2(_x))
        _x = self.r(self.c3(_x))
        return self.c4(_x) + x

class Pop(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.k1 = Kernel()
        self.k2 = Kernel()
        self.k3 = Kernel()

        self.final = torch.nn.Conv2d(6, 3, 3, padding=1, padding_mode="reflect")

    def forward(self, x):
        x = self.k1(x)
        x = self.k2(x)
        x = self.k3(x)
        
        x = self.final(x)
        return torch.clamp(x, 0, 1)
