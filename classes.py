# Classes

#Creating a class ,represents a travel destination with its details and associated activities.
class Destination:
    '''
    Initializing the classes attributes:
    name of the destination,
    country of the destination,
    start and end date of the destination,
    activities of the destination.
    '''
    def __init__(self, name, country, start_date, end_date):
        self.name = name
        self.country = country
        self.start_date = start_date
        self.end_date = end_date
        self.activities = []
    #Defining a function that adds an activity to the activities list
    def add_activity(self, activity):
        self.activities.append(activity)
    #Defining a function that sums the total cost of all activities in the list
    def calculate_total_cost(self):
        return sum(activity.cost for activity in self.activities)

#Creating an activities class ,represents an activity planned at a specific destination.
class Activity:
    '''
    Initializing the classes attributes:
    name of the activity,
    category of the activity,
    cost of the activity.
    '''
    def __init__(self, name, category, cost):
        self.name = name
        self.category = category
        self.cost = cost

#Creating a budget class with relevant attributes and functions ,Represents the budget for a trip.
class Budget:
    '''
    Initializing the classes attributes:
    total cost of the budget.
    amount of money spent in the budget.
    '''

    def __init__(self, total_budget):
        self.total_budget = total_budget
        self.spent_amount = 0
    #Defining a function that adds the amount of money spent on each activity
    def add_expense(self, amount):
        self.spent_amount += amount
    #Defining a function the subtracts the amount spent from the budget to get the remaining budget
    def remaining_amount(self):
        return self.total_budget - self.spent_amount
