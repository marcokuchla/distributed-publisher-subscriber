#!/usr/bin/env python3
import sys
import Pyro4
import subscriber

def main():
    sys.excepthook = Pyro4.util.excepthook
    s1 = subscriber.Subscriber('S1')
    s2 = subscriber.Subscriber('S2')
    with Pyro4.Daemon() as daemon:
        s1_uri = daemon.register(s1)
        s2_uri = daemon.register(s2)
        with Pyro4.locateNS() as ns:
            ns.register('subscriber1', s1_uri)
            ns.register('subscriber2', s2_uri)
        print('Subscribers available.')
        daemon.requestLoop()

if __name__ == '__main__':
    main()
