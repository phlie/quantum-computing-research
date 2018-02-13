# By applying a Y_Gate after a H Gate you tend to get the same results
# As just applying an H Gate

import helper.some_framework as sf

C = sf.SomeFramework(1, shots=1000)
C.h_gate(0)
C.y_gate(0)
C.run_circuit()
