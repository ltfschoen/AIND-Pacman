# Build a Pacman AI-Agent

# Table of Contents
  * [Chapter 1 - My Setup Checklist](#chapter-1)
  * [Chapter 2 - Info from Udacity](#chapter-2)
  * [Chapter 3 - References](#chapter-3)

# Chapter 1 - My Setup Checklist <a id="chapter-1"></a>

### Instructions and Setup Environment
* Switch to Miniconda environment
    `source activate aind`
* Install dependencies `python -m pip install mypy typing`
* IntelliJ: File > Project Structure > Project Settings > Project > Project SDK > Python 3.6 (~/miniconda3/bin/python)
* Review possible commands in search/commands.txt:
* Change into the search directory `cd search`
* Show Help of possible commands `python pacman.py -h`
* Play Pacman and use arrow keys to control and capture ghosts `python pacman.py`
* Run GoWest agent on map with no turning required `python pacman.py --layout testMaze --pacman GoWestAgent`
* Run GoWest agent on map with turning required `python pacman.py --layout tinyMaze --pacman GoWestAgent`
* Run SearchAgent using tinyMazeSearch Algorithm that plans a path to navigate maze successfully
    `python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch`
* Run Program with a possible command: `python pacman.py --layout smallClassic --zoom 2`
* Run MyPy Linter with `mypy search/pacman.py`

### IntelliJ Debugging Setup

* Create new Python debug configuration script
* Select `python.py` as the Script
* Add ` -l tinyMaze -p SearchAgent -a fn=depthFirstSearch -z 0.5` ad the script parameters
* Select Python 3.6 specified interpreter (i.e. Miniconda Python 3.6)
* Ensure that `.py` type files are being included. Press CMD+, then go to Editor > File Types > Python and
add `.py` in addition to `.pyw` that may be the only one that already exists. Click OK and wait for IntelliJ to reindex
* Now you can set breakpoints in the search.py file and run Debug

### Questions

* Goal: Run Algorithms I create that formulate a plan to navigate the maze

* Question 1: DFS Algorithm using Graph Search and avoid expainding previously
visited states:
    `python pacman.py -l tinyMaze -p SearchAgent -a fn=depthFirstSearch -z 0.5`

### Autograder

* Download autograder from [here](http://ai.berkeley.edu/search.html)
* Copied/pasted the following as a minimum to autograde Question 1

```
test_cases/CONFIG
test_cases/q1/*
autograder.py
grading.py
projectParams.py
searchTestClasses.py
testClasses.py
testParser.py
```

* Run the following commands to convert code from Python 2 to Python 3
```
2to3 autograder.py -w
2to3 grading.py -w
2to3 projectParams.py -w
2to3 searchTestClasses.py -w
2to3 testClasses.py -w
2to3 testParser.py -w
```

* Delete all the `.bak` files that are generated

* Show available autograder commands:
`python autograder.py -h`

* Run the autograder against Question 1
`python autograder.py --question=q1`

### Hints

* Try solving DFS Algorithm first
* Use Stack, Queue and PriorityQueue types in util.py

### Objective

* [ ] - Score of 20

### Files Used

* search.py         - Search Algorithms (i.e. BFS, DFS, A*)
* searchAgent.py    - AI-agent

* pacman.py         - runs Pacman game (with GameState type)
* game.py           - logic describing types: AgentState, Agent, Direction, Grid
* util.py           - data structures for implementing Search Algorithms

# Chapter 2 - Info from Udacity <a id="chapter-2"></a>

* Goal: Help Pac-Man navigate his world in the most efficient way to
find food and other objects by implementing BFS, DFS, and A\* Search.

# Chapter 3 - References <a id="chapter-3"></a>

* Pacman search code https://d17h27t6h515a5.cloudfront.net/topher/2017/January/587da420_pacman/pacman.zip
* Pacman problem set instructions https://inst.eecs.berkeley.edu/~cs188/fa10/projects/search/search.html
* Instructions https://inst.eecs.berkeley.edu/~cs188/fa10/projects/search/search.html