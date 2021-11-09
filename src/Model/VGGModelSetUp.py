from tensorflow.keras.models import load_model
import os
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

        for obj in bucket.objects:
            if not os.path.exists(os.path.dirname(obj.key)):
                os.makedirs(os.path.dirname(obj.key))
            bucket.download_file(obj.key, os.path.join(CONF.MODELS_PATH, obj.key))

    model = load_model(os.path.join(CONF.MODELS_PATH, CONF.MODEL_WEIGHTS))
    return model
