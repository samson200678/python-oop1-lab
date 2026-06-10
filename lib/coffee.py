def _init_(self, size, price):
        self.size = size
        self.price = price

@property
def size(self):
    return self._size

@size.setter
def size(self, value):
    if value in ["Small", "Medium", "Large"]:
        self._size = value
    else:
            print("size must be Small, Medium, or Large")

def tip(self):
    print("This coffee is great, here's a tip!")
    self.price += 1