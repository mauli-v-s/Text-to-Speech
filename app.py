import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import pandas as pd
import numpy as np

import nltk
from gtts import gTTS
import os
import tempfile

# Download necessary NLTK resources
nltk.download('punkt')

def text_to_speech(text, language='en'):
    """Converts text to speech and plays it in the web page."""
    # Tokenize the text into sentences
    sentences = nltk.sent_tokenize(text)

    # Create a temporary directory for audio files
    with tempfile.TemporaryDirectory() as tmpdir:
        audio_files = []

        # Convert each sentence to speech and save to temporary files
        for idx, sentence in enumerate(sentences):
            tts = gTTS(text=sentence, lang=language, slow=False)
            filename = f"output_{idx}.mp3"
            filepath = os.path.join(tmpdir, filename)
            tts.save(filepath)
            audio_files.append(filepath)

        # Play the audio files
        for file in audio_files:
            st.audio(file, format='audio/mp3')

        # Clean up temporary audio files (not strictly necessary in this case)
        for file in audio_files:
            os.remove(file)

    st.success("Text-to-speech conversion complete.")

# Create a Streamlit app interface
def home():
    st.write("""
    <style>
    .animated-background {
        animation: slide 50s linear infinite alternate;
        background-image: url('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2Fhistory-improvements-text-to-speech-technology-altaf-hossain-limon&psig=AOvVaw0y-M7DsMoVcAQlJSP_HjS_&ust=1712251870258000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPCM0t3JpoUDFQAAAAAdAAAAABAK'); /* Add your background image URL here */
        background-size: cover;
        width: 50%;
        height: 50vh;
        overflow: hidden;
        background-color: pink;
    }

    @keyframes slide {
        0% { background-position-x: 0%; }
        100% { background-position-x: 100%; }
    }
    </style>
    <div class="animated-background"></div>
    """, unsafe_allow_html=True)

    st.write("<h1 style='text-align: center;'>Welcome to the Text to Speech App</h1>", unsafe_allow_html=True)

    st.title("Text to Speech Converter")

    input_text = st.text_area("Enter text to convert to speech")

    if st.button("Convert to Speech"):
        if input_text:
            text_to_speech(input_text)
        else:
            st.warning("Please enter some text to convert.")

def main():
    st.set_page_config(layout="wide")
    st.title("Text To Speech App")
    # Create the tab layout
    # Show the appropriate page based on the user selection
    home()

main()
