# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

from tkinter import *
from tkinter import messagebox

# Create The Main App Window
app = Tk()

# Change App Text
app.title("Calculate Shortest Path")

# Set Dimensions
app.geometry("400x200")

# Write Text Label
the_text = Label(app, text="Write Your Start Node",
                 height=2, font=("Arial", 20))
the_text.pack()  # Place The Text Into The Main Window

# Node Variables
Nodes = StringVar()

# Set Default Value For Node
Nodes.set("A")

# Create The Input For Node
nodes_input = Entry(app, width=2, font=("Arial", 30), textvariable=Nodes)
nodes_input.pack()  # Place The Input Into The Main Window


def dijkstra(nodes, distances):
    # These are all the nodes which have not been visited yet
    unvisited = {node: None for node in nodes}
    # It will store the shortest distance from one node to another
    visited = {}
    current = 'A'
    # It will store the predecessors of the nodes
    currentDistance = 0
    unvisited[current] = currentDistance
    # Running the loop while all the nodes have been visited
    while True:
        # iterating through all the unvisited node
        for neighbour, distance in distances[current].items():
            # Iterating through the connected nodes of current_node (for)
            # example, a is connected with b and c having values 10 and 3
            # respectively) and the weight of the edges
            if neighbour not in unvisited:
                continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        # Till now the shortest distance between the source node and target node
        # has been found. Set the current node as the target node
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]
    return visited


nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}


def test():

    messagebox.showinfo("Your Shortest Path Is:",
                        "\n".join(dijkstra(nodes, distances)))


print(f"Your Shortest Path Is:")
print(dijkstra(nodes, distances))

# Create The Calculate Button
btn = Button(app, text="Calculate Shortest Path", width=20,
             height=2, bg="#e91e63", fg="white", borderwidth=0, command=test)
btn.pack()  # Place Button in The Main Window


# Run App Infinitely
app.mainloop()

# This code is contributed by Anas Rabea & Ahmed Abdelrhim & Mohamed Saaid
