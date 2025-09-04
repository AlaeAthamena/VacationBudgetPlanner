# Main Program

#Importing modules
from planner_app import PlannerApp
import tkinter as tk

#Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PlannerApp(root)
    root.mainloop()