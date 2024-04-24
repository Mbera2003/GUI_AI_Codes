import tkinter as tk
from tkinter import ttk
import numpy as np

def fit_decision_tree(X, y, max_depth=None):
    # Your existing code for fitting the decision tree goes here

def visualize_tree(tree):
    # Your existing code for visualizing the decision tree goes here

def predict_with_gui(X_test, predict_func):
    predictions = predict_func(X_test)
    return predictions

class DecisionTreeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Decision Tree Predictor")

        self.data_label = ttk.Label(self.root, text="Enter test data (each row separated by commas):")
        self.data_label.pack()

        self.data_entry = tk.Text(self.root, height=4, width=50)
        self.data_entry.pack()

        self.predict_button = ttk.Button(self.root, text="Predict", command=self.predict)
        self.predict_button.pack()

        self.output_frame = ttk.Frame(self.root)
        self.output_frame.pack()

    def predict(self):
        data_text = self.data_entry.get("1.0", tk.END).strip()
        if data_text:
            try:
                X_test = [row.split(',') for row in data_text.split('\n')]
                predictions = predict_with_gui(X_test, predict)
                self.show_output(predictions)
            except Exception as e:
                self.show_error(str(e))
        else:
            self.show_error("Please enter test data.")

    def show_output(self, predictions):
        self.clear_output()
        predictions_label = ttk.Label(self.output_frame, text="Predictions:")
        predictions_label.pack()
        for i, prediction in enumerate(predictions):
            prediction_label = ttk.Label(self.output_frame, text=f"Instance {i+1}: {prediction}")
            prediction_label.pack()

    def clear_output(self):
        for widget in self.output_frame.winfo_children():
            widget.destroy()

    def show_error(self, message):
        error_label = ttk.Label(self.output_frame, text=message, foreground="red")
        error_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = DecisionTreeGUI(root)
    root.mainloop()
