

import tkinter as tk
from tkinter import ttk

def convert():
    try:
        val = float(entry.get())
        ct = conversion_type.get()
        direction = conversion_direction.get()

        if ct == "Length":
            if direction == "Km to Miles":
                result = f"{val} kilometers = {round(val * 0.6214, 2)} miles"
            else:
                result = f"{val} miles = {round(val / 0.6214, 2)} kilometers"

        elif ct == "Weight":
            if direction == "Kg to Pounds":
                result = f"{val} kilograms = {round(val * 2.2046, 2)} pounds"
            else:
                result = f"{val} pounds = {round(val / 2.2046, 2)} kilograms"

        elif ct == "Temperature":
            if direction == "C to F":
                result = f"{val}°C = {round((val * 9/5) + 32, 2)}°F"
            else:
                result = f"{val}°F = {round((val - 32) * 5/9, 2)}°C"

        result_label.config(text=result)
    except:
        result_label.config(text="Please enter a valid number.")

def update_direction(event=None):
    ct = conversion_type.get()
    if ct == "Length":
        direction_menu["values"] = ["Km to Miles", "Miles to Km"]
        conversion_direction.set("Km to Miles")
    elif ct == "Weight":
        direction_menu["values"] = ["Kg to Pounds", "Pounds to Kg"]
        conversion_direction.set("Kg to Pounds")
    elif ct == "Temperature":
        direction_menu["values"] = ["C to F", "F to C"]
        conversion_direction.set("C to F")

root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")
root.config(bg="#f8f9fa")

tk.Label(root, text="Unit Converter", font=("Arial", 16, "bold"), bg="#f8f9fa").pack(pady=10)

conversion_type = tk.StringVar()
conversion_dropdown = ttk.Combobox(root, textvariable=conversion_type, state="readonly", font=("Arial", 12))
conversion_dropdown["values"] = ["Length", "Weight", "Temperature"]
conversion_dropdown.current(0)
conversion_dropdown.bind("<<ComboboxSelected>>", update_direction)
conversion_dropdown.pack(pady=5)

conversion_direction = tk.StringVar()
direction_menu = ttk.Combobox(root, textvariable=conversion_direction, state="readonly", font=("Arial", 12))
direction_menu.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 12), width=20)
entry.pack(pady=10)

convert_btn = tk.Button(root, text="Convert", font=("Arial", 12), bg="#4caf50", fg="white", width=15, command=convert)
convert_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f8f9fa", fg="#333")
result_label.pack(pady=10)

update_direction()
root.mainloop()





