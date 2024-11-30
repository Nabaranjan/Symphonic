import streamlit as st
from backend.gemini_api import query_gemini
from backend.langchain import generate_prompt

# App Configuration
st.set_page_config(
    page_title="Literature & Poetry Hub",
    page_icon="📚",
    layout="wide"
)

# App Title
st.title("📖 Literature & Poetry Hub")
st.markdown(
    """
    Welcome to the **Literature & Poetry Hub**, a platform for exploring the beauty of words and expressions.  
    Personalize your preferences, submit a query, or select from timeless classics to receive a tailored response in your chosen language.
    """
)

# Sidebar for Customization
st.sidebar.header("🔧 Customize Your Experience")
language = st.sidebar.radio("🌐 Select Language", ["Odia", "Hindi", "English"])
lang_map = {"Odia": "or", "Hindi": "hi", "English": "en"}

mode = st.sidebar.selectbox("✍️ Response Format", ["Prose", "Poetry", "Narrative", "Philosophical"])
tone = st.sidebar.selectbox("🎭 Tone of Response", ["Neutral", "Formal", "Casual", "Passionate", "Contemplative", "Humorous"])

# Footer
footer = st.sidebar.markdown(
    """
    Developed by **Aditya**  
    © 2024 | All Rights Reserved
    """
)

# User Input Section
st.subheader("🔍 Enter Your Query")
query = st.text_input("Type your topic, theme, or idea (e.g., 'love', 'nature', etc.)")

st.markdown("##### Or select from famous works:")
preloaded_queries = {
    "Odia": ["ଉତ୍କଳ ଗୀତ", "ଅଭିମନ୍ୟୁ ଉପାଖ୍ୟାନ"],
    "Hindi": ["रामायण की कथा", "महाकवि सूरदास के दोहे"],
    "English": ["Shakespearean sonnet", "Romanticism themes"]
}
example_query = st.selectbox("🔖 Choose from popular works", [""] + preloaded_queries[language])

# Automatically use the example query if no manual input
if example_query and not query:
    query = example_query

# Generate Response
if st.button("Generate Response"):
    if query:
        with st.spinner("Crafting a response..."):
            # Generate the prompt
            prompt = generate_prompt(
                query=query, 
                language=lang_map[language], 
                mode=mode.lower(), 
                tone=tone.lower()
            )
            # Query the Gemini API
            response = query_gemini(
                context=f"You are a literature and poetry expert, responding in {language}.", 
                prompt=prompt
            )

        # Display the Response
        if response:
            st.success("### Generated Response:")
            st.markdown(f"**{mode} in {language} ({tone} tone):**")
            st.write(response)
        else:
            st.error("⚠️ No response received. Please try again later.")
    else:
        st.warning("⚠️ Please enter a query or select a famous work.")

