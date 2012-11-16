#!/usr/bin/python
# From http://stackoverflow.com/questions/968673/speed-dating-algorithm/968724
import random

class Person(object):

    def __init__(self, name):
        self.name = name
        self.known_people = dict()

    def meets(self, a_guy, propagation = True):
        "self meets a_guy, and a_guy meets self"
        if a_guy not in self.known_people:
            self.known_people[a_guy] = 1
        else:
            self.known_people[a_guy] += 1

        if propagation: a_guy.meets(self, False)

    def points(self, table):
        "Calculates how many new guys self will meet at table"
        return len([p for p in table if p not in self.known_people])

    def chooses(self, tables, n_seats):
        "Calculate what is the best table to sit at, and return it"
        points = 0
        free_seats = 0
        ret = random.choice([t for t in tables if len(t)<n_seats])

        for table in tables:
            tmp_p = self.points(table)
            tmp_s = n_seats - len(table)
            if tmp_s == 0: continue
            if tmp_p > points or (tmp_p == points and tmp_s > free_seats):
                ret = table
                points = tmp_p
                free_seats = tmp_s

        return ret

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


def Switcher(n_seats, people):
    """calculate how many tables and what switches you need
        assuming each table has n_seats seats"""

    n_people = len(people)
    n_tables = n_people/n_seats

    switches = []
    while not all(len(g.known_people) == n_people-1 for g in people):
        tables = [[] for t in xrange(n_tables)]

        random.shuffle(people) # need to change "starter"

        for the_guy in people:
            table = the_guy.chooses(tables, n_seats)
            tables.remove(table)
            for guy in table:
                the_guy.meets(guy)
            table += [the_guy]
            tables += [table]

        switches += [tables]

    return switches



lst_people = [
	Person('Alice'),
	Person('Bob'),
	Person('Carol'),
	Person('Chuck'),
	Person('Dan'),
	Person('Eve'),
	Person('Mallory'),
	Person('Oscar'),
	Person('Peggy'),
	Person('Victor'),
	Person('Trent'),
	Person('Walter')
      ] 

s = Switcher(6, lst_people)

print "You need %d tables and %d turns" % (len(s[0]), len(s))
turn = 1
for tables in s:
    print 'Turn #%d' % turn
    turn += 1
    tbl = 1
    for table in tables:
        print '  Table #%d - '%tbl, table
        tbl += 1
    print '\n'