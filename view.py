import tkinter
from tkinter import ttk
#from tkinter import messagebox
from model import Habit

# Grouping into HabitView class the creation of the view.
class HabitView(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title("Habit Tracking App")

        self.tab_control = ttk.Notebook(self)
        self.tab_control.pack(expand=1, fill="both")
        
        self.create_habit_page()
        self.track_habit_page()
        self.end_habit_page()
        self.analyze_habit_page()

    def create_habit_page(self):
        habit_creation_frame = ttk.Frame(self.tab_control)
        self.tab_control.add(habit_creation_frame, text="Create Habit")

        new_habit_label = ttk.Label(habit_creation_frame, text="Create your habit:", font='Helvetica 12 bold')
        new_habit_label.grid(row=0, column=0)
        predefined_habit_label = ttk.Label(habit_creation_frame, text="Or choose a predefined one:", font='Helvetica 12 bold')
        predefined_habit_label.grid(row=0, column=1)
        new_habit_entry = ttk.Entry(habit_creation_frame)
        new_habit_entry.grid(row=1, column=0)

        predefined_habit_combobox = ttk.Combobox(habit_creation_frame, values=["Exercise", "Drinking", "Studying", "Reading", "Meditate"])
        predefined_habit_combobox.grid(row=1, column=1)

        for widget in habit_creation_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

            # --- Start Habit Creation Inner Frame ---
        periodicity_frame = tkinter.LabelFrame(habit_creation_frame, text="Choose a periodicity") 
        periodicity_frame.grid(row=2, column=0, padx=0, pady=5, sticky="news", columnspan=2)

        daily_radiobutton = ttk.Radiobutton(periodicity_frame, text="Daily", value="daily")
        daily_radiobutton.grid(row=0, column=0)
        weekly_radiobutton = ttk.Radiobutton(periodicity_frame, text="Weekly", value="weekly")
        weekly_radiobutton.grid(row=0, column=1)

        for widget in periodicity_frame.winfo_children():
            widget.grid_configure(padx=80, pady=5)
            # --- End Habit Creation Inner Frame ---

        create_button = ttk.Button(habit_creation_frame, text="CREATE")
        create_button.grid(row=3, column=0, columnspan=2, pady=5)

    def track_habit_page(self):

        habit_tracking_frame = ttk.Frame(self.tab_control)
        self.tab_control.add(habit_tracking_frame, text="Track Habit")

        tracking_habit_label = ttk.Label(habit_tracking_frame, text="Name", font='Helvetica 12 bold')
        tracking_habit_label.grid(row=0, column=0)
        tracking_habit_entry = ttk.Entry(habit_tracking_frame)
        tracking_habit_entry.grid(row=1, column=0)

        tracking_checkbox_label = ttk.Label(habit_tracking_frame, text="Completed today/this week?", font='Helvetica 12 bold')
        tracking_checkbox_label.grid(row=0, column=1, pady=20)
        tracking_var = tkinter.StringVar(value="Not Completed")
        tracking_checkbox = ttk.Checkbutton(habit_tracking_frame, text="Completed", variable=tracking_var, onvalue="Completed", offvalue="Not Completed")
        tracking_checkbox.grid(row=1, column=1)

        for widget in habit_tracking_frame.winfo_children():
            widget.grid_configure(padx=20)

        # Adjusting button placement for symmetry
        submit_complete = ttk.Button(habit_tracking_frame, text="SUBMIT")
        submit_complete.grid(row=2, column=0, columnspan=2, pady=45)  # ew means east-west

    def end_habit_page(self):

        end_habit_frame = ttk.Frame(self.tab_control)
        self.tab_control.add(end_habit_frame, text="Drop Habit")

        end_habit_name_label = ttk.Label(end_habit_frame, text="Name", font='Helvetica 12 bold')
        end_habit_name_label.grid(row=0, column=0)
        end_habit_name_entry = ttk.Entry(end_habit_frame)
        end_habit_name_entry.grid(row=1, column=0, pady=5)

        end_habit_button_label = ttk.Label(end_habit_frame, text="Drop it?", font='Helvetica 12 bold')
        end_habit_button_label.grid(row=0, column=1)
        end_habit_button = ttk.Button(end_habit_frame, text="Drop it!")
        end_habit_button.grid(row=1, column=1, pady=5)

        for widget in end_habit_frame.winfo_children():
            widget.grid_configure(padx=35)

            
    def analyze_habit_page(self):
            
        habit_analysis_frame = ttk.Frame(self.tab_control)
        self.tab_control.add(habit_analysis_frame, text="Analyze Habit")

        currently_tracked_button = ttk.Button(habit_analysis_frame, text="Currently Tracked Habits")
        currently_tracked_button.grid(row=0, column=0)

        same_periodicity_button = ttk.Button(habit_analysis_frame, text="Same periodicity Habits")
        same_periodicity_button.grid(row=0, column=1)

        longest_streak_of_all_button = ttk.Button(habit_analysis_frame, text="Longest streak (all)")
        longest_streak_of_all_button.grid(row=1, column=0)

        longest_streak_single_button = ttk.Button(habit_analysis_frame, text="Longest streak (single)")
        longest_streak_single_button.grid(row=1, column=1)

        for widget in habit_analysis_frame.winfo_children():
            widget.grid_configure(padx=20, pady=30)
