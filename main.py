from quantum.circuits.circuit import Circuit
from quantum.implementations.simulated_gates import SimulatedGates
from quantum.plotter.simulated_bloch_plotter import plot_qubit_on_bloch_sphere
import numpy as np

sg = SimulatedGates()
qc = Circuit(1)
state = np.array([1.0, 0.0], dtype=complex)
qc.set_state(0, state)
qc.apply_operation(0, sg.Hadamard)
qc.apply_operation(0, sg.S)
new_state = qc.get_qubit_state(0)
print(new_state)
plot_qubit_on_bloch_sphere(new_state)