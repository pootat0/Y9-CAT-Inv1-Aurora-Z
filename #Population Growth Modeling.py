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