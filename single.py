#!/usr/env/bin python3

class Intermediary(object):
    def __init__(self, name):
        super(Intermediary, self).__init__()
        self.name = name
        self.routing = {}
        self.subscribers = {}
        self.neighbours = set()
        self.client = None

    def subscription(self, node, event):
        if self.client == node:
            self.subscribers[node] = event
            print("'{}' subscribed client '{}' for event '{}'".format(self, node, event))
        else:
            self.routing[node] = event
            print("'{}' registered route '{}' for event '{}'".format(self, node, event))
        [n.subscription(self, event) for n in self.neighbours - {node} if isinstance(n, Intermediary)]


    def publish(self, node, event):
        matchlist = [n for (n, e) in self.subscribers.iteritems() if e == event]
        [self.notifying(n, event) for n in matchlist]
        forwardlist = [n for (n, e) in self.routing.iteritems() if e == event]
        [self.forwarding(n, event) for n in forwardlist if n != node]

    def notifying(self, node, event):
        print("'{}' notifying '{}' with event '{}'".format(self, node, event))
        node.notify(event)

    def forwarding(self, node, event):
        print("'{}' forwarding to '{}' a published event '{}'".format(self, node, event))
        node.publish(self, event)

    def __str__(self):
        return self.name

class Subscriber(object):
    def __init__(self, name):
        super(Subscriber, self).__init__()
        self.name = name

    def notify(self, event):
        print("'{}' received event '{}'".format(self, event))

    def __str__(self):
        return self.name

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

def main():
    p1 = Publisher('P1', 'X')
    p2 = Publisher('P2', 'Y')
    s1 = Subscriber('S1')
    s2 = Subscriber('S2')
    i1 = Intermediary('I1')
    i2 = Intermediary('I2')
    i3 = Intermediary('I3')
    p1.intermediary = i1
    p2.intermediary = i3
    i2.client = s1
    i3.client = s2
    i1.neighbours.add(p1)
    i1.neighbours.add(i2)
    i1.neighbours.add(i3)
    i1.neighbours.add(i3)
    i2.neighbours.add(i1)
    i2.neighbours.add(i1)
    i3.neighbours.add(p2)
    i3.neighbours.add(i1)
    i3.neighbours.add(s2)
    i2.subscription(s1, 'X')
    print
    i3.subscription(s2, 'Y')
    print
    p1.publish()
    print
    p2.publish()

if __name__ == '__main__':
    main()
