import helper.some_framework as sf

num_bits = 3
num_shots = 1000

C = sf.SomeFramework(7, shots=num_shots, number_of_bits=num_bits)
rl = C.create_lookup(num_bits)
C.u3_gate(0, rl["110"])
C.u3_gate(1, rl["011"])
C.u3_gate(2, rl["001"])
C.u3_gate(3, rl["010"])
C.u3_gate(4, rl["001"])
C.u3_gate(5, rl["000"])
C.u3_gate(6, rl["001"])
C.run_circuit()
C.decode_classic_gate_mode()
