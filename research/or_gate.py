# OR Gate made out of a qubit
import helper.some_framework as sqf
import helper.bit_decoder as bd

# The initialization variables
test_bits = "01"
shots = 1000
num_bits = 2

C = sqf.SomeFramework(1, shots=shots)
rl = C.create_lookup(num_bits)
C.u3_gate(0, rl[test_bits])

output = C.run_circuit()
output_bits = C.decode_qubit(0, num_bits)        # Decode the output for the only Qubit

# Or is only 0 for the case both bits are 0
out = C.or_gate(0)
# if output_bits == "00":
#     out = "0"
# else:
#     out = "1"

print("Output:", test_bits, "through OR Gate:", out)
