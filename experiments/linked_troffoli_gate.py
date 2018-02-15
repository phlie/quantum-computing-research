# The idea behind this experiment is to link the Troffoli Gate

import helper.some_framework as sf

input_bits = ["11", "10", "01", "00"]
shots = 1000
my_file = open("data/input_0_cx_on_troffoli_gate.txt", "w")
my_file.write(" Qb0  |  Qb1  |  Qb2  \n")
for bit0 in input_bits:
    for bit1 in input_bits:
        C = sf.SomeFramework(3, shots=shots, number_of_bits=2)
        rl = C.create_lookup(2)
        C.u3_gate(0, rl[bit0])
        C.u3_gate(1, rl[bit1])
        # C.cx_gate(0,2)
        C.cx_gate(0,2)
        C.ccx_gate(0,1,2)
        # C.ccx_gate(0, 1, 2)             # Take the |11> of the first two Qubits
        output = C.run_circuit()
        my_file.write("%5s, %5s, %5s\n" % (output[0], output[1], output[2]))
        C.decode_classic_gate_mode()

my_file.close()
