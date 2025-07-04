# TSA Helper

An AI-powered web application to help Technology Student Association (TSA) students with event guidelines and requirements.

## Features

- 🤖 AI-powered chat assistant for each TSA event
- 📄 Automatic PDF processing and content extraction
- 💬 Interactive chat interface with context-aware responses
- 📱 Responsive design that works on all devices
- 🔄 Real-time chat with typing indicators
- 📊 Event statistics and overview

## Quick Start

### 1. Install Requirements

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 2. Add Your PDF Files

Create a `pdfs/` directory and add your TSA event guide PDF files:

\`\`\`
pdfs/
├── dragster_design.pdf
├── video_game_design.pdf
├── architectural_design.pdf
└── ... (other event guides)
\`\`\`

### 3. Run the Application

\`\`\`bash
python run.py
\`\`\`

Or directly:

\`\`\`bash
python app.py
\`\`\`

### 4. Open Your Browser

Navigate to: http://localhost:5000

## File Structure

\`\`\`
tsa-helper/
├── app.py                 # Main Flask application
├── run.py                 # Application runner with setup checks
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── static/
│   └── style.css         # Custom CSS styles
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Event selection page
│   ├── event.html        # Chat interface
│   └── error.html        # Error page
├── utils/
│   └── pdf_parser.py     # PDF text extraction
└── pdfs/                 # Your TSA event guide PDFs
    ├── dragster_design.pdf
    └── ... (other PDFs)
\`\`\`

## How It Works

1. **PDF Processing**: The application automatically reads all PDF files from the `pdfs/` directory and extracts their text content.

2. **Event Discovery**: Events are automatically discovered based on the PDF filenames in the directory.

3. **AI Integration**: Uses the Puter API (free OpenAI-compatible API) to provide intelligent responses based on the PDF content.

4. **Context-Aware Chat**: The AI assistant has access to the complete event guide content and can answer specific questions about rules, requirements, and judging criteria.

## API Configuration

The application uses the Puter API for AI responses. No API key is required as it's a free service. The API endpoint is configured in `app.py`:

```python
'https://api.puter.com/v1/chat/completions'
