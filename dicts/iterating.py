'''
One of the philosophies of Python is that "There should be one-- and 
preferably only one --obvious way to do it."

Unfortunately one area where this philosophy seemed to be neglected was in
iterating over a dictionary, as there's *many* different ways to do it.

There's three typical approaches (in Python 2.x):

- using the items() method
- using the iteritems() method
- iterating over the dictionary directly

This file shows some timing of these approaches, by providing three functions
which do the same operation over a large dictionary, using these three 
mechanisms for iteration.
'''

import timeit

def items(mydict):
    '''
    Iterate using the items() method.  The disadvantage of items() is that a
    copy of the dictionaries keys & values are created whenever it is called.
    Thus, the memory overhead if the dictionary is large is quite significant.

    In Python 3, items() now performs the exact same operation that iteritems()
    does (uses a generator).
    '''
    total = 0
    for k, v in mydict.items():
        total += k + v
    return total

def iteritems(mydict):
    '''
    Iterate using the iteritems method.  The big upside to iteritems() is that
    a generator is used, so at any given time only 1 key and value need to be
    in memory for the loop.

    In Python 3, iteritems() was removed (instead the functionality was moved
    into items())
    '''
    total = 0
    for k, v in mydict.iteritems():
        total += k + v
    return total
        
def justdict(mydict):
    '''
    Iterate over the dictionary itself.  This doesn't require an itermediate list
    be created (like with items()), but has the drawback that your loop only gets
    the key values, so to get the values, you have to then do a regular dictionary
    lookup.  Thus if you need both the key *and* value of each slot in the dict,
    you are better off using iteritems().

    Additionally, if you only need the keys of a dict, there is also the .keys() 
    (which copies the keys to a list, much like items() does), and iterkeys()
    (which uses a generator to iterate over the keys(), much like iteritems() 
    does)
    '''
    total = 0
    for k in mydict:
        total += k + mydict[k]
    return total
    
# create a dictionary which maps the integers from 0 to lim-1, to the integers
# lim to lim + lim -1 (ie: (0, lim), (1, lim + 1), ..., (lim-1, lim + lim -1)
lim = 1000000
mydict = dict(zip(range(lim), range(lim, lim + lim)))

def main():
    num_iter = 100
    
    # time the three approaches
    t1 = timeit.Timer("items(mydict)", "from __main__ import mydict, items")
    print "Using items: %s" % t1.timeit(num_iter)
    t2 = timeit.Timer("iteritems(mydict)", "from __main__ import mydict, iteritems")
    print "Using iteritems: %s" % t2.timeit(num_iter)
    t3 = timeit.Timer("justdict(mydict)", "from __main__ import mydict, justdict")
    print "Using justdict: %s" % t3.timeit(num_iter)
    
    print items(mydict)
    print iteritems(mydict)
    print justdict(mydict)

if __name__ == '__main__':
    main()
