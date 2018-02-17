# Right now, this is where I test my current ideas, this happens to be a Fredkin Gate

import helper.some_framework as sf

input_bits = ["11", "10", "01", "00"]
shots = 1000

total_output = []
# my_file.write(" Qb0   | Qb1  |  Qb2  \n")
C = sf.SomeFramework(4, shots=shots, number_of_bits=2)
rl = C.create_lookup(2)
C.u3_gate(0, rl[input_bits[0]])
C.u3_gate(1, rl[input_bits[1]])
C.u3_gate(2, rl[input_bits[2]])
C.u3_gate(3, rl[input_bits[2]])
# C.cx_gate(0,2)
# C.cx_gate(0,2)
# C.ccx_gate(0,1,2)
C.cswap_gate(0,1,2)
# C.ccx_gate(0, 1, 2)             # Take the |11> of the first two Qubits
output = C.run_circuit()
# my_file.write("%5s, %5s, %5s\n" % (output[0], output[1], output[2]))
total_output.append(output)
C.decode_classic_gate_mode()
