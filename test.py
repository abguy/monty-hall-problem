#!/usr/bin/env python

import sys
import random

tests_number = int(sys.argv[1]) if (len(sys.argv) > 1) else 100

def make_experiment():
    """
    Returns a tuple with 3 elements but with a single success (true).
    """
    result = [False, False, True]
    random.shuffle(result)
    return tuple(result)

def open_goat(experiment_result, choice):
    """
    Returns index of goat except user choice.
    """
    while True:
        potential_goat = random.randrange(3)
        if potential_goat == choice:
            continue
        if experiment_result[potential_goat]:
            # It is not goat actually
            continue
        return potential_goat

stick_failures_number = 0
switch_failures_number = 0
for i in range(tests_number):
    experiment_result = make_experiment()
    choice = random.randrange(3)
    goat = open_goat(experiment_result, choice)
    if experiment_result[choice]:
        switch_failures_number += 1
    else:
        stick_failures_number += 1

print ("Stick choice failures: {0} ({1:.2%})".format(stick_failures_number, stick_failures_number / tests_number))
print ("Switch choice failures: {0} ({1:.2%})".format(switch_failures_number, switch_failures_number / tests_number))
