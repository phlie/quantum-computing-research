import helper.some_framework as sf

C = sf.SomeFramework(5, shots=1000)
C.h_gate([0, 2, 4])
C.run_circuit()

