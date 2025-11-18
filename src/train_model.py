import os
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from extract_features import extract_features

os.makedirs("../model", exist_ok=True)

DATA = "../data"
features, labels = [], []

for label in os.listdir(DATA):
    d = os.path.join(DATA, label)
    if not os.path.isdir(d): continue
    for f in os.listdir(d):
        p = os.path.join(d, f)
        try:
            feat = extract_features(p)
            features.append(feat); labels.append(label)
        except: pass

X, y = np.array(features), np.array(labels)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))
joblib.dump(model, "../model/sound_model.pkl")
