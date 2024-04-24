import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import heapq

def water_jug_a_star(jug1_capacity, jug2_capacity, target_amount):
    start_state = (0, 0)
    open_list = [(0, start_state)]  # (f-value, state)
    closed_set = set()
    steps = []

    while open_list:
        current_cost, current_state = heapq.heappop(open_list)

        if current_state == (target_amount, 0) or current_state == (0, target_amount):
            # Goal reached
            steps.append(current_state)
            return steps

        closed_set.add(current_state)

        # Generate successor states
        successors = generate_successors(current_state, jug1_capacity, jug2_capacity)

        if successors is not None:
            for successor in successors:
                if successor not in closed_set:
                    # Calculate f-value (cost + heuristic)
                    cost = current_cost + 1  # Assuming each step has a cost of 1
                    heuristic = calculate_heuristic(successor, target_amount)
                    f_value = cost + heuristic
                    heapq.heappush(open_list, (f_value, successor))
            steps.append(current_state)

    # No solution found
    return None

def generate_successors(state, jug1_capacity, jug2_capacity):
    # Basic implementation for generating successors
    jug1, jug2 = state
    successors = []

    # Fill jug 1
    successors.append((jug1_capacity, jug2))

    # Fill jug 2
    successors.append((jug1, jug2_capacity))

    # Empty jug 1
    successors.append((0, jug2))

    # Empty jug 2
    successors.append((jug1, 0))

    # Pour water from jug 1 to jug 2
    pour = min(jug1, jug2_capacity - jug2)
    successors.append((jug1 - pour, jug2 + pour))

    # Pour water from jug 2 to jug 1
    pour = min(jug2, jug1_capacity - jug1)
    successors.append((jug1 + pour, jug2 - pour))

    return successors

def calculate_heuristic(state, target_amount):
    # Basic heuristic: Absolute difference between the total amount in both jugs and the target amount
    return abs(sum(state) - target_amount)

def plot_steps(steps, jug1_capacity, jug2_capacity):
    x_labels = ['Jug 1', 'Jug 2']
    x = range(1, 3)

    for i, state in enumerate(steps):
        plt.figure()
        plt.bar(x, state, tick_label=x_labels)
        plt.title(f"Step {i+1}")
        plt.xlabel('Jugs')
        plt.ylabel('Water Amount')
        plt.ylim(0, max(jug1_capacity, jug2_capacity))
        plt.show()

class WaterJugGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Jug Problem Solver")

        self.jug1_label = tk.Label(self.root, text="Capacity of Jug 1:")
        self.jug1_label.pack()
        self.jug1_entry = tk.Entry(self.root)
        self.jug1_entry.pack()

        self.jug2_label = tk.Label(self.root, text="Capacity of Jug 2:")
        self.jug2_label.pack()
        self.jug2_entry = tk.Entry(self.root)
        self.jug2_entry.pack()

        self.target_label = tk.Label(self.root, text="Target Amount:")
        self.target_label.pack()
        self.target_entry = tk.Entry(self.root)
        self.target_entry.pack()

        self.solve_button = tk.Button(self.root, text="Solve", command=self.solve_problem)
        self.solve_button.pack()

    def solve_problem(self):
        try:
            jug1_capacity = int(self.jug1_entry.get())
            jug2_capacity = int(self.jug2_entry.get())
            target_amount = int(self.target_entry.get())

            # Run A* algorithm
            steps = water_jug_a_star(jug1_capacity, jug2_capacity, target_amount)

            if steps:
                messagebox.showinfo("Solution Found", "Steps to reach the target:\n" + "\n".join(map(str, steps)))
                # Plotting steps
                plot_steps(steps, jug1_capacity, jug2_capacity)
            else:
                messagebox.showinfo("No Solution", "No solution found.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for capacities and target amount.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WaterJugGUI(root)
    root.mainloop()
