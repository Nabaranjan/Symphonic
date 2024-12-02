import streamlit as st
from backend.gemini_api import query_gemini
from backend.langchain import generate_prompt

# App Configuration
st.set_page_config(
    page_title="Symphonic: Literature & Poetry Hub",
    page_icon="🎶",
    layout="wide"
)

# Custom CSS
st.markdown(
    """
    <style>
        .main-title {
            font-size: 42px;
            font-weight: 900;
            color: #2E86AB;
            text-align: center;
        }
        .subtitle {
            font-size: 20px;
            color: #5D6D7E;
            text-align: center;
            margin-bottom: 20px;
        }
        .divider {
            margin: 20px 0;
            border-top: 2px solid #2E86AB;
        }
        .footer {
            text-align: center;
            color: #7D8CA3;
            font-size: 14px;
            margin-top: 50px;
        }
        .stButton button {
            background-color: #2E86AB !important;
            color: white !important;
            font-size: 16px !important;
            padding: 8px 20px !important;
            border-radius: 10px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

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
col1, col2 = st.columns(2)

# Column 1: Customization Options
with col1:
    st.markdown("### 🎨 **Customize Your Response**")
    language = st.radio("🌐 Select Language", ["Odia", "Hindi", "English"], horizontal=True)
    mode = st.selectbox("✍️ **Response Format**", ["Prose 🖋️", "Poetry 🎼", "Narrative 📖", "Philosophical 🧘‍♂️"])
    tone = st.selectbox(
        "🎭 **Tone of Response**", 
        ["Neutral 🤝", "Formal 🧑‍⚖️", "Casual 😊", "Passionate ❤️", "Contemplative 🤔", "Humorous 😄"]
    )

# Column 2: User Input
with col2:
    st.markdown("### 🔍 **Enter Your Query**")
    query = st.text_input("💡 Type your topic, theme, or idea (e.g., 'love', 'nature')")

    st.markdown("##### 🎯 **Or select from famous works:**")
    preloaded_queries = {
        "Odia": ["ଉତ୍କଳ ଗୀତ 🎶", "ଅଭିମନ୍ୟୁ ଉପାଖ୍ୟାନ 🔱"],
        "Hindi": ["रामायण की कथा 🕉️", "महाकवि सूरदास के दोहे 🌹"],
        "English": ["Shakespearean sonnet ✒️", "Romanticism themes 🌄"]
    }
    example_query = st.selectbox("🔖 **Choose from popular works**", [""] + preloaded_queries[language])

    # Automatically use the example query if no manual input
    if example_query and not query:
        query = example_query

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
