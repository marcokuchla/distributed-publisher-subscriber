#!/usr/bin/env python3
import json
import sys
import Pyro4
import subscriber
import publisher

def subscriber_dict_to_class(classname, d):
    print('deserializing {}'.format(d))
    return subscriber.Subscriber(d['name'])

def publisher_dict_to_class(classname, d):
    p = publisher.Publisher(d['name'], d['event'])
    p.intermediary = d['intermediary']
    return p

Pyro4.util.SerializerBase.register_dict_to_class('subscriber.Subscriber', subscriber_dict_to_class)
Pyro4.util.SerializerBase.register_dict_to_class('publisher.Publisher', publisher_dict_to_class)

@Pyro4.expose
@Pyro4.behavior(instance_mode='single')
class Intermediary(object):
    def __init__(self, name):
        super(Intermediary, self).__init__()
        self._name = name
        self._routing = {}
        self._subscribers = {}
        self._neighbours = set()
        self._client = None

    @property
    def name(self):
        return self._name

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        self._client = value

    def print_neighbours(self):
        print(self._neighbours)

    def add_neighbours(self, nodelist):
        self._neighbours.update(nodelist)

    def subscription(self, node, event):
        if self._client == node:
            self._subscribers[node] = event
            print("'{}' subscribed client '{}' for event '{}'".format(self, node.name, event))
        else:
            self._routing[node] = event
            print("'{}' registered route '{}' for event '{}'".format(self, node.name, event))
        [n.subscription(self, event) for n in self._neighbours if n.name != node.name]

    def publish(self, node, event):
        matchlist = [n for (n, e) in self._subscribers.items() if e == event]
        [self.notifying(n, event) for n in matchlist]
        forwardlist = [n for (n, e) in self._routing.items() if e == event]
        [self.forwarding(n, event) for n in forwardlist if n != node]

    def notifying(self, node, event):
        print("'{}' notifying '{}' with event '{}'".format(self, node, event))
        node.notify(event)

    def forwarding(self, node, event):
        print("'{}' forwarding to '{}' a published event '{}'".format(self, node.name, event))
        node.publish(self, event)

    def __str__(self):
        return self._name

    def __eq__(self, other):
        return other and self.name == other.name

    def __ne__(self, other):
        return not(self == other)

    def __hash__(self):
        return hash(self.name)

def main():
    sys.excepthook = Pyro4.util.excepthook
    i1 = Intermediary('I1')
    i2 = Intermediary('I2')
    i3 = Intermediary('I3')
    i1.add_neighbours([i2, i3])
    i2.add_neighbours([i1])
    i3.add_neighbours([i1])
    with Pyro4.locateNS() as ns:
        s1 = Pyro4.Proxy('PYRONAME:subscriber1')
        s2 = Pyro4.Proxy('PYRONAME:subscriber2')
    i2.client = s1
    i3.client = s2
    i2.subscription(s1, 'X')
    print
    i3.subscription(s2, 'Y')
    print
    with Pyro4.Daemon() as daemon:
        i1_uri = daemon.register(i1)
        i2_uri = daemon.register(i2)
        i3_uri = daemon.register(i3)
        with Pyro4.locateNS() as ns:
            ns.register('intermediary1', i1_uri)
            ns.register('intermediary2', i2_uri)
            ns.register('intermediary3', i3_uri)
        print('Intermediaries available.')
        daemon.requestLoop()

if __name__ == '__main__':
    main()
