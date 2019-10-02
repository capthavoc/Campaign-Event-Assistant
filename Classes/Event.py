# This is the class definition of generic events

# Will we want different event types? possibly, but this is fine for now.

class Event:
    
    def __init__(self, event_title):
        print("Event Initialized.")
        self.title = event_title
        
    
    