# Encodes and decodes two bits in one Qubit

# Checking the version of PYTHON; we only support > 3.5
import sys
if sys.version_info < (3,5):
    raise Exception('Please use Python version 3.5 or greater.')

# useful additional packages 
# import matplotlib.pyplot as plt

import numpy as np
from math import pi

# importing the QISKit
from qiskit import QuantumProgram
# import Qconfig

backend = 'local_qasm_simulator' # the device to run on
shots = 1000    # the number of shots in the experiment 

#to record the rotation number for encoding 00, 10, 11, 01
rotationNumbers = {"00":1, "10":3, "11":5, "01":7}

Q_program = QuantumProgram()


# Creating registers
# qubit for encoding 2 bits of information
qr = Q_program.create_quantum_register("qr", 1)
# bit for recording the measurement of the qubit
cr = Q_program.create_classical_register("cr", 1)

# dictionary for encoding circuits
encodingCircuits = {}
# Quantum circuits for encoding 00, 10, 11, 01
for bits in ("00", "01", "10", "11"):
    circuitName = "Encode"+bits
    encodingCircuits[circuitName] = Q_program.create_circuit(circuitName, [qr], [cr])
    encodingCircuits[circuitName].u3(rotationNumbers[bits]*pi/4.0, 0, 0, qr[0])
    encodingCircuits[circuitName].barrier()

# dictionary for decoding circuits
decodingCircuits = {}
# Quantum circuits for decoding the first and second bit
for pos in ("First", "Second"):
    circuitName = "Decode"+pos
    decodingCircuits[circuitName] = Q_program.create_circuit(circuitName, [qr], [cr])
    if pos == "Second": #if pos == "First" we can directly measure
        decodingCircuits[circuitName].h(qr[0])
    decodingCircuits[circuitName].measure(qr[0], cr[0])

#combine encoding and decoding of QRACs to get a list of complete circuits
circuitNames = []
for k1 in encodingCircuits.keys():
    for k2 in decodingCircuits.keys():
        circuitNames.append(k1+k2)
        Q_program.add_circuit(k1+k2, encodingCircuits[k1]+decodingCircuits[k2])

print("List of circuit names:", circuitNames) #list of circuit names

# The value that you want to encode
bitArrangement = "10"

# Gets the results of the quantum circuit
results = Q_program.execute(["Encode"+bitArrangement+"DecodeFirst", "Encode"+bitArrangement+"DecodeSecond"], backend=backend, shots=shots)

# Outputs the least significant bit and the more significant bit's 1's vs 0's
bitOut0 = results.get_counts("Encode"+bitArrangement+"DecodeFirst")
bitOut1 = results.get_counts("Encode"+bitArrangement+"DecodeSecond")

print("First Bit: ", bitOut0, "Second Bit: ", bitOut1)

# Initialize bit array
bitArray = [0, 0]

# If there are more 1's than 0's, the first digit is a 1
if bitOut0['1'] > bitOut0['0']:
    print("First bit is 1")
    bitArray[0] = 1
else:
    print("First bit is 0")
    bitArray[0] = 0

if bitOut1['1'] > bitOut1['0']:
    print("Second bit is 1")
    bitArray[1] = 1
else:
    print("Second bit is 0")
    bitArray[1] = 0

# Outputs the encoded and then decoded value
print("The output is: ", bitArray[0], bitArray[1])


