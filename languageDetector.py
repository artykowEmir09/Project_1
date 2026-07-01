import fasttext
import tkinter as tk
from tkinter import messagebox

# 📦 Model path
MODEL_PATH = r"C:\fasttext\lid.176.bin"

# load model
model = fasttext.load_model(MODEL_PATH)

# language mapping
language_mapping = {
    "en": "English",
    "tr": "Turkish",
    "id": "Indonesian",
    "ms": "Malay",
    "nl": "Dutch",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "sw": "Swahili"
}

# 🎯 detect function
def detect_language():
    text = entry.get()

    if not text.strip():
        messagebox.showwarning("Warning", "Please enter text!")
        return

    label, prob = model.predict(text)
    lang_code = label[0].replace("__label__", "")

    result_text = f"""
🌍 Language: {language_mapping.get(lang_code, lang_code)}
📊 Confidence: {prob[0]*100:.2f}%
"""

    result_label.config(text=result_text)


# 🖥️ UI window
window = tk.Tk()
window.title("Language Detector AI")
window.geometry("400x250")

# input box
entry = tk.Entry(window, width=40)
entry.pack(pady=20)

# button
btn = tk.Button(window, text="Detect Language", command=detect_language)
btn.pack()

# result label
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=20)

# run app
window.mainloop()
