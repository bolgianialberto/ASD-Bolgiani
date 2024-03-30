import os
import psutil

def compute_memory_usage():
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss
    return mem/1024/1024 # MB