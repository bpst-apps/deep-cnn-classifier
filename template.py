# Importing required packages
import os
import logging
from pathlib import Path

# Define logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s: '
)

# Define package name
package_name = 'DeepClassifier'

# Define list of files
project_files = [
    '.github/workflows/.gitkeep',
    f'src/{package_name}/__init__.py',
    f'src/{package_name}/components/__init__.py',
    f'src/{package_name}/utils/__init__.py',
    f'src/{package_name}/config/__init__.py',
    f'src/{package_name}/pipeline/__init__.py',
    f'src/{package_name}/entity/__init__.py',
    f'src/{package_name}/constants/__init__.py',
    'tests/__init__.py',
    'tests/unit/__init__.py',
    'tests/integration/__init__.py',
    'configs/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'init_setup.sh',
    'requirements.txt',
    'requirements_dev.txt',
    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    'tox.ini',
    'research/trials.ipynb'
]

# Create files
for file_path in project_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f'Creating directory: {file_dir} for file: {file_name}')

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            logging.info(f'Creating empty file: {file_path}')
            pass  # create an empty file
    else:
        logging.info(f'{file_name} already exists')
