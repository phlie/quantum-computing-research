# Testing the mathematical derivitation of the Y-Gate in
# an experiment on the Y-Gate. The problem is I don't know
# How to use the imaginary number in it

import helper.some_framework as sf
import math
import random as r
shots = 1000
num_loops = 10

my_file = open("data/controlled_y_gate_experiment.txt", "w")

my_file.write("This is a %s shot experiment on the Controlled Y-Gate with %s loops\n" % (shots, num_loops))
my_file.write("Pre:, Act: \n")
for x in range(num_loops):
    print("Current loop: ", x)
    C = sf.SomeFramework(2, shots=shots)

    # The rotation is a random number between 0 and \pi
    rotation_0 = r.uniform(0, math.pi)
    rotation_1 = r.uniform(0, math.pi)

    # Calculate what the output percent should be
    expected_0 = math.sin(rotation_0/2)**2
    expected_1 = math.sin(rotation_1/2)**2

    # Setup rotation
    C.u3_gate(0, rotation_0)
    C.u3_gate(1, rotation_1)

    C.cy_gate(0, 1)             # If the controlled gate is the MSB, then the math holds true

    output = C.run_circuit()

    # This equation predicts the amount of 1's on the second Qubit using the
    # mathematical prediction derived for the Controlled X-Gate
    q_out = shots * (expected_0 + expected_1 - 2*expected_0*expected_1)

    q_out = int(q_out)

    my_file.write("%4s, %4s\n" % (q_out, output[1]))


my_file.close()
