import numpy as np

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def quantum_optimize(mean_returns):

    mean_returns = mean_returns.values

    num_assets = len(mean_returns)

    # Create quantum circuit
    qc = QuantumCircuit(num_assets)

    # Superposition
    for qubit in range(num_assets):
        qc.h(qubit)

    # Measurement
    qc.measure_all()

    simulator = AerSimulator()

    result = simulator.run(
        qc,
        shots=1024
    ).result()

    counts = result.get_counts()

    # Most probable quantum state
    best_state = max(
        counts,
        key=counts.get
    )

    # Convert binary string to weights
    binary_selection = np.array(
        [int(bit) for bit in best_state[::-1]]
    )

    # Avoid all-zero state
    if np.sum(binary_selection) == 0:
        binary_selection[0] = 1

    weights = binary_selection / np.sum(binary_selection)

    expected_return = np.dot(
        weights,
        mean_returns
    )

    return {
        "weights": weights.tolist(),
        "expected_return": float(expected_return),
        "selected_assets": binary_selection.tolist(),
        "shots": 1024,
        "most_probable_state": best_state,
        "num_qubits": num_assets
    }