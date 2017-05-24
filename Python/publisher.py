import sys
import Pyro4

class Publisher(object):
    def __init__(self, name, event):
        super(Publisher, self).__init__()
        self.name = name
        self.event = event
        self.intermediary = None

    def publish(self):
        print("'{}' publishes event '{}'".format(self, self.event))
        self.intermediary.publish(self, self.event)

    def __str__(self):
        return self.name
