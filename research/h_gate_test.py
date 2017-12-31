# A test of whether a single H Gate actually produces even probability

from qiskit import QuantumProgram, QISKitError

# Number of qubits and classical registers
num_qubits = 1                   # Number of qubits and classical registers
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

print("Prints the number of 1's and 0's")
print("Shots: ", shots)

try:
    # Initializes the Program
    qp = QuantumProgram(specs=Q_SPECS)
    qc = qp.get_circuit(circuit_name)

    # Get both registers
    q_r = qp.get_quantum_register('qr')
    c_r = qp.get_classical_register('cr')

    # Circuit Design Goes here
    qc.h(q_r[0])           # Superposition r0

    # Measure all the available qubits
    for qubit in range(num_qubits):
        qc.measure(q_r[qubit], c_r[qubit])
    
    # Compiles and executes the code
    out = qp.execute(circuit_name, backend=backend, shots=shots)

    # Get the results of the circuit
    result = out.get_counts(circuit_name)

    # The results section where you print out the information of the experiment
    print("1's: ", result['1'])
    print("0's: ", result['0'])

# For errors in the circuit
except QISKitError as ex:
  print('There was an error in the circuit!. Error = {}'.format(ex))
