import os

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_extension(filename):
    return os.path.splitext(filename)[1].lower()