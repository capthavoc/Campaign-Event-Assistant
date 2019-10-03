""" --------------------------------------------
@ file      PathManager.py
@ authors   George Engel
@brief      Contains all functionality related to navigating the project's file structure.
"""

import os
from pathlib import Path

class PathManager:
    
    # TODO: Use a config file for the default save folder & events folder locations
    def __init__(self):
        print("Path manager initializing...")
        
        # Stores the root directory of the project.
        self.ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Initializes the folder name for the directory that holds the campeign Saves.
        self.campeign_saves_folder = "Campeign_Saves"
        
        # Initializes the folder name for the directory that holds the Events.
        self.events_folder = "Events"
        
        # Initialize this to empty
        self.current_selected_folder = ""
        
        print("Path manager Initialized!")
        
    ### PATH RELATED:    
    
    def get_ROOT_DIR(self):
        return self.ROOT_DIR
        
    # Returns the entire path of the Campeign Saves collection folder.
    def get_campeign_saves_dir(self):
        return os.path.join(self.ROOT_DIR, self.campeign_saves_folder)
    
    # Returns the entire path of the Events collection folder.
    def get_events_dir(self):
        return os.path.join(self.ROOT_DIR, self.events_folder)
    
    # TODO: Replace this invalid function with the equivalent for choosing sub directories from the Events folder & Campeign Saves folder.
    # Sets the currently selected folder to the foldername specified, which will then be used to generate the new folder path.
    def set_databases_folder(self, folder_name):
        if self.validate_dir(os.path.join(self.ROOT_DIR, folder_name)):
            self.current_selected_folder = folder_name
        else:
            print("Please enter a valid database collection directory.")
        
    # Gets the currently selected folder
    def get_current_selected_folder(self):
        return self.current_selected_folder
    
    # Sets the currently selected folder
    def set_current_selected_folder(self, parent_dir, folder_name):
        if self.validate_dir(os.path.join(parent_dir, folder_name)):
            self.current_selected_folder = folder_name
        else:
            print("Error: Invalid directory for currently selected folder:", folder_name, "@", os.path.join(parent_dir, folder_name))
    
    def get_current_selected_dir(self, parent_dir):
        return os.path.join(parent_dir, self.current_selected_folder)