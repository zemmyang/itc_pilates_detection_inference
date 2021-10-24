from typing import List
import numpy as np
from cv2 import VideoCapture, CAP_PROP_POS_MSEC, CAP_PROP_FPS, waitKey, destroyAllWindows
import io
from PIL import Image
import base64

from Model import SettingsAndPaths as CONST


class FrameDisplay:
    """ takes the video that the user uploaded and displays it on the analysis page """
    def __init__(self, video, start_msec=0, output_type="NP"):
        self._video = video
        self._start_millisec = start_msec
        self._frames = List[np.ndarray]
        self._use_numpy_output = True if output_type == "NP" else False

        self._image_list = []
        self._open_and_read_video()

# ------------------- internal functions ------------------- #

    def _open_and_read_video(self):
        self._video_capture = VideoCapture(self._video)
        self._generate_frames()
        self._close_video()

    def _generate_frames(self):
        _frames_to_generate = CONST.SHOW_FRAMES
        _frames_delay = CONST.SHOW_FRAMES_SKIP
        _fps = int(self._video_capture.get(CAP_PROP_FPS))

        _count = 0
        while self._video_capture.isOpened():
            self._video_capture.set(CAP_PROP_POS_MSEC, self._start_millisec)
            _, _frame = self._video_capture.read()

            if _count == 0:
                print(_count)
                self._image_list.append(_frame)
            elif _count == int(_frames_delay * _fps):
                print(_count)
                self._image_list.append(_frame)
            _count += 1

            # Check end of video
            if waitKey(1) & 0xFF == ord('q'):
                break
            elif len(self._image_list) == _frames_to_generate:
                break

    def _close_video(self):
        self._video_capture.release()
        destroyAllWindows()

# ------------------- external functions ------------------- #

# ------------------- magic functions ------------------- #

    def __getitem__(self, item):
        if self._use_numpy_output:
            return self._image_list[item]
        else:
            return decode_for_flask(self._image_list[item])

    def __len__(self):
        return len(self._image_list)
        # return CONST.SHOW_FRAMES

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


def decode_for_flask(image):
    # convert BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

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

    return '<img src="data:image/png;base64,{}" class="img-thumbnail" />'.format(data)


# ------------------- for testing ------------------- #
if __name__ == '__main__':
    fd = FrameDisplay('./test.mkv')
    print([i.dtype for i in fd])
