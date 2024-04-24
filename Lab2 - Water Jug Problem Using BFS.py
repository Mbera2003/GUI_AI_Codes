import tkinter as tk
from tkinter import messagebox
from collections import deque
import matplotlib.pyplot as plt

def jug_diagram_visualize(a, b, jug1, jug2):
    final_x = jug1 - a
    final_y = jug2 - b
    key = ['Jug 1', 'Jug 2']
    list1 = [a, b]
    list2 = [final_x, final_y]
    plt.bar(key, list1, color=['red', 'yellow'])
    plt.bar(key, list2, bottom=list1, color=['white', 'white'], edgecolor='black')
    plt.xlabel("Jugs")
    plt.ylabel("Amount of Water (in L)")
    plt.title("Water Jug Problem")
    plt.show()

def water_jug_solver_visualize_bfs(jug1, jug2, goal):
    visited = set()
    queue = deque([(0, 0)])
    while queue:
        current_state = queue.popleft()
        jug_diagram_visualize(current_state[0], current_state[1], jug1, jug2)
        if current_state[0] == goal or current_state[1] == goal:
            messagebox.showinfo("Goal achieved!", "Goal achieved!")
            break
        visited.add(current_state)
        next_states = [
            (jug1, current_state[1]),
            (current_state[0], jug2),
            (0, current_state[1]),
            (current_state[0], 0),
            (max(0, current_state[0] - (jug2 - current_state[1])), min(jug2, current_state[1] + current_state[0])),
            (min(jug1, current_state[0] + current_state[1]), max(0, current_state[1] - (jug1 - current_state[0])))
        ]
        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)

def solve():
    try:
        jug1_capacity = int(jug1_entry.get())
        jug2_capacity = int(jug2_entry.get())
        goal_amount = int(goal_entry.get())
        if jug1_capacity <= 0 or jug2_capacity <= 0 or goal_amount < 0:
            raise ValueError("Capacity and goal must be positive integers.")
        print("\nSteps:")
        water_jug_solver_visualize_bfs(jug1_capacity, jug2_capacity, goal_amount)
    except ValueError as e:
        messagebox.showerror("Error", f"{e}. Please enter valid inputs.")

root = tk.Tk()
root.title("Water Jug Problem Solver")

jug1_label = tk.Label(root, text="Capacity of Jug 1:")
jug1_label.grid(row=0, column=0, padx=5, pady=5)
jug1_entry = tk.Entry(root)
jug1_entry.grid(row=0, column=1, padx=5, pady=5)

jug2_label = tk.Label(root, text="Capacity of Jug 2:")
jug2_label.grid(row=1, column=0, padx=5, pady=5)
jug2_entry = tk.Entry(root)
jug2_entry.grid(row=1, column=1, padx=5, pady=5)

goal_label = tk.Label(root, text="Desired amount to measure:")
goal_label.grid(row=2, column=0, padx=5, pady=5)
goal_entry = tk.Entry(root)
goal_entry.grid(row=2, column=1, padx=5, pady=5)

solve_button = tk.Button(root, text="Solve", command=solve)
solve_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
