import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_qubit_on_bloch_sphere(qubit_state: np.ndarray):
    # Normalizar
    norm = np.linalg.norm(qubit_state)
    if norm == 0:
        raise ValueError("El estado del cúbit no puede ser el vector cero.")
    alpha = qubit_state[0] / norm
    beta = qubit_state[1] / norm

    theta = 2 * np.arccos(np.abs(alpha))

    # Calcular fase relativa robustamente
    if np.abs(alpha) < 1e-12 and np.abs(beta) < 1e-12:
        phi = 0  # No debería pasar nunca si el estado estaba normalizado
    elif np.abs(beta) < 1e-12:
        phi = 0
    elif np.abs(alpha) < 1e-12:
        phi = 0
    else:
        phi = np.angle(beta) - np.angle(alpha)

    phi = phi % (2 * np.pi)
    
    # create figure
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # draw sphere
    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, np.pi, 30)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    
    ax.plot_surface(x, y, z, color='lightblue', alpha=0.2, linewidth=0)
    
    # plot axes
    axes_limits = [-1.2, 1.2]
    ax.plot([axes_limits[0], axes_limits[1]], [0, 0], [0, 0], 'r-', linewidth=2, label='X')
    ax.plot([0, 0], [axes_limits[0], axes_limits[1]], [0, 0], 'g-', linewidth=2, label='Y')
    ax.plot([0, 0], [0, 0], [axes_limits[0], axes_limits[1]], 'b-', linewidth=2, label='Z')
    
    # label axes
    ax.text(1.3, 0, 0, 'X', color='red', fontsize=12)
    ax.text(0, 1.3, 0, 'Y', color='green', fontsize=12)
    ax.text(0, 0, 1.3, 'Z', color='blue', fontsize=12)
    
    # states
    base_states = {
        '|0⟩': (0, 0, 1),
        '|1⟩': (0, 0, -1),
        '|+⟩': (1, 0, 0),
        '|-⟩': (-1, 0, 0),
        '|i⟩': (0, 1, 0),
        '|-i⟩': (0, -1, 0)
    }
    
    for label, (x, y, z) in base_states.items():
        ax.scatter(x, y, z, color='black', s=30, alpha=0.7)
        ax.text(x + 0.1, y + 0.1, z + 0.1, label, fontsize=9)
    
    # Convertir a coordenadas cartesianas para el vector
    x_vec = np.sin(theta) * np.cos(phi)
    y_vec = np.sin(theta) * np.sin(phi)
    z_vec = np.cos(theta)
    
    # draw vector
    ax.quiver(0, 0, 0, x_vec, y_vec, z_vec, 
              color='purple', linewidth=3, arrow_length_ratio=0.1, 
              label=f'|ψ⟩ = ({alpha.real:.3f}{alpha.imag:+.3f}i)|0⟩ + ({beta.real:.3f}{beta.imag:+.3f}i)|1⟩')
    
    # Punto en la superficie
    ax.scatter([x_vec], [y_vec], [z_vec], color='purple', s=100)
    
    # Círculo ecuatorial
    theta_eq = np.linspace(0, 2 * np.pi, 100)
    x_eq = np.cos(theta_eq)
    y_eq = np.sin(theta_eq)
    z_eq = np.zeros_like(theta_eq)
    ax.plot(x_eq, y_eq, z_eq, 'gray', linestyle='--', alpha=0.5)
    
    # Configuración final
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_zlim(-1.2, 1.2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Estado del Qubit en Esfera de Bloch\n'
                f'|ψ⟩ = ({alpha.real:.3f}{alpha.imag:+.3f}i)|0⟩ + ({beta.real:.3f}{beta.imag:+.3f}i)|1⟩')
    ax.legend()
    
    # Vista inicial
    ax.view_init(elev=20, azim=45)
    
    plt.tight_layout()
    plt.show()
    
    return theta, phi
