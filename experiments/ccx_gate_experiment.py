# From this experiment we have determined that the CCX Gate
# Can lead to two Qubits changing the probability of a third
# Qubit

# If the MSB bit is in a one 

import helper.some_framework as sf

C = sf.SomeFramework(4, shots=10000, number_of_bits=3)
rl = C.create_lookup(3)
C.u3_gate(0, rl["000"])
C.u3_gate(1, rl["010"])
C.u3_gate(2, rl["100"])
C.u3_gate(3, rl["111"])
output = C.run_circuit()
C.decode_classic_gate_mode()
