from datetime import datetime

class Habit:
    def __init__(self, name, habit_type='daily', date=None, completed=False):
        self.name = name
        self.habit_type = habit_type
        self.date = date or datetime.now()  # Current date if it's not provided
        self.completed = completed

# class HabitDB:
#     def __init__(self):
