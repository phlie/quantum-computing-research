import helper.some_framework as sf
import math

num_loops = 5

for x in range(num_loops):
    C = sf.SomeFramework(1, shots=1000)
    C.u3_gate(0, math.pi / 2)
    C.run_circuit()
