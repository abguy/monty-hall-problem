# Problem statement

The [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem) is a counter-intuitive statistics puzzle:

* There are 3 doors, behind which are two goats and a car.
* You pick a door (call it door A). You’re hoping for the car of course.
* Monty Hall, the game show host, examines the other doors (B & C) and always opens one of them with a goat (Both doors might have goats; he’ll randomly pick one to open)

Here’s the game: Do you stick with door A (original guess) or switch to the other unopened door? Does it matter?

Surprisingly, the odds aren’t 50-50. If you switch doors you’ll win 2/3 of the time!

# Goal

I am going to prove it via experiment.

# How to check

```
$ git clone git@github.com:abguy/monty-hall-problem.git monty-hall-problem
$ cd monty-hall-problem
$ sudo pip3 install -e .
```
