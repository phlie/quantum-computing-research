# In this experiment, we calculate the amount of 1's that should
# be observed after the Fredkin Gate given that it has a certain
# Rotation and then observe the actual amount of 1's outputted

import helper.some_framework as sf
import math
import random as r
shots = 250
num_loops = 1000

my_file = open("data/fredkin_gate_data2.txt", "w")
my_file.write("This is a %s shot experiment on the Fredkin Gate with %s loops\n" % (shots, num_loops))
my_file.write("Pre:, Ac1: \n")
for x in range(num_loops):
    print("Current loop:", x)
    C = sf.SomeFramework(3, shots=shots)

    # Get the rotation of each Qubit of the Theta angle
    # rotation_0 = rl["1100"]
    # rotation_1 = rl["1000"]X
    # rotation_init = rl["1101"]

    # Rotate each Qubit around the Theta axis a random amount from 0 to \pi
    rotation_0 = r.uniform(0, math.pi)
    rotation_1 = r.uniform(0, math.pi)
    rotation_2 = r.uniform(0, math.pi)

    # print("Rotation 0: ", rotation_0)
    # print("Rotation 1: ", rotation_1)
    # print("Rotation 2: ", rotation_2)

    # Calculate what the output percent should be
    expected_0 = math.sin(rotation_0/2)**2
    expected_1 = math.sin(rotation_1/2)**2
    expected_2 = math.sin(rotation_2/2)**2

    # Setup rotation
    C.u3_gate(0, rotation_0)
    C.u3_gate(1, rotation_1)
    C.u3_gate(2, rotation_2)
    C.cswap_gate(0, 1, 2)             # Take the |11> of the first two Qubits
    
    output = C.run_circuit()

    # This is the predicted amount of 1's for Q[1] for a standard Fredkin Gate
    # it uses the math equation that I recently derived
    q_out = shots * (expected_1 + expected_0*(expected_2 - expected_1))

    q_out = int(q_out)

    my_file.write("%4s, %4s\n" % (q_out, output[1]) )

# Print the output of both experiments
# print("The amount of 1's predicted is: ", q_out)
# print("The amount of 1's expected is: ", q_real_out)
my_file.close()
