#Planner Application module

#Importing modules
from tkinter import ttk, messagebox
import tkinter as tk
from classes import Destination, Activity, Budget

# Creating the travel planner apps class
class PlannerApp:
    '''
    This is the main class for the application
    '''
    def __init__(self, root):
        self.root = root
        self.root.title("Travel Planner")
        self.destinations = []
        self.budget = None
        # Setup GUI
        self.setup_gui()
    #Defining a function that sets up the GUI
    def setup_gui(self):
        #Creating destination Frame
        destination_frame = ttk.LabelFrame(self.root, text="Add Destination")
        destination_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        ttk.Label(destination_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.destination_name_entry = ttk.Entry(destination_frame)
        self.destination_name_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(destination_frame, text="Country:").grid(row=1, column=0, padx=5, pady=5)
        self.destination_country_entry = ttk.Entry(destination_frame)
        self.destination_country_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(destination_frame, text="Start Date:").grid(row=2, column=0, padx=5, pady=5)
        self.destination_start_date_entry = ttk.Entry(destination_frame)
        self.destination_start_date_entry.grid(row=2, column=1, padx=5, pady=5)
        ttk.Label(destination_frame, text="End Date:").grid(row=3, column=0, padx=5, pady=5)
        self.destination_end_date_entry = ttk.Entry(destination_frame)
        self.destination_end_date_entry.grid(row=3, column=1, padx=5, pady=5)
        add_destination_button = ttk.Button(destination_frame, text="Add Destination", command=self.add_destination)
        add_destination_button.grid(row=4, column=0, columnspan=2, pady=5)

        # Creating activity Frame
        activity_frame = ttk.LabelFrame(self.root, text="Add Activity")
        activity_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        ttk.Label(activity_frame, text="Destination:").grid(row=0, column=0, padx=5, pady=5)
        self.destination_combobox = ttk.Combobox(activity_frame, state="readonly")
        self.destination_combobox.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(activity_frame, text="Activity Name:").grid(row=1, column=0, padx=5, pady=5)
        self.activity_name_entry = ttk.Entry(activity_frame)
        self.activity_name_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(activity_frame, text="Category:").grid(row=2, column=0, padx=5, pady=5)
        self.activity_category_entry = ttk.Entry(activity_frame)
        self.activity_category_entry.grid(row=2, column=1, padx=5, pady=5)
        ttk.Label(activity_frame, text="Cost:").grid(row=3, column=0, padx=5, pady=5)
        self.activity_cost_entry = ttk.Entry(activity_frame)
        self.activity_cost_entry.grid(row=3, column=1, padx=5, pady=5)
        add_activity_button = ttk.Button(activity_frame, text="Add Activity", command=self.add_activity)
        add_activity_button.grid(row=4, column=0, columnspan=2, pady=5)

        #Crating budget Frame
        budget_frame = ttk.LabelFrame(self.root, text="Set Budget")
        budget_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        ttk.Label(budget_frame, text="Total Budget:").grid(row=0, column=0, padx=5, pady=5)
        self.budget_entry = ttk.Entry(budget_frame)
        self.budget_entry.grid(row=0, column=1, padx=5, pady=5)
        set_budget_button = ttk.Button(budget_frame, text="Set Budget", command=self.set_budget)
        set_budget_button.grid(row=1, column=0, columnspan=2, pady=5)

        #Creating summary Frame
        summary_frame = ttk.LabelFrame(self.root, text="Summary")
        summary_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        self.summary_text = tk.Text(summary_frame, height=10, width=50)
        self.summary_text.grid(row=0, column=0, padx=5, pady=5)
        update_summary_button = ttk.Button(summary_frame, text="Update Summary", command=self.update_summary)
        update_summary_button.grid(row=1, column=0, pady=5)
    #Defining a function to add destinations
    def add_destination(self):
        '''
        Collects user input for a new destination, validates the input,
        and creates a Destination object to add to the planner.
        '''
        name = self.destination_name_entry.get()
        country = self.destination_country_entry.get()
        start_date = self.destination_start_date_entry.get()
        end_date = self.destination_end_date_entry.get()

        if not name or not country or not start_date or not end_date:
            messagebox.showerror("Error", "Please fill out all destination fields.")
            return

        destination = Destination(name, country, start_date, end_date)
        self.destinations.append(destination)
        self.destination_combobox["values"] = [d.name for d in self.destinations]
        messagebox.showinfo("Success", f"Destination '{name}' added successfully.")
    #Defining a function allow the user to add activities to the planner
    def add_activity(self):
        '''
        Associates an activity with a destination by collecting user input,
        validating it, and creating an Activity object.

        Validates that the cost is numeric and ensures all fields are completed.
        '''
        destination_name = self.destination_combobox.get()
        activity_name = self.activity_name_entry.get()
        category = self.activity_category_entry.get()
        try:
            cost = float(self.activity_cost_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Cost must be a number.")
            return

        if not destination_name or not activity_name or not category:
            messagebox.showerror("Error", "Please fill out all activity fields.")
            return

        destination = next((d for d in self.destinations if d.name == destination_name), None)
        if not destination:
            messagebox.showerror("Error", "Selected destination not found.")
            return

        activity = Activity(activity_name, category, cost)
        destination.add_activity(activity)
        messagebox.showinfo("Success", f"Activity '{activity_name}' added to '{destination_name}'.")
    #Defining a function that allows the user to set the budget

    def set_budget(self):
        '''
        Collects user input for a budget, validates the input,
        and sets it as the budget.
        '''
        try:
            total_budget = float(self.budget_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Budget must be a number.")
            return

        self.budget = Budget(total_budget)
        messagebox.showinfo("Success", f"Budget set to {total_budget}.")
    #Defining a function that updates the summary of the planner
    def update_summary(self):
        '''
        Updates the summary section to display the current destinations,
        their activities, and budget details.
        '''
        self.summary_text.delete(1.0, tk.END)
        if not self.destinations:
            self.summary_text.insert(tk.END, "No destinations added.\n")
        else:
            for destination in self.destinations:
                self.summary_text.insert(tk.END, f"Destination: {destination.name} ({destination.country})\n")
                self.summary_text.insert(tk.END, f"Dates: {destination.start_date} to {destination.end_date}\n")
                self.summary_text.insert(tk.END, "Activities:\n")
                for activity in destination.activities:
                    self.summary_text.insert(tk.END, f"  - {activity.name} ({activity.category}), Cost: {activity.cost}\n")
                self.summary_text.insert(tk.END, f"Total Cost: {destination.calculate_total_cost()}\n\n")

        if self.budget:
            total_spent = sum(d.calculate_total_cost() for d in self.destinations)
            remaining = self.budget.remaining_amount() - total_spent
            self.summary_text.insert(tk.END, f"Budget: {self.budget.total_budget}, Spent: {total_spent}, Remaining: {remaining}\n")
        else:
            self.summary_text.insert(tk.END, "No budget set.\n")
