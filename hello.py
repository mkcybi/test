#!/usr/bin/env python

def greet_times(times):
    for ii in range(times):
        print "hello world %i" % (ii+1)

if __name__ == "__main__":
    greet_times(10)
