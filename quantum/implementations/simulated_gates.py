from math import sqrt
from quantum.circuits.gates.quantum_gates import IQuantumGates
import numpy as np

class SimulatedGates(IQuantumGates):

    def Hadamard(self, state: np.ndarray) -> np.ndarray:
        h = np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex)
        h = h * (1/sqrt(2))
        return np.dot(h, state)

    def X(self, state: np.ndarray) -> np.ndarray:
        x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
        return np.dot(x, state)

    def Y(self, state: np.ndarray) -> np.ndarray:
        y = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
        return np.dot(y, state)

    def Z(self, state: np.ndarray) -> np.ndarray:
        z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
        return np.dot(z, state)

    def I(self, state: np.ndarray) -> np.ndarray:
        identity = np.array([[1.0, 0.0], [0.0, 1.0]], dtype=complex)
        return np.dot(identity, state)

    def S(self, state: np.ndarray) -> np.ndarray:
        s = np.array([[1.0, 0.0], [0.0, 1.0j]], dtype=complex)
        return np.dot(s, state)
    
    def S_adjoin(self, state: np.ndarray) -> np.ndarray:
        s_dag = np.array([[1.0, 0.0], [0.0, -1.0j]], dtype=complex)
        return np.dot(s_dag, state)
    
    def T(self, state: np.ndarray) -> np.ndarray:
        t = np.array([[1.0, 0.0], [0.0, np.exp(1j * np.pi / 4)]], dtype=complex)
        return np.dot(t, state)
    
    def T_adjoint(self, state: np.ndarray) -> np.ndarray:
        t_dag = np.array([[1.0, 0.0], [0.0, np.exp(-1j * np.pi / 4)]], dtype=complex)
        return np.dot(t_dag, state)

    def V(self, state: np.ndarray) -> np.ndarray:
        v = np.array([[1+1j, 1-1j], [1-1j, 1+1j]], dtype=complex) * 0.5
        return np.dot(v, state)
    
    def V_adjoint(self, state: np.ndarray) -> np.ndarray:
        v_dag = np.array([[1-1j, 1+1j], [1+1j, 1-1j]], dtype=complex) * 0.5
        return np.dot(v_dag, state)