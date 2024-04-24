import tkinter as tk
from tkinter import messagebox
from collections import deque

def find_path_bfs(maze, start, goal):
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
        x, y = current

        if current == goal:
            return path + [current]

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            if (0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and
                    maze[next_x][next_y] == 0 and (next_x, next_y) not in path):
                queue.append(((next_x, next_y), path + [current]))

    return None

def create_maze():
    maze = []
    for i in range(rows):
        row = []
        for j in range(columns):
            if (i, j) in walls:
                row.append(1)  # 1 represents an obstacle
            else:
                row.append(0)  # 0 represents an empty cell
        maze.append(row)
    return maze

def solve_maze_bfs():
    maze = create_maze()
    start = (0, 0)
    goal = (rows - 1, columns - 1)
    path = find_path_bfs(maze, start, goal)
    if path:
        messagebox.showinfo("Path found (BFS)", f"Path: {path}")
    else:
        messagebox.showinfo("No path found (BFS)", "No path found")

def toggle_wall(event):
    x, y = event.x // cell_size, event.y // cell_size
    if (x, y) in walls:
        walls.remove((x, y))
        canvas.itemconfig(cells[x][y], fill="white")
    else:
        walls.add((x, y))
        canvas.itemconfig(cells[x][y], fill="black")

# Create the main window
root = tk.Tk()
root.title("Maze Solver")

# Set maze parameters
rows = 5
columns = 5
cell_size = 30

# Create the canvas for the maze
canvas = tk.Canvas(root, width=columns * cell_size, height=rows * cell_size)
canvas.pack()

# Create cells in the maze
cells = []
for i in range(rows):
    row = []
    for j in range(columns):
        cell = canvas.create_rectangle(j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size, fill="white", outline="gray")
        row.append(cell)
    cells.append(row)

# Add event binding to toggle walls
walls = set()
canvas.bind("<Button-1>", toggle_wall)

# Create solve buttons for BFS
solve_button_bfs = tk.Button(root, text="Solve Maze (BFS)", command=solve_maze_bfs)
solve_button_bfs.pack()

# Run the application
root.mainloop()
