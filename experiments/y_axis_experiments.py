import helper.some_framework as sf

shots = 1000
num_loops = 10

for x in range(10):
    C = sf.SomeFramework(2, shots=1000)
    C.h_gate(0)
    C.h_gate(1)

    C.x_gate(0)
    C.y_gate(1)
    # rotation_0 = r.uniform(0, math.pi)
    # rotation_i = r.uniform(0, math.pi)
    # C.u3_gate(0, rotation_0, rotation_i)
    C.run_circuit()
