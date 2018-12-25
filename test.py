import tkinter as tk
import tkinter.messagebox as tk_mb
import matplotlib as mpl
import matplotlib.pyplot as plt
import milne


class Window:
    def __init__(self):
        self.root = None
        self.f_entry = None
        self.f_label = None
        self.x_entry = None
        self.x_label = None
        self.y_entry = None
        self.y_label = None
        self.a_entry = None
        self.a_label = None
        self.b_entry = None
        self.b_label = None
        self.n_entry = None
        self.n_label = None
        self.decision_label = None
        self.decision_entry = None

        self.f_var = None
        self.x_var = None
        self.y_var = None
        self.b_var = None
        self.n_var = None
        self.decision_var = None

        self.calc_button = None
        self.refresh_button = None

        self.TEXT_WIDTH = 20
        self.PAD_X = 2
        self.PAD_Y = 5
        self.WIDTH = 200
        self.HEIGHT = 350

        self.x = list()
        self.y = list()

    def start(self):
        self.root = tk.Tk()
        self.root.title("YegorR: Задача Коши")
        self.root.geometry(str(self.WIDTH)+"x"+str(self.HEIGHT))
        self.root.resizable(width=False, height=False)
        self.init_vars()
        self.widgets()
        self.layout()

        self.loop()

    def loop(self):
        self.root.mainloop()

    def init_vars(self):
        self.f_var = tk.StringVar(value="(y**2)-x")
        self.x_var = tk.StringVar(value="1")
        self.y_var = tk.StringVar(value="0")
        self.b_var = tk.StringVar(value="3")
        self.n_var = tk.StringVar(value="10")
        self.decision_var = tk.StringVar()

    def widgets(self):
        self.f_entry = tk.Entry(self.root, width=self.TEXT_WIDTH,
                                textvariable=self.f_var)
        self.f_label = tk.Label(self.root, text="f")
        self.x_entry = tk.Entry(self.root, width=self.TEXT_WIDTH,
                                textvariable=self.x_var)
        self.x_label = tk.Label(self.root, text="x0")
        self.y_entry = tk.Entry(self.root, width=self.TEXT_WIDTH,
                                textvariable=self.y_var)
        self.y_label = tk.Label(self.root, text="y0")
        self.a_entry = tk.Entry(self.root, width=self.TEXT_WIDTH,
                                textvariable=self.x_var, state=tk.DISABLED)
        self.a_label = tk.Label(self.root, text="a")
        self.b_entry = tk.Entry(self.root, width=self.TEXT_WIDTH,
                                textvariable=self.b_var)
        self.b_label = tk.Label(self.root, text="b")
        self.n_entry = tk.Entry(self.root, width=self.TEXT_WIDTH,
                                textvariable=self.n_var)
        self.n_label = tk.Label(self.root, text="n")

        self.calc_button = tk.Button(self.root, text="Решение",
                                     command=self.calculate)
        self.refresh_button = tk.Button(self.root, text="Очистить",
                                        command=self.refresh)
        self.decision_label = tk.Label(self.root, text="Решение")
        self.decision_entry = tk.Entry(self.root, width=self.TEXT_WIDTH,
                                       textvariable=self.decision_var)

    def layout(self):
        self.f_label.grid(row=0, column=0, padx=self.PAD_X, pady=self.PAD_Y,
                          sticky=tk.W)
        self.f_entry.grid(row=0, column=1, padx=self.PAD_Y, pady=self.PAD_Y,
                          sticky=tk.W)
        self.x_label.grid(row=1, column=0, padx=self.PAD_X, pady=self.PAD_Y,
                          sticky=tk.W)
        self.x_entry.grid(row=1, column=1, padx=self.PAD_Y, pady=self.PAD_Y,
                          sticky=tk.W)
        self.y_label.grid(row=2, column=0, padx=self.PAD_X, pady=self.PAD_Y,
                          sticky=tk.W)
        self.y_entry.grid(row=2, column=1, padx=self.PAD_Y, pady=self.PAD_Y,
                          sticky=tk.W)
        self.a_label.grid(row=3, column=0, padx=self.PAD_X, pady=self.PAD_Y,
                          sticky=tk.W)
        self.a_entry.grid(row=3, column=1, padx=self.PAD_Y, pady=self.PAD_Y,
                          sticky=tk.W)
        self.b_label.grid(row=4, column=0, padx=self.PAD_X, pady=self.PAD_Y,
                          sticky=tk.W)
        self.b_entry.grid(row=4, column=1, padx=self.PAD_Y, pady=self.PAD_Y,
                          sticky=tk.W)
        self.n_label.grid(row=5, column=0, padx=self.PAD_X, pady=self.PAD_Y,
                          sticky=tk.W)
        self.n_entry.grid(row=5, column=1, padx=self.PAD_Y, pady=self.PAD_Y,
                          sticky=tk.W)
        self.calc_button.grid(row=6, column=0, columnspan=2, padx=self.PAD_X,
                              pady=self.PAD_Y)
        self.refresh_button.grid(row=7, column=0, columnspan=2,
                                 padx=self.PAD_X)
        self.decision_label.grid(row=8, column=0, padx=self.PAD_X,
                                 pady=self.PAD_Y+30)
        self.decision_entry.grid(row=8, column=1, padx=self.PAD_X,
                                 pady=self.PAD_Y+30)

    def calculate(self):
        if not self.validate_date():
            return
        x_0 = float(self.x_var.get())
        y_0 = float(self.y_var.get())
        b = float(self.b_var.get())
        n = int(self.n_var.get())

        try:
            f = lambda x,y: eval(self.f_var.get())
            x, y = milne.runge_cutta_4(x_0, y_0, b, f, n)
            milne.milne(x, y, b, f, n)
        except OverflowError:
            tk_mb.showwarning("Ошибка", "Ошибка переполнения")
            return
        self.x.append(x)
        self.y.append(y)
        answ = ""
        for i in range(len(x)):
            answ += "(" + str(x[i]) + ";" + str(y[i]) + ") "
            print(x[i], "\t\t", y[i])
        self.decision_var.set(answ)


        plt.figure()
        for i in range(len(self.x)-1):
            plt.plot(self.x[i], self.y[i], linestyle='--')
        plt.plot(self.x[len(self.x)-1], self.y[len(self.x)-1])
        plt.show()


    def refresh(self):
        self.x.clear()
        self.y.clear()

    def validate_date(self):
        try:
            x = float(self.x_var.get())
        except ValueError:
            tk_mb.showwarning("Ошибка", "Введите корректный x0")
            return False
        try:
            y = float(self.y_var.get())
        except ValueError:
            tk_mb.showwarning("Ошибка", "Введите корректный y0")
            return False
        try:
            float(eval(self.f_var.get()))
        except SyntaxError:
            tk_mb.showwarning("Ошибка", "Введите корректную функцию")
            return False
        except ValueError:
            tk_mb.showwarning("Ошибка", "Введите корректную функцию")
            return False
        try:
            b = float(self.b_var.get())
            if b <= x:
                tk_mb.showwarning("Ошибка", "Введите корректный b")
                return False
        except ValueError:
            tk_mb.showwarning("Ошибка", "Введите корректный b")
            return False
        try:
            eps = float(self.n_var.get())
            if eps <= 0:
                tk_mb.showwarning("Ошибка", "Введите корректную точность")
                return False
        except ValueError:
            tk_mb.showwarning("Ошибка", "Введите корректную точность")
            return False
        return True


if __name__ == "__main__":
    w = Window()
    w.start()
