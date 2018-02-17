import helper.some_framework as sf
from math import pi

rotation = 1.25

C = sf.SomeFramework(3, shots=10000)
C.u3_gate(0, rotation)
C.u3_gate(1, rotation)
C.u3_gate(1, rotation)
C.u3_gate(2, 2.0*rotation)
C.run_circuit()
