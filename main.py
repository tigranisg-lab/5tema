import tkinter as tk
import math

def make_f(expr_str):
    allowed_names = {
        'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
        'exp': math.exp, 'log': math.log, 'log10': math.log10,
        'sqrt': math.sqrt, 'pi': math.pi, 'e': math.e,
        'abs': abs, 'pow': pow}
    def f(t, u):
        return eval(expr_str, {"__builtins__": {}}, {**allowed_names, 't': t, 'u': u})
    try:
        f(0, 0)
    except Exception as e:
        raise ValueError(f"Ошибка в выражении: {e}")
    return f

def euler_method(f, t0, T, u0, h):
    t_vals = [t0]
    u_vals = [u0]
    t = t0
    u = u0
    while t < T - 1e-12:
        u = u + h * f(t, u)
        t = t + h
        t_vals.append(t)
        u_vals.append(u)
    return t_vals, u_vals


def heun_method(f, t0, T, u0, h):
    t_vals = [t0]
    u_vals = [u0]
    t = t0
    u = u0
    while t < T - 1e-12:
        k1 = f(t, u)
        u_predictor = u + h * k1
        k2 = f(t + h, u_predictor)
        u = u + h * 0.5 * (k1 + k2)
        t = t + h
        t_vals.append(t)
        u_vals.append(u)
    return t_vals, u_vals

root = tk.Tk()
root.title("Численное решение ОДУ (Эйлер и Хойн)")

# Поля ввода
tk.Label(root, text="Правая часть f(t,u):").grid(row=0, column=0, sticky='e')
entry_f = tk.Entry(root, width=25)
entry_f.insert(0, "u - t**2 + 1")
entry_f.grid(row=0, column=1)

tk.Label(root, text="t0:").grid(row=1, column=0, sticky='e')
entry_t0 = tk.Entry(root, width=10)
entry_t0.insert(0, "0")
entry_t0.grid(row=1, column=1, sticky='w')

tk.Label(root, text="T:").grid(row=2, column=0, sticky='e')
entry_T = tk.Entry(root, width=10)
entry_T.insert(0, "2")
entry_T.grid(row=2, column=1, sticky='w')

tk.Label(root, text="u0:").grid(row=3, column=0, sticky='e')
entry_u0 = tk.Entry(root, width=10)
entry_u0.insert(0, "0.5")
entry_u0.grid(row=3, column=1, sticky='w')

tk.Label(root, text="Шаг h:").grid(row=4, column=0, sticky='e')
entry_h = tk.Entry(root, width=10)
entry_h.insert(0, "0.1")
entry_h.grid(row=4, column=1, sticky='w')

# Холст и статус
canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

status = tk.Label(root, text="Введите данные и нажмите 'Решить'", fg="blue")
status.grid(row=7, column=0, columnspan=2)

def solve():
    try:
        expr = entry_f.get()
        t0 = float(entry_t0.get())
        T = float(entry_T.get())
        u0 = float(entry_u0.get())
        h = float(entry_h.get())

        if t0 >= T:
            raise ValueError("t0 должно быть меньше T")
        if h <= 0:
            raise ValueError("Шаг h должен быть положительным")

        f = make_f(expr)
        t_euler, u_euler = euler_method(f, t0, T, u0, h)
        t_heun, u_heun = heun_method(f, t0, T, u0, h)

        plot(t_euler, u_euler, t_heun, u_heun)
        status.config(text="График построен", fg="green")

    except Exception as e:
        status.config(text=f"Ошибка: {e}", fg="red")
        canvas.delete("all")


def plot(t1, u1, t2, u2):
    canvas.delete("all")
    W = 600
    H = 400
    margin = 50

    all_u = u1 + u2
    u_min, u_max = min(all_u), max(all_u)
    if u_min == u_max:
        u_min -= 1
        u_max += 1
    t_min = min(t1[0], t2[0])
    t_max = max(t1[-1], t2[-1])

    def tx(t):
        return margin + (t - t_min) / (t_max - t_min) * (W - 2 * margin)

    def ty(u):
        return H - margin - (u - u_min) / (u_max - u_min) * (H - 2 * margin)

    canvas.create_line(margin, H - margin, W - margin, H - margin, arrow=tk.LAST)
    canvas.create_line(margin, H - margin, margin, margin, arrow=tk.LAST)
    canvas.create_text(W - margin + 10, H - margin, text="t", anchor=tk.W)
    canvas.create_text(margin - 10, margin, text="u", anchor=tk.E)

    for i in range(6):
        t_val = t_min + i * (t_max - t_min) / 5
        x = tx(t_val)
        canvas.create_line(x, H - margin - 5, x, H - margin + 5)
        canvas.create_text(x, H - margin + 15, text=f"{t_val:.2f}")

    for i in range(6):
        u_val = u_min + i * (u_max - u_min) / 5
        y = ty(u_val)
        canvas.create_line(margin - 5, y, margin + 5, y)
        canvas.create_text(margin - 20, y, text=f"{u_val:.2f}")

    def draw_line(t_vals, u_vals, color, label, y_legend):
        points = []
        for i in range(len(t_vals)):
            x = tx(t_vals[i])
            y = ty(u_vals[i])
            points.extend([x, y])
        canvas.create_line(points, fill=color, width=2)

        canvas.create_line(W - 150, y_legend, W - 130, y_legend, fill=color, width=2)
        canvas.create_text(W - 120, y_legend, text=label, anchor=tk.W)

    draw_line(t1, u1, "blue", "Эйлер", 20)
    draw_line(t2, u2, "red", "Хойн", 40)

btn_solve = tk.Button(root, text="Решить и построить", command=solve)
btn_solve.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()



