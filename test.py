x = 3

print(id(x))
print(type(x))
print(x)


## integer caching
a=256
b=256

print(f"id(a) = {id(a)} == id(b) = {id(b)}")

a=257
b=257
print(f"id(a) = {id(a)} == id(b) = {id(b)}")


import weakref
import gc
import sys

class LifecycleDemo:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")

    def __del__(self):
        print(f"{self.name} destroyed")

    def __repr__(self):
        return f"LifecycleDemo({self.name})"

# Creation and reference counting
obj1 = LifecycleDemo("obj1")
obj2 = obj1  # Reference count increases
print(f"Reference count: {sys.getrefcount(obj1) - 1}")  # -1 for getrefcount's temporary reference


# Integer Caching
def show_int_caching():
    # Small integers (-5 to 256)
    a = 256
    b = 256
    print(f"256 cached: {id(a) == id(b)}")  # True

    c = 1000000
    d = 1000000
    print(f"1000000 not cached: {id(c) == id(d)}")  # False

    # Integer caching in loops
    total = 0
    for i in range(5):  # Uses cached integers
        print(f"id of {i}: {id(i)}")

# String Interning
def show_string_interning():
    # Automatic interning
    str1 = "hello"
    str2 = "hello"
    print(f"Same string ids: {id(str1) == id(str2)}")  # True

    # String operations create new objects
    str3 = "hel" + "lo"
    print(f"Concatenated string interned: {id(str1) == id(str3)}")  # True

    # Runtime strings not automatically interned
    str4 = ''.join(['h', 'e', 'l', 'l', 'o'])
    print(f"Runtime string not interned: {id(str1) == id(str4)}")  # False

    # Force interning with sys.intern()
    import sys
    str5 = sys.intern(''.join(['h', 'e', 'l', 'l', 'o']))
    print(f"Forced interning: {id(str1) == id(str5)}")  # True

# Common string methods create new objects
original = "hello"
upper = original.upper()
print(f"New object for upper(): {id(original) != id(upper)}")


show_int_caching()
print("\nString Interning Examples:")
show_string_interning()


def test_int_caching():
    # Direct assignment
    a1 = 257
    a2 = 257
    print(f"Direct 257: {id(a1) == id(a2)}")  # May be True!

    # Creating through computation
    b1 = 256 + 1
    b2 = 256 + 1
    print(f"Computed 257: {id(b1) == id(b2)}")  # Usually False

    numbers = []
    for i in range(256, 259):
        numbers.append(i)

    for j in range(256, 259):
        print(f"Loop {j}: {id(numbers[j-256]) == id(j)}")

test_int_caching()
