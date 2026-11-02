"""Display a live digital clock."""

from datetime import datetime
import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title("Clock")
    clock = tk.Label(root, font=("Arial", 48), padx=20, pady=10)
    clock.pack()

    def update() -> None:
        clock.config(text=datetime.now().strftime("%H:%M:%S"))
        root.after(1000, update)

    update()
    root.mainloop()


if __name__ == "__main__":
    main()