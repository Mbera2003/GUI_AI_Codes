import tkinter as tk
from tkinter import ttk

def find_s_algorithm(training_data):
    h0 = training_data[0][:-1].copy()
    for instance in training_data:
        if instance[-1] == 'Yes':
            hi = h0.copy()
            for i in range(len(h0)):
                if instance[i] != hi[i]:
                    hi[i] = '?'
            h0 = hi
    return h0

def predict(hypothesis, instance):
    for i in range(len(hypothesis)):
        if hypothesis[i] != '?' and hypothesis[i] != instance[i]:
            return 'No'
    return 'Yes'

def visualize(training_data, hypothesis, prediction):
    root = tk.Tk()
    root.title("Find-S Algorithm")

    # Frames
    input_frame = ttk.Frame(root)
    input_frame.pack(padx=10, pady=10)

    output_frame = ttk.Frame(root)
    output_frame.pack(padx=10, pady=(0, 10))

    # Labels and entry widgets for input data
    headers = ['Sky', 'Air Temp', 'Humidity', 'Wind', 'Water', 'Forecast', 'Play']
    for j, header in enumerate(headers):
        label = ttk.Label(input_frame, text=header)
        label.grid(row=0, column=j, padx=5, pady=5)

    input_entries = []
    for i, row in enumerate(training_data):
        row_entries = []
        for j, value in enumerate(row):
            entry = ttk.Entry(input_frame, width=10)
            entry.grid(row=i + 1, column=j, padx=5, pady=5)
            entry.insert(0, value)
            row_entries.append(entry)
        input_entries.append(row_entries)

    # Function to execute when the button is clicked
    def run_algorithm():
        training_data = [[entry.get() for entry in row] for row in input_entries]
        hypothesis = find_s_algorithm(training_data)
        test_instance = [entry.get() for entry in input_entries[-1]]  # Assume last row is test instance
        prediction = predict(hypothesis, test_instance)

        final_hypothesis_value.config(text="<" + ", ".join(hypothesis) + ">")
        prediction_value.config(text=f"[{prediction}]")

    # Button to trigger the algorithm
    run_button = ttk.Button(input_frame, text="Run Algorithm", command=run_algorithm)
    run_button.grid(row=len(training_data) + 1, columnspan=len(headers), padx=5, pady=10)

    # Labels to display output
    final_hypothesis_label = ttk.Label(output_frame, text="Final Hypothesis:")
    final_hypothesis_label.pack(pady=(20, 5))

    hypothesis_str = "<" + ", ".join(hypothesis) + ">"
    final_hypothesis_value = ttk.Label(output_frame, text=hypothesis_str)
    final_hypothesis_value.pack(pady=5)

    prediction_label = ttk.Label(output_frame, text="Prediction for Test Instance:")
    prediction_label.pack(pady=(20, 5))

    prediction_value = ttk.Label(output_frame, text="")
    prediction_value.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    training_data = [['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
                     ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
                     ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
                     ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']]
    hypothesis = find_s_algorithm(training_data)
    visualize(training_data, hypothesis, "")
