from tensorflow.keras.models import load_model
import zipfile
import os
from pathlib import Path
from glob import glob
from Model import SettingsAndPaths as CONF


def model_reconstruct():
    if os.path.isfile(os.path.join(CONF.MODELS_PATH, CONF.MODEL_WEIGHTS)):
        print("Loading model...")
    else:
        print("Model not found, unzipping from archives...")
        zip_list = [Path(i) for i in glob(f'{CONF.MODELS_PATH}/21oct.h5.zip.*')]

        for zipName in zip_list:
            with open(os.path.join(CONF.MODELS_PATH, "21oct.zip"), "ab") as f, \
                    open(os.path.join(CONF.MODELS_PATH, zipName), "rb") as z:
                f.write(z.read())

        print(f"Model zip: {os.path.isfile(os.path.join(CONF.MODELS_PATH, '21oct.zip'))}")
        with zipfile.ZipFile(os.path.join(CONF.MODELS_PATH, "21oct.zip"), "r") as zipObj:
            zipObj.extractall(os.path.join(CONF.MODELS_PATH, '21oct.h5'))

        [os.remove(file)for file in zip_list]
        os.remove(os.path.join(CONF.MODELS_PATH, "21oct.zip"))

    model = load_model(os.path.join(CONF.MODELS_PATH, CONF.MODEL_WEIGHTS))
    return model
