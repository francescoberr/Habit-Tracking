import sqlite3
from datetime import datetime


class Habit:
    def __init__(self, name, habit_type='daily', date=None, completed=False):
        self.name = name
        self.habit_type = habit_type
        self.date = date or datetime.now()  # Current date if it's not provided
        self.completed = completed

class HabitDataBase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Habits
                               (id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                habit_type TEXT,
                                date INTEGER,
                                completed INTEGER)''')
        self.conn.commit()

    def insert_habit(self, habit):
        self.cursor.execute('''INSERT INTO Habits (name, habit_type, date, completed)
                               VALUES (?, ?, ?, ?)''', (habit.name, habit.habit_type, habit.date, habit.completed))
        self.conn.commit()

    def close(self):
        self.conn.close()
    