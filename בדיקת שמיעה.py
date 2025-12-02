import tkinter as tk
from tkinter import ttk
import winsound

def play_beep():
    try:
        freq = int(freq_var.get())
        dur_sec = float(dur_var.get())  # מספר שניות
        dur_ms = int(dur_sec * 1000)    # המרה למילי-שניות
        winsound.Beep(freq, dur_ms)
    except ValueError:
        pass  # אם המשתמש לא בחר ערך תקין פשוט לא ננגן

root = tk.Tk()
root.title("בדיקת שמיעה")

frame = ttk.Frame(root, padding=20)
frame.pack()

# תדרים אפשריים
frequencies = [str(f) for f in range(0, 22000, 500)]
# זמני השמעה במספר שניות
durations = ["1", "2"]

freq_var = tk.StringVar(value="1000")
dur_var = tk.StringVar(value="1")

# קומבובוקס לתדר
ttk.Label(frame, text="תדר (Hz):", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
freq_combo = ttk.Combobox(frame, textvariable=freq_var, values=frequencies, width=10)
freq_combo.grid(row=0, column=1, padx=10, pady=10)

# קומבובוקס לזמן בשניות
ttk.Label(frame, text="משך (שניות):", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
dur_combo = ttk.Combobox(frame, textvariable=dur_var, values=durations, width=10)
dur_combo.grid(row=1, column=1, padx=10, pady=10)

# כפתור להשמעה
ttk.Button(frame, text="השמע צליל", command=play_beep).grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
