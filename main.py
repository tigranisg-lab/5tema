import tkinter as tk

root = tk.Tk()
root.title("Решение ОДУ (Эйлер и Хойн)")

tk.Label(root, text="Правая часть f(t,u):").grid(row=0, column=0, sticky='e')
entry_f = tk.Entry(root, width=30)
entry_f.insert(0, "u - t**2 + 1")
entry_f.grid(row=0, column=1, pady=5)

tk.Button(root, text="Решить и построить график").grid(row=5, column=0, columnspan=2, pady=10)

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
