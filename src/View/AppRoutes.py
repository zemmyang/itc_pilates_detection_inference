from flask import render_template, request
from werkzeug.utils import secure_filename
import os

from Control.FrameExtract import extract_frames
from Control.DeleteInputData import clear_input_data
from Model.RunPrediction import predict
from Model.GetUniqueFrames import get_unique_frames
from Model import SettingsAndPaths as CONST


def index_page():
    clear_input_data()

    return render_template('index.html',
                           page_title=CONST.MAIN_PAGE_TITLE,
                           page_subheader=CONST.MAIN_PAGE_SUBTITLE,
                           max_file_size=str(CONST.MAX_FILE_SIZE/1e9) + "GB")


def details_page():
    return render_template('details.html',
                           page_title="page for project details",
                           page_subheader='in progress',
                           text="etc")


def team_page():
    return render_template('team.html',
                           page_title="Meet the team: 2+2",
                           page_subheader='we are very good, yes?')


def show_uploaded_file(model):
    if request.method == 'POST':
        # put the file somewhere locally
        f = request.files['file']
        video_path = os.path.join(CONST.VIDEO_FOLDER, secure_filename(f.filename))
        f.save(video_path)

        # split the video into frames
        extract_frames(video_path, CONST.FRAMES_PATH)

        # run the model.predict
        res, per_frame_predictions = predict(model)

        # fd = FrameDisplay(video_path, output_type="CV")
        display = res.replace("_", " ").capitalize()

        unique_frames = get_unique_frames(per_frame_predictions)

        # output the analysis template
        return render_template("analysis.html", results=display, frame_display=unique_frames)
