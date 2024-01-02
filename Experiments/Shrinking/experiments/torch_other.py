import torch

import numpy as np

from sklearn.metrics import r2_score
from tqdm import tqdm
import pandas as pd

import matplotlib.pyplot as plt

length=10
records = []

grad_rec = []

x_train = pd.read_csv("Shrinking/BIG5/data.csv", sep="\t", usecols=['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10'])
x_train.replace(0, 3)
print(x_train.head(3))

y_train = pd.read_csv("Shrinking/BIG5/data.csv", sep="\t", usecols=['age', 'gender'])

model = torch.nn.Sequential( #this might be dumb
    torch.nn.LazyLinear(50).double(),
    torch.nn.ReLU(),
    torch.nn.LazyLinear(25).double(),
    torch.nn.ReLU(),
    torch.nn.LazyLinear(2).double(),
    torch.nn.Flatten(1).double()
)

loss_fn = torch.nn.MSELoss()
opt = torch.optim.Adam(params=model.parameters(), lr=0.1)

x_train_tensor = torch.tensor(x_train.values).double()
y_train_tensor = torch.tensor(y_train.values).double()

for _ in tqdm(range(1_000)):
    y_pred = model(x_train_tensor)
    loss = loss_fn(y_pred, y_train_tensor)

    #this is dumb
    opt.zero_grad()
    loss.backward()
    opt.step()

    #grad_rec.append(loss.grad)
    records.append(loss.item())

y_pred = model(x_train_tensor)

y_pred_df = pd.DataFrame(data=torch.round(y_pred).detach().numpy(), columns=y_train.columns)

loss = loss_fn(y_pred, y_train_tensor)
print("Loss: ", loss.item())

score = r2_score(y_pred_df, y_train)
print("Score: ", score)

print(y_pred_df.head(10))

plt.scatter(range(len(records)),records)
plt.show()