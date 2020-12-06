import tkinter as tk

from src.count import Count

if __name__ == '__main__':
    count = Count()

    window = tk.Tk()
    window.title('简易计算器')
    window.geometry('300x500')

    e2 = tk.Text(window)
    e2.pack()
    window.mainloop()
