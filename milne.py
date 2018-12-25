import math


"""def runge_cutta(x_0, y_0, b, f, n):
    x = list()
    y = list()
    x.append(x_0)
    y.append(y_0)
    i = 0
    while x[i] <= b:
        k1 = h*f(x[i], y[i])
        k2 = h*f(x[i]+h/2, y[i]+k1/2)
        k3 = h*f(x[i]+h/2, y[i]+k2/2)
        k4 = h*f(x[i]+h, y[i]+k3)
        d = math.fabs((k2-k3)/(k1-k2))
        if d> 0.01:
            h /= 2
        else:
            x.append(x[i]+h)
            y.append((k1+2*k2+2*k3+k4)/6+y[i])
            i+=1
    return x, y"""

def runge_cutta_4(x_0, y_0, b, f, n):
    h = (b-x_0)/n
    print(h)
    x = list()
    y = list()
    x.append(x_0)
    y.append(y_0)
    i = 0
    while i < 4-1 and x[i] <= b:
        k1 = h*f(x[i], y[i])
        k2 = h*f(x[i]+h/2, y[i]+k1/2)
        k3 = h*f(x[i]+h/2, y[i]+k2/2)
        k4 = h*f(x[i]+h, y[i]+k3)
        x.append(x[i]+h)
        y.append((k1+2*k2+2*k3+k4)/6+y[i])
        i += 1
    return x, y


def milne(x, y, b, f, n):
    i = len(x) - 1
    h = (b-x[0])/n
    print(h)
    while x[i] <= b:
        y_t = y[i-3] + 4*h/3*(2*f(x[i], y[i])-f(x[i-1], y[i-1])+2*f(x[i-2], y[i-2]))
        y_ = y[i-1] + h/3*(f(x[i]+h, y_t)+4*f(x[i], y[i])+f(x[i-1], y[i-1]))
        d = math.fabs(y_t - y_)/29
        # print(y_t, y_, d)
        x.append(x[i]+h)
        y.append(y_)
        i += 1



def fun(x, y):
    return (y**2)-x


if __name__ == "__main__":
    x_0 = 1
    y_0 = 0
    b = 3
    n = 10
    """x, y = runge_coota_4(x_0, y_0, b, fun, h, eps)
    milne(x, y, b, fun, h, eps)
    for i in range(len(x)):
        print(x[i], "\t", y[i])"""
    x, y = runge_cutta_4(x_0, y_0, b, fun, n)
    milne(x, y, b, fun, n)
    for i in range(len(x)):
        print(x[i], "\t", y[i])
