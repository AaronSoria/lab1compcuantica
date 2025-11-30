from quantum.circuits.circuit import Circuit
from quantum.implementations.simulated_gates import SimulatedGates
from quantum.plotter.simulated_bloch_plotter import plot_qubit_on_bloch_sphere

sg = SimulatedGates()
qc = Circuit(2)
qc.apply_operation(0, sg.Hadamard)
state = qc.get_qubit_state(0)
plot_qubit_on_bloch_sphere(state)