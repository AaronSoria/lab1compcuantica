# lab1compcuantica
Laboratorio 1 de computacion cuántica

# 📘 Simulador de Cúbit y Esfera de Bloch — Laboratorio de Computación Cuántica

Este proyecto implementa **desde cero** un simulador de un cúbit, incluyendo:

- representación del estado cuántico,  
- implementación manual de compuertas cuánticas fundamentales,  
- visualización del estado en la **esfera de Bloch** usando `matplotlib`,  
- un **circuito cuántico básico** que administra y encapsula los cúbits,  
- compatibilidad con **Qiskit**,  
- y un **simulador interactivo por consola** para experimentar con estados y compuertas.

El objetivo principal es **pedagógico**: entender cómo las compuertas unitarias actúan sobre un cúbit y cómo se ven sus transformaciones en la esfera de Bloch sin utilizar visualizadores preconstruidos.

---

## 🌟 Características principales

### ✅ Representación interna del cúbit  
- Vector complejo de dimensión 2  
- Normalización garantizada  
- Validación automática del estado  
- Manejo de fase global y relativa

### ✅ Esfera de Bloch implementada manualmente  
- Sin dependencias externas (sin BlochVisualizer de Qiskit)  
- Coordenadas calculadas a partir de  
  \[
  |\psi\rangle = \alpha|0\rangle + \beta |1\rangle
  \]

### ✅ Compuertas cuánticas implementadas a mano  
Incluye:

| Grupo | Compuertas |
|-------|------------|
| Paulis | X, Y, Z, I |
| Clifford | H, S, S† |
| No-Clifford | T, T† |
| Raíz de X | V, V† |

Todas implementadas mediante matrices unitarias con `numpy`.

### ✅ Arquitectura modular  
- **Circuit**: orquesta y encapsula todos los cúbits  
- **Qubit**: maneja su propio estado y validación  
- **SimulatedGates**: implementación manual de compuertas  
- **Plotter**: generación visual en 3D  
- **Patrón Bridge** para desacoplar la abstracción de compuertas  
- **Delegados** (callables en Python) para aplicar operaciones

### ✅ Interfaz interactiva por consola  
Permite:

- asignar estados |ψ⟩ manualmente  
- aplicar compuertas una por una  
- visualizar el resultado en la esfera de Bloch  

---

## 📁 Estructura del Proyecto

```
lab1compcuantica/
│
├── quantum/
│   ├── circuits/
│   │   └── circuit.py
│   ├── implementations/
│   │   └── simulated_gates.py
│   ├── plotter/
│   │   └── simulated_bloch_plotter.py
│   └── qubit/
│       └── qubit.py
│
├── notebooks/
│   └── simulacion_cubit.ipynb
│
├── simulation.py      # App interactiva
├── requirements.txt
└── README.md
```

---

## 🚀 Instalación

### Requisitos
- Python ≥ 3.10  
- pip  

### 1. Crear entorno virtual (recomendado)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso del simulador interactivo

Ejecutar:

```bash
python simulation.py
```

### El menú permite:

```
1. Asignar un estado cuántico
2. Aplicar una compuerta cuántica
3. Graficar esfera de Bloch
4. Salir
```

---

## 🧪 Ejemplo rápido de uso en Python

```python
from quantum.circuits.circuit import Circuit
from quantum.implementations.simulated_gates import SimulatedGates
from quantum.plotter.simulated_bloch_plotter import plot_qubit_on_bloch_sphere

sg = SimulatedGates()
qc = Circuit(1)

qc.set_state(0, [1.0, 0.0])   # Estado |0>
qc.apply_operation(0, sg.X)   # Aplicar X → |1>

state = qc.get_qubit_state(0)
print(state)

plot_qubit_on_bloch_sphere(state)
```

---

## 📓 Notebook incluido

En `notebooks/simulacion_cubit.ipynb` encontrarás:

- cómo construir estados válidos,
- ejemplos de estados inválidos,
- cómo usar cada compuerta,
- visualización final en la esfera de Bloch,

---

## 🧱 Arquitectura del Sistema

### **1️⃣ Circuit**
Capa principal del simulador.  
Encapsula todos los cúbits → el usuario *interactúa sólo con Circuit*.

### **2️⃣ Qubit**
Clase interna, no accesible directamente.  
Se encarga de:

- almacenar |ψ⟩
- validar normalización
- manejar colapso (si se extendiera)
- gestionar entrelazamiento (futuro)

### **3️⃣ Compuertas — Patrón Bridge**
`IQuantumGates` define *qué* es una compuerta.  
`SimulatedGates` define *cómo* se implementa.

Esto permite reemplazar la implementación por Qiskit sin cambiar Circuit.

### **4️⃣ Plotter**
Genera esfera de Bloch 3D:

- calcula θ y φ  
- dibuja ejes, malla y vector  
- muestra el estado final

---

## 📚 Referencias

- Nielsen & Chuang — *Quantum Computation and Quantum Information*  
- Watrous — *Theory of Quantum Information*  
- Qiskit Textbook  
- Bloch (1946), Sakurai (1994)

---

## 🧑‍💻 Autor

**Luis Aaron Maximiliano Soria**  
Máster en Ciencias Computacionales y Matematica · Ingeniero en Informática  
Estudiante de Computacion Cuantica