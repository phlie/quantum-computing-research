# Can not find out what the S Gate does, still need to do more experiments
import helper.some_framework as sf

C = sf.SomeFramework(1, shots=1000)
C.h_gate(0)
C.s_gate(0)
C.x_gate(0)
C.run_circuit()
