import uuid
from storage import Storage

class EventManager:
    def __init__(self):
        self.storage = Storage()

    def get_all_events(self):
        events = sorted(self.storage.load_events(), key=lambda x: x['start_time'])
        return {'events': events}

    def create_event(self, data):
        event = {
            'id': str(uuid.uuid4()),
            'title': data['title'],
            'description': data.get('description', ''),
            'start_time': data['start_time'],
            'end_time': data['end_time']
        }
        events = self.storage.load_events()
        events.append(event)
        self.storage.save_events(events)
        return {'message': 'Event created', 'event': event}

    def update_event(self, event_id, data):
        events = self.storage.load_events()
        for event in events:
            if event['id'] == event_id:
                event.update(data)
                self.storage.save_events(events)
                return {'message': 'Event updated', 'event': event}
        return {'message': 'Event not found'}, 404

    def delete_event(self, event_id):
        events = self.storage.load_events()
        events = [e for e in events if e['id'] != event_id]
        self.storage.save_events(events)
        return {'message': 'Event deleted'}
