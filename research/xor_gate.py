# XOR Gate made out of a single Qubit
import helper.some_framework as sqf
import helper.bit_decoder as bd

# The initialization variables
test_bits = "11"
shots = 1000
num_bits = 2

C = sqf.SomeFramework(1, shots=shots)
rl = C.create_lookup(num_bits)  # Use the bit_decoder lookup table
C.u3_gate(0, rl[test_bits])     # Get the rotation

output = C.run_circuit()
output_bits = C.decode_qubit(0, num_bits)  # Decode the output for the only Qubit
out = C.xor_gate(0)
# # The logic of the XOR Gate
# if output_bits == "00" or output_bits == "11":
#     out = "0"
# else:
#     out = "1"

print("Output:", test_bits, "through XOR Gate:", out)
