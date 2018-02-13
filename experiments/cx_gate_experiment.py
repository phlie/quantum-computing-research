# An attempt to see if anything can be made out of cx Gates, so far no luck.

import helper.some_framework as sf
import math
C = sf.SomeFramework(5, shots=1000)
C.u3_gate(0, math.pi / 4)
C.cx_gate(0, 1)
C.cx_gate(0, 2)
C.cx_gate(0, 3)
C.cx_gate(0, 4)
C.run_circuit()
