# From this experiment we have determined that the CCX Gate
# Can lead to two Qubits changing the probability of a third
# Qubit

# If the MSB bit is in a one 

import helper.some_framework as sf

C = sf.SomeFramework(3, shots=1000, number_of_bits=1)
rl = C.create_lookup(1)
C.u3_gate(0, rl["0"])
C.u3_gate(1, rl["1"])
C.h_gate(2)
C.ccx_gate(0, 1, 2)             # Take the |11> of the first two Qubits
output = C.run_circuit()
C.decode_classic_gate_mode()
