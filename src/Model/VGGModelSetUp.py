from tensorflow.keras.models import load_model


def model_reconstruct(weights):
    model = load_model(weights)
    return model
