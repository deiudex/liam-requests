import tkinter as tk
import random

class RandomGridApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Grid Generator")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.button = tk.Button(self.root, text="Randomize Grid", command=self.draw_random_grid)
        self.button.pack(side=tk.BOTTOM, pady=10)

        self.draw_random_grid()

        self.canvas.bind("<Configure>", lambda e: self.draw_random_grid())

    def draw_random_grid(self):
        self.canvas.delete("all")

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if width < 50 or height < 50:
            return

        cols = random.randint(4, 8)
        rows = random.randint(4, 6)

        col_widths = [random.randint(int(width/(cols*2)), int(width/cols)) for _ in range(cols)]
        row_heights = [random.randint(int(height/(rows*2)), int(height/rows)) for _ in range(rows)]

        total_w = sum(col_widths)
        total_h = sum(row_heights)
        scale_x = width / total_w
        scale_y = height / total_h
        col_widths = [int(w * scale_x) for w in col_widths]
        row_heights = [int(h * scale_y) for h in row_heights]

        y = 0
        for r in range(rows):
            x = 0
            for c in range(cols):
                color = random.choice(["#FF9999", "#99CCFF", "#99FF99", "#FFFF99", "#FFCC99", "#CC99FF"])
                self.canvas.create_rectangle(
                    x, y, x + col_widths[c], y + row_heights[r],
                    fill=color, outline="black"
                )
                x += col_widths[c]
            y += row_heights[r]

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomGridApp(root)
    root.mainloop()
