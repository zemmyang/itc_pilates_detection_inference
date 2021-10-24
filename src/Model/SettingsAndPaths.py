import os


TEMPLATE_FOLDER = 'View/templates'
STATIC_FOLDER = 'View/static'
DATA_UPLOAD_FOLDER = 'input_data'
FRAMES_FOLDER = "frames_folder"

MAIN_PAGE_TITLE = "Computer Vision-based Pilates Detector"
MAIN_PAGE_SUBTITLE = 'A project by 2+2 for the Israel Tech Challenge'

MAX_FILE_SIZE = 5e9  # in bytes


FLASK_HOST = "0.0.0.0"
FLASK_PORT = 7070



MODEL_WEIGHTS = '21oct.h5'
MODELS_DIRECTORY = 'model_weights'



# shows x frames from the video that the user uploaded
SHOW_FRAMES = 2
SHOW_FRAMES_SKIP = 1  # in sec



########### PATHS ############

FRAMES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), FRAMES_FOLDER)
VIDEO_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), DATA_UPLOAD_FOLDER)
MODELS_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), MODELS_DIRECTORY)

