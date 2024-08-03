import torch

print(torch.cuda.is_available())  # Should output: True
print(torch.cuda.device_count())  # Should output the number of GPUs available
print(torch.cuda.get_device_name(0))  # Should output the name of your GPU
