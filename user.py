class User:
    def __init__(self, name):
        self.name = name;
        self.version = "old"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not(self.name == other.name)

    def __str__(self):
        return self.name + ',' + str(id(self))

    def __repr__(self):
        return str(self)