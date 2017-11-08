# by convention, we give classes PascalCase names
class Set:

    # these are the member functions
    # every one takes a first parameter "self" (another convention)
    # that refers to the particular Set object being used
    def __init__(self, values=None):

        self.dict = {}  # each instance of Set has its own dict property # which is what we'll use to track memberships
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):

        """this is the string representation of a Set object
        if you type it at the Python prompt or pass it to str()"""
        print("Set: " + str(self.dict.keys()))

    # we'll represent membership by being a key in self.dict with value True
    def add(self, value):
        print(value)
        self.dict[value] = True

    # value is in the Set if it's a key in the dictionary
    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]

s = Set([1,2,2,3])
s.__repr__()
s.add(4)
print(s.contains(4))
s.remove(3)
print(s.contains(3))