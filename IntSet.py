class IntSet(object):

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Asumes e is an integer and inserts e intro self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer, returns True if e is in self, False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self, raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def getMembers(self):
        """Returns a list containing the elements of self. Nothing can be assumed about the order"""
        return self.vals[:]

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'

s = IntSet()
s.insert(3)
s.insert(4)
s.insert(6)
s.insert(9)
temp1 = s.member(7)
s.remove(4)
#s.remove(7)
s1 = s.getMembers()
print(s)