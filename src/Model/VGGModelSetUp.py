from tensorflow.keras.models import load_model
import os
from pathlib import Path
import boto3
from Model import SettingsAndPaths as CONF


def model_reconstruct():
    if os.path.isfile(os.path.join(CONF.MODELS_PATH, CONF.MODEL_WEIGHTS)):
        print("Loading model...")
    else:
        print("Model not found, downloading from AWS...")

        s3r = boto3.resource('s3', aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                             aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])
        bucket = s3r.Bucket(os.environ['S3_BUCKET_NAME'])

        for obj in bucket.objects.all():
            path, filename = os.path.split(obj.key)
            if filename:  # prevents loop from downloading empty directories
                print(f"Downloading {path, filename}")
                Path(os.path.join(CONF.MODELS_PATH, path)).mkdir(parents=True, exist_ok=True)
                bucket.download_file(obj.key, os.path.join(CONF.MODELS_PATH, path, filename))

    model = load_model(os.path.join(CONF.MODELS_PATH, CONF.MODEL_WEIGHTS))
    return model
