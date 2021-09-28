from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.applications.vgg16 import VGG16


def get_model(model_weights):
    base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    base_model.trainable = False  ## Not trainable weights

    model = Sequential([base_model])
    model.add(Flatten())
    model.add(Dense(1024, activation='relu', input_shape=(25088,)))
    model.add(Dropout(0.5))
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(3, activation='softmax'))

    model.load_weights(model_weights)

    model.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])

    return model
