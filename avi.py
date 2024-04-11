import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

def calculate_age():
    birth_date_str = birth_entry.get()  # Get birthdate from entry widget
    try:
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        age_label.config(text=f"You are {age} years old", font=("Helvetica", 14, "bold"), foreground="blue")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid date (YYYY-MM-DD)")

# Create main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("350x200")  # Set window size

# Create label and entry for birthdate
ttk.Label(root, text="Enter your birthdate (YYYY-MM-DD):").pack(pady=10)
birth_entry = ttk.Entry(root, width=12, font=("Helvetica", 12))
birth_entry.pack(pady=5)

# Create button to calculate age
calculate_button = ttk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=10)

# Create label to display age
age_label = ttk.Label(root, text="", font=("Helvetica", 16))
age_label.pack(pady=10)

# Configure style for the window and widgets
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))
style.configure("TLabel", font=("Helvetica", 12))

# Run the main event loop
root.mainloop()
