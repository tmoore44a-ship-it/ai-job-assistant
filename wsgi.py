"""
WSGI entry point for Render / Gunicorn.

Important:
- Our Flask application object lives in main.py
- Gunicorn uses this file when the start command is: gunicorn wsgi:app
"""

from main import app