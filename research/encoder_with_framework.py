# This is a test of the SomeFramework which is designed to make
# Quantum Computing as simple as possible

# Import statements
import helper.some_framework as sqf
import helper.bit_decoder as bd
import math
from random import randint

# Custom Variables
num_qs = 5
shots = 1000
loops = 1
num_bits_in_array = 4
# bits = "0101"

# Functions for initiation
rotation_lookup = bd.generate_lookup(num_bits_in_array)
bits_to_test = bd.init_generate_bits(num_bits_in_array)

# Used to store input and output over loops
total_input = []
total_output = []

for i in range(loops):
    bits = []
    output_bits = []
    for x in range(num_qs):
        bits.append(bits_to_test[randint(0,2**num_bits_in_array - 1)])
    print("Bits: ", bits)
    # bits = bits_to_test[randint(0,2**num_bits_in_array - 1)]
    # print("Bits To Test: ", bits)


    # The Q-Code
    C = sqf.SomeFramework(num_qs, "my_circuit", shots)
    for gate in range(num_qs):
        C.u3_gate(gate, rotation_lookup[bits[gate]])
    C.barrier_gate()
    # C.u3_gate(0, rotation_lookup[bits])
    output = C.run_circuit()

    print(output)

    # The result
    for x in range(num_qs):
        output_bits.append(bd.decoder(output[x], shots, num_bits_in_array))
    # output_bits = bd.decoder(output[0], shots, num_bits_in_array)
    print("Ouput: ", output_bits)
    # print("Output: ", output_bits)
    C.output_test(bits, output_bits)

    # Gets the total output
    total_input.append(bits)
    total_output.append(output_bits)

print("In:  ", total_input)
print("Out: ", total_output)
