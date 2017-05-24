#!/usr/bin/env python3
import sys
import Pyro4
import publisher

def main():
    sys.excepthook = Pyro4.util.excepthook
    p1 = publisher.Publisher('P1', 'X')
    p2 = publisher.Publisher('P2', 'Y')
    with Pyro4.locateNS() as ns:
        i1 = Pyro4.Proxy('PYRONAME:intermediary1')
        i2 = Pyro4.Proxy('PYRONAME:intermediary2')
        i3 = Pyro4.Proxy('PYRONAME:intermediary3')
    p1.intermediary = i1
    p2.intermediary = i3
    p1.publish()
    print
    p2.publish()

if __name__ == '__main__':
    main()
