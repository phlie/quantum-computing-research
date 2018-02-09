# This is a multiple gate experiement
import helper.some_framework as sqf
import helper.bit_decoder as bd

# The test bits of the three Quantum Gates
test_bits_0 = "11"
test_bits_1 = "10"
test_bits_2 = "10"

# Init constants
shots = 300
num_bits = 2


C = sqf.SomeFramework(3, shots=shots)
C.setup_in_classic_gate_mode([test_bits_0, test_bits_1, test_bits_2])

# rl = C.create_lookup(num_bits)
# # Setup the three storage logic gates
# C.u3_gate(0, rl[test_bits_0])
# C.u3_gate(1, rl[test_bits_1])
# C.u3_gate(2, rl[test_bits_2])

output = C.run_circuit()
# Decode the qubits
# Automate this
# output_bits_0 = C.decode_qubit(0, num_bits)
# output_bits_1 = C.decode_qubit(1, num_bits)
output_bits = C.decode_classic_gate_mode()
print("Output Bits: ", output_bits)

# output_bits_2 = C.decode_qubit(2, num_bits)

out_0 = C.and_gate(0)
out_1 = C.and_gate(1)
out_2 = C.or_gate(2)
out = C.xor_gate(C.and_gate(out_0 + out_1) + out_2)

print("Output:", test_bits_1 + test_bits_0, "through AND Gates then XOR Gate:", out)
