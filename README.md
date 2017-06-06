# Tiny, tiny mazes

Alice found herself very tiny and wandering around Wonderland.
Even the grass around her seemed like a maze.

This is a tiny maze solver.

A maze is represented by a matrix

```python
[
 [S 0 1]
 [1 0 1]
 [1 0 E]
]
```


S : start of the maze
E : end of the maze
1 : This is a wall that you cannot pass through
0 : A free space that you can move through.

The goal is the get to the end of the maze.
A solved maze will have an x in the start, the path,
and the end of the maze, like this.

```python
[
    [x x 1]
    [1 x 1]
    [1 x x]
]
```

## Installing

Clone the repo and cd to the project directory.
You should have [Python 3](https://www.python.org/downloads/) and  [pip](https://pip.pypa.io/en/stable/installing/) installed.  Making a new [virtualenv](https://virtualenv.pypa.io/en/stable/) is nice also :)

```bash
pip install -r requirements.txt
```

## Running the tests

This kata's test tools include

0. `nosetest` for running your Python tests from the command line
1. `rednose` for colorizing the test output and making it easier to read
2. `nosewatch` to re-run tests automatically as you change your code or tests
3. `coverage` to show you how much of your code is being tested.

To run the tests in watch mode:
```bash
./test.sh        // runs nosetests --cover-branches --with-coverage --rednose --with-watch --cover-erase --cover-html
```


Source: https://github.com/gigasquid/wonderland-clojure-katas
