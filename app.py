import streamlit as st
import os
import whisper
import tempfile
import librosa
from similarity import calculate_similarity
from pdf_report import generate_pdf
import matplotlib.pyplot as plt
import librosa.display

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Voice-Based Concept Understanding Analyser",
    page_icon="🎤",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🎤 Voice-Based Concept Understanding Analyser")

st.markdown("""
This AI-powered application evaluates how well you understand a concept by analyzing your spoken explanation.

### Features
- 🎙 Speech-to-Text using Whisper
- 🧠 Semantic Similarity Analysis
- 📊 Audio Fluency Analysis
- 📄 PDF Report Generation
""")

st.divider()

# -----------------------------
# Concept Selection
# -----------------------------
concept = st.selectbox(
    "📚 Select a Concept",
    [
        "Machine Learning",
        "Artificial Intelligence",
        "Cloud Computing"
    ]
)
# -----------------------------
# Reference Answers
# -----------------------------
reference_answers = {
    "Artificial Intelligence":
        "Artificial Intelligence is a branch of computer science that enables machines to perform tasks that normally require human intelligence. It is used in healthcare, self-driving cars, robotics, and virtual assistants.",

    "Machine Learning":
        "Machine Learning is a subset of Artificial Intelligence that enables computers to learn from data without being explicitly programmed. It uses algorithms to identify patterns and make predictions.",

    "Cloud Computing":
        "Cloud Computing is the delivery of computing services such as servers, storage, databases, networking, and software over the internet."
}
# -----------------------------
# Upload Audio
# -----------------------------
st.info("📌 Supported formats: WAV, MP3, M4A, MP4, OGG, OPUS, FLAC (Max 200 MB)")

audio_file = st.file_uploader(
    "🎵 Upload your Audio Explanation",
    type=["wav", "mp3", "m4a", "mp4", "ogg", "opus", "flac"],
    help="Upload a recording explaining the selected concept."
)

if audio_file:

    st.success("Audio uploaded successfully!")

    # Play Audio
    st.audio(audio_file)

    # Save Audio
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    save_path = os.path.join("uploads", audio_file.name)

    with open(save_path, "wb") as f:
        f.write(audio_file.getbuffer())

    st.write("📂 File saved successfully.")

    
    # Analyze Button
    if st.button("🚀 Analyze Concept"):

        with st.spinner("Loading Whisper model..."):
            model = whisper.load_model("base")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
            tmp_file.write(audio_file.read())
            temp_audio_path = tmp_file.name

        with st.spinner("Transcribing audio..."):
            result = model.transcribe(temp_audio_path)

        st.success("✅ Transcription Completed!")

        st.subheader("📝 Transcribed Text")
        st.write(result["text"])

      # -----------------------------
      # Semantic Similarity
      # -----------------------------
        score = calculate_similarity(
        reference_answers[concept],
        result["text"]
        )

        st.subheader("📊 Similarity Score")
        st.metric("Understanding Score", f"{score:.2f}%")

        # -----------------------------
        # Understanding Level
        # -----------------------------
        if score >= 85:
         level = "🟢 Excellent"

        elif score >= 70:
         level = "🟡 Good"

        elif score >= 50:
         level = "🟠 Fair"

        else:
         level = "🔴 Needs Improvement"

        st.subheader("🎓 Understanding Level")
        st.success(level)

        # -----------------------------
        # Fluency Analysis
        # -----------------------------

        audio, sr = librosa.load(temp_audio_path)

        duration = librosa.get_duration(y=audio, sr=sr)

        word_count = len(result["text"].split())

        wpm = (word_count / duration) * 60

        st.subheader("🎤 Fluency Analysis")

        st.write(f"⏱ Duration: {duration:.2f} seconds")
        st.write(f"📝 Words Spoken: {word_count}")
        st.write(f"⚡ Speaking Speed: {wpm:.2f} WPM")


        if wpm < 90:
            fluency = "🔴 Slow"

        elif wpm < 150:
            fluency = "🟢 Good"

        else:
            fluency = "🟠 Fast"

        st.write(f"🎓 Fluency: {fluency}")


        # ----------------------------------
        # Waveform Visualization
        # ----------------------------------

        st.subheader("📈 Audio Waveform")

        fig, ax = plt.subplots(figsize=(10,3))

        librosa.display.waveshow(audio, sr=sr, ax=ax)

        ax.set_title("Voice Waveform")
        ax.set_xlabel("Time (seconds)")
        ax.set_ylabel("Amplitude")

        st.pyplot(fig)
        plt.savefig("waveform.png", bbox_inches="tight")
        plt.close(fig)


        # ----------------------------------
        # Pause Detection
        # ----------------------------------

        import numpy as np

        st.subheader("⏸ Pause Analysis")

        # Silence threshold
        threshold = 0.01

        # Find silent samples
        silent_samples = np.abs(audio) < threshold

        # Total pause duration
        pause_duration = np.sum(silent_samples) / sr

        # Pause percentage
        pause_percent = (pause_duration / duration) * 100

        st.write(f"⏸ Total Pause Time: {pause_duration:.2f} seconds")
        st.write(f"📊 Pause Ratio: {pause_percent:.2f}%")

        if pause_percent < 10:
            pause_level = "🟢 Excellent"
        elif pause_percent < 20:
            pause_level = "🟡 Moderate"
        else:
            pause_level = "🔴 Too Many Pauses"

        st.write(f"🎯 Pause Quality: {pause_level}")


        # ----------------------------------
        # RMS Energy Analysis
        # ----------------------------------

        st.subheader("🔊 RMS Energy Analysis")

        # Calculate RMS Energy
        rms = librosa.feature.rms(y=audio)[0]

        # Average RMS
        avg_rms = rms.mean()

        st.write(f"🔊 Average RMS Energy: {avg_rms:.4f}")

        if avg_rms > 0.08:
            energy = "🟢 High Energy"
        elif avg_rms > 0.04:
            energy = "🟡 Moderate Energy"
        else:
            energy = "🔴 Low Energy"

        st.write(f"🎙 Voice Energy: {energy}")

        # ----------------------------------
        # Filler Word Detection
        # ----------------------------------

        st.subheader("🗣 Filler Word Analysis")

        # Common filler words
        fillers = [
            "um",
            "uh",
            "like",
            "you know",
            "actually",
            "basically",
            "so",
            "well"
        ]

        text = result["text"].lower()

        filler_count = 0
        found_fillers = {}

        for filler in fillers:
            count = text.count(filler)
            if count > 0:
                found_fillers[filler] = count
                filler_count += count

        st.write(f"📝 Total Filler Words: {filler_count}")

        if found_fillers:
            st.write("Detected Fillers:")
            st.json(found_fillers)
        else:
            st.success("✅ No filler words detected!")

        #Quality Rating
        if filler_count == 0:
            filler_level = "🟢 Excellent"
        elif filler_count <= 3:
            filler_level = "🟡 Good"
        else:
            filler_level = "🔴 Too Many Fillers"

        st.write(f"🎯 Filler Quality: {filler_level}")


        # ----------------------------------
        # AI Feedback
        # ----------------------------------

        st.subheader("🤖 AI Performance Summary")

        feedback = ""

        # Understanding
        if score >= 85:
            feedback += "The explanation demonstrates an excellent understanding of the selected concept. "
        elif score >= 70:
            feedback += "The explanation shows a good understanding of the concept, covering most of the important ideas. "
        elif score >= 50:
            feedback += "The explanation demonstrates a fair understanding of the concept but could include more relevant details. "
        else:
            feedback += "The explanation shows limited understanding of the concept and should include more accurate information. "

        # Speaking Speed
        if wpm < 90:
            feedback += "The speaking speed is slightly slow. "
        elif wpm <= 150:
            feedback += "The speaking speed is appropriate and easy to follow. "
        else:
            feedback += "The speaking speed is quite fast and may affect clarity. "

        # Pause Analysis
        if pause_percent < 10:
            feedback += "Very few pauses were detected, indicating smooth speech delivery. "
        elif pause_percent < 20:
            feedback += "A moderate number of pauses were detected, but the speech remained understandable. "
        else:
            feedback += "Frequent pauses were detected, which affected the flow of speech. "

        # Voice Energy
        if avg_rms > 0.08:
            feedback += "The voice energy was strong and confident. "
        elif avg_rms > 0.04:
            feedback += "The voice energy was moderate throughout the explanation. "
        else:
            feedback += "The voice energy was low; speaking with more confidence is recommended. "

        # Filler Words
        if filler_count == 0:
            feedback += "No filler words were detected, indicating clear communication."
        elif filler_count <= 3:
            feedback += "Only a few filler words were used, which did not significantly affect communication."
        else:
            feedback += "A high number of filler words were detected; reducing them will improve communication."

        st.info(feedback)

       
        # -----------------------------
        # Generate PDF
        # -----------------------------
        pdf_filename = "Concept_Report.pdf"

        generate_pdf(
        pdf_filename,
        concept,
        result["text"],
        score,
        level,
        duration,
        word_count,
        wpm,
        fluency,
        pause_duration,
        pause_percent,
        pause_level,
        avg_rms,
        energy,
        filler_count,
        filler_level,
        feedback
    )

        st.success("📄 PDF Report Generated Successfully!")

        with open(pdf_filename, "rb") as pdf_file:
         st.download_button(
        label="📥 Download PDF Report",
        data=pdf_file,
        file_name=pdf_filename,
        mime="application/pdf"
    )