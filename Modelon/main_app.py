# This is the main application file for the BMI App
# All the depenedant classes files are called here in this file.

# Imports
import tkinter as tk
from Classes_Folder.BMI_App_Class import BMIApp



# Initializing Class instance for BMI GUI.
def main():
    root = tk.Tk()
    
    # Set desired window size (e.g., 400x400)
    window_width = 400
    window_height = 400
    
    app = BMIApp(root, width=window_width, height=window_height)
    center_window(root)  # Center the main window on the screen
    root.mainloop()


# This function is used to center the window
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == "__main__":
    main()