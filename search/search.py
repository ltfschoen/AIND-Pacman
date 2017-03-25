# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util
import random

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

# Delete multiple values from a list, given values we want to delete, and return new list. lst not modified.
def delete_by_values(lst, values):
    values_as_set = set(values)
    return [ x for x in lst if x not in values_as_set ]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]

  Depth-First Search (instance of Graph-Search Algorithm)
  - DFS uses LIFO queue (where most recently generated node is chosen to be expansion),
  which must be deepest unexpanded node (one deeper than its parent)
  - Proceeds to deepest levels nodes in current frontier first
  (where nodes have no successors)
  - Expand deepest level nodes, then remove them from frontier, then
  "back up" the search in reverse to the next deepest node (that still
  has unexplored successors)
  - Graph-Search version avoids repeated states and redundant paths, and is
  complete (since all nodes eventually expanded)
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

  function GRAPH-SEARCH(problem) returns a solution, or failure
    initialize the frontier using the initial state of problem
    initialize the explored set to be empty
    loop do
      if the frontier is empty then return failure
      choose a leaf node and remove it from the frontier
      if the node contains a goal state then return corresponding solution
      add the node to explored set
      expand chosen node, adding resulting nodes to frontier
        only if not in frontier or explored set
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """

  # MY INITIAL APPROACH
  #
  # print ("Start: {}".format(problem.getStartState()))
  # print ("Is the start a goal? {}".format(problem.isGoalState(problem.getStartState())))
  # print ("Start's successors: {}".format(problem.getSuccessors(problem.getStartState())))
  #
  # # Note: Running `python pacman.py -l tinyMaze -p SearchAgent -a fn=depthFirstSearch -z 0.5`
  # # runs a PositionSearchProblem in searchAgents.py, which is passed into this DFS method as
  # # argument 'problem'. Familiarise with the properties of the PositionSearchProblem class
  #
  # # Note: Running `python pacman.py -l mediumMaze -p SearchAgent -a fn=depthFirstSearch -z 0.5`
  # # should have length 130
  #
  # # Note: Try using Stack data structure in util.py since DFS uses LIFO
  # # Use Stack for storing what though??
  #
  # # Initialisations including current state and expanding it and adding its successor nodes to frontier
  # state_initial = problem.getStartState()
  # frontier = problem.getSuccessors(state_initial) # i.e. [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
  # explored_set = [] # list of coordinates only
  # state_next_chosen = ()
  # actions = []
  # finished = False
  #
  # # # Add initial node to the explored set
  # # explored_set.append(state_initial)
  #
  # # Loop
  # while not finished:
  #
  #   print ("Length of explored set: {}".format(len(explored_set)))
  #
  #   # Return failure if frontier is empty
  #   if len(frontier) == 0:
  #       print("Failed to find Goal State")
  #       finished = True
  #       return []
  #
  #   # Choose leaf node and remove it from frontier
  #   state_next_chosen = random.choice(frontier)
  #   frontier.remove(state_next_chosen)
  #
  #   # Return solution if chosen leaf node contains a goal state
  #   if problem.isGoalState(state_next_chosen[0]):
  #       print("Successfully found Goal State")
  #       actions.append(state_next_chosen)
  #       finished = True
  #       return actions
  #
  #   # Add chosen leaf node to the explored set
  #   explored_set.append(state_next_chosen[0])
  #
  #   # Get successor nodes of chosen leaf and extra coords from each tuple's first element
  #   successors = problem.getSuccessors(state_next_chosen[0])
  #
  #   # Get successors coords and frontiers coords
  #   successors_coords = [s[0] for s in successors]
  #   frontiers_coords = [f[0] for f in frontier]
  #
  #   # Filter the successors (tuples in list) by removing any that already exist
  #   # in the frontier array or the expored set array
  #   successors_coords_already_in_frontier = list(set(successors_coords) & set(frontiers_coords))
  #
  #   successors_coords_not_already_in_frontier = delete_by_values(successors_coords, successors_coords_already_in_frontier)
  #   successors_coords_already_in_explored_set = list(set(successors_coords_not_already_in_frontier).intersection(explored_set))
  #   successors_coords_not_already_in_frontier_or_explored_set = delete_by_values(successors_coords_not_already_in_frontier, successors_coords_already_in_explored_set)
  #
  #   # Retrieve tuples with coords (first element) matching the list of successors coords not already in frontier or explored set
  #   successors_not_already_in_frontier_or_explored_set = [tup for tup in successors if tup[0] in successors_coords_not_already_in_frontier_or_explored_set]
  #
  #   # Add the filtered list of successor nodes to the frontier to expand the chosen leaf node
  #   for s in successors_not_already_in_frontier_or_explored_set:
  #       frontier.append(s)
  #
  # # Return Sequence of Actions as an array
  # return actions

  # ALTERNATIVE APPROACH

  # Note:
  #
  # An essential resource for help deriving the appropriate code for Pacman is
  # the Python code derived from all the algorithms' pseudo-code in the AIMA textbook
  # found at this link https://github.com/aimacode/aima-python/blob/master/search.py.
  # For instance to solve Question 1 just take a look at the code for the function
  # `graph_search` and modify.

  # function GRAPH-SEARCH(problem)
  # returns a solution, or failure
  def is_goal(node):
      return problem.isGoalState(node)

  # initialize the frontier using the initial state of problem
  init_state = problem.getStartState()
  stack = util.Stack()
  stack.push((init_state, []))

  # initialize the explored set to be empty
  visited = set()

  # loop do
  while not stack.isEmpty():

      # choose a leaf node and remove it from the frontier
      (node, path) = stack.pop()

      # if the node contains a goal state then return corresponding solution
      if is_goal(node):
          # returns a solution
          return path

      # add the node to explored set
      visited.add(node)

      # expand chosen node, adding resulting nodes to frontier
      successors = problem.getSuccessors(node)
      for state, action, cost in successors:
          # only if not in frontier or explored set
          if state not in visited:
              stack.push((state, path + [action]))
  # if the frontier is empty then return failure
  return []

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]

  Breadth-First Search (instance of Graph-Search Algorithm)
  - BFS uses FIFO queue
  """

  # Note: Try using Queue or PriorityQueue data structure since DFS uses FIFO

  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
