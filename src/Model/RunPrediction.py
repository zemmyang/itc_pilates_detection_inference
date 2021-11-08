from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np
# from scipy import stats
import pandas as pd
from glob import glob
from pathlib import Path

from Model import SettingsAndPaths as CONST


def predict(model):
    ONLY = 0
    pred_df = pd.get_dummies(pd.Series(['double_leg', 'rollup', 'criss_cross']))

    frames_path = [Path(file) for file in glob(f"{CONST.FRAMES_PATH}/*.jpg")]

    prediction_images = []
    for k, frame in enumerate(frames_path):
        img = image.load_img(frame, target_size=(224, 224, 3))
        img = image.img_to_array(img)
        prediction_images.append(img)
        print(f"Running predict on frame {k}")

    prediction_images = preprocess_input(np.array(prediction_images))
    prediction = np.argmax(model.predict(prediction_images), axis=-1)

    # return pred_df.columns.values[stats.mode(prediction)[ONLY][ONLY]], pred_df.columns.values[prediction]
    return pred_df.columns.values[no_scipy_mode(prediction)], pred_df.columns.values[prediction]


def no_scipy_mode(arr):
    return np.apply_along_axis(lambda x: np.bincount(x).argmax(), axis=0, arr=arr)
