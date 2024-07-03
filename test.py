import torch
import numpy as np

# set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Device: {device}")
torch.set_default_device(device)


# Create a tensor
x = torch.tensor([1, 2, 3])
print(x)