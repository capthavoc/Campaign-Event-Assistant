# This is the class definition of generic events

# Will we want different event types? possibly, but this is fine for now.

class Event:
    
    def __init__(self, event_title):
        print("Event Initialized.")
        self.title = event_title
        
    # All Events need:
    # -required conditions for when they can occur
    # -a way to relate to other events/signal them?
    
    # TO BE ADDED: some kind of file storage for storing information between game sessions
    # (Use Jpickle)
    