# MutateMaze
Experimentation in creating mazes with python.\
Also see: [FriesW/GrowMaze](https://github.com/FriesW/GrowMaze)

## Use
Created in Python 2.7. To use, simply invoke Run.py. To make mazes in other pieces of software, import make_maze from Maze.py.

## A maze!
This looks okay in a desktop browser, but might not look right on mobile. Aparently mobile github code blocks don't use a monospace font.
```
Maze Hash: ge3hymjtpqzdaod4j5yvuv3tonyeynct
Dimensions: 16x13
Mutations: 208
███████████████████████████████████████████████████████████████████████████████████████████████████
███                           ███   ███   ███   ███         ███                           ███   ███
███████████████   ███   █████████   ███   ███   ███   █████████   ███████████████   █████████   ███
███         ███   ███         ███         ███   ███                           ███   ███         ███
█████████   ███████████████   █████████   ███   █████████   ███████████████████████████   █████████
███                     ███                                 ███   ███         ███         ███   ███
███   ███   ███   ███   █████████████████████   ███████████████   █████████   ███   █████████   ███
███   ███   ███   ███               ███   ███   ███                     ███                     ███
█████████   ███████████████████████████   ███   █████████   █████████   ███   ███████████████   ███
███                     ███                     ███   ███   ███                           ███   ███
███   ███████████████████████████   ███████████████   █████████   █████████   ███   ███████████████
███   ███   ███                     ███                     ███   ███         ███         ███   ███
███   ███   ███████████████   ███   ███   ███████████████   ███   █████████████████████   ███   ███
███                           ███         ███               ███   ███                           ███
█████████████████████   █████████████████████   ███   ███████████████████████████   █████████   ███
███                     ███                     ███                     ███   ███   ███   ███   ███
█████████   ███████████████████████████   █████████   █████████████████████   ███   ███   █████████
███                                 ███         ███                                 ███         ███
███████████████   ███   █████████   ███   ███████████████   █████████   █████████████████████   ███
███               ███   ███   ███   ███   ███         ███   ███                     ███         ███
███████████████   █████████   ███████████████   ███████████████████████████   ███████████████   ███
███                     ███                     ███                     ███   ███               ███
███████████████   ███████████████████████████   ███   ███   █████████   █████████   ███████████████
███               ███                                 ███   ███   ███                           ███
███   █████████████████████   █████████████████████   █████████   █████████   ███   ███████████████
███                                             ███                     ███   ███               ███
███████████████████████████████████████████████████████████████████████████████████████████████████
```

## How it works
A grid is created, which is essentially a 2D doubly-linked list. This grid is then filled with a one path, s-curve maze. To see this, run make_maze with 0 mutations. Then, a disconnected adjacency is chosen at random and connected. This creates a loop in the maze. The loop is found by backtracking to the origin of the maze from both nodes of the adjacency, and then removing similar items from the backtrack. Then, a random adjacency on the loop is chosen to be closed.

Part of the reason for this code was to experiment with a different and novel way to generate mazes. However, this implementation is very inefficient. I wonder if there would be a more efficient way... Either way, I prefer the [growth method](https://github.com/FriesW/GrowMaze).
