# fdds/models/triggers.py

class Trigger:
    """
    Base class for all triggers in FDDS.
    """

    def __init__(self, name, event, action):
        """
        Initializes the trigger.
        
        :param name: The name of the trigger.
        :param event: The event that triggers the action (e.g., 'INSERT', 'UPDATE', 'DELETE').
        :param action: A callable that defines the action to be performed.
        """
        self.name = name
        self.event = event
        self.action = action

    def execute(self, row):
        """
        Executes the trigger's action.
        
        :param row: The row of data that caused the trigger to fire.
        """
        self.action(row)

class TriggerManager:
    """
    Manages triggers for a table in FDDS.
    """

    def __init__(self):
        self.triggers = []

    def add_trigger(self, trigger):
        """
        Adds a new trigger to the manager.
        
        :param trigger: The trigger to add.
        """
        self.triggers.append(trigger)

    def remove_trigger(self, trigger_name):
        """
        Removes a trigger by name.
        
        :param trigger_name: The name of the trigger to remove.
        """
        self.triggers = [t for t in self.triggers if t.name != trigger_name]

    def execute_triggers(self, event, row):
        """
        Executes all triggers associated with a given event.
        
        :param event: The event that occurred (e.g., 'INSERT', 'UPDATE', 'DELETE').
        :param row: The row of data that caused the trigger to fire.
        """
        for trigger in self.triggers:
            if trigger.event == event:
                trigger.execute(row)
