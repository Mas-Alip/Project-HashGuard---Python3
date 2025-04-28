import hashlib
import os
from datetime import datetime

def hash_file(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def save_hash_to_file(filename, hash_value, save_dir="data/saved_hashes"):
    os.makedirs(save_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    basename = os.path.basename(filename)
    safe_name = f"{basename}_{timestamp}.txt"
    save_path = os.path.join(save_dir, safe_name)
    
    with open(save_path, "w") as f:
        f.write(f"File: {basename}\n")
        f.write(f"Waktu: {timestamp}\n")
        f.write(f"SHA-256: {hash_value}\n")
    
    return save_path

def read_hash_from_file(filepath):
    """Baca hash dari file .txt"""
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("SHA-256:"):
                return line.strip().split("SHA-256:")[1].strip()
    return None

def list_saved_hashes(folder_path):
    """List semua file hash di folder"""
    hash_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r') as f:
                content = f.read()
                hash_list.append(content)
    return hash_list
