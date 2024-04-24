import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os

class ExperimentDashboard:
    def __init__(self, master):
        self.master = master
        self.master.title("AIML Dashboard")
        self.master.geometry("400x500")

        self.main_frame = tk.Frame(master)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.label_heading = tk.Label(self.main_frame, text="Experiment Dashboard", font=("Arial", 16, "bold"))
        self.label_heading.pack(pady=10)

        self.label_experiments = tk.Label(self.main_frame, text="List of Experiments", font=("Arial", 12))
        self.label_experiments.pack()

        self.scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.experiments_frame = tk.Frame(self.main_frame)
        self.experiments_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.experiments_frame, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar.config(command=self.canvas.yview)

        self.experiment_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.experiment_frame, anchor=tk.NW)

        experiments = {
            "Lab 1.1: Maze Problem Using DFS": "Lab1.1 - Maze Problem Using DFS.py",
            "Lab 1.2: Maze Problem Using BFS": "Lab1.2 - Maze Problem Using BFS.py",
            "Lab2: Water Jug Problem Using BFS": "Lab2 - Water Jug Problem Using BFS.py",
            "Lab3: Tic-Tac-Toe Using BFS": "Lab3 - Tic-Tac-Toe Using BFS.py",
            "Lab4: 8-Puzzle Using Best First Search": "Lab4 - 8-Puzzle Using Best First Search.py",
            "Lab5: 8-Puzzle Using Hill Climbing": "Lab5 - 8-Puzzle Using Hill Climbing.py",
            "Lab6: Water Jug Problem Using A_Star Algorithm": "Lab6 - Water Jug Problem Using A_Star Algorithm.py",
            "Lab7: 8-Puzzle Using A_Star Algorithm": "Lab7 - 8-Puzzle Using A_Star Algorithm.py",
            "Lab8: Traveling Salesman Problem Using Heuristic Search": "Lab8 - Traveling Salesman Problem Using Heuristic Search.py",
            "Lab9: Find-S Algorithm": "Lab9 - Find-S Algorithm.py",
            "Lab10: Candidate Elimination Algorithm": "Lab10 - Candidate Elimination Algorithm.py",
            "Lab11: Decision Tree Using CART": "Lab11 - Decision Tree Using CART.py"
        }

        for experiment, script_name in experiments.items():
            button = tk.Button(self.experiment_frame, text=experiment, command=lambda script=script_name: self.run_experiment(script), width=50)
            button.pack(pady=5)
            button.config(cursor="hand2")

        self.scrollable_frame_id = self.canvas.create_window((0, 0), window=self.experiment_frame, anchor="nw")

        self.experiment_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        self.label_info = tk.Label(self.master, text="Moulima Bera, 219302099\nIT-6B", font=("Arial", 10))
        self.label_info.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfigure(self.scrollable_frame_id, width=event.width)

    def run_experiment(self, script_name):
        input_dialog = tk.Toplevel(self.master)
        input_dialog.title("Experiment Input")
        input_dialog.geometry("300x200")

        label_input = tk.Label(input_dialog, text="Enter any number between 1-10:")
        label_input.pack(pady=10)

        entry_input = tk.Entry(input_dialog, width=30)
        entry_input.pack(pady=5)

        def run_with_input():
            input_value = entry_input.get()
            home_dir = os.path.expanduser("C:/Users/Puja/OneDrive/")
            script_path = os.path.join(home_dir, "Desktop", "AIML Lab", script_name)
            if os.path.isfile(script_path):
                os.system(f"python \"{script_path}\" \"{input_value}\"")
            else:
                messagebox.showerror("Error", f"No Python script found for {script_name}.")
            input_dialog.destroy()

        button_run = tk.Button(input_dialog, text="Run", command=run_with_input)
        button_run.pack(pady=10)
if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="darkgray")  # Set the background color of the root window
    app = ExperimentDashboard(root)
    root.mainloop()
