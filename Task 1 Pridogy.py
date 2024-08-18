import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    temp = float(entry_temp.get())
    unit = entry_unit.get().strip().upper()

    if unit == 'K':
        celsius = temp - 273.15
        fahrenheit = 1.8 * (temp - 273.15) + 32
        result = f"Temperature in Celsius (C): {celsius:.2f}\nTemperature in Fahrenheit (F): {fahrenheit:.2f}"
    elif unit == 'F':
        celsius = (temp - 32) * 5 / 9
        kelvin = (temp - 32) * 5 / 9 + 273.15
        result = f"Temperature in Celsius (C): {celsius:.2f}\nTemperature in Kelvin (K): {kelvin:.2f}"
    elif unit == 'C':
        fahrenheit = temp * 9 / 5 + 32
        kelvin = temp + 273.15
        result = f"Temperature in Fahrenheit (F): {fahrenheit:.2f}\nTemperature in Kelvin (K): {kelvin:.2f}"
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid temperature unit (K, C, or F).")
        return
    
    label_result.config(text=result)


root = tk.Tk()
root.title("Temperature Converter")


label_temp = tk.Label(root, text="Enter temperature:")
label_temp.grid(row=0, column=0, padx=10, pady=5)

entry_temp = tk.Entry(root)
entry_temp.grid(row=0, column=1, padx=10, pady=5)

label_unit = tk.Label(root, text="Enter unit (K/C/F):")
label_unit.grid(row=1, column=0, padx=10, pady=5)

entry_unit = tk.Entry(root)
entry_unit.grid(row=1, column=1, padx=10, pady=5)

button_convert = tk.Button(root, text="Convert", command=convert_temperature)
button_convert.grid(row=2, columnspan=2, pady=10)

label_result = tk.Label(root, text="", justify=tk.LEFT)
label_result.grid(row=3, columnspan=2, padx=10, pady=5)


root.mainloop()
