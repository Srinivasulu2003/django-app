

```markdown
# Django Chatbot Project

## Overview

This project is a Django-based chatbot application that uses a Retrieval-Augmented Generation (RAG) model to answer user queries. The application can handle text input and support PDF file uploads to extract and process data from PDFs.

## Features

- **Text Queries**: Answer queries based on static text data.
- **PDF Uploads**: Upload PDF files, extract text, and query the content.
- **Conversation Memory**: Maintain context across multiple queries (optional implementation).

## Prerequisites

- Python 3.12 or higher
- Django
- LangChain libraries
- Cohere API key
- HuggingFace API token

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/chatbot_project.git
   cd chatbot_project
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   venv/Scripts/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API keys**:

   Set up your environment variables for the Cohere API key and HuggingFace token. You can add these to your `.env` file or set them directly in your environment:

   ```bash
   export COHERE_API_KEY='your_cohere_api_key'
   export HF_TOKEN='your_huggingface_token'
   ```

## Usage

1. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

2. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

3. **Access the chatbot**:

   Open your web browser and go to `http://127.0.0.1:8000/` to interact with the chatbot.

## Usage Instructions

1. **Send a Query**: Type your query in the input field and press "Send" to get a response based on the static text data or uploaded PDF content.

2. **Upload a PDF**: Use the file input to upload a PDF. The chatbot will extract the text and use it to answer your queries.

## Directory Structure

```
chatbot_project/
│
├── chatbot/                    # Django app for chatbot functionality
│   ├── migrations/             # Database migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── chatbot/
│           └── index.html
│
├── chatbot_project/            # Django project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py                   # Django management script
├── requirements.txt            # Project dependencies
└── README.md                   #this file
|__sample.txt                   # Text file
```

## Contributing

If you would like to contribute to this project, please fork the repository, create a new branch, and submit a pull request. Ensure that your code adheres to the project's coding standards and includes relevant tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [LangChain](https://www.langchain.com)
- [Cohere](https://cohere.ai)
- [HuggingFace](https://huggingface.co)

```

