import os
from box.exceptions import BoxValueError
import yaml
from SpellingCorrection.logging import logger  # Ensure this path is correct
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Dict, Any, Union

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Function to read the yaml file.
    
    :param path_to_yaml: Path: Path to the yaml file
    :return: ConfigBox: Dictionary of the yaml file
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Reading the yaml file from the path: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        logger.error(f"Error in reading the yaml file from the path: {path_to_yaml}")
        return None
    except FileNotFoundError:
        logger.error(f"File not found: {path_to_yaml}")
        return None
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise e

@ensure_annotations
def create_directories(paths_to_directories: list, verbose=True):
    """
    Function to create the directories.
    
    :param paths_to_directories: list: List of the directories to be created
    :param verbose: bool: Verbose
    :return: None
    """
    for path in paths_to_directories:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Creating the directory: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Function to get the size of the file.
    
    :param path: Path: Path to the file
    :return: str: Size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"
