import tkinter as tk
from tkinter import messagebox

class PuzzleNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = 0

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))


class BestFirstSearch:
    def __init__(self, start_state, goal_state):
        self.start_node = PuzzleNode(start_state)
        self.goal_state = goal_state
        self.explored = set()
        self.frontier = []

    def h(self, state):
        # Calculate the number of misplaced tiles (heuristic function)
        count = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != self.goal_state[i][j]:
                    count += 1
        return count

    def get_blank_position(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def generate_successors(self, node):
        successors = []
        i, j = self.get_blank_position(node.state)
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in moves:
            new_i, new_j = i + move[0], j + move[1]
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row[:] for row in node.state]
                new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                successor_node = PuzzleNode(new_state, node, move)
                successors.append(successor_node)
        return successors

    def solve(self):
        self.frontier.append(self.start_node)
        while self.frontier:
            current_node = min(self.frontier)
            self.frontier.remove(current_node)
            self.explored.add(current_node)
            if current_node.state == self.goal_state:
                return self.construct_solution(current_node)
            successors = self.generate_successors(current_node)
            for successor in successors:
                if successor not in self.explored:
                    successor.cost = self.h(successor.state)
                    self.frontier.append(successor)
        return None

    def construct_solution(self, node):
        solution = []
        while node.parent:
            solution.append((node.move, node.state))
            node = node.parent
        solution.reverse()
        return solution

class PuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Puzzle Solver")

        self.start_label = tk.Label(self.root, text="Enter the initial state (3x3 grid) row-wise, separated by space:")
        self.start_label.pack()

        self.start_state_entries = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.start_state_entries[i][j] = tk.Entry(self.root, width=3)
                self.start_state_entries[i][j].pack(side="left")

        self.goal_label = tk.Label(self.root, text="Enter the goal state (3x3 grid) row-wise, separated by space:")
        self.goal_label.pack()

        self.goal_state_entries = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.goal_state_entries[i][j] = tk.Entry(self.root, width=3)
                self.goal_state_entries[i][j].pack(side="left")

        self.solve_button = tk.Button(self.root, text="Solve Puzzle", command=self.solve_puzzle)
        self.solve_button.pack()

        self.solution_text = tk.Text(self.root, height=10, width=50)
        self.solution_text.pack()

    def solve_puzzle(self):
        start_state = [[int(entry.get()) for entry in row] for row in self.start_state_entries]
        goal_state = [[int(entry.get()) for entry in row] for row in self.goal_state_entries]

        solver = BestFirstSearch(start_state, goal_state)
        solution = solver.solve()

        if solution:
            self.solution_text.delete(1.0, tk.END)
            self.solution_text.insert(tk.END, "Moves to reach the goal state:\n")
            for move, state in solution:
                if move:
                    self.solution_text.insert(tk.END, f"Move: {move}\n")
                self.solution_text.insert(tk.END, f"{state[0]}\n{state[1]}\n{state[2]}\n\n")
        else:
            messagebox.showinfo("No Solution", "No solution found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleGUI(root)
    root.mainloop()
