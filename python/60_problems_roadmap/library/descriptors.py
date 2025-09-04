class UpperCaseDescriptor:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = instance.__dict__.get(self.private_name)
        return value.upper() if value else None

    def __set__(self, instance, value):
        if not value or not isinstance(value, str):
            raise ValueError(f"{self.public_name.capitalize()} must be a non-empty string.")
        instance.__dict__[self.private_name] = value


class PositiveNumber:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"{self.public_name.capitalize()} must be a positive number.")
        instance.__dict__[self.private_name] = value


"""
Notes:
    - `owner` refers to the class the descriptor will be used in, I only will use it if i worked on a class-level attribute 
    -  If you're working with class-level attributes, you should replace instance with owner in the __set__ method.
        - usage: owner.__dict__[self.private_name]

    - `instance` refers to the object of the class the descriptor will be used in to work on the instance attributes
        - usage: instance.__dict__[self.private_name]
"""