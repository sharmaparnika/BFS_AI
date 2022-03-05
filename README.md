# Breadth First Search

BFS is a traversing algorithm where you should start traversing from a selected node (source or starting node) and traverse the graph layerwise thus exploring the neighbour nodes (nodes which are directly connected to source node). You must then move towards the next-level neighbour nodes.

## BFS algorithm 

A standard BFS implementation puts each vertex of the graph into one of two categories:

* Visited
* Not Visited

The purpose of the algorithm is to mark each vertex as visited while avoiding cycles.

The algorithm works as follows:

1.	Start by putting any one of the graph's vertices at the back of a queue.
2.	Take the front item of the queue and add it to the visited list.
3.	Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the back of the queue.
4.	Keep repeating steps 2 and 3 until the queue is empty.
The graph might have two different disconnected parts so to make sure that we cover every vertex, we can also run the BFS algorithm on every node

## Output:

![image](https://user-images.githubusercontent.com/73773202/156866851-5296cd21-d488-49b8-8528-3b7f68ab7ab9.png)


---
