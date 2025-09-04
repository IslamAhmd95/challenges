"""
Problem:
    Define an Enum class called Weekday with the days of the week. Then, create a function is_weekend(day) that returns True if the day is Saturday or Friday.
"""


from enum import Enum


class Weekday(Enum):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7

    def is_weekend(self):
        return self in [Weekday.FRIDAY, Weekday.SATURDAY]


WEEKEND_DAYS = [Weekday.FRIDAY, Weekday.SATURDAY]


def is_weekend(day: int | str | Weekday) -> bool:

    if isinstance(day, str):

        try:
            day = Weekday[day.upper()]
        except KeyError:
            return False    # Invalid input
        
    elif isinstance(day, int):

        try:
            day = Weekday(day)
        except ValueError:
            return False    # Invalid input

    # return day in WEEKEND_DAYS  # using the `WEEKEND_DAYS` constant

    return day.is_weekend()   # using the instance method




print(is_weekend(6))           # True (Friday)
print(is_weekend("saturday"))  # True
print(is_weekend(3))           # False (Tuesday)
print(is_weekend(9))           # False "Invalid input"
print(is_weekend("holiday"))   # False "Invalid input"
print(is_weekend(Weekday.SUNDAY))  # False



"""
Notes:

1. Writing variable names in ALL CAPS (like WEEKEND_DAYS) is a common Python convention 
   to indicate that the variable is a constant. This is just a naming guideline — Python 
   doesn’t enforce immutability.

2. Enums are primarily used to define fixed sets of constant values. 
   It's generally best practice to avoid adding unrelated logic or complex methods to them.
   If additional behavior is necessary, it's cleaner to place it in external helper functions 
   or use class methods when appropriate.

3. You can retrieve an enum member using its value by calling the enum class:
       day = Weekday(1)
       print(day)  # Output: Weekday.SUNDAY

4. You can also retrieve an enum member by its name (key) using bracket notation:
       day = Weekday["SUNDAY"]
       print(day)  # Output: Weekday.SUNDAY
"""

