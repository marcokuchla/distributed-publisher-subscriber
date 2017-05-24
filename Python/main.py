#!/usr/bin/env python3
import sys
import Pyro4
from intermediary import Intermediary
from publisher import Publisher
from subscriber import Subscriber

def main():
    sys.excepthook = Pyro4.util.excepthook
    p1 = Publisher('P1', 'X')
    p2 = Publisher('P2', 'Y')
    s1 = Subscriber('S1')
    s2 = Subscriber('S2')
    with Pyro4.locateNS() as ns:
        i1 = Pyro4.Proxy('PYRONAME:intermediary1')
        i2 = Pyro4.Proxy('PYRONAME:intermediary2')
        i3 = Pyro4.Proxy('PYRONAME:intermediary3')
    p1.intermediary = i1
    p2.intermediary = i3
    i2.client = s1
    i3.client = s2
    i1.add_neighbours([p1, i2, i3])
    i1.print_neighbours()
    print
    # i1.neighbours.add(p1)
    # i1.neighbours.add(i2)
    # i1.neighbours.add(i3)
    i2.add_neighbours([i1, s1])
    # i2.neighbours.add(i1)
    # i2.neighbours.add(s1)
    i3.add_neighbours([p2, i1, s2])
    # i3.neighbours.add(p2)
    # i3.neighbours.add(i1)
    # i3.neighbours.add(s2)
    i2.subscription(s1, 'X')
    print
    i3.subscription(s2, 'Y')
    print
    p1.publish()
    print
    p2.publish()

if __name__ == '__main__':
    main()
