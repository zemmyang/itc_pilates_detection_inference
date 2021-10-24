from tensorflow.keras.models import load_model
import requests
import os
from Model import SettingsAndPaths as CONF


def download_h5():
    path_to_h5 = "https://github.com/zemmyang/itc_pilates_detection_inference/raw/master/src/Model/model_weights/21oct.h5"
    r = requests.get(path_to_h5)
    with open(os.path.join(CONF.MODELS_PATH, CONF.MODEL_WEIGHTS), 'wb') as f:
        f.write(r.content)
    print("Downloaded h5 file")


def model_reconstruct():
    if not os.path.isfile(os.path.join(CONF.MODELS_PATH, CONF.MODEL_WEIGHTS)):
        print("h5 file not found, downloading")
        download_h5()

    print("Loading model...")
    model = load_model(os.path.join(CONF.MODELS_PATH, CONF.MODEL_WEIGHTS))
    return model
