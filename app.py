from flask import Flask, request
from events import EventManager

app = Flask(__name__)
manager = EventManager()

@app.route('/events', methods=['GET'])
def get_events():
    return manager.get_all_events(), 200

@app.route('/events', methods=['POST'])
def create_event():
    data = request.json
    return manager.create_event(data), 201

@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.json
    return manager.update_event(event_id, data), 200

@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    return manager.delete_event(event_id), 204

if __name__ == '__main__':
    app.run(debug=True)
