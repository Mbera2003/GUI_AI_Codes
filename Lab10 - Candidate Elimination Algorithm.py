import tkinter as tk
from tkinter import ttk, messagebox

def train_candidate_elimination(data, num_features, max_hypothesis=10):
    G, S = [(['?'] * num_features, ['?'] * num_features)], [('0' * num_features, '?' * num_features)]
    total_hypothesis = 0

    def remove_inconsistent(instance, hypothesis):
        return [h for h in hypothesis if all(h_i == '?' or h_i == i for h_i, i in zip(h, instance))]

    def generalize(instance, hypothesis):
        new_hypothesis = [([h_i if h_i == i else '?' for h_i, i in zip(h[0], instance)], h[1]) for h in hypothesis]
        return hypothesis + new_hypothesis[:max_hypothesis]

    def specialize(instance, hypothesis):
        new_hypothesis = [(h[0][:i] + [instance[i]] + h[0][i + 1:], h[1][:i] + [instance[i]] + h[1][i + 1:]) for h in hypothesis for i, h_i in enumerate(h[0]) if h_i == '?']
        return hypothesis + new_hypothesis[:max_hypothesis]

    for instance in data:
        x, y = instance[:-1], instance[-1]
        if total_hypothesis >= max_hypothesis:
            break
        if y == 1:
            S, G = generalize(x, S), remove_inconsistent(x, G)
        else:
            G, S = specialize(x, G), remove_inconsistent(x, S)
        total_hypothesis = len(G) + len(S)
    return G, S

class CandidateEliminationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Candidate Elimination Algorithm")

        self.num_features_label = ttk.Label(self.root, text="Number of Features:")
        self.num_features_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.num_features_entry = ttk.Entry(self.root)
        self.num_features_entry.grid(row=0, column=1, padx=5, pady=5)

        self.data_label = ttk.Label(self.root, text="Training Data:")
        self.data_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.data_entries = []
        for i in range(5):  # Maximum of 5 data points for simplicity
            row_entries = []
            for j in range(7):  # Assuming 7 attributes (features) and 1 label
                entry = ttk.Entry(self.root, width=10)
                entry.grid(row=i + 2, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.data_entries.append(row_entries)

        self.solve_button = ttk.Button(self.root, text="Run Algorithm", command=self.run_algorithm)
        self.solve_button.grid(row=7, column=0, columnspan=2, padx=5, pady=10)

        self.output_frame = ttk.Frame(self.root)
        self.output_frame.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    def run_algorithm(self):
        try:
            num_features = int(self.num_features_entry.get())
            data = [[entry.get() for entry in row] for row in self.data_entries]

            G, S = train_candidate_elimination(data, num_features)

            self.show_output(G, S)
        except ValueError:
            self.show_error("Please enter a valid integer for the number of features.")

    def show_output(self, G, S):
        self.clear_output()
        g_label = ttk.Label(self.output_frame, text="General Hypothesis (G):")
        g_label.pack()
        for h in G:
            h_label = ttk.Label(self.output_frame, text=h)
            h_label.pack()

        s_label = ttk.Label(self.output_frame, text="\nSpecific Hypothesis (S):")
        s_label.pack()
        for h in S:
            h_label = ttk.Label(self.output_frame, text=h)
            h_label.pack()

    def clear_output(self):
        for widget in self.output_frame.winfo_children():
            widget.destroy()

    def show_error(self, message):
        messagebox.showerror("Error", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = CandidateEliminationGUI(root)
    root.mainloop()
