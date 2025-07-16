# Database Chat Agent

A modern web application that allows users to interact with their e-commerce database using natural language. Built with Flask, Flask-Login, SQLAlchemy, Bootstrap 5, and Socket.IO, it features user authentication, admin dashboard, and a real-time AI-powered chat interface for querying business data.

## Features
- User registration and login
- Admin dashboard for managing users and viewing analytics
- Real-time chat interface to ask questions about sales, products, customers, inventory, orders, and analytics
- Beautiful, responsive UI with Bootstrap 5 and custom styles
- Flash messages for user feedback

## How It Works
- Users can register and log in to access the chat interface
- Admins have access to a dashboard for managing users and viewing key metrics
- The chat interface allows users to ask questions about their business data in natural language
- The backend processes queries and returns answers in real time

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chat_with_db_langchain.git
   cd chat_with_db_langchain
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   # On Windows:
   env\Scripts\activate
   # On macOS/Linux:
   source env/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```bash
   # If needed, run the provided seed/initialization scripts
   python -m app.commands.seeds
   ```
5. Run the application:
   ```bash
   flask run
   ```
   Or, if you have a main.py entry point:
   ```bash
   python main.py
   ```

6. Open your browser and go to `http://127.0.0.1:5000`

## Folder Structure
- `app/` - Main application package
- `app/templates/` - HTML templates
- `app/static/` - Static files (CSS, JS, images)
- `app/models.py` - Database models
- `app/auth/` - Authentication blueprint
- `app/admin/` - Admin dashboard blueprint
- `app/chat/` - Chat interface blueprint
- `main.py` - App entry point
- `requirements.txt` - Python dependencies

## License
MIT
