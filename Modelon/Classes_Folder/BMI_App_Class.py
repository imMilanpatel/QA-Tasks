# This file contains the Class template for a GUI Design of BMI Application.

# Imports
import tkinter as tk
from tkinter import messagebox
from Classes_Folder.BMI_Class import BMICalculator


# Class definition
class BMIApp:

    # Constructor initializing the GUI elements.
    def __init__(self, master, width=400, height=300):
        self.master = master
        self.master.title("BMI Calculator")

        # Set window size and prevent resizing
        self.master.geometry(f"{width}x{height}")
        self.master.resizable(False, False)

        # Create a frame to hold the UI elements
        self.frame = tk.Frame(master)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Adding a label to UI "Weight (kg) and it's respective user input entry box"
        self.label_weight = tk.Label(self.frame, text="Weight (kg):")
        self.label_weight.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

        self.entry_weight = tk.Entry(self.frame)
        self.entry_weight.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        # Adding a label to UI "Height (m): and it's respective user input entry box"
        self.label_height = tk.Label(self.frame, text="Height (m):")
        self.label_height.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

        self.entry_height = tk.Entry(self.frame)
        self.entry_height.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        # Adding Calculate button to the UI
        self.btn_calculate = tk.Button(self.frame, text="Calculate BMI", command=self.calculate_bmi)
        self.btn_calculate.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

        # Adding Logout button to the UI.
        self.btn_logout = tk.Button(self.frame, text="Logout", command=self.logout)
        self.btn_logout.grid(row=3, column=0, columnspan=2, padx=10, pady=10)



    # Function to be called when user clicks "Calculate button"
    def calculate_bmi(self):
        weight_str = self.entry_weight.get().strip()
        height_str = self.entry_height.get().strip()

        # Basic Error checking for invalid user inputs and prompting it.
        if not weight_str or not height_str:
            messagebox.showerror("Error", "Please enter both weight and height.")
            return

        try:
            weight = float(weight_str)
            height = float(height_str)

            if weight <= 0 or height <= 0:
                messagebox.showerror("Error", "Weight and height must be positive numbers.")
                return

            calculator = BMICalculator()
            bmi = calculator.calculate_bmi(weight, height)

            if bmi is not None:
                category = calculator.get_bmi_category(bmi)
                messagebox.showinfo("BMI Result", f"Your BMI: {bmi:.2f}\nCategory: {category}")
            else:
                messagebox.showerror("Error", "Invalid input. Please enter valid weight and height.")
        
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numeric values for weight and height.")


    # Function to be called when user clicks #Logout button
    def logout(self):
        self.master.destroy()

if __name__ == "__main__":
    BMIApp