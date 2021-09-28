import os
import zipfile
import gdown
import json

import program_constants as CONF
from model_setup import get_model


with open(CONF.GDRIVE_DIRECTORY, 'r') as f:
    directory = json.load(f)

model_parameters = directory[CONF.MODEL_WEIGHTS]
gdrive_link = 'https://drive.google.com/uc?id={}'.format(model_parameters['link'])
extracted_model_path = os.path.join(CONF.MODELS_PATH, model_parameters['path'])


gdown.download(gdrive_link, "temp_weights.zip", quiet=False)

with zipfile.ZipFile('temp_weights.zip', 'r') as zip_ref:
    zip_ref.extractall(CONF.MODELS_PATH)
os.remove("temp_weights.zip")

model = get_model(extracted_model_path)

print(model.summary())
