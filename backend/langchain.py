from langchain.prompts import PromptTemplate

def generate_prompt(query, language, mode, tone):
    """
    Generate a dynamic and detailed prompt for the Gemini model using LangChain.
    The prompt is structured to encourage complete and full responses in different genres,
    including poetry, literature, and prose, with the desired tone.

    Args:
        query (str): The user query or input (topic, theme, idea).
        language (str): The response language (e.g., 'English', 'Hindi', 'Odia').
        mode (str): The response mode (e.g., 'prose', 'poetry').
        tone (str): The tone of the response (e.g., 'formal', 'casual').

    Returns:
        str: Formatted prompt string.
    """
    
    # Template for Prose with Various Tones
    prose_templates = {
        "neutral": """
        You are a skilled literature expert in {language}. 
        Respond to the query in {mode} style, maintaining a neutral tone. 
        The response should be comprehensive and insightful. 
        Query: {query}
        Write a full, well-structured {mode} response based on the theme or topic.
        """,
        "formal": """
        You are an eloquent writer in {language}. 
        Respond to the query in {mode} style with a formal tone, using sophisticated language and structure. 
        Provide a comprehensive and authoritative answer. 
        Query: {query}
        Write a formal {mode} that explores the query in depth.
        """,
        "casual": """
        You are a creative writer in {language}. 
        Respond to the query in {mode} style with a casual, friendly tone. 
        The response should be approachable, warm, and engaging. 
        Query: {query}
        Write a relaxed and informal {mode} that captures the essence of the theme.
        """
    }

    # Template for Poetry with Various Tones
    poetry_templates = {
        "neutral": """
        You are a poet in {language}. 
        Respond to the query in {mode} style with a neutral tone. 
        Write a full and expressive poem that captures the essence of the theme. 
        Query: {query}
        Write a complete {mode} piece that reflects the theme or idea with neutral emotional depth.
        """,
        "passionate": """
        You are a passionate poet in {language}. 
        Respond to the query in {mode} style with an emotional, intense tone. 
        The poem should evoke strong feelings and imagery. 
        Query: {query}
        Write a full {mode} that expresses the raw emotion and passion surrounding the theme.
        """,
        "contemplative": """
        You are a contemplative poet in {language}. 
        Respond to the query in {mode} style with a thoughtful and introspective tone. 
        The poem should explore deep philosophical or reflective themes. 
        Query: {query}
        Write a {mode} that invites contemplation and introspection, exploring the theme in depth.
        """,
        "humorous": """
        You are a witty poet in {language}. 
        Respond to the query in {mode} style with a humorous tone. 
        The poem should be lighthearted, playful, and amusing. 
        Query: {query}
        Write a humorous and entertaining {mode} that adds fun to the theme.
        """
    }

    # Select the correct template based on mode and tone
    if mode.lower() == "poetry":
        template = poetry_templates.get(tone.lower(), poetry_templates["neutral"])
    else:
        template = prose_templates.get(tone.lower(), prose_templates["neutral"])

    # Create the PromptTemplate object with dynamic input variables
    prompt = PromptTemplate(
        input_variables=["query", "language", "mode", "tone"],
        template=template.strip()  # Removes extra spaces/lines
    )

    # Return the formatted prompt
    return prompt.format(query=query, language=language, mode=mode, tone=tone)
