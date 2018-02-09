# Stores data instead of in bits, in hexadecimal

import helper.some_framework as sf
import helper.bit_decoder as bd

hex_to_test = ["A", "0", "F", "5", "9"]
print("Hex To Test:", hex_to_test)
num_qubits = 5
shots = 1000
rl = bd.hex_generate_lookup()

C = sf.SomeFramework(num_qubits, shots=shots)
for x in range(num_qubits):
    C.u3_gate(x, rl[hex_to_test[x]])
output = C.run_circuit()

for x in range(num_qubits):
    print(bd.hex_decoder(output[x], shots))



