class Subscriber(object):
    def __init__(self, name):
        super(Subscriber, self).__init__()
        self.name = name

    def notify(self, event):
        print("'{}' received event '{}'".format(self, event))

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(self.name)
