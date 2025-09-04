from banking.saving_account import SavingAccount
from banking.bank_account import BankAccount
from banking.business_account import BusinessAccount


account1 = BankAccount("islam", "Islam@gmail.com", 30)
account2 = BankAccount("mohamed", "mo@gmail.com", 40)
account1.email = "Eslam@yahoo.com"
print(account1.email)
print(BankAccount.accounts)
account1.display_account_info()


account1.deposit(10)
print(account1.balance)

account1.withdraw(10)
print(account1.balance)

print("_"*60)

account3 = SavingAccount("mohamed", "mo@gmail.com", 50)
account4 = SavingAccount("Heba", "heba@gmail.com", 50)
account5 = SavingAccount("Nour", "Nour@gmail.com", 50)

print(SavingAccount.accounts)
account4.display_account_info()

account3.deposit(10)
print(account3.balance)

account3.withdraw(10)
print(account3.balance)
print(type(account3).__name__) # get the type name of the object "class name"

print("_"*60)

account6 = BusinessAccount("Axxa", "axxa@gmail.com", 7000)
print(BusinessAccount.accounts)
print(account6.name)
account6.display_account_info()
account6.deposit(2000)
print(account6.balance)
account6.withdraw(3000)
print(account6.balance)

account6.add_interest()
account6.cut_monthly_fees()


def func(lst=[]):
    lst.append(1)
    print(lst)

func()
func([2])
"""
Notes:

    1. Encapsulation
        - What it is: Restricting direct access to an object’s internal data.
        - How it works: You hide the data (__private_attr) and expose it through methods or properties that can add checks, logging, formatting, etc.
        - Goal: Protect the integrity of the data and prevent misuse.
        - Analogy: ATM — you can’t open the bank vault, but you can use the machine to withdraw cash in a controlled way.

    2. Abstraction
        - What it is: Focusing on what an object does, not how it does it.
        - How it works: You define an interface (methods, behaviors) without showing the internal implementation.
        - Goal: Hide complexity from the user.
        - Analogy: When you drive a car, you press the brake pedal (you know what it does: slows the car) — you don’t care how the brake system works internally.

    3. Inheritance
        - What it is: A mechanism where a class (child/subclass) can reuse and extend the behavior and attributes of another class (parent/superclass).
        - How it works: The child class automatically gets the parent’s methods and attributes, but can override or add new ones.
        - Goal: Promote code reuse, reduce duplication, and create a logical class hierarchy.
        - Analogy: A child inherits physical traits and abilities from a parent (eye color, height) but can also develop unique skills of their own.

    4. How to Decide What Goes in the Abstract Class ?
        - Abstract class = the contract → “Any bank account must have these features.”
        - Concrete class = the implementation → “Here’s how this particular bank account works.”
        - Think about:
            - What every type of account must be able to do, regardless of how it’s implemented.
            - Don’t include small helper/validation methods — those are internal details that subclasses can handle in their own way.

    5. Methods

        - Instance method
            - gets self, can access both instance & class attributes/methods.
            - Can be called from @classmethod or @staticmethod only if you explicitly pass an instance as an argument (uncommon, usually bad practice).
            - Calling: self.method()

        - Class method
            - gets cls as a parameter.
            - Can access class-level attributes/methods.
            - Can access instance data only if an instance is passed in (but that’s usually a design smell).
            - Calling:
                - For inheritance flexibility → type(self).method()
                - To force this class only or to use in the same class → ClassName.method()

        - Static method
            - gets nothing automatically.
            - Can’t access instance or class data unless explicitly passed in.
            - Behaves like a plain function living in the class namespace.
            - Calling:
                - For inheritance flexibility → type(self).method()
                - To force this class only or to use in the same class → ClassName.method()

        - Design tip:
            - If you find yourself passing an instance into a class method or static method just to get instance data, that’s a signal:
            "This should probably have been an instance method instead."

        - Ex:
            class Demo:
                val = 10  # class attr

                def instance_method(self):
                    print(self.val)  # self → instance

                @classmethod
                def class_method(cls):
                    print(cls.val)   # cls → class

                @staticmethod
                def static_method():
                    print("I know nothing unless you tell me.")


    6. Attributes

        - Instance attribute – unique per object, set in __init__.
        - Class attribute – shared across all instances, set in class body.
        - Static attribute – same as class attribute, often constants in ALL_CAPS.
        - Ex:
            class Demo:
                shared_val = 10  # class/static attr

                def __init__(self, val):
                    self.instance_val = val  # instance attr

                    
            d1 = Demo(5)
            d2 = Demo(7)

            # Instance attrs → separate
            print(d1.instance_val, d2.instance_val)  # 5, 7

            # Class attrs → shared
            print(d1.shared_val, d2.shared_val)  # 10, 10
            Demo.shared_val = 20
            print(d1.shared_val, d2.shared_val)  # 20, 20


    7. Polymorphism means “many forms.”
        - It’s when the same function name or method can work with different types of objects and behave in a way that’s specific to each type.
        - Two main types of polymorphism (method overriding vs method overloading)
        - Think: One command, different results depending on who you give it to.
        - Ex:
            class Dog:
                def speak(self):
                    return "Woof!"

            class Cat:
                def speak(self):
                    return "Meow!"

            class Duck:
                def speak(self):
                    return "Quack!"

            # Polymorphism in action
            animals = [Dog(), Cat(), Duck()]

            for animal in animals:
                print(animal.speak())

    8. Method Overriding (Runtime Polymorphism)
        - When?
            Happens in inheritance — a child class replaces a method of the parent class with its own version.
        - Analogy:
            - Think of a parent teaching their kid how to greet people:
                - Parent says: "Say 'Hello!'"
                - The kid grows up, travels to France, and now greets people with: "Bonjour!"
                Same action name (greet), but different way of doing it.
        - Ex:
            class Animal:
                def speak(self):
                    return "Some generic sound"

            class Dog(Animal):
                def speak(self):
                    return "Woof!"

            class Cat(Animal):
                def speak(self):
                    return "Meow!"

            animals = [Dog(), Cat(), Animal()]
            for a in animals:
                print(a.speak())

            # Key point: The method is overridden at runtime — Python looks at the actual object type before calling the method.

    9. Method Overloading (Compile-time Polymorphism*)
        - (Note: Python doesn’t have true method overloading like Java or C++, but we can simulate it.)
        - When?
            - Same method name, but different parameters (number or type).
            - The method does different things based on what arguments you pass.
            - Simulated using default args / *args / **kwargs
        - Analogy:
            - Imagine a restaurant waiter:
                - If you say, "I’ll have just water" → they bring water.
                - If you say, "I’ll have water and salad" → they bring both.
                - Same request method ("order"), but behavior changes based on input.

        - Python Simulation:
            class Calculator:
                def add(self, a=None, b=None, c=None):
                    if a is not None and b is not None and c is not None:
                        return a + b + c
                    elif a is not None and b is not None:
                        return a + b
                    elif a is not None:
                        return a
                    else:
                        return 0

            calc = Calculator()
            print(calc.add(2, 3))       # 5
            print(calc.add(2, 3, 4))    # 9
            print(calc.add(7))          # 7

            # Key point: Python achieves this by checking arguments manually inside one method (because it can’t have multiple methods with the same name and different signatures like Java/C++).
"""