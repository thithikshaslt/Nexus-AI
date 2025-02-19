# ChatApp - Unbound Hackathon Challenge

## Overview
ChatApp is a Django-based chat system that supports LLM integrations with special routing for regex-based prompt redirection and file uploads. This project was developed for the Unbound Hackathon Challenge.

## Features
- **Dynamic Model Provider System**: Fetch supported providers and models from the database.
- **Chat Completion API**: Send prompts and receive responses from the selected model.
- **Regex-Based Routing**: Redirects prompts to different models based on regex rules.
- **Simple Web UI**: Frontend built using HTML, CSS, and JavaScript for chat interaction.
- **Special Routing for File Uploads**: Routes uploaded files to designated models based on file type.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/thithikshaslt/Unbound-Security-Hackathon-2025.git
cd chatapp
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional for Admin Access)
```bash
python manage.py createsuperuser
```

### 6. Start the Server
```bash
python manage.py runserver
```

The API is now available at `http://127.0.0.1:8000/api/v1/`.

---

## API Endpoints

### 1. Fetch Available Models
**Endpoint:** `GET /api/v1/models/`

Response:
```json
{
  "models": [
    {"provider": "anthropic", "model": "claude-v1"},
    {"provider": "openai", "model": "gpt-3.5"}
  ]
}
```

### 2. Chat Completion
**Endpoint:** `POST /api/v1/chat/completions/`

Request Body:
```json
{
  "provider": "openai",
  "model": "gpt-4",
  "prompt": "Hello, how are you?"
}
```

Response:
```json
{
  "provider": "openai",
  "model": "gpt-4",
  "response": "I'm doing great! How can I assist you today?"
}
```

### 3. File Upload Routing
**Endpoint:** `POST /api/v1/upload/`

Request Body:
```json
{
  "file": "example.pdf"
}
```

Response:
```json
{
  "provider": "anthropic",
  "model": "claude-v1",
  "response": "Anthropic: File processed with secure file analysis."
}
```

---

## Design Choices & Architecture
- **Django & Django REST Framework (DRF)**: Provides structured API endpoints.
- **Regex-Based Prompt Routing**: Ensures prompts are directed to the right model.
- **Database-Driven Model Configuration**: Admin can define routing rules dynamically.
- **Frontend UI**: Simple HTML, CSS, and JavaScript-based chat interface.
- **File Upload Processing**: Special routing logic directs files to designated models.

---

## Frontend Usage
The chat interface is built using vanilla HTML, CSS, and JavaScript.
- Open `templates/chat.html` in the browser.
- Enter a prompt and receive responses from the backend API.

---

## Demo Video
A demo showcasing the project in action can be found [here](#) (Replace with actual video link).

