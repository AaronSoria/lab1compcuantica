from abc import ABC, abstractmethod
import numpy as np

class IQuantumGates(ABC):
    @abstractmethod
    def Hadamard(self, state: np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def X(self, state: np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def Y(self, state: np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def Z(self, state: np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def I(self, state: np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def S(self, state: np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def V(self, state: np.ndarray) -> np.ndarray:
        pass