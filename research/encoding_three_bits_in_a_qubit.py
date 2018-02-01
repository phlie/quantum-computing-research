# Used to store three bits on a single Q and only use a classical register for decoding

from qiskit import QuantumProgram, QISKitError, RegisterSizeError
import math
# Number of qubits and classical registers
num_qubits = 1                   # Number of qubits and classical registers
shots = 10000                    # Number of times the program should run
backend = 'local_qasm_simulator'  # Whether to use the simulator or the real thing
circuit_name = 'circuit'          # What you wish to call the circuit
loops = 8                         # The amount of times it loops over the whole program

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
# The rotation lookup table gives the percents to rotate the u3 gate by
rotation_lookup = {"000":0.0, "001":0.125, "010":0.25, "011":0.375, "100":0.5, "101":0.625, "110":0.75, "111":0.875, 'X': 1}
# These are the bits to test
bits_to_test = ["000", "001", "010", "011", "100", "101", "110", "111"]
try:
    for i in range(loops):
        # Initializes the Program
        # Get the bits to test for this iteration
        bits = bits_to_test[i]
        print("Input Bits:  ", bits)

        qp = QuantumProgram(specs=Q_SPECS)
        qc = qp.get_circuit(circuit_name)

        # Get both registers
        q_r = qp.get_quantum_register('qr')
        c_r = qp.get_classical_register('cr')

        # ENCODER
        # Circuit Design Goes here
        qc.u3(rotation_lookup[bits]*math.pi, 0, 0,q_r[0])

        # DECODER
        # Measure all the available qubits
        for qubit in range(num_qubits):
            qc.measure(q_r[qubit], c_r[qubit])

        # Compiles and executes the code
        out = qp.execute(circuit_name, backend=backend, shots=shots)

        # Get the results of the circuit
        result = out.get_counts(circuit_name)

        # This is what the ouput is but was done with approximate calculations, gets back the encoded message
        if '1' in result:
            if result['1'] < 50:
                print("Output Bits: ", "000")
            elif result['1'] < 900:
                print("Output Bits: ", "001")
            elif result['1'] < 2300:
                print("Output Bits: ", "010")
            elif result['1'] < 4100:
                print("Output Bits: ", "011")
            elif result['1'] < 5900:
                print("Output Bits: ", "100")
            elif result['1'] < 7600:
                print("Output Bits: ", "101")
            elif result['1'] < 9100:
                print("Output Bits: ", "110")
            else:
                print("Output Bits: ", "111")
        else:
            print("Output Bits: ", "000")  # In the 0 case

        print()
# For errors in the circuit
except QISKitError as ex:
    print('There was an error in the circuit!. Error = {}'.format(ex))
except RegisterSizeError as ex:
    print("Error in number of registers!. Error = {}".format(ex))
