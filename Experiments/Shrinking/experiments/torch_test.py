import torch

import numpy as np

from sklearn.metrics import r2_score
from tqdm import tqdm
import pandas as pd

import matplotlib.pyplot as plt

length=10
records = []

train = pd.read_csv("Shrinking/BIG5/data.csv", sep="\t", usecols=['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10'])

train.replace(0, 3)

print(train.head(3))

compressor = torch.nn.Sequential( #this might be dumb
    torch.nn.LazyLinear(50).double(),
    torch.nn.Sigmoid(),
    torch.nn.LazyLinear(50).double(),
    torch.nn.Sigmoid(),
    torch.nn.LazyLinear(25).double(),
    torch.nn.Sigmoid(),
    torch.nn.LazyLinear(12).double(),
    torch.nn.Sigmoid(),
    torch.nn.LazyLinear(12).double(),
    torch.nn.Sigmoid(),
    torch.nn.LazyLinear(6).double()
)

decompressor = torch.nn.Sequential(
    torch.nn.LazyLinear(6).double(),
    torch.nn.Sigmoid(),
    torch.nn.LazyLinear(50).double(),
)

loss_fn     = torch.nn.MSELoss()
comp_opt    = torch.optim.Adam(params=compressor.parameters(), lr=1)
decomp_opt  = torch.optim.Adam(params=decompressor.parameters(), lr=1)

print("\nStarting Era Nr.1:")
for epoch in range(length):
    train_tensor = torch.tensor(train.iloc[epoch::length].values).double()

    for _ in tqdm(range(200), desc=f"Epoch Nr.{epoch+1}"):
        compressed = compressor(train_tensor)
        pred = decompressor(compressed)
        loss = loss_fn(pred, train_tensor)

        records.append(loss.item())

        #this is dumb
        comp_opt.zero_grad() 
        decomp_opt.zero_grad()

        loss.backward()

        comp_opt.step()
        decomp_opt.step()

train_tensor = torch.tensor(train.values).double()

print("\nStarting Pass Nr.1:")
for _ in tqdm(range(500)):
    compressed = compressor(train_tensor)
    pred = decompressor(compressed)
    loss = loss_fn(pred, train_tensor)

    records.append(loss.item())

    #this is dumb
    comp_opt.zero_grad() 
    decomp_opt.zero_grad()

    loss.backward()

    comp_opt.step()
    decomp_opt.step()

print("\nStarting Era Nr.2:")
for epoch in range(length):
    train_tensor = torch.tensor(train.iloc[epoch::length].values).double()

    for _ in tqdm(range(200), desc=f"Epoch Nr.{epoch+1}"):
        compressed = compressor(train_tensor)
        pred = decompressor(compressed)
        loss = loss_fn(pred, train_tensor)

        records.append(loss.item())

        #this is dumb
        comp_opt.zero_grad() 
        decomp_opt.zero_grad()

        loss.backward()

        comp_opt.step()
        decomp_opt.step()

train_tensor = torch.tensor(train.values).double()

for param_group in comp_opt.param_groups:
    param_group['lr'] = 0.1
for param_group in decomp_opt.param_groups:
    param_group['lr'] = 0.1

print("\nStarting Pass Nr.2")
for _ in tqdm(range(500)):
    compressed = compressor(train_tensor)
    pred = decompressor(compressed)
    loss = loss_fn(pred, train_tensor)

    records.append(loss.item())

    #this is dumb
    comp_opt.zero_grad() 
    decomp_opt.zero_grad()

    loss.backward()

    comp_opt.step()
    decomp_opt.step()

compressed = compressor(train_tensor)
pred = decompressor(compressed)

compressed_df = pd.DataFrame(data=compressed.detach().numpy(), columns=[1, 2, 3, 4, 5, 6])
pred_df = pd.DataFrame(data=torch.round(pred).detach().numpy(), columns=train.columns)

loss = loss_fn(pred, train_tensor)
print("Loss: ", loss.item())

score = r2_score(pred_df, train)
print("Score: ", score)

print(train.head(3))
print(pred_df.head(3))

print(compressed_df)

plt.scatter(range(len(records)),records)
plt.show()