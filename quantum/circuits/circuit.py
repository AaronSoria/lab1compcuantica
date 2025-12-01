from __future__ import annotations
from typing import Callable
import random
import numpy as np
from quantum.circuits.qubit import Qubit

QuantumOperation = Callable[[np.ndarray], np.ndarray]

class Circuit:
    size = 0
    qubit_array: list[Qubit] = []
    def __init__(self, size):
        self.size = size
        for i in range(self.size):
            self.qubit_array.append(Qubit(i, np.array([0.0,1.0], dtype=complex)))
    
    def entanglement(self, first_id:int, second_id: int) -> None:
        self.qubit_array[first_id].entanglement(self.qubit_array[second_id])

    def apply_operation(self, id:int, operation: QuantumOperation):
        self.qubit_array[id].apply_operation(operation)

    def set_state(self, id:int, state: np.ndarray) -> None:
        self.qubit_array[id].state = state

    def mesure(self, id):
        qubit = self.qubit_array[id]
        qubit.collapse()
        state = qubit.state
        prob_0 = abs(state[0]) ** 2
        prob_1 = abs(state[1]) ** 2

        total_prob = prob_0 + prob_1
        prob_0 = prob_0 / total_prob
        prob_1 = prob_1 / total_prob
        
        result = 0
        random_result = random.random()
        if random_result < prob_0:
            qubit.state = [1.0, 0.0]
            result = 0
        else:
            qubit.state = [0.0, 1.0]
            result = 1

        print(f"Qubit {id} colapsó a |{result}⟩ (prob |0⟩: {prob_0:.3f}, prob |1⟩: {prob_1:.3f})")
        return result
    
    def get_qubit_state(self, id: int) -> np.ndarray:
        return self.qubit_array[id].state

    def messure_all(self):
        results = []
        for qubit in self.qubit_array:
            result = self.mesure(qubit.id)
            results.append(result)
        return results

    