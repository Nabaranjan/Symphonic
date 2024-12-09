import streamlit as st
from backend.gemini_api import query_gemini
from backend.langchain import generate_prompt
from gtts import gTTS
import re
from io import BytesIO

# App Configuration
st.set_page_config(
    page_title="Symphonic: Literature & Poetry Hub",
    page_icon="🎶",
    layout="wide"  # Centered layout for a more professional feel
)

# Load custom CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Load the CSS file
load_css("Ui/Style.css")

# Remove special characters and improve formatting
def clean_text(text):
    # Retain only alphabetic characters, numbers, punctuation, and spaces
    clean_text = re.sub(r'[^a-zA-Z0-9.,!?;:()\'\" \n]', '', text)
    return re.sub(r'\s+', ' ', clean_text).strip()


# Header Section
st.markdown(
    """
    <h1 class="main-title">🎶 Symphonic: Literature & Poetry Hub</h1>
    <p class="subtitle">✨ Experience the symphony of words, crafted uniquely for you ✨</p>
    <div class="divider"></div>
    """,
    unsafe_allow_html=True,
)

# About Project Section
st.markdown(
    """
    ### 📝 About This Project
    **Symphonic** is your gateway to personalized literature and poetry, blending the art of words with AI precision. 
    From timeless classics to creative modern renditions, Symphonic caters to your literary cravings. 

    **✨ Features:**
    - 🌐 **Multi-language Support**: Respond in **English**, **Hindi**, or **Odia**.
    - 🎭 **Custom Styles**: Choose between prose, poetry, narrative, or philosophical formats.
    - 🎨 **Dynamic Tones**: From neutral to contemplative, select your preferred tone.

    Perfect for enthusiasts, students, and professionals seeking inspiration or literary magic. 🪄
    """
)
st.divider()

# Layout Configuration
st.markdown("### 🎨 **Customize Your Response**")
# Language, Mode, Tone Selection
language = st.radio("🌐 Select Language", ["Odia", "Hindi", "English"], horizontal=True)
mode = st.selectbox("✍️ **Response Format**", ["Prose 🖋️", "Poetry 🎼", "Narrative 📖", "Philosophical 🧘‍♂️"])
tone = st.selectbox(
    "🎭 **Tone of Response**", 
    ["Neutral 🤝", "Formal 🧑‍⚖️", "Casual 😊", "Passionate ❤️", "Contemplative 🤔", "Humorous 😄"]
)

# User Input Query
st.markdown("### 🔍 **Enter Your Query**")
query = st.text_input("💡 Type your topic, theme, or idea (e.g., 'love', 'nature')")


# Generate Response Button
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
if st.button("🎤 **Generate Response**"):
    if query:
        with st.spinner("🎶 Composing your literary masterpiece..."):
            # Generate the prompt
            prompt = generate_prompt(
                query=query, 
                language=language.lower(), 
                mode=mode.split()[0].lower(),  # Extracting plain text mode
                tone=tone.split()[0].lower()  # Extracting plain text tone
            )
            # Query the Gemini API
            response = query_gemini(
                context=f"You are a literature and poetry expert, responding in {language}.", 
                prompt=prompt
            )

        # Display the Response
        if response:
            st.success("### 🎶 **Your Symphonic Creation**:")
            st.markdown(f"**{mode} in {language} ({tone}):**")
            st.write(response)
            clean_response = clean_text(response)
            tts = gTTS(clean_response)
            audio_file = BytesIO()
            tts.write_to_fp(audio_file)
            st.audio(audio_file, format='audio/mp3')
        else:
            st.error("⚠️ No response received. Please try again later.")
    else:
        st.warning("⚠️ Please enter a query or select a famous work.")

# Footer Section
st.markdown(
    """
    <div class="footer">
        Developed with ❤️ by <b>Aditya</b> | © 2024 Symphonic🎶
    </div>
    """,
    unsafe_allow_html=True,
)
