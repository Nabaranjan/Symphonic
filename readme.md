

# 📖 **Symphonic** : A Harmonious Journey Through Literature & Poetry


Welcome to the **Symphonic**, an interactive platform designed to explore the beauty of words, poetry, and literature. With the power of AI, users can query a vast range of topics in their chosen language and receive expertly crafted responses in prose or poetry, with customizable tones.

---

## 🔧 **Table of Contents**
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
  - [Setting Up API Keys](#setting-up-api-keys)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## 📚 **Project Overview**

The **Symphonic** offers users the ability to:
- Select from a variety of languages (Odia, Hindi, English).
- Choose between prose and poetry formats.
- Set the tone of the response (Neutral, Formal, Casual).
- Receive responses to user queries based on preloaded literary works or custom topics.

This project integrates LangChain for dynamic prompt generation and the Gemini API to generate rich literary responses.

---

## 🚀 **Features**
- **Customizable Response Style**: Prose or poetry with tone control.
- **Multi-language Support**: Odia, Hindi, and English.
- **Famous Works**: Preloaded literary works for quick access.
- **Interactive Interface**: Built with Streamlit for a smooth user experience.

---

## 🛠 **Installation**

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/CYBERBULL123/Symphonic.git
    cd Symphonic
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## ⚙️ **Configuration**

To use the API keys securely and configure the environment, follow the steps below:

### **Setting Up API Keys**

1. **Create a `secrets.toml` file**:
   - After cloning the repository, navigate to the `.streamlit` folder.
   - Copy the `secrets.toml.sample` file and rename it to `secrets.toml`.

     ```bash
     cp .streamlit/secrets.toml.sample .streamlit/secrets.toml
     ```

2. **Edit the `secrets.toml` file**:
   - Open the `secrets.toml` file in a text editor and replace the placeholders with your actual API keys and secrets.
   
   Example `secrets.toml` file:

   ```toml
   # secrets.toml.sample

    # Sample API Key for Gemini (users should replace this with their actual API key)

    [api_keys]
    gemini = "your-gemini-api-key-here"


   ```

3. **Ensure that the `.gitignore` file is configured**:
   The `.gitignore` file should already include the following line to ignore the `secrets.toml` file from being committed to version control.

   ```txt
   # Ignore the secrets file
   .streamlit/secrets.toml
   ```

4. **Load Secrets in Your App**:
   The `secrets.toml` file will automatically be loaded by Streamlit. You can access these secrets in your app as shown 

---

## 🖥 **Usage**

1. **Running the app**:
    - After setting up your environment and secrets, run the app using the following command:
      ```bash
      streamlit run app.py
      ```

2. **Interacting with the app**:
    - **Language Selection**: Choose between Odia, Hindi, or English.
    - **Response Style**: Select between Prose or Poetry.
    - **Tone**: Set the tone of the response (Neutral, Formal, Casual).
    - **Query Input**: Enter your query (e.g., a theme, topic, or famous work).

    The app will generate a literary response based on your inputs, returning either prose or poetry with the selected tone.

---

## 🤝 **Contributing**

We welcome contributions to this project! If you'd like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Open a pull request with a clear description of your changes.

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### **Project Structure**

Here's the directory structure of the project:

```plaintext
Symphonic
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore configuration
├── .streamlit/
│   └── secrets.toml.sample # Sample secrets file
└── backend/
    ├── gemini_api.py     # API integration for Gemini
    ├── langchain.py      # LangChain prompt generation
    └── __pycache__/      # Compiled Python files
```

---

