import os
import numpy as np
from pathlib import Path
from glob import glob

from Control.FrameDisplay import FrameDisplay
from Model import SettingsAndPaths as CONST


def get_unique_frames(lst):
    unique, idx, _, _ = np.unique(lst, return_counts=True, return_index=True, return_inverse=True)

    _frames = [Path(file) for file in glob(f"{CONST.FRAMES_PATH}/*.jpg")]

    _dict = dict(zip(unique, idx))

    fd = FrameDisplay()
    for k, v in _dict.items():
        fd.add_image(_frames[v], caption=k)

    return fd
