#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        # assert type(size)==int, "size must be an integer"
        self.brand = brand
        self.size = size


    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise AssertionError("size must be an integer")
        else:
            self._size=value
    
    def __repr__(self):
        return f"I have a pair of {self.brand} size {self.size}"
    
    def cobble(self):
        self.condition = "New"
        return f"Your {self.brand} are as good as new!"

    pass