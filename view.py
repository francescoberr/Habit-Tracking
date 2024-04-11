import tkinter
from tkinter import ttk
from tkinter import messagebox

window = tkinter.Tk()
window.title("Habit Tracking App")

frame = tkinter.Frame(window)
frame.pack()

# --- Start Habit Creation Outer Frame ---

habit_creation_frame = tkinter.LabelFrame(frame, text="Here you can create an habit", borderwidth=5)
habit_creation_frame.grid(row=0, column=0, padx=20, pady=10)

new_habit_label = tkinter.Label(habit_creation_frame, text="Create your habit:", font='Helvetica 12 bold')
new_habit_label.grid(row=0, column=0)
predefined_habit_label = tkinter.Label(habit_creation_frame, text="Or choose a predefined one:", font='Helvetica 12 bold')
predefined_habit_label.grid(row=0, column=1)

new_habit_entry = tkinter.Entry(habit_creation_frame)
new_habit_entry.grid(row=1, column=0)

predefined_habit_combobox = ttk.Combobox(habit_creation_frame, values=["Exercise", "Drinking", "Studying", "Reading", "Meditate"])
predefined_habit_combobox.grid(row=1, column=1)

for widget in habit_creation_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

    # --- Start Habit Creation Inner Frame ---
periodicity_frame = tkinter.LabelFrame(habit_creation_frame, text="Choose a periodicity") 
periodicity_frame.grid(row=2, column=0, padx=0, pady=5, sticky="news", columnspan=2)

daily_radiobutton = tkinter.Radiobutton(periodicity_frame, text="Daily", value="daily")
daily_radiobutton.grid(row=0, column=0)
weekly_radiobutton = tkinter.Radiobutton(periodicity_frame, text="Weekly", value="weekly")
weekly_radiobutton.grid(row=0, column=1)

for widget in periodicity_frame.winfo_children():
    widget.grid_configure(padx=80, pady=5)
    # --- End Habit Creation Inner Frame ---

create_button = tkinter.Button(habit_creation_frame, text="CREATE")
create_button.grid(row=3, column=0, columnspan=2, pady=5)

# --- End Habit Creation Outer Frame ---

# --- Start Habit Completion Frame ---

habit_completion_frame = tkinter.LabelFrame(frame, text="Here you can mark an habit \"complete\"", borderwidth=5)
habit_completion_frame.grid(row=1, column=0, padx=20, pady=10, sticky="news", columnspan=2)

completed_habit_label = tkinter.Label(habit_completion_frame, text="Name", font='Helvetica 12 bold')
completed_habit_label.grid(row=0, column=0)
completed_habit_entry = tkinter.Entry(habit_completion_frame)
completed_habit_entry.grid(row=1, column=0, pady=5)

completed_checkbox_label = tkinter.Label(habit_completion_frame, text="Completed?", font='Helvetica 12 bold')
completed_checkbox_label.grid(row=0, column=1)
completed_var = tkinter.StringVar(value="Not Completed")
completed_checkbox = tkinter.Checkbutton(habit_completion_frame, text="I've completed this habit", variable=completed_var, onvalue="Completed", offvalue="Not Completed")
completed_checkbox.grid(row=1, column=1, pady=5)

for widget in habit_completion_frame.winfo_children():
    widget.grid_configure(padx=20)

    # --- Start Inner Habit Completion Frame ---
submit_button_frame = tkinter.LabelFrame(habit_completion_frame)
submit_button_frame.grid(row=2, column=0, sticky="news", columnspan=2)

submit_complete = tkinter.Button(submit_button_frame, text="SUBMIT")
submit_complete.grid(row=0, pady=5, padx=182)
    # --- End Inner Habit Completion Frame ---

# --- End Habit Completion Frame ---

# --- Start Habit Analysis Frame ---

habit_analysis_frame = tkinter.LabelFrame(frame, text="Here you can analyze your habits", borderwidth=5)
habit_analysis_frame.grid(row=2, column=0, padx=20, pady=10, sticky="news", columnspan=2)

currently_tracked_button = tkinter.Button(habit_analysis_frame, text="Currently Tracked Habits")
currently_tracked_button.grid(row=0, column=0)

same_periodicity_button = tkinter.Button(habit_analysis_frame, text="Same periodicity Habits")
same_periodicity_button.grid(row=0, column=1)

longest_streak_of_all_button = tkinter.Button(habit_analysis_frame, text="Longest streak (all)")
longest_streak_of_all_button.grid(row=1, column=0)

longest_streak_single_button = tkinter.Button(habit_analysis_frame, text="Longest streak (single)")
longest_streak_single_button.grid(row=1, column=1)

for widget in habit_analysis_frame.winfo_children():
    widget.grid_configure(padx=20, pady=5)

window.mainloop()