import tkinter as tk

from screens import render_main_enter_screen


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry('600x600')
    window.title('GUI Bank')
    render_main_enter_screen(window)
    window.mainloop()
