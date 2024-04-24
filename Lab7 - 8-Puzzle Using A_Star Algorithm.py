import tkinter as tk
from tkinter import messagebox
import numpy as np
import heapq
import matplotlib.pyplot as plt

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, depth=0):
        self.state, self.parent, self.action, self.depth, self.cost = state, parent, action, depth, 0

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return np.array_equal(self.state, other.state)

def manhattan_distance(state, goal_state):
    return np.sum(np.abs(np.subtract(np.where(state != 0), np.where(goal_state != 0))))

def get_possible_moves(state):
    return [(dr, dc) for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]
            if 0 <= (zero_row := np.where(state == 0)[0][0]) + dr < 3 and 0 <= (zero_col := np.where(state == 0)[1][0]) + dc < 3]

def apply_move(state, move):
    zero_position = np.where(state == 0)
    zero_row, zero_col = zero_position[0][0], zero_position[1][0]
    new_row, new_col = zero_row + move[0], zero_col + move[1]
    new_state = state.copy()
    new_state[zero_row, zero_col], new_state[new_row, new_col] = new_state[new_row, new_col], new_state[zero_row, zero_col]
    return new_state

def a_star_search(initial_state, goal_state):
    initial_node = PuzzleNode(initial_state)
    initial_node.cost = manhattan_distance(initial_state, goal_state)
    frontier, explored, explored_states = [initial_node], set(), set()
    while frontier:
        current_node = heapq.heappop(frontier)
        if np.array_equal(current_node.state, goal_state):
            return current_node
        explored.add(tuple(map(tuple, current_node.state)))
        explored_states.add(tuple(map(tuple, current_node.state)))
        for move in get_possible_moves(current_node.state):
            new_state = apply_move(current_node.state, move)
            if tuple(map(tuple, new_state)) not in explored_states:
                child_node = PuzzleNode(new_state, current_node, move, current_node.depth + 1)
                child_node.cost = child_node.depth + manhattan_distance(new_state, goal_state)
                heapq.heappush(frontier, child_node)
    return None

def plot_steps(steps):
    for i, state in enumerate(steps):
        plt.figure()
        plt.imshow(state, cmap='viridis', interpolation='nearest')
        for r in range(state.shape[0]):
            for c in range(state.shape[1]):
                plt.text(c, r, state[r, c], va='center', ha='center', color='black')
        plt.title(f"Step {i+1}")
        plt.axis('off')
        plt.show()

class PuzzleSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("8-Puzzle Solver")

        self.initial_label = tk.Label(self.root, text="Enter the initial state (3x3 grid) row-wise, separated by space:")
        self.initial_label.pack()
        self.initial_state_entries = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.initial_state_entries[i][j] = tk.Entry(self.root, width=3)
                self.initial_state_entries[i][j].pack(side="left")

        self.goal_label = tk.Label(self.root, text="Enter the goal state (3x3 grid) row-wise, separated by space:")
        self.goal_label.pack()
        self.goal_state_entries = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.goal_state_entries[i][j] = tk.Entry(self.root, width=3)
                self.goal_state_entries[i][j].pack(side="left")

        self.solve_button = tk.Button(self.root, text="Solve Puzzle", command=self.solve_puzzle)
        self.solve_button.pack()

    def solve_puzzle(self):
        initial_state = np.array([[int(entry.get()) for entry in row] for row in self.initial_state_entries])
        goal_state = np.array([[int(entry.get()) for entry in row] for row in self.goal_state_entries])

        # Run A* algorithm
        goal_node = a_star_search(initial_state, goal_state)

        if goal_node:
            path, current_node = [], goal_node
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            path.reverse()
            plot_steps(path)
        else:
            messagebox.showinfo("No Solution", "No solution found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleSolverGUI(root)
    root.mainloop()
