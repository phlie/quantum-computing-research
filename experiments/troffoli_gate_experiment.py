# In this experiment, we calculate the amount of 1's that should
# be observed after the Troffoli Gate given that it has a certain
# Rotation and then observe the actual amount of 1's outputted

import helper.some_framework as sf
import math
import random as r
shots = 1000
num_loops = 100

my_file = open("troffoli_gate_data.txt", "w")
my_file.write("Pre:, Act: \n")
for x in range(num_loops):
    C = sf.SomeFramework(4, number_of_bits=4, shots=shots)
    rl = C.create_lookup(4)

    # Get the rotation of each Qubit of the Theta angle
    # rotation_0 = rl["1100"]
    # rotation_1 = rl["1000"]X
    # rotation_init = rl["1101"]

    rotation_0 = r.uniform(0, math.pi)
    rotation_1 = r.uniform(0, math.pi)
    rotation_init = r.uniform(0, math.pi)

    print("Rotation 0: ", rotation_0)
    print("Rotation 1: ", rotation_1)
    print("Rotation i: ", rotation_init)

    # Calculate what the output percent should be
    expected_0 = math.sin(rotation_0/2)**2
    expected_1 = math.sin(rotation_1/2)**2
    expected_init = math.sin(rotation_init/2)**2

    # Setup rotation
    C.u3_gate(0, rotation_0)
    C.u3_gate(1, rotation_1)
    C.u3_gate(2, rotation_init)
    C.u3_gate(3, rotation_init)     # Used to get the amount of 1's Qubit three should have
    C.ccx_gate(0, 1, 2)             # Take the |11> of the first two Qubits
    
    output = C.run_circuit()
    C.decode_classic_gate_mode()

    # This is the predicted 1's as equated using research on the Troffoli Gate along with
    # equations giving the amount of 1's for each angle
    q_out = shots * ((expected_0 * expected_1) * (1-2*expected_init) + expected_init)

    # This is the same calculation as above based on the amount of 1's observed in the actual experiment
    q_real_out = shots * ((output[0] / shots) * (output[1] / shots) * (1-2*(output[3] / shots)) + output[3] / shots)
    q_out = int(q_out)

    my_file.write("%4s, %4s\n" % (q_out, output[2]) )

# Print the output of both experiments
# print("The amount of 1's predicted is: ", q_out)
# print("The amount of 1's expected is: ", q_real_out)
my_file.close()
