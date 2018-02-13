# A template anyone can use for trying out different quantum circuits

from qiskit import QuantumProgram, QISKitError, RegisterSizeError
import math
import helper.get_nth_qubit as gnq  # The helper function used in the Quantum Decoding

# Number of qubits and classical registers
num_qubits = 2                   # Number of qubits and classical registers
shots = 255                    # Number of times the program should run
backend = 'local_qasm_simulator'  # Whether to use the simulator or the real thing
circuit_name = 'circuit'          # What you wish to call the circuit
loops = 1                         # The amount of times it loops over the whole program

# For running on the actual quantum computer
# backend = 'ibmqx5'
# import helper.Qconfig as Qconfig

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
    for i in range(loops):
        # Initializes the Program
        qp = QuantumProgram(specs=Q_SPECS)
        qc = qp.get_circuit(circuit_name)

        # For running the code on IBM's Q
        # qp.set_api(Qconfig.APItoken, Qconfig.config['url'])

        # Get both registers
        q_r = qp.get_quantum_register('qr')
        c_r = qp.get_classical_register('cr')

        # Circuit Design Goes here
        qc.x(q_r[1])            # Put the register into the excited state

        # qc.cx(q_r[1], q_r[2])  # CNOT from 1 to 2
        # qc.x(q_r[1])

        # Measure all the available qubits
        for qubit in range(num_qubits):
            qc.measure(q_r[qubit], c_r[qubit])

        # Compiles and executes the code
        out = qp.execute(circuit_name, backend=backend, shots=shots)

        # Get the results of the circuit
        result = out.get_counts(circuit_name)

        output = []        # Saves the output
        # print("Result: ", result)  # Ouputs the total result array

        # Loop through all the Qubits to get the total amount of 1's for each Qubit
        for current_qubit in range(num_qubits):  # For each Q in the circuit, loop through
            possible_results = []                # We want to initialize this to nil
            current_bit_result = 0;              # Each itteration start fresh

            # Use the helper function to get an array of possible arrangements of the classical registers
            possible_results = gnq.init_bit_find(num_qubits, current_qubit)
            # print("PR: ", possible_results)

            # For all the possible results, loop through and ...
            for r in range(len(possible_results)):
                if possible_results[r] in result:  # If the current possible result is in results
                    current_bit_result += result[possible_results[r]]  # Add to the total 1's for that Q

            # Outputs the amount of 1's from MSB to LSB for each individual Qubit
            output.insert(0, current_bit_result)

        # The results section where you print out the information of the experiment
        print("Output: ", output)


# For errors in the circuit
except QISKitError as ex:
    print('There was an error in the circuit!. Error = {}'.format(ex))
except RegisterSizeError as ex:
    print("Error in number of registers!. Error = {}".format(ex))
