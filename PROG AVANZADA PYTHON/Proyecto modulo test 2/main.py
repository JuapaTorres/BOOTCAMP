import tkinter as tk
from gui import InterfazCliente

def main():
    root = tk.Tk()
    app = InterfazCliente(root)
    root.mainloop()

if __name__ == "__main__":
    main()