import tkinter as tk
from tkinter import messagebox

class EightPuzzle:
    def __init__(self, initial_state, goal_state):
        self.state = initial_state
        self.goal_state = goal_state

    def generate_neighbors(self):
        neighbors = []
        empty_tile_index = self.state.index(0)
        row, col = divmod(empty_tile_index, 3)
        if col > 0:
            neighbor = self.state[:]
            neighbor[empty_tile_index], neighbor[empty_tile_index - 1] = neighbor[empty_tile_index - 1], neighbor[empty_tile_index]
            neighbors.append(neighbor)
        if col < 2:
            neighbor = self.state[:]
            neighbor[empty_tile_index], neighbor[empty_tile_index + 1] = neighbor[empty_tile_index + 1], neighbor[empty_tile_index]
            neighbors.append(neighbor)
        if row > 0:
            neighbor = self.state[:]
            neighbor[empty_tile_index], neighbor[empty_tile_index - 3] = neighbor[empty_tile_index - 3], neighbor[empty_tile_index]
            neighbors.append(neighbor)
        if row < 2:
            neighbor = self.state[:]
            neighbor[empty_tile_index], neighbor[empty_tile_index + 3] = neighbor[empty_tile_index + 3], neighbor[empty_tile_index]
            neighbors.append(neighbor)
        return neighbors

    def evaluate(self):
        return sum(x != y for x, y in zip(self.state, self.goal_state))


def hill_climbing(problem, max_iterations=1000):
    current_solution = problem.state
    current_value = problem.evaluate()
    for _ in range(max_iterations):
        neighbors = problem.generate_neighbors()
        neighbor_values = [problem.evaluate() for _ in range(len(neighbors))]
        best_neighbor_value = min(neighbor_values)
        if best_neighbor_value >= current_value:
            break
        best_neighbor_index = neighbor_values.index(best_neighbor_value)
        current_solution = neighbors[best_neighbor_index]
        current_value = best_neighbor_value
    return current_solution, current_value

def print_matrix(matrix):
    for i in range(3):
        print(matrix[i])

def run_hill_climbing():
    initial_state_str = entry_initial_state.get()
    goal_state_str = entry_goal_state.get()

    initial_state = [int(x.strip()) for x in initial_state_str.split(',')]
    goal_state = [int(x.strip()) for x in goal_state_str.split(',')]

    if len(initial_state) != 9 or len(goal_state) != 9:
        messagebox.showerror("Error", "Please enter 9 comma-separated values for each state.")
        return

    eight_puzzle = EightPuzzle(initial_state, goal_state)
    best_solution, best_value = hill_climbing(eight_puzzle)

    best_solution_str = "\n".join([" ".join(map(str, best_solution[i:i+3])) for i in range(0, 9, 3)])
    label_best_solution.config(text="Best Solution:\n" + best_solution_str)
    label_best_value.config(text="Best Value: " + str(best_value))


root = tk.Tk()
root.title("8 Puzzle Solver")

label_initial_state = tk.Label(root, text="Initial State:")
label_initial_state.grid(row=0, column=0, padx=5, pady=5)
entry_initial_state = tk.Entry(root)
entry_initial_state.grid(row=0, column=1, padx=5, pady=5)

label_goal_state = tk.Label(root, text="Goal State:")
label_goal_state.grid(row=1, column=0, padx=5, pady=5)
entry_goal_state = tk.Entry(root)
entry_goal_state.grid(row=1, column=1, padx=5, pady=5)

button_run = tk.Button(root, text="Run Hill Climbing", command=run_hill_climbing)
button_run.grid(row=2, column=0, columnspan=2, pady=10)

label_best_solution = tk.Label(root, text="")
label_best_solution.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

label_best_value = tk.Label(root, text="")
label_best_value.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
