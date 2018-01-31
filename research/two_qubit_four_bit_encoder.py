# A two Q's encoder that uses a total of four Q's for decoding, uses four classical registers
from qiskit import QuantumProgram, QISKitError, RegisterSizeError
import math

# The encoded bits
bits_to_encode = "1001"         # Edit these bits to change what values are encoded

# Number of qubits and classical registers
num_qubits = 4                   # Number of qubits and classical registers
shots = 10000                    # Number of times the program should run
backend = 'local_qasm_simulator'  # Whether to use the simulator or the real thing
circuit_name = 'circuit'          # What you wish to call the circuit
loops = 1                         # The amount of times it loops over the whole program

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

# The Q's are encoded in the order from MSB to LSB
rotation_numbers = {"00":1, "10":3, "11":5, "01":7}
print("Bits to encode", bits_to_encode)
bits_to_encode_msb = bits_to_encode[0:2]
bits_to_encode_lsb = bits_to_encode[2:]

try:
    for i in range(loops):
        # Initializes the Program
        qp = QuantumProgram(specs=Q_SPECS)
        qc = qp.get_circuit(circuit_name)

        # Get both registers
        q_r = qp.get_quantum_register('qr')
        c_r = qp.get_classical_register('cr')

        # The encoder, uses the Qubits 0 and 2 and then puts up a barrier
        qc.u3(rotation_numbers[bits_to_encode_lsb]*math.pi/4.0, 0, 0, q_r[0])
        qc.u3(rotation_numbers[bits_to_encode_msb]*math.pi/4.0, 0, 0, q_r[2])
        qc.barrier()

        # Decoder, uses four Qubits to decode
        qc.u3(rotation_numbers[bits_to_encode_lsb]*math.pi/4.0, 0, 0, q_r[1])
        # Flip the X and Z axis to get the other position of the LSB
        qc.h(q_r[1])
        qc.u3(rotation_numbers[bits_to_encode_msb]*math.pi/4.0, 0, 0, q_r[3])
        # Flip the X and Z axis to get the other position of the MSB
        qc.h(q_r[3])

        # Measure all the available qubits
        for qubit in [0, 2]:
            qc.measure(q_r[qubit], c_r[qubit])

        for qubit in [1, 3]:
            qc.measure(q_r[qubit], c_r[qubit])

        # Compiles and executes the code
        out = qp.execute(circuit_name, backend=backend, shots=shots)

        # Get the results of the circuitnn
        result = out.get_counts(circuit_name)
            
        # The results section where you print out the information of the experiment
        print(result)
        # msb_count = result['1000'] + result['1001'] + result['1010'] + result['1011'] + result['1100'] + result['1101'] + result['1110'] + result['1111']
        # lsb_count = result['0001'] + result['0011']+ result['0101'] + result['0111'] + result['1001'] + result['1011'] + result['1101'] + result['1111']
        # Initialize the decoder output bits
        bit_0_count = 0
        bit_1_count = 0
        bit_2_count = 0
        bit_3_count = 0

        # Loop through all the possibilities of the positions of the other bits that aren't 1
        for x in ['0', '1']:
            for y in ['0', '1']:
                for z in ['0', '1']:
                    bit_0_count += result[x + y + '1' + z]  # Passed through the H Gate
                    bit_1_count += result[x + y + z + '1']
                    bit_2_count += result['1' + x + y + z]  # Passed through the H Gate
                    bit_3_count += result[x + '1' + y + z]

        bit_array = ''

        # Gets the decoder values
        if bit_3_count < shots / 2:
            bit_array += '0'
            print("3 bit is a 0")
        else:
            bit_array += '1'
            print("3 bit is a 1")

        if bit_2_count < shots / 2:
            bit_array += '0'
            print("2 bit is a 0")
        else:
            bit_array += '1'
            print("2 bit is a 1")

        if bit_1_count < shots / 2:
            bit_array += '0'
            print("1 bit is a 0")
        else:
            bit_array += '1'
            print("1 bit is a 1")

        if bit_0_count < shots / 2:
            bit_array += '0'
            print("0 bit is a 0")
        else:
            bit_array += '1'
            print("0 bit is a 1")

        print("Bits when decode: ", bit_array)

# For errors in the circuit
except QISKitError as ex:
    print('There was an error in the circuit!. Error = {}'.format(ex))
except RegisterSizeError as ex:
    print("Error in number of registers!. Error = {}".format(ex))
