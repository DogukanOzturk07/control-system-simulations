import numpy as np
import matplotlib.pyplot as plt


def simulate_lyapunov_control():
    """
    Simple Lyapunov-based control example for a first-order nonlinear system.

    System:
        dx/dt = -x^3 + u

    Goal:
        Stabilize x to zero.

    Lyapunov candidate:
        V(x) = 0.5 * x^2

    Choose control law:
        u = -k*x

    Then:
        dx/dt = -x^3 - k*x

    and
        dV/dt = x * dx/dt = -x^4 - k*x^2 <= 0

    This demonstrates asymptotic stability in a simple educational setting.
    """

    # Control gain
    k = 2.0

    # Simulation settings
    dt = 0.01
    t_end = 10.0
    t = np.arange(0.0, t_end + dt, dt)

    # Initial condition
    x = 2.0

    # Storage
    x_values = []
    u_values = []
    v_values = []

    for _ in t:
        # Lyapunov-based control law
        u = -k * x

        # Nonlinear system update
        dx = -x**3 + u
        x += dx * dt

        # Lyapunov function
        v = 0.5 * x**2

        # Save data
        x_values.append(x)
        u_values.append(u)
        v_values.append(v)

    return t, np.array(x_values), np.array(u_values), np.array(v_values)


def plot_results(t, x, u, v):
    plt.figure(figsize=(10, 6))
    plt.plot(t, x, label="State x(t)")
    plt.title("Lyapunov-Based Control - State Response")
    plt.xlabel("Time (s)")
    plt.ylabel("State")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 4))
    plt.plot(t, u, label="Control Input u(t)")
    plt.title("Lyapunov-Based Control Input")
    plt.xlabel("Time (s)")
    plt.ylabel("u(t)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 4))
    plt.plot(t, v, label="Lyapunov Function V(x)")
    plt.title("Lyapunov Function Evolution")
    plt.xlabel("Time (s)")
    plt.ylabel("V(x)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    t, x, u, v = simulate_lyapunov_control()
    plot_results(t, x, u, v)
