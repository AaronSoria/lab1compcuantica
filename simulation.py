import subprocess
import sys
import importlib



def check_and_install_dependencies():
    required = ["numpy", "matplotlib"]
    missing = []

    print("Verificando dependencias...")

    for pkg in required:
        try:
            importlib.import_module(pkg)
        except ImportError:
            missing.append(pkg)

    if not missing:
        print("✔ Todas las dependencias están instaladas.\n")
        return

    print("⚠ Faltan dependencias:", ", ".join(missing))
    choice = input("¿Desea instalarlas automáticamente? (s/n): ").lower()

    if choice == "s":
        for pkg in missing:
            print(f"Instalando {pkg}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
        print("✔ Dependencias instaladas correctamente.\n")
    else:
        print("No se instalaron dependencias. El programa puede fallar.\n")

def ingresar_estado():
    print("\nIngrese los valores del estado |ψ⟩ = α|0⟩ + β|1⟩")

    try:
        a_real = float(input("α parte real: "))
        a_imag = float(input("α parte imaginaria: "))
        b_real = float(input("β parte real: "))
        b_imag = float(input("β parte imaginaria: "))
    except ValueError:
        print("Entrada inválida. Intente nuevamente.\n")
        return None

    alpha = complex(a_real, a_imag)
    beta = complex(b_real, b_imag)

    state = np.array([alpha, beta], dtype=complex)

    # Normalización automática
    norm = np.linalg.norm(state)
    if norm == 0:
        print("Estado inválido: el vector no puede ser cero.")
        return None

    state = state / norm
    print(f"Estado normalizado asignado: {state}\n")
    return state


def seleccionar_compuerta(sg):
    print("\nSeleccione la compuerta cuántica:")
    gates = {
        "H": sg.Hadamard,
        "X": sg.X,
        "Y": sg.Y,
        "Z": sg.Z,
        "I": sg.I,
        "S": sg.S,
        "S†": sg.S_adjoin,
        "T": sg.T,
        "T†": sg.T_adjoint,
        "V": sg.V,
        "V†": sg.V_adjoint
    }

    for i, g in enumerate(gates.keys(), start=1):
        print(f"{i}. {g}")

    try:
        opc = int(input("\nIngrese el número de la compuerta: "))
        if opc < 1 or opc > len(gates):
            raise ValueError
    except ValueError:
        print("Opción inválida.\n")
        return None

    selected_gate = list(gates.values())[opc - 1]
    selected_name = list(gates.keys())[opc - 1]

    print(f"Compuerta seleccionada: {selected_name}\n")
    return selected_gate

check_and_install_dependencies()

from quantum.circuits.circuit import Circuit
from quantum.implementations.simulated_gates import SimulatedGates
from quantum.plotter.simulated_bloch_plotter import plot_qubit_on_bloch_sphere
import numpy as np


def main():
    check_and_install_dependencies()
    sg = SimulatedGates()
    qc = Circuit(1)

    print("=== Simulador Interactivo de Cúbit ===\n")

    while True:
        print("Seleccione una opción:")
        print("1. Asignar un estado cuántico")
        print("2. Aplicar una compuerta cuántica")
        print("3. Graficar esfera de Bloch")
        print("4. Salir")

        opcion = input("\nIngrese su elección: ")

        if opcion == "1":
            state = ingresar_estado()
            if state is not None:
                qc.set_state(0, state)

        elif opcion == "2":
            gate = seleccionar_compuerta(sg)
            if gate:
                qc.apply_operation(0, gate)
                new_state = qc.get_qubit_state(0)
                print(f"Nuevo estado: {new_state}\n")

        elif opcion == "3":
            state = qc.get_qubit_state(0)
            print(f"Estado actual: {state}")
            plot_qubit_on_bloch_sphere(state)

        elif opcion == "4":
            print("Saliendo del simulador. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.\n")


if __name__ == "__main__":
    main()
