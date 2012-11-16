Introduction
------------

For the annual X-mas dinner at work, we want to be able to optimize the seating like this:
* There are three rounds, starter, main and dessert.
* All persons would optimally not meet the same person twice

Implementation
--------------

The start is a list of names, and the number of seats per table.
From that we calculate the number of tables we need, and start populating the tables.
After the tables are filled for the first time, we start switching people.

After three rounds, we calculate the score of the solution.

If this solution scores better than previous ones, we return it, otherwise print score and restart.