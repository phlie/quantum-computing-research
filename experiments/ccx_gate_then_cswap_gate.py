# In this experiment, we calculate the amount of 1's that should
# be observed after the Troffoli Gate given that it has a certain
# Rotation and then observe the actual amount of 1's outputted

import helper.some_framework as sf
import math
import random as r
shots = 1000
num_loops = 100

print("Number Of Loops: ", num_loops)

my_file = open("data/ccx_gate_then_cswap_data.txt", "w")
my_file.write("Q_0: , Q_1, Q_2:\n")
for x in range(num_loops):
    C = sf.SomeFramework(3, shots=shots)

    # Get the rotation of each Qubit of the Theta angle
    # rotation_0 = rl["1100"]
    # rotation_1 = rl["1000"]X
    # rotation_init = rl["1101"]

    rotation_0 = r.uniform(0, math.pi)
    rotation_1 = r.uniform(0, math.pi)
    rotation_init = r.uniform(0, math.pi)

    # Setup rotation
    C.u3_gate(0, rotation_0)
    C.u3_gate(1, rotation_1)
    C.u3_gate(2, rotation_init)
    C.ccx_gate(0, 1, 2)             # Take the |11> of the first two Qubits
    C.cswap_gate(2,0,1)
    output = C.run_circuit()

    my_file.write("%4s, %4s, %4s\n" % (output[0], output[1], output[2]))

# Print the output of both experiments
# print("The amount of 1's predicted is: ", q_out)
# print("The amount of 1's expected is: ", q_real_out)
my_file.close()
