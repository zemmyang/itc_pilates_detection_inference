from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from Model import SettingsAndPaths as CONST
import os

from Control.FrameExtract import extract_frames
from Control.FrameDisplay import FrameDisplay
from Model.RunPrediction import predict
from Model import SettingsAndPaths as CONF
from Model.VGGModelSetUp import model_reconstruct


app = Flask(__name__,
            template_folder=CONST.TEMPLATE_FOLDER,
            static_folder=CONST.STATIC_FOLDER)

model = model_reconstruct(os.path.join(CONF.MODELS_PATH, CONF.MODEL_WEIGHTS))


@app.route('/')
def index_page():
    return render_template('index.html',
                           page_title=CONST.MAIN_PAGE_TITLE,
                           page_subheader=CONST.MAIN_PAGE_SUBTITLE,
                           max_file_size=str(CONST.MAX_FILE_SIZE/1e9) + "GB")


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # put the file somewhere locally
        f = request.files['file']
        video_path = os.path.join(CONST.VIDEO_FOLDER, secure_filename(f.filename))
        f.save(video_path)

        # split the video into frames
        extract_frames(video_path, CONST.FRAMES_PATH)

        # run the model.predict
        res = predict(model)

        print(res)

        # fd = FrameDisplay(video_path, output_type="CV")

        # output the analysis template
        return render_template("analysis.html", frame_display=[res])


@app.route('/project')
def project_page():
    return render_template('details.html',
                           page_title="page for project details",
                           page_subheader='in progress',
                           text="etc")


@app.route('/team')
def team_page():
    return render_template('team.html',
                           page_title="Meet the team: 2+2",
                           page_subheader='we are very good, yes?')


@app.route('/test')
def image_test_page():
    return render_template('image_test.html',
                           image_list=[""])


if __name__ == '__main__':
    port = os.environ.get('PORT')

    if port:
        # 'PORT' variable exists - running on Heroku, listen on external IP and on given by Heroku port
        app.run(host='0.0.0.0', port=int(port))
    else:
        # running locally, run with default Flask values
        app.run()
