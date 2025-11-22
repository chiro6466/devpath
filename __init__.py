import os
import sys

# CRITICAL FIX: The name of the local development folder (the one containing pak1, pak2, etc.)
# MUST be different from the installed package name ('devpath') to avoid collisions.
DEV_FOLDER_NAME = 'paks_repo' 

def _enable_dev_mode():
    """
    Searches for the development folder 'paks_repo' and injects its path into sys.path.
    This makes the internal packages (pak1) directly importable.
    """
    current_search_dir = os.getcwd()

    for _ in range(5):
        dev_path = os.path.join(current_search_dir, DEV_FOLDER_NAME)
        
        if os.path.isdir(dev_path):
            # THE MAGIC: We use sys.path.insert(0) to elevate the contents 
            # of 'paks_repo' to top-level modules.
            if dev_path not in sys.path: 
                sys.path.insert(0, dev_path)
            return
        
        new_dir = os.path.dirname(current_search_dir)
        if new_dir == current_search_dir:
            break
        current_search_dir = new_dir

_enable_dev_mode()