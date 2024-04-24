import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def tsp_heuristic(graph):
    start_node, visited = 0, [0]
    unvisited = set(range(1, len(graph)))
    while unvisited:
        current_node = visited[-1]
        nearest_node = min(unvisited, key=lambda x: graph[current_node][x])
        visited.append(unvisited.remove(nearest_node) or nearest_node)
    return visited, sum(graph[visited[i - 1]][node] for i, node in enumerate(visited))

class TSPSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Traveling Salesman Problem Solver")

        self.num_nodes_label = tk.Label(self.root, text="Enter the number of nodes:")
        self.num_nodes_label.grid(row=0, column=0, pady=5)

        self.num_nodes_entry = tk.Entry(self.root)
        self.num_nodes_entry.grid(row=0, column=1, pady=5)

        self.graph_label = tk.Label(self.root, text="Enter the distance matrix for the graph:")
        self.graph_label.grid(row=1, column=0, columnspan=2, pady=5)

        self.graph_entries = []
        for i in range(5):  # Maximum of 5 nodes for simplicity
            row_entries = []
            for j in range(5):
                entry = tk.Entry(self.root, width=5)
                entry.grid(row=i + 2, column=j, padx=5, pady=2)
                row_entries.append(entry)
            self.graph_entries.append(row_entries)

        self.solve_button = tk.Button(self.root, text="Solve TSP", command=self.solve_tsp)
        self.solve_button.grid(row=7, column=0, columnspan=2, pady=10)

    def solve_tsp(self):
        try:
            num_nodes = int(self.num_nodes_entry.get())
            graph = np.zeros((num_nodes, num_nodes), dtype=int)
            for i in range(num_nodes):
                for j in range(num_nodes):
                    graph[i, j] = int(self.graph_entries[i][j].get())

            path, distance = tsp_heuristic(graph)
            messagebox.showinfo("TSP Solution", f"Optimal Path: {path}\nTotal Distance: {distance}")

            plt.figure(figsize=(8, 6))
            plt.title("Traveling Salesman Problem - Optimal Path")
            plt.scatter(*zip(*enumerate(path)), color='red', zorder=2)
            for i in range(len(path) - 1):
                plt.plot([path[i], path[i + 1]], [i, i + 1], color='blue')
                plt.annotate("", xy=(path[i + 1], i + 1), xytext=(path[i], i), arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="green", linewidth=2))
            plt.plot([path[-1], path[0]], [len(path) - 1, 0], color='blue')
            plt.annotate("", xy=(path[0], 0), xytext=(path[-1], len(path) - 1), arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="green", linewidth=2))
            plt.xlabel("Node")
            plt.ylabel("Order of Visit")
            plt.grid(True)
            plt.show()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for the distance matrix.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TSPSolverGUI(root)
    root.mainloop()
