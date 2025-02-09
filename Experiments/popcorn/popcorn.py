import numpy as np
import torch
import torchvision
import torchsummary

from tqdm import tqdm

import matplotlib.pyplot as plt

from rich import print
from rich.traceback import install
install()

class VideoLoader(torch.utils.data.Dataset):
    def __init__(self, f, transforms):
        super().__init__()
        self.vid, *_ = torchvision.io.read_video(f, output_format="TCHW")
        self.vid = transforms(self.vid)
    
    def __len__(self):
        return self.vid.shape[0] - 2
    
    def __getitem__(self, idx):
        return torch.cat((self.vid[idx], self.vid[idx+2])), self.vid[idx+1]
    
    def get_test(self, idx):
        return torch.cat((self.vid[idx], self.vid[idx+1]))

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

class VideoLoader2(torch.utils.data.Dataset):
    def __init__(self, f, transforms):
        super().__init__()
        self.vid, *_ = torchvision.io.read_video(f, output_format="TCHW")
        self.vid = transforms(self.vid)
    
    def __len__(self):
        return self.vid.shape[0] - 1
    
    def __getitem__(self, idx):
        return self.vid[idx], self.vid[idx+1]
    
    def get_test(self, idx):
        return self.vid[idx]

class Kernel2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.c1 = torch.nn.Conv2d(3, 6, 9, padding=4, padding_mode="reflect")
        self.c2 = torch.nn.Conv2d(6, 12, 7, padding=3, padding_mode="reflect")
        self.c3 = torch.nn.Conv2d(12, 6, 5, padding=2, padding_mode="reflect")
        self.c4 = torch.nn.Conv2d(6, 3, 3, padding=1, padding_mode="reflect")
    
    def forward(self, x):
        _x = self.c1(x)
        _x = self.c2(_x)
        _x = self.c3(_x)
        return self.c4(_x) + x

class Pop2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.k1 = Kernel2()
        self.k2 = Kernel2()

        self.final = torch.nn.Conv2d(3, 3, 3, padding=1, padding_mode="reflect")

    def forward(self, x):
        x = self.k1(x)

        x = self.final(x)
        return torch.clamp(x, 0, 1)

def plot_image(img):
    plt.imshow(np.transpose(img.detach().numpy(), (1, 2, 0)))
    plt.show()

EPOCHS = 20
input_size = (180, 320)

model = Pop()
#model.load_state_dict(torch.load("save1.pt", weights_only=True))
print("loaded")
transforms = torchvision.transforms.Compose([
    torchvision.transforms.ConvertImageDtype(dtype=torch.float32),
    torchvision.transforms.Resize(input_size),
])
vidld = VideoLoader("test.mp4", transforms)
test_input = vidld.get_test(0)
torchsummary.summary(model, test_input.shape, device="cpu")
print(model)
l = len(vidld)

record = []
avg_record = []

criterion = torch.nn.L1Loss()
optimizer = torch.optim.AdamW(model.parameters())

for i in range(EPOCHS):
    running_loss = 0
    for X,y in tqdm(vidld):
        pred = model(X)

        loss = criterion(y, pred)
        record.append(loss.item())
        running_loss += loss.item()
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    avg_record.append(running_loss)
    print(f"Epoch {i+1}: {running_loss/l}")

torch.save(model.state_dict(), "save.pt")

plt.plot(avg_record)
plt.show()

model.eval()
test = vidld[0]
test_pred = model(test[0])
test_true = test[1]
print(criterion(test_true, test_pred).item())
plot_image(test_pred)
plot_image(test_true)

test = model(test_input)
plot_image(test)

def out():
    t = torch.zeros((213, 3, 180, 320))
    torchvision.io.write_video("out.mp4", np.transpose(t.detach().numpy()*255,(0,2,3,1)).astype(np.uint8), 60, video_codec="h264")
    for i in tqdm(range(len(vidld) + 1)):
        t[2*i] = vidld.vid[i]
        t[2*i+1] = model(vidld.get_test(i))

    torchvision.io.write_video("out.mp4", np.transpose(t.detach().numpy()*255,(0,2,3,1)).astype(np.uint8), 60, video_codec="h264")
