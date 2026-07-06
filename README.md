# 🎤 Voice-Based Concept Understanding Analyser (VBCUA)

## 📌 Project Overview

The **Voice-Based Concept Understanding Analyser (VBCUA)** is an AI-powered web application that evaluates a user's conceptual understanding by analyzing spoken explanations. The system combines **speech recognition**, **semantic similarity analysis**, **audio signal processing**, and **automated report generation** to assess both conceptual knowledge and communication skills.

The application is built using **Python** and **Streamlit**, providing an interactive interface where users can upload an audio explanation of a selected concept and receive detailed AI-based feedback.

---

# 🎯 Objectives

- Evaluate conceptual understanding through spoken explanations.
- Convert speech into text using OpenAI Whisper.
- Measure semantic similarity between user explanations and reference concepts.
- Analyze speech fluency and communication quality.
- Generate a professional PDF performance report.

---

# ✨ Features

## 🎙 Speech-to-Text Transcription
- Converts uploaded audio into text using **OpenAI Whisper**.

## 🧠 Semantic Similarity Analysis
- Compares the user's explanation with a predefined reference answer using **Sentence Transformers**.
- Calculates an understanding score based on cosine similarity.

## 📊 Understanding Evaluation
Provides qualitative assessment:
- 🟢 Excellent
- 🟡 Good
- 🟠 Fair
- 🔴 Needs Improvement

## 🎤 Fluency Analysis
Evaluates:
- Speech Duration
- Word Count
- Speaking Speed (Words Per Minute)

## ⏸ Pause Analysis
Analyzes:
- Total Pause Time
- Pause Ratio
- Pause Quality

## 🔊 Voice Energy Analysis
Measures average RMS energy to estimate speaking confidence.

## 🗣 Filler Word Detection
Detects common filler words such as:
- um
- uh
- like
- basically
- actually
- so
- well

and provides communication quality feedback.

## 🤖 AI Performance Summary
Generates intelligent feedback based on:
- Concept Understanding
- Speaking Speed
- Pause Analysis
- Voice Energy
- Filler Word Usage

## 📈 Audio Waveform Visualization
Displays the waveform of the uploaded audio for visual speech analysis.

## 📄 PDF Report Generation
Generates a downloadable PDF report containing:
- Transcript
- Similarity Score
- Understanding Level
- Fluency Analysis
- Pause Analysis
- Voice Energy Analysis
- Filler Word Analysis
- AI Performance Summary
- Audio Waveform

---

# 🏗 Project Architecture

```
Audio Upload
      │
      ▼
OpenAI Whisper
      │
      ▼
Speech-to-Text
      │
      ▼
Sentence Transformer
      │
      ▼
Semantic Similarity
      │
      ▼
Audio Feature Extraction
 │      │      │
 ▼      ▼      ▼
Pause  RMS   Fillers
      │
      ▼
AI Performance Summary
      │
      ▼
PDF Report Generation
```

---

# 🛠 Technologies Used

### Programming Language
- Python

### Framework
- Streamlit

### AI / Machine Learning
- OpenAI Whisper
- Sentence Transformers
- Scikit-learn

### Audio Processing
- Librosa
- NumPy

### Visualization
- Matplotlib

### Report Generation
- ReportLab

---

# 📂 Project Structure

```
Voice-Based-Concept-Understanding-Analyser/

│── app.py
│── similarity.py
│── pdf_report.py
│── requirements.txt
│── README.md
│── .gitignore

├── assets/
├── images/
├── reference/
├── reports/
└── uploads/
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Voice-Based-Concept-Understanding-Analyser.git
```

Move into the project folder

```bash
cd Voice-Based-Concept-Understanding-Analyser
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📖 How to Use

1. Launch the Streamlit application.
2. Select a concept.
3. Upload an audio explanation.
4. Click **Analyze Concept**.
5. Review:
   - Transcript
   - Similarity Score
   - Understanding Level
   - Fluency Analysis
   - Pause Analysis
   - Voice Energy
   - Filler Word Analysis
   - AI Performance Summary
6. Download the generated PDF report.

---

# 📸 Sample Output

The application provides:

- Speech transcription
- Semantic similarity score
- Concept understanding evaluation
- Fluency metrics
- Pause statistics
- RMS energy analysis
- Filler word detection
- AI-generated feedback
- Audio waveform visualization
- PDF report

---

# 🚀 Future Enhancements

- Support for additional concepts.
- Real-time microphone recording.
- Multi-language speech recognition.
- User authentication.
- Performance history dashboard.
- Cloud deployment.
- Advanced AI feedback using Large Language Models.

---

# 👥 Team Members

- Prayag Bhardwaj
- Ayush Mirotha
- Gagan Aloriya
- Anushka
- Prinsu Singh

---

# 📜 License

This project was developed for educational and academic purposes as part of a B.Tech Artificial Intelligence project.

---

# 🙏 Acknowledgements

- OpenAI Whisper
- Sentence Transformers
- Streamlit
- Librosa
- ReportLab
- Scikit-learn