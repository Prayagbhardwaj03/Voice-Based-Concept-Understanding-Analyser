from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image
import os


def generate_pdf(
    filename,
    concept,
    transcript,
    similarity,
    level,
    duration,
    words,
    wpm,
    fluency,
    pause_time,
    pause_ratio,
    pause_quality,
    rms_energy,
    energy_level,
    filler_count,
    filler_quality,
    ai_feedback
):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("<b>Voice-Based Concept Understanding Analyser</b>", styles["Title"]))
    elements.append(Paragraph("<br/>", styles["Normal"]))

    elements.append(Paragraph(f"<b>Concept:</b> {concept}", styles["Normal"]))
    elements.append(Paragraph("<br/>", styles["Normal"]))

    elements.append(Paragraph("<b>Transcript:</b>", styles["Heading2"]))
    elements.append(Paragraph(transcript, styles["Normal"]))
    elements.append(Paragraph("<br/>", styles["Normal"]))
    # -----------------------------
    # Similarity Analysis
    # -----------------------------
    elements.append(Paragraph("<b>Similarity Analysis</b>", styles["Heading2"]))
    elements.append(Paragraph(f"Similarity Score: {similarity:.2f}%", styles["Normal"]))
    elements.append(Paragraph(f"Understanding Level: {level}", styles["Normal"]))
    elements.append(Paragraph("<br/><br/>", styles["Normal"]))

    elements.append(Paragraph("<b>Fluency Analysis</b>", styles["Heading2"]))
    elements.append(Paragraph(f"Duration: {duration:.2f} seconds", styles["Normal"]))
    elements.append(Paragraph(f"Words Spoken: {words}", styles["Normal"]))
    elements.append(Paragraph(f"Speaking Speed: {wpm:.2f} WPM", styles["Normal"]))
    elements.append(Paragraph(f"Fluency: {fluency}", styles["Normal"]))
    
    # -----------------------------
    # Pause Analysis
    # -----------------------------
    elements.append(Paragraph("<br/><b>Pause Analysis</b>", styles["Heading2"]))
    elements.append(Paragraph(f"Total Pause Time: {pause_time:.2f} seconds", styles["Normal"]))
    elements.append(Paragraph(f"Pause Ratio: {pause_ratio:.2f}%", styles["Normal"]))
    elements.append(Paragraph(f"Pause Quality: {pause_quality}", styles["Normal"]))

    # -----------------------------
    # Voice Energy
    # -----------------------------
    elements.append(Paragraph("<br/><b>Voice Energy Analysis</b>", styles["Heading2"]))
    elements.append(Paragraph(f"Average RMS Energy: {rms_energy:.4f}", styles["Normal"]))
    elements.append(Paragraph(f"Energy Level: {energy_level}", styles["Normal"]))

    # -----------------------------
    # Filler Analysis
    # -----------------------------
    elements.append(Paragraph("<br/><b>Filler Word Analysis</b>", styles["Heading2"]))
    elements.append(Paragraph(f"Total Filler Words: {filler_count}", styles["Normal"]))
    elements.append(Paragraph(f"Filler Quality: {filler_quality}", styles["Normal"]))

    # -----------------------------
    # AI Performance Summary
    # -----------------------------
    elements.append(Paragraph("<br/><b>AI Performance Summary</b>", styles["Heading2"]))
    elements.append(Paragraph(ai_feedback, styles["Normal"]))

    

    # -----------------------------
    # Waveform
    # -----------------------------
    elements.append(Paragraph("<br/><b>Audio Waveform</b>", styles["Heading2"]))

    if os.path.exists("waveform.png"):
        img = Image("waveform.png", width=450, height=180)
        elements.append(img)

    # Always build the PDF
    doc.build(elements)