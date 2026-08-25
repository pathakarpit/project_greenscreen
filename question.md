# M Coloring Problem

**Difficulty:** Medium  
**Link:** [https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1](https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1)

---

## Problem Statement

**The M Coloring Problem**
=========================

### Description
The M Coloring Problem is a classic graph coloring problem that involves finding the minimum number of colors required to color a given graph such that no two adjacent vertices have the same color. This problem can be approached using backtracking algorithms or branch-and-bound techniques.

### Examples
#### Example 1
* Input: A simple graph with 4 vertices and 5 edges.
	+ Graph structure:
		- Vertex 1 connected to Vertex 2, 3, 4.
		- Vertex 2 connected to Vertex 1, 3, 4.
		- Vertex 3 connected to Vertex 1, 2, 4.
		- Vertex 4 connected to Vertex 1, 2, 3.
* Output: The minimum number of colors required to color the graph.

#### Example 2
* Input: A more complex graph with 6 vertices and 8 edges.
	+ Graph structure:
		- Vertex 1 connected to Vertex 2, 3, 4, 5, 6.
		- Vertex 2 connected to Vertex 1, 3, 4, 5.
		- Vertex 3 connected to Vertex 1, 2, 4, 6.
		- Vertex 4 connected to Vertex 1, 2, 3, 5.
		- Vertex 5 connected to Vertex 1, 2, 4.
		- Vertex 6 connected to Vertex 1, 3.
* Output: The minimum number of colors required to color the graph.

#### Example 3
* Input: A bipartite graph with 10 vertices and 15 edges.
	+ Graph structure:
		- Vertex 1 connected to Vertex 2, 4, 6, 8, 10.
		- Vertex 2 connected to Vertex 1, 5, 7.
		- Vertex 3 connected to Vertex 9.
		- Vertex 4 connected to Vertex 1, 8.
		- Vertex 5 connected to Vertex 2.
		- Vertex 6 connected to Vertex 1, 10.
		- Vertex 7 connected to Vertex 2.
		- Vertex 8 connected to Vertex 1, 4.
		- Vertex 9 connected to Vertex 3.
		- Vertex 10 connected to Vertex 1, 6.
* Output: The minimum number of colors required to color the graph.

### Constraints
* Graph size: N vertices and M edges.
* Number of colors: Use as few colors as possible (minimize the number of colors).
* Coloring constraint: No two adjacent vertices have the same color.
