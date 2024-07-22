import os
from pathlib import Path
import logging

# Set up logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s] %(levelname)s: %(message)s')

project_name = 'text-sumarrization'


list_of_files = [
    ".github/workflows/.gitkeep", 
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init.py",
    f"src/{project_name}/config/__init.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__inti__.py",
    f"src/{project_name}/entity/__inti__.py",
    f"src/{project_name}/constants/__inti__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
]


for file in list_of_files:
    file_path = Path(file)
    filedir, filename = os.path.split(file_path)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"File directories {filedir} is created.")


    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        logging.info(f"Creating empty file {filename}.")
        with open(file_path, 'w') as f:
            f.write("")
    else:
        logging.info(f"{filename} is already exist.")
        