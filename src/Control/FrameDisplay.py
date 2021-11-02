from typing import List
import numpy as np
from cv2 import VideoCapture, CAP_PROP_POS_MSEC, CAP_PROP_FPS, waitKey, destroyAllWindows, \
    cvtColor, COLOR_BGR2RGB, imread
import io
from PIL import Image
import base64

from Model import SettingsAndPaths as CONST


class FrameDisplay:
    def __init__(self):
        self._images = []
        self._decoded_images = []

# -------------------- internal functions ------------------- #

    @staticmethod
    def decode_for_flask(image, caption) -> str:
        image = imread(str(image))

        # convert BGR to RGB
        image = cvtColor(image, COLOR_BGR2RGB)

        # convert numpy array to PIL Image
        img = Image.fromarray(image.astype('uint8'))

        # create file-object in memory
        file_object = io.BytesIO()

        # write PNG in file-object
        img.save(file_object, 'PNG')

        # move to beginning of file so `send_file()` it will read from start
        file_object.seek(0)

        data = file_object.getvalue()  # get data from file (BytesIO)

        data = base64.b64encode(data)  # convert to base64 as bytes
        data = data.decode()  # convert bytes to string

        # return '<img src="data:image/png;base64,{image}" class="img-thumbnail w-50" />'.format(image=data)

        return """
                <figure class="figure">
                    <img src="data:image/png;base64,{image}" class="img-fluid img-thumbnail h-200 /">
                        <figcaption class="figure-caption">Prediction: {caption}</figcaption>
                </figure>
                """.format(image=data, caption=caption.replace("_", " ").capitalize())

# -------------------- external functions ------------------- #
    def add_image(self, image_path, caption="") -> None:
        self._images.append(image_path)
        self._decoded_images.append(self.decode_for_flask(image_path, caption))

    # --------------------- magic functions --------------------- #

    def __getitem__(self, item):
        return self._decoded_images[item]

    def __len__(self):
        return len(self._images)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self):
            result = self[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration
