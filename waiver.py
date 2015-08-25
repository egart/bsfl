#!/usr/bin/env python
#

import random

# Input teams
teams = ['Joe', #1
     'Speer',   #2
     'Burns',   #3
     'Eric',    #4
     'Aaron',   #5
     'Trey',    #6
     'Ben',     #7
     'Alex',    #8
     'Johnny',  #9
     'Dave',    #10
     'Tim',     #11
     'Steve']   #12

# Iterate over weeks 1-16
for wk in range(1,17):

    print("=== Week",wk,"===")              # Header for week
    random.shuffle(teams)                   # Randomize team order

    # Print team order for week
    for order in range(1,13):
        print(str(order).rjust(2),teams[order-1])
