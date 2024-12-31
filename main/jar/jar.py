class Jar:
    def __init__(self, capacity=12): # called with Jar(#)
        self.capacity = capacity #capacity is a property with variable _capacity
        self.size = 0 #size is a property with variable _size

    def __str__(self):
        return f"{'🍪' * self.size}"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        self.size -= n

    @property # Getter called with self.capacity
    def capacity(self):
        return self._capacity

    @capacity.setter # Setter called with "self.capacity ="
    def capacity(self, capacity):
        if int(capacity) < 0:
            raise ValueError
        self._capacity = capacity

    @property # Getter called with self.size
    def size(self):
        return self._size

    @size.setter # Setter called with "self.size ="
    def size(self, n):
        self._size = n

# class Jar:
#     def __init__(self, capacity=12): # called with Jar(#)
#         if int(capacity) < 0:
#             raise ValueError
#         self._capacity = capacity #capacity is a property with private variable _capacity (all alteration is within methods)
#         self._size = 0 #size is a property with private variable _size (all alteration is within methods)

#     def __str__(self):
#         return f"{'🍪' * self._size}"

#     def deposit(self, n): #Directly alters the private variable _size
#         if self._size + n > self._capacity:
#             raise ValueError
#         self._size += n

#     def withdraw(self, n): #Directly alters the private variable _size
#         if self._size - n < 0:
#             raise ValueError
#         self._size -= n

#     @property # Getter called with self.capacity # Getter used only for read access
#     def capacity(self):
#         return self._capacity

#     @property # Getter called with self.size # Getter used only for read access
#     def size(self):
#         return self._size
