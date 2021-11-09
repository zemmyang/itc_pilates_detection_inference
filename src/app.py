from flask import Flask
from Model import SettingsAndPaths as CONST
import os

from Model.VGGModelSetUp import model_reconstruct
from View import AppRoutes

app = Flask(__name__,
            template_folder=CONST.TEMPLATE_FOLDER,
            static_folder=CONST.STATIC_FOLDER)

model = model_reconstruct()
CONST.create_folders()


@app.route('/')
def index_page():
    return AppRoutes.index_page()


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    return AppRoutes.show_uploaded_file(model=model)


@app.route("/clear", methods=['POST'])
def clear_data():
    return AppRoutes.index_page()


@app.route('/project')
def project_page():
    return AppRoutes.details_page()


@app.route('/team')
def team_page():
    return AppRoutes.team_page()


if __name__ == '__main__':
    port = os.environ.get('PORT')

    if port:
        # 'PORT' variable exists - running on Heroku, listen on external IP and on given by Heroku port
        app.run(host='0.0.0.0', port=int(port))
    else:
        # running locally, run with default Flask values
        app.run()
