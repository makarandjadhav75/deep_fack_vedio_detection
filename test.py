import torch

if torch.cuda.is_available():
    print("PyTorch is installed for GPU")
else:
    print("PyTorch is not installed for GPU")