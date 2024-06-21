import tkinter as tk
import numpy as np

class GameOfLife:
    def __init__(self, root, rows=50, cols=50, cell_size=10):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.is_running = False

        self.canvas = tk.Canvas(root, width=cols*cell_size, height=rows*cell_size, bg="white")
        self.canvas.pack()

        self.grid = np.zeros((rows, cols), dtype=int)
        self.rectangles = {}
        self.draw_grid()

        self.canvas.bind("<Button-1>", self.toggle_cell)
        self.root.bind("<space>", self.start_stop)
        self.root.bind("<Return>", self.step)

        self.root.after(100, self.update)

    def draw_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
                self.rectangles[(r, c)] = rect

    def toggle_cell(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        self.grid[row, col] = 1 - self.grid[row, col]
        color = "black" if self.grid[row, col] == 1 else "white"
        self.canvas.itemconfig(self.rectangles[(row, col)], fill=color)

    def start_stop(self, event=None):
        self.is_running = not self.is_running

    def step(self, event=None):
        self.grid = self.next_generation()
        self.update_canvas()

    def update(self):
        if self.is_running:
            self.grid = self.next_generation()
            self.update_canvas()
        self.root.after(100, self.update)

    def update_canvas(self):
        for r in range(self.rows):
            for c in range(self.cols):
                color = "black" if self.grid[r, c] == 1 else "white"
                self.canvas.itemconfig(self.rectangles[(r, c)], fill=color)

    def next_generation(self):
        new_grid = np.zeros((self.rows, self.cols), dtype=int)
        for r in range(self.rows):
            for c in range(self.cols):
                alive_neighbors = np.sum(self.grid[r-1:r+2, c-1:c+2]) - self.grid[r, c]
                if self.grid[r, c] == 1 and alive_neighbors in [2, 3]:
                    new_grid[r, c] = 1
                elif self.grid[r, c] == 0 and alive_neighbors == 3:
                    new_grid[r, c] = 1
        return new_grid

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Conway's Game of Life")
    game = GameOfLife(root)
    root.mainloop()
