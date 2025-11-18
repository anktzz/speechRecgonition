import librosa
import numpy as np

def extract_features(file_path):
    audio, sr = librosa.load(file_path, duration=2)
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=20)
    return np.mean(mfccs.T, axis=0)
