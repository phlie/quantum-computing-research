# This helper function decodes a 4 bits stored into a single Q.
# The decoder is manually inputed to guess what range the values
# Of a certain input will take
# Takes in the previous array and the number left in the recurences
import math                     # The math library is used for sin, and pi

array_of_possibilities = []     # The array holds all the possible bit configurations 

# Starts the generation of the bit array
def init_generate_bits(num_of_qubits):
    global array_of_possibilities  # Makes sure to get the global
    array_of_possibilities = []    # Reset array
    generate_bits('', num_of_qubits - 1)  # Qubits are counted from 1
    return array_of_possibilities         # Return

# Generates the bit configurations using recur
def generate_bits(previous_bit_array, num_to_recur):
    for x in ['0', '1']:        # Loop over the two possible values
        # As long as there are still some positionsleft
        if num_to_recur > 0:
            # Add together the previous step plus either the '1' or '0' from the for
            new_bit_array = previous_bit_array + x
            generate_bits(new_bit_array, num_to_recur - 1)  # Recur decrementing the num_to_recur
        else:
            array_of_possibilities.append(previous_bit_array + x)  # Else call the final step and append

# |0> + |1> at 1/2 pi = |1>/sqrt(2)
# angle = abs(pi/2 - theta ) for between 0 and pi so if at pi it will equal pi/2 which is 

# Generates the breaks in requried for that amount of bits and that amount of shots
def generate_limits(num_of_limits, shots):
    limit_array = []            # Init 'limit_array'
    angle_increments = math.pi / num_of_limits  # Find the divisions
    starting_angle = angle_increments / 2       # Get the offset
    # print(angle_increments)
    # Loop through the num_of_limits
    for x in range(num_of_limits):
        angle = (angle_increments * x) + starting_angle    # Get the angle for that step
        limits = int(shots*math.sin(angle/2)**2)           # Calculate the break points
        limit_array.append(limits)                         # Form the array

    return limit_array          # Return the limits array

# less_than_array = [20, 225, 600, 1250, 1875, 2725, 3600, 4500, 5500, 6400, 7275, 8125, 8750, 9400, 9775, 9980]
                    # [24, 215, 590, 1134, 1828, 2643, 3548, 4509, 5490, 6451, 7356, 8171, 8865, 9409, 9784, 9975]

# The current amount of 1's, the number of shots, and the number of traditional bits
def decoder(current_bit_result, shots, num_bits):
    bit_possible_array = init_generate_bits(num_bits)  # Call the generate all the possible configurations function
    output_bits = bit_possible_array[0]                # If no if below, use '0000' or '00' or whatever amount of '0's
    less_than_array = generate_limits(num_bits**2, shots)  # Generate the limits given the num_bits and the shots
    # print(less_than_array)
    length_lta = len(less_than_array)
    for x in range(length_lta):
        # print("X: ", x)
        if current_bit_result > less_than_array[x]:  # If the bits to test is greater than the break array
            output_bits = bit_possible_tarray[x + 1]  # Save the output bits for later
            # print("OB: ", output_bits);
    return output_bits          # Return the total bits
