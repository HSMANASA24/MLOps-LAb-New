import os
from datetime import datetime

def create_directory(path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory created: {path}")
    else:
        print(f"Directory already exists: {path}")

def get_current_timestamp():
    """Return current timestamp"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_message(message):
    """Simple log message with timestamp"""
    print(f"[{get_current_timestamp()}] {message}")

if __name__ == "__main__":
    create_directory("data")
    log_message("Pipeline utility test")