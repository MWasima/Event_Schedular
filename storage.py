import json
import os

class Storage:
    def __init__(self, filepath='data/events.json'):
        self.filepath = filepath
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                json.dump([], f)

    def load_events(self):
        with open(self.filepath, 'r') as f:
            return json.load(f)

    def save_events(self, events):
        with open(self.filepath, 'w') as f:
            json.dump(events, f, indent=4)
