import joblib
import pandas as pd
import sys, os, joblib
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from src.extract_features import extract_features

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODEL_PATH = os.path.join(ROOT_DIR, "model", "sound_model.pkl")

model = joblib.load(MODEL_PATH)

def predict_sound(path):
    feat = extract_features(path)
    return model.predict([feat])[0]
