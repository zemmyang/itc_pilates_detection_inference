import os
from Control.DeleteInputData import clear_input_data
from Model import SettingsAndPaths as CONST


def check_data_folders():
    folders_to_check = [CONST.FRAMES_PATH, CONST.VIDEO_FOLDER, CONST.OUT_FRAMES_PATH, CONST.MODELS_PATH]

    for folder in folders_to_check:
        if os.path.isdir(folder):
            clear_input_data()
        elif len(os.listdir(folder)) == 0:
            pass
        else:
            os.mkdir(folder)
