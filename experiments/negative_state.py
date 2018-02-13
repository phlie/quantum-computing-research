# The negative state has the same results as the positive state
import helper.some_framework as sf

C = sf.SomeFramework(1, shots=1000)
C.h_gate(0)
C.z_gate(0)
C.run_circuit()
