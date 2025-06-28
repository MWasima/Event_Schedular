# Event Scheduler System

This is a simple Flask-based event scheduler system.

## Setup Instructions

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the Flask server:
```
python app.py
```

3. Use Postman to test the API endpoints:
- `GET /events`: Get all events
- `POST /events`: Create a new event
- `PUT /events/<id>`: Update an existing event
- `DELETE /events/<id>`: Delete an event
