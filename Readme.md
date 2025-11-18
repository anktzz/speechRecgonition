Here is a **clean, polished, GitHub-ready README** with badges and professional layout — **all in one copy-paste block** just like before:

---

```markdown
# 🎧 Sound Classification ML Project  
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

A machine learning project that classifies short audio clips (beep, clap, noise, etc.) using **Python**, **Librosa**, **Scikit-Learn**, and **FastAPI**.  
Includes a full backend API and a reusable ML pipeline.

---

## 📁 Project Structure

```

speechRecognition/
│
├── dataset/               # Training audio dataset
│   ├── beep/
│   ├── clap/
│   └── noise/
│
├── model/
│   └── sound_model.pkl    # Saved ML model (after training)
│
├── src/
│   ├── extract_features.py
│   ├── train_model.py
│   └── predict.py
│
├── api/
│   └── main.py            # FastAPI server
│
├── requirements.txt
└── README.md

````

---

# ⚙️ Installation & Setup

## 1️⃣ Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
````

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### The requirements file should contain:

```
librosa
numpy
scikit-learn
soundfile
fastapi
uvicorn
python-multipart
joblib
```

---

# 🎤 3️⃣ Prepare the Dataset

Add audio files organized like this:

```
dataset/beep/*.wav
dataset/clap/*.wav
dataset/noise/*.wav
```

✔ Use `.wav` format
✔ 1–3 seconds recommended
✔ The label = the folder name

---

# 🧠 4️⃣ Train the ML Model

Run the training script:

```bash
python src/train_model.py
```

This creates:

```
model/sound_model.pkl
```

If `model/` doesn’t exist:

```bash
mkdir model
```

---

# 🚀 5️⃣ Run the FastAPI Server

Start the backend API:

```bash
uvicorn api.main:app --reload
```

API URL:

```
http://127.0.0.1:8000
```

---

# 🔊 6️⃣ Make Predictions (Send Audio)

## Option A — Using curl

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@your_audio.wav"
```

Response example:

```json
{
  "prediction": "clap"
}
```

---

## Option B — Python client example

```python
import requests

url = "http://127.0.0.1:8000/predict"
file = {'file': open("sound.wav", "rb")}
res = requests.post(url, files=file)

print(res.json())
```

Run:

```bash
python test_predict.py
```

---

# 🛠 Common Issues & Fixes

### ❌ `FileNotFoundError: ../model/sound_model.pkl`

➡️ Fix:

```bash
mkdir model
python src/train_model.py
```

---

### ❌ Missing python-multipart

```
RuntimeError: Form data requires "python-multipart"
```

➡️ Fix:

```bash
pip install python-multipart
```

---

### ❌ 404 at "/"

Not an issue — you can add this if you want:

```python
@app.get("/")
def home():
    return {"message": "Sound Classification API Running"}
```

---

# 🌟 Features

✔ Audio feature extraction using Librosa
✔ ML model using RandomForestClassifier
✔ Easy-to-train dataset folder structure
✔ FastAPI backend for audio inference
✔ Upload audio via API or Python client
✔ Clean, modular code

---

# 📜 License

This project is released under the **MIT License**.

---

# 🙌 Contributions

Pull requests are welcome — add more sound classes, UI frontends, or improved models.

---

# 🎉 You're Ready!

Your sound classification ML system is now fully operational.
If you want, I can generate a **React frontend UI** that uploads audio and shows predictions.

```
```

