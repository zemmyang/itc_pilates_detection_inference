from pathlib import Path
from glob import glob
import os
from Model import SettingsAndPaths as CONST


def clear_input_data():
    _frames = [Path(file) for file in glob(f"{CONST.FRAMES_PATH}/*.jpg")]
    _videos = [Path(file) for file in glob(f"{CONST.VIDEO_FOLDER}/*")]

    print("Removing frames")
    try:
        [os.remove(i) for i in _frames]
    except:
        pass

    print("Removing videos")
    try:
        [os.remove(i) for i in _videos]
    except:
        pass

    print("Done")
