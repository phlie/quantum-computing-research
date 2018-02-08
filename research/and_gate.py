# AND Gate for a Quantum Computer
import helper.some_framework as sqf
import helper.bit_decoder as bd

test_bits = "11"
shots = 1000
num_bits = 2

C = sqf.SomeFramework(1, shots=shots)
rl = C.create_lookup(num_bits)
C.u3_gate(0, rl[test_bits])

output = C.run_circuit()
output_bits = C.decode_qubit(0, num_bits)

out = C.and_gate(0)

# # Old output
# if output_bits == "11":
#     out = "1"
# else:
#     out = "0"

print("Output:", test_bits, "through AND Gate:", out)

