# 42 Jordan Chatbot

A Flask-based web chatbot powered by a fine-tuned DistilGPT-2 model, designed to answer questions about 42 Amman, 42 Irbid, the 42 Network, and Jordan-related topics. Features domain-restricted responses, conversation history, clickable links in answers, and a dark/light mode toggle for a sleek user experience.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Domain-Specific Responses**: Answers questions only about 42 Amman, 42 Irbid, the 42 Network, and Jordan, rejecting off-topic queries.
- **Conversation History**: Remembers prior interactions within a session for contextual responses.
- **Clickable Links**: URLs in answers render as clickable links using Markdown/HTML.
- **Dark/Light Mode**: Toggle between themes, with user preferences saved via `localStorage`.
- **Scalable API Integration**: Optional Groq API support for paraphrasing or expanding datasets.
- **Responsive UI**: Clean, modern interface built with HTML, CSS, and JavaScript.

## Tech Stack
- **Backend**: Flask (Python) for serving the chatbot and handling requests.
- **Model**: Fine-tuned DistilGPT-2 for lightweight, efficient NLP.
- **Frontend**: HTML, CSS, JavaScript with `marked` and `DOMPurify` for safe link rendering.
- **Optional Tools**:
  - LangChain for domain restriction and conversation memory.
  - Groq API for dataset expansion (paraphrasing Q&A pairs).
- **Data**: JSONL dataset with 1,000 Q&A pairs about 42 Amman/Irbid and Jordan.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/aliatyat/AI-hakton.git
   cd 42-jordan-chatbot
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Fine-Tuned Model**:
   - Place your fine-tuned DistilGPT-2 model in the `models/` directory.
   - Alternatively, fine-tune DistilGPT-2 using Hugging Face Transformers (see [Dataset](#dataset)).

5. **Configure Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your Groq API key (if used for paraphrasing):
     ```bash
     GROQ_API_KEY=your_groq_api_key
     ```

6. **Run the Application**:
   ```bash
   python app.py
   ```
   - Access the chatbot at `http://localhost:5000`.

## Usage
- **Interact with the Chatbot**:
  - Open the web interface in your browser.
  - Ask questions about 42 Amman, 42 Irbid, the 42 Network, or Jordan.
  - Example: "What is 42 Amman?" or "Tell me about Jordan’s culture."
  - Off-topic questions (e.g., "What’s the weather in Tokyo?") will be politely rejected.
- **Toggle Themes**: Click the theme button to switch between dark and light modes.
- **View Links**: Answers with URLs (e.g., 42 Amman’s website) render as clickable links.

## Dataset
- **Format**: JSONL with `prompt` and `completion` fields.
- **Content**: 1,000 Q&A pairs about 42 Amman, 42 Irbid, the 42 Network, and Jordan.
- **Source**: Expanded from an initial 100-question JSON file using paraphrasing (via Groq API or manual scripting).
- **Example**:
  ```json
  {"prompt": "What is 42 Amman?", "completion": "42 Amman is a tuition-free coding school in Jordan, part of the global 42 Network, offering innovative peer-to-peer learning. Learn more at <a href='https://www.42amman.com'>42 Amman</a>."}
  ```
- **Fine-Tuning**: Used with Hugging Face Transformers to train DistilGPT-2.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/awesome-feature`).
3. Commit changes (`git commit -m 'Add awesome feature'`).
4. Push to the branch (`git push origin feature/awesome-feature`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
