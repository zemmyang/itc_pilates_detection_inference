import os
from pathlib import Path


TEMPLATE_FOLDER = 'View/templates'
STATIC_FOLDER = 'View/static'
DATA_UPLOAD_FOLDER = 'input_data'
FRAMES_FOLDER = "frames_folder"
OUT_FOLDER = 'output_data'

MAIN_PAGE_TITLE = "Computer Vision-based Pilates Classifier"
MAIN_PAGE_SUBTITLE = 'A project by 2+2 for the Israel Tech Challenge. Only works for three specific exercises'

MAX_FILE_SIZE = 5e9  # in bytes

FLASK_HOST = "0.0.0.0"
FLASK_PORT = 7070

MODEL_WEIGHTS = '21oct.h5'
MODELS_DIRECTORY = 'model_weights'

########### PATHS ############

FRAMES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), FRAMES_FOLDER)
VIDEO_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), DATA_UPLOAD_FOLDER)
OUT_FRAMES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), OUT_FOLDER)
MODELS_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), MODELS_DIRECTORY)

Path(FRAMES_PATH).mkdir(parents=True, exist_ok=True)
Path(VIDEO_FOLDER).mkdir(parents=True, exist_ok=True)
Path(OUT_FRAMES_PATH).mkdir(parents=True, exist_ok=True)
Path(MODELS_PATH).mkdir(parents=True, exist_ok=True)
