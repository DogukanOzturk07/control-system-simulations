import numpy as np
import matplotlib.pyplot as plt


def simulate_pi_control():
    """
    Simple PI control example for a first-order plant.

    Plant:
        dx/dt = -a*x + b*u

    Control:
        e = r - x
        integral_e = integral of e
        u = Kp*e + Ki*integral_e

    This is a basic educational simulation to demonstrate
    control-oriented thinking and PI regulation behavior.
    """

    # Plant parameters
    a = 1.2
    b = 1.0

    # PI controller gains
    kp = 2.5
    ki = 1.2

    # Simulation settings
    dt = 0.01
    t_end = 10.0
    t = np.arange(0.0, t_end + dt, dt)

    # Reference signal
    r = 1.0

    # Initial conditions
    x = 0.0
    integral_e = 0.0

    # Storage
    x_values = []
    u_values = []
    e_values = []
    r_values = []

    for _ in t:
        # Control error
        e = r - x

        # Integral term
        integral_e += e * dt

        # PI control law
        u = kp * e + ki * integral_e

        # Plant update (Euler integration)
        dx = -a * x + b * u
        x += dx * dt

        # Save data
        x_values.append(x)
        u_values.append(u)
        e_values.append(e)
        r_values.append(r)

    return t, np.array(r_values), np.array(x_values), np.array(u_values), np.array(e_values)


def plot_results(t, r, x, u, e):
    plt.figure(figsize=(10, 6))
    plt.plot(t, r, label="Reference")
    plt.plot(t, x, label="System Output")
    plt.title("PI Control - System Response")
    plt.xlabel("Time (s)")
    plt.ylabel("Output")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 4))
    plt.plot(t, u, label="Control Input")
    plt.title("PI Control Input")
    plt.xlabel("Time (s)")
    plt.ylabel("u(t)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 4))
    plt.plot(t, e, label="Tracking Error")
    plt.title("PI Control Error")
    plt.xlabel("Time (s)")
    plt.ylabel("Error")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    t, r, x, u, e = simulate_pi_control()
    plot_results(t, r, x, u, e)
