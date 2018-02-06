import helper.some_framework as sf

C = sf.SomeFramework(5, shots=1000)
C.h_gate(1)
C.h_gate(3)
C.h_gate(4)
print(C.run_circuit())

