#Population Growth Modeling
import time
import math

#input helper
def input_number(prompt, dtype=float):
    while True:
        value = input(prompt)
        try:
            return dtype(value)
        except ValueError:
            print("Please enter a valid number.")

# Time conversion dictionary for flexible unit conversions
TIME_UNITS = {
    'day': {'half-day': 2, 'quarter-day': 4, 'hour': 24, 'minute': 1440, 'second': 86400},
    'half-day': {'quarter-day': 2, 'hour': 12, 'minute': 720, 'second': 43200},
    'quarter-day': {'hour': 6, 'minute': 360, 'second': 21600},
    'hour': {'minute': 60, 'second': 3600},
    'minute': {'second': 60}
}

def convert_units(amount, from_unit, to_unit):
    if from_unit == to_unit:
        return amount
    if from_unit in TIME_UNITS and to_unit in TIME_UNITS[from_unit]:
        return amount * TIME_UNITS[from_unit][to_unit]
    elif to_unit in TIME_UNITS and from_unit in TIME_UNITS[to_unit]:
        return amount / TIME_UNITS[to_unit][from_unit]
    else:
        raise ValueError(f"Cannot convert from {from_unit} to {to_unit}")
    
#calculates population growth using naive model
def basic_growth(start, rate, steps):
    return start + (start * rate / 100) * steps

# calculates population growth using sophisticated model
def advanced_growth(start, rate, steps):
    return start * (1 + rate / 100) ** steps
