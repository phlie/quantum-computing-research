# A template anyone can use for trying out different quantum circuits

from qiskit import QuantumProgram, QISKitError

# Number of qubits and classical registers
num_qubits = 3                   # Number of qubits and classical registers
shots = 1024                    # Number of times the program should run
backend = 'local_qasm_simulator'  # Whether to use the simulator or the real thing
circuit_name = 'circuit'          # What you wish to call the circuit


# This is where the quantum and classical registers are defined
Q_SPECS = {
    'circuits': [{
        'name': circuit_name,
        'quantum_registers': [{
            'name': 'qr',
            'size': num_qubits
        }],
        'classical_registers': [{
            'name': 'cr',
            'size': num_qubits
        }]}],
}

try:
    # Initializes the Program
    qp = QuantumProgram(specs=Q_SPECS)
    qc = qp.get_circuit(circuit_name)

    # Get both registers
    q_r = qp.get_quantum_register('qr')
    c_r = qp.get_classical_register('cr')

    # Circuit Design Goes here
    qc.x(q_r[2])           # Put r2 in the |1> position
    qc.h(q_r[0])           # Superposition r0
    qc.t(q_r[0])           # Rotate pi/4 around the z-axis in the positive direction
    qc.h(q_r[0])           # Maps X->Z and Z->X
    qc.cx(q_r[0], q_r[1])  # If it is in 11 -> 01, 01 -> 11
    qc.cx(q_r[1], q_r[2])  # CNOT from 1 to 2
    # qc.x(q_r[1])

    # Measure all the available qubits
    for qubit in range(num_qubits):
        qc.measure(q_r[qubit], c_r[qubit])

    # Compiles and executes the code
    out = qp.execute(circuit_name, backend=backend, shots=shots)

    # Get the results of the circuit
    result = out.get_counts(circuit_name)

    # The results section where you print out the information of the experiment
    print(result)

# For errors in the circuit
except QISKitError as ex:
  print('There was an error in the circuit!. Error = {}'.format(ex))
