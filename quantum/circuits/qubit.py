from __future__ import annotations
import numpy as np
from typing import Callable

QuantumOperation = Callable[[np.ndarray], np.ndarray]
class Qubit:
    id = -1
    state = np.array([0.0, 1.0], dtype=complex)
    entanglement_qubit: Qubit = None
    applying_operation = False
    collapsed = False

    def __init__(self, id: int, state: np.ndarray):
        self.id = id
        self.state = state
        self.applying_operation = False

    def apply_operation(self, operation: QuantumOperation) -> None:
        if self.applying_operation:
            return
        
        self.applying_operation = True
        self.state = operation(self.state)
        if self.is_entangled():
            self.entanglement_qubit.apply_operation(operation=operation)
            self.applying_operation = False


    def entanglement(self, entanglement_qubit: Qubit) -> None:
        if self.applying_operation:
            return
        
        self.applying_operation = True
        self.entanglement_qubit = entanglement_qubit
        self.entanglement_qubit.entanglement(self)
        self.applying_operation = False

    def is_entangled(self) -> bool:
        return self.entanglement_qubit is not None
    
    def collapse(self) -> None:
        if self.collapsed:
            return
        
        self.collapsed = True
        if self.is_entangled():
            self.entanglement_qubit.collapse()


    def is_colapsed(self) -> bool:
        return self.collapsed