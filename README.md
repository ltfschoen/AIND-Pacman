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
* IntelliJ: File > Project Structure > Project Settings > Project > Project SDK > Python 2.7 (~/miniconda3/bin/python)
* Review possible commands in search/commands.txt:
* Change into the search directory `cd search`
* Show Help of possible commands `python pacman.py -h`
* Run Program with a possible command: `python pacman.py --layout smallClassic --zoom 2`
* Run MyPy Linter with `mypy search/pacman.py`

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