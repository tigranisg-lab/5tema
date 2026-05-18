import tkinter as tk
import math

def make_f(expr_str):
    def f(t, u):
        safe_dict = {'sin': math.sin, 'cos': math.cos, 'exp': math.exp, 't': t, 'u': u}
        return eval(expr_str, {"__builtins__": {}}, safe_dict)
    f(0, 0.1) 
    return f

def euler_method(f, t0, T, u0, h):
    t_vals, u_vals = [t0], [u0]
    t, u = t0, u0
    while t < T - 1e-9: 
        u = u + h * f(t, u)
        t = t + h
        t_vals.append(t)
        u_vals.append(u)
    return t_vals, u_vals

def heun_method(f, t0, T, u0, h):
    t_vals, u_vals = [t0], [u0]
    t, u = t0, u0
    while t < T - 1e-9:
        k1 = f(t, u)
        u_predictor = u + h * k1
        k2 = f(t + h, u_predictor)
        u = u + h * 0.5 * (k1 + k2)
        t = t + h
        t_vals.append(t)
        u_vals.append(u)
    return t_vals, u_vals

root = tk.Tk()
root.title("Решение ОДУ")

tk.Label(root, text="Правая часть f(t,u):").grid(row=0, column=0)
entry_f = tk.Entry(root); entry_f.insert(0, "u - t**2 + 1"); entry_f.grid(row=0, column=1)

tk.Label(root, text="t0:").grid(row=1, column=0)
entry_t0 = tk.Entry(root); entry_t0.insert(0, "0"); entry_t0.grid(row=1, column=1)

tk.Label(root, text="T:").grid(row=2, column=0)
entry_T = tk.Entry(root); entry_T.insert(0, "2"); entry_T.grid(row=2, column=1)

tk.Label(root, text="u0:").grid(row=3, column=0)
entry_u0 = tk.Entry(root); entry_u0.insert(0, "0.5"); entry_u0.grid(row=3, column=1)

tk.Label(root, text="h:").grid(row=4, column=0)
entry_h = tk.Entry(root); entry_h.insert(0, "0.1"); entry_h.grid(row=4, column=1)

tk.Button(root, text="Решить").grid(row=5, column=0, columnspan=2)
canvas = tk.Canvas(root, width=600, height=400, bg='white'); canvas.grid(row=7, column=0, columnspan=2)

root.mainloop()
