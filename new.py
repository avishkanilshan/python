import tkinter as tk
from datetime import datetime

def calculate_age():
    birth_date_str = birth_entry.get()  # Get birthdate from entry widget
    try:
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        age_label.config(text=f"Your age is {age} years")
    except ValueError:
        age_label.config(text="Please enter a valid date (YYYY-MM-DD)")

# Create main window
root = tk.Tk()
root.title("Age Calculator")

# Create label and entry for birthdate
tk.Label(root, text="Enter your birthdate (YYYY-MM-DD):").pack(pady=10)
birth_entry = tk.Entry(root)
birth_entry.pack(pady=5)

# Create button to calculate age
calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=10)

# Create label to display age
age_label = tk.Label(root, text="")
age_label.pack(pady=10)

# Run the main event loop
root.mainloop()