import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def load_saved_artifacts():
    global __locations
    global __data_columns
    global __model

    print("Loading saved artifacts...")

    with open("artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]

    __locations = __data_columns[3:]

    with open("artifacts/model.pkl", "rb") as f:
        __model = pickle.load(f)

    print("Artifacts loaded successfully.")


def get_location_names():
    return __locations


def predict_price(location, sqft, bath, bhk):
    loc_index = -1

    try:
        loc_index = __data_columns.index(location)
    except ValueError:
        pass

    x = np.zeros(len(__data_columns))

    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


# Load model automatically when util.py is imported
load_saved_artifacts()