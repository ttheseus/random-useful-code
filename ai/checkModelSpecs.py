import os
import psutil
from ultralytics import YOLO

model_path = "/home/user/runs/detect/train5/weights/best.pt"
model_size = os.path.getsize(model_path)
model = YOLO("yolov8n.pt")

model_size_MB = model_size / (1024*1024)

print(f"Model size: {model_size_MB}")

process = psutil.Process(os.getpid())
memory_info = process.memory_info()

print(f"Memory usage: {memory_info.rss/(1024**2):.2f} MB")

