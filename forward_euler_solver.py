import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def forward_euler(f, I, R, y0, I0, t0, tn, h):
    t_values = [t0]
    y_values = [y0]
    I_values = [I0]
    R_values = [0]

    while t_values[-1] < tn:
        t_n = t_values[-1] + h
        y_n = y_values[-1] + h * f(t_values[-1], y_values[-1], I_values[-1])
        I_n = I_values[-1] + h * I(t_values[-1], y_values[-1], I_values[-1])
        R_n = R_values[-1] + h * R(t_values[-1], I_values[-1])
        t_values.append(t_n)
        y_values.append(y_n)
        I_values.append(I_n)
        R_values.append(R_n)

        ##print(f"t_n: {t_n}, y_n: {y_n}, I_n: {I_n}, R_n: {R_n}")

    return t_values, y_values, I_values, R_values



def S_dot(t, S, I):
    B = 2
    N = 1000
    return -(B * S * I) / N

def I_dot(t, S, I):
    B = 2
    N = 1000
    lam = 0.5
    value = ((B * S * I) / N) - lam * I
    return value

def R_dot(t, I):
    lam = 0.5
    value = lam * I
    return value


if __name__ == "__main__":
    S0 = 999
    N = 1000
    t0 = 0
    tn = 50
    h = .1
    I0 = 1


    graph_values = forward_euler(S_dot, I_dot, R_dot, S0, I0, 0, 50, h)

    out_file = "S Plot"
    t_values, S_values, I_values, R_values = graph_values

    plt.plot(t_values, S_values)
    plt.plot(t_values, I_values)
    plt.plot(t_values, R_values)
    plt.xlabel('Time')
    plt.ylabel('People')
    plt.title('Forward Euler Simulation')
    plt.legend(['S(t)', 'I(t)', 'R(t)'])
    plt.text(55, 950, 'Tehran Law', fontsize=10, color='black')

    plt.show()

    plt.savefig(out_file,bbox_inches='tight')

