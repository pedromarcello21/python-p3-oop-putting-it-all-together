#!/usr/bin/env python3

class Book:

    def __init__(self, title, page_count, page_reading):
        self.page_count = page_count
        self.title = title
        self.page_reading = page_reading
        
    def __repr__(self):
        return f"I'm reading {self.title}. It's {self.page_count} pages long and I\'m currently on page {self.page_reading}"
    
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            raise AssertionError("page_count must be an integer")
        else:
            self._page_count=value

    @property
    def page_reading(self):
        return self._page_reading
    
    @page_reading.setter
    def page_reading(self, value):
        if not isinstance(value, int):
            raise AssertionError("page_reading must be an integer")
        else:
            self._page_reading=value

    
    def turn_page(self):
        self.page_reading +=1
    
    pass
    
        