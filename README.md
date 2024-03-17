# Graph Library

A graph library written in python with implementation features of insert_vertex, insert_edge, DFS, BFS, Dijkstra, and find_path.

## Running Instructions

To run:
1. Clone the repository to your machine.
2. Make sure you have python installed and a python interpreter configured
3. Open terminal and run "python main.py"

Currently there is a pre-inputted graph with randomly chosen vertices and edges but you can simply change that to try other graph inputs. Also there are error catchers if you try and input a vertext that doesn't exist in the graph, the program raises a ValueError which ends the program.


## Test Graph

Example used :


![graph_library_example](https://github.com/RileySuomi/graph_library/assets/97262216/d7fb0e90-af7e-4df1-85a2-c818d1612cc8)


Note, DFS doesnt operate in conventions of choosing a child that is "less", it rather just operates in the order of how the stack pop is the last. As shown with example if the neighbors of a node (A) are (B, C) it will pop C first and perform DFS from C then come back to B.



