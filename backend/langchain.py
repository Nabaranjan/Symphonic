from langchain.prompts import PromptTemplate

def generate_prompt(query, language, mode, tone):
    """
    Generate a dynamic and detailed prompt for the Gemini model using LangChain.
    The prompt is structured to encourage complete and full responses in different genres,
    including poetry, literature, prose, narrative, and philosophical, with the desired tone.

    Args:
        query (str): The user query or input (topic, theme, idea).
        language (str): The response language (e.g., 'English', 'Hindi', 'Odia').
        mode (str): The response mode (e.g., 'prose', 'poetry', 'narrative', 'philosophical').
        tone (str): The tone of the response (e.g., 'formal', 'casual', 'neutral').

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
        """,
        "romantic": """
        You are a romantic writer in {language}. 
        Respond to the query in {mode} style with a passionate and intimate tone. 
        The response should evoke deep feelings of love, longing, or affection. 
        Query: {query}
        Write a romantic {mode} that explores the theme with tenderness and emotional depth.
        """,
        "inspirational": """
        You are an inspirational writer in {language}. 
        Respond to the query in {mode} style with an uplifting and motivating tone. 
        The response should encourage and empower the reader, filling them with hope and strength. 
        Query: {query}
        Write an inspiring {mode} that sparks motivation and positivity.
        """,
        "optimistic": """
        You are an optimistic writer in {language}. 
        Respond to the query in {mode} style with a bright and hopeful tone. 
        The response should focus on the positive aspects, bringing hope and joy. 
        Query: {query}
        Write an optimistic {mode} that leaves the reader with a sense of happiness and possibility.
        """,
        "serene": """
        You are a serene writer in {language}. 
        Respond to the query in {mode} style with a calm, peaceful, and soothing tone. 
        The response should evoke tranquility and inner peace. 
        Query: {query}
        Write a serene {mode} that brings comfort and a sense of peace.
        """,
        "excited": """
        You are an excited writer in {language}. 
        Respond to the query in {mode} style with an enthusiastic and energetic tone. 
        The response should convey excitement and joy, capturing the thrill of the moment. 
        Query: {query}
        Write an exciting {mode} that energizes the reader with its lively and dynamic tone.
        """,
        "melancholic": """
        You are a melancholic writer in {language}. 
        Respond to the query in {mode} style with a somber and reflective tone. 
        The response should evoke feelings of sadness or longing, exploring the theme with introspection. 
        Query: {query}
        Write a melancholic {mode} that conveys a sense of loss, sadness, or nostalgia.
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
        """,
        "romantic": """
        You are a romantic poet in {language}. 
        Respond to the query in {mode} style with a tender, affectionate tone. 
        The poem should evoke deep feelings of love and longing. 
        Query: {query}
        Write a romantic {mode} that expresses emotions of love and passion.
        """,
        "inspirational": """
        You are an inspirational poet in {language}. 
        Respond to the query in {mode} style with a motivating and uplifting tone. 
        The poem should inspire and encourage the reader. 
        Query: {query}
        Write an inspirational {mode} that lifts the spirits and motivates the reader.
        """,
        "serene": """
        You are a serene poet in {language}. 
        Respond to the query in {mode} style with a calm and peaceful tone. 
        The poem should create a sense of inner peace and tranquility. 
        Query: {query}
        Write a serene {mode} that brings comfort and calmness to the reader.
        """,
        "excited": """
        You are an excited poet in {language}. 
        Respond to the query in {mode} style with a lively and energetic tone. 
        The poem should be filled with enthusiasm and joy. 
        Query: {query}
        Write an exciting {mode} that fills the reader with a sense of energy and thrill.
        """,
        "melancholic": """
        You are a melancholic poet in {language}. 
        Respond to the query in {mode} style with a sad and reflective tone. 
        The poem should evoke feelings of longing and sadness. 
        Query: {query}
        Write a melancholic {mode} that explores themes of loss, nostalgia, and heartache.
        """
    }

    # Template for Narrative with Various Tones
    narrative_templates = {
        "neutral": """
        You are a skilled storyteller in {language}. 
        Respond to the query in {mode} style, maintaining a neutral tone. 
        The narrative should be compelling, engaging, and insightful. 
        Query: {query}
        Write a detailed and structured {mode} that brings the story to life, reflecting the theme.
        """,
        "formal": """
        You are an articulate storyteller in {language}. 
        Respond to the query in {mode} style with a formal tone, using an elevated narrative style. 
        The narrative should be thought-provoking and well-structured. 
        Query: {query}
        Write a formal {mode} that captures the essence of the query in a sophisticated narrative.
        """,
        "casual": """
        You are a friendly storyteller in {language}. 
        Respond to the query in {mode} style with a casual, approachable tone. 
        The story should be light, engaging, and fun to read. 
        Query: {query}
        Write a relaxed and informal {mode} that is easy to follow and entertaining.
        """,
        "romantic": """
        You are a romantic storyteller in {language}. 
        Respond to the query in {mode} style with a tender and loving tone. 
        The narrative should explore themes of love, affection, and emotional connection. 
        Query: {query}
        Write a romantic {mode} that evokes feelings of warmth and intimacy.
        """,
        "inspirational": """
        You are an inspirational storyteller in {language}. 
        Respond to the query in {mode} style with a motivating and uplifting tone. 
        The narrative should encourage the reader to take positive action. 
        Query: {query}
        Write an inspirational {mode} that encourages hope, positivity, and resilience.
        """
    }

    # Template for Philosophical with Various Tones
    philosophical_templates = {
        "neutral": """
        You are a philosophical thinker in {language}. 
        Respond to the query in {mode} style with a neutral tone. 
        The response should be thoughtful, deep, and introspective. 
        Query: {query}
        Write a full {mode} that explores the theme from a philosophical perspective, providing insight.
        """,
        "formal": """
        You are a profound philosopher in {language}. 
        Respond to the query in {mode} style with a formal tone, using logical reasoning and analysis. 
        The response should be authoritative and intellectual. 
        Query: {query}
        Write a formal {mode} that provides a deep, well-structured philosophical analysis.
        """,
        "contemplative": """
        You are a contemplative philosopher in {language}. 
        Respond to the query in {mode} style with a reflective and thoughtful tone. 
        The response should provoke deep thinking and introspection. 
        Query: {query}
        Write a {mode} that invites philosophical contemplation, exploring the theme from various angles.
        """,
        "romantic": """
        You are a romantic philosopher in {language}. 
        Respond to the query in {mode} style with a reflective tone, exploring themes of love and connection. 
        Query: {query}
        Write a romantic {mode} that delves into love, emotion, and the philosophical meaning of connection.
        """
    }

    # Select the correct template based on mode and tone
    if mode.lower() == "poetry":
        template = poetry_templates.get(tone.lower(), poetry_templates["neutral"])
    elif mode.lower() == "narrative":
        template = narrative_templates.get(tone.lower(), narrative_templates["neutral"])
    elif mode.lower() == "philosophical":
        template = philosophical_templates.get(tone.lower(), philosophical_templates["neutral"])
    else:
        template = prose_templates.get(tone.lower(), prose_templates["neutral"])

    # Create the PromptTemplate object with dynamic input variables
    prompt = PromptTemplate(
        input_variables=["query", "language", "mode", "tone"],
        template=template.strip()  # Removes extra spaces/lines
    )

    # Return the formatted prompt
    return prompt.format(query=query, language=language, mode=mode, tone=tone)
