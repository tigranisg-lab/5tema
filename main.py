import tkinter as tk
import math

def make_f(expr_str):
    def f(t, u):
        safe_dict = {'sin': math.sin, 'cos': math.cos, 't': t, 'u': u}
        return eval(expr_str, {"__builtins__": {}}, safe_dict)
    f(0, 0.1) 
    return f

root = tk.Tk()
root.title("Решение ОДУ (Эйлер и Хойн)")

tk.Label(root, text="Правая часть f(t,u):").grid(row=0, column=0, sticky='e')
entry_f = tk.Entry(root, width=30); entry_f.insert(0, "u - t**2 + 1"); entry_f.grid(row=0, column=1)

tk.Label(root, text="Начальное время t0:").grid(row=1, column=0, sticky='e')
entry_t0 = tk.Entry(root, width=15); entry_t0.insert(0, "0"); entry_t0.grid(row=1, column=1, sticky='w')

tk.Label(root, text="Конечное время T:").grid(row=2, column=0, sticky='e')
entry_T = tk.Entry(root, width=15); entry_T.insert(0, "2"); entry_T.grid(row=2, column=1, sticky='w')

tk.Label(root, text="Начальное условие u0:").grid(row=3, column=0, sticky='e')
entry_u0 = tk.Entry(root, width=15); entry_u0.insert(0, "0.5"); entry_u0.grid(row=3, column=1, sticky='w')

tk.Label(root, text="Шаг h:").grid(row=4, column=0, sticky='e')
entry_h = tk.Entry(root, width=15); entry_h.insert(0, "0.1"); entry_h.grid(row=4, column=1, sticky='w')

tk.Button(root, text="Решить и построить график").grid(row=5, column=0, columnspan=2, pady=10)
canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
