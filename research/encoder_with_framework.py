# This is a test of the SomeFramework which is designed to make
# Quantum Computing as simple as possible

# Import statements
import helper.some_quantum_framework as sqf
import helper.bit_decoder as bd
import math

# Custom Variables
num_bits_in_array = 4
bits = "0101"

# Functions for initiation
rotation_lookup = bd.generate_lookup(num_bits_in_array)
bits_to_test = bd.init_generate_bits(num_bits_in_array)

# The Q-Code
C = sqf.SomeFramework(1, "my_circuit", 10000)
C.u3_gate(0, rotation_lookup[bits])
output = C.run_circuit()

# The result
output_bits = bd.decoder(output[0], 10000, num_bits_in_array)
print(output_bits)
