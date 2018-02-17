import helper.some_framework as sf

C = sf.SomeFramework(5, shots=10000, number_of_bits=4)
rl = C.create_lookup(4)
C.u3_gate(0, rl["1111"])
C.u3_gate(1, rl["1010"])
C.u3_gate(2, rl["1100"])
C.u3_gate(3, rl["1101"])
C.u3_gate(4, rl["0000"])

C.run_circuit()
output_bits = C.decode_classic_gate_mode()

