# An attempt to see if anything can be made out of cx Gates, so far no luck.

import helper.some_framework as sf

C = sf.SomeFramework(3, shots=1000)
C.h_gate(0)
C.h_gate(1)
C.x_gate(2)
C.cx_gate(1, 0)
C.cx_gate(2, 1)
C.run_circuit()
