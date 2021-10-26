# FRAME EXTRACTION

from cv2 import VideoCapture, imwrite


def extract_frames(video_path, frames_path):
    """
    :param video_path: the video path
    :param frames_path: the frames path
    :return:
    """

    # Frame rate
    FRAMES = 20
    # Max attempts before it will give up?
    MAX_ATTEMPTS = 10

    # storing the frames from training videos
    counter_videos = 0

    counter_frames = 0
    counter_attempts = 0

    cap = VideoCapture(video_path)  # capturing the video from the given path
    while cap.isOpened():
        ret, frame = cap.read()
        if ret is False:
            if counter_attempts < MAX_ATTEMPTS:
                counter_attempts += 1
                continue
            else:
                break
        if counter_frames < FRAMES:
            # storing the frames in a new folder named train
            filename = f'{frames_path}/video{counter_videos}_frame{counter_frames}.jpg'
            counter_frames += 1

            imwrite(filename, frame)
            # frame_videos_list.append({'video': video[NAME], 'image': filename, 'class': video[TAG]})
    counter_videos += 1

    cap.release()
    print('Done reading the videos and writing the frames')
    # return frame_videos_list
