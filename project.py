import tkinter as tk
from time import strftime

def time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, time)  # update every 1 second

# Create main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("350x150")
root.resizable(False, False)
root.configure(bg='black')

# Create and style the label
label = tk.Label(root, font=('Arial', 50, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center', pady=20)

# Start the clock
time()

# Run the GUI loop
root.mainloop()