# Program to test out new features with classical gates on Qubits
import helper.some_framework as sf

in_bits = ["11", "11", "11", "01", "00", "10"]

C = sf.SomeFramework(6, shots=1000)
C.setup_in_classic_gate_mode(in_bits)
C.run_circuit()
C.decode_classic_gate_mode()

out = [0] * 6

out[0] = C.and_gate(0)
out[1] = C.or_gate(1)
out[2] = C.xor_gate(2)
out[3] = C.not_gate(3)
out[4] = C.and_gate(4)
out[5] = C.or_gate(5)
print("In:  ", in_bits)
print("Out: ", out)

total_output = C.combine_bits(out)
print("TO: ", total_output)
not_output = C.not_gate('0')
print("No: ", not_output)
print("Ouput of gates: ", C.xor_gate(total_output))
