# This helper function decodes a 4 bits stored into a single Q.
# The decoder is manually inputed to guess what range the values
# Of a certain input will take
# Takes in the previous array and the number left in the recurences
import math                     # The math library is used for sin, and pi

array_of_possibilities = []     # The array holds all the possible bit configurations 

# Starts the generation of the bit array
def init_generate_bits(num_of_bits):
    global array_of_possibilities  # Makes sure to get the global
    array_of_possibilities = []    # Reset array
    generate_bits('', num_of_bits - 1)  # Qubits are counted from 1
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
def generate_limits(num_of_bits, shots):
    num_of_limits = 2**num_of_bits - 1
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

def generate_lookup(num_of_bits):
    lookup_dict = {}
    bit_increment_array = init_generate_bits(num_of_bits)
    # print("BIA: ", bit_increment_array)
    number_of_loops = 2 ** num_of_bits
    # angle_increments = math.pi / (2**num_of_bits)  # Find the divisions;
    angle_increments = math.pi / (number_of_loops - 1)
    # print("Max Angle: ", angle_increments * (number_of_loops - 1))
    for x in range(2**num_of_bits):
        angle = round(angle_increments * x, 3)
        lookup_dict[bit_increment_array[x]] = angle
    return lookup_dict

def init_hex_numbers():
    return ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

def hex_generate_lookup():
    lookup_dict = {}
    bit_increment_array = init_hex_numbers()
    angle_increments = math.pi / 16
    for x in range(16):
        angle = round(angle_increments * x, 3)
        lookup_dict[bit_increment_array[x]] = angle
    return lookup_dict

def hex_generate_limits(shots):
    num_of_limits = 16
    limit_array = []            # Init 'limit_array'
    # angle_increments = math.pi / num_of_limits  # Find the divisions
    starting_angle = angle_increments / 2       # Get the offset
    # print(angle_increments)
    # Loop through the num_of_limits
    for x in range(num_of_limits):
        angle = (angle_increments * x) + starting_angle    # Get the angle for that step
        limits = int(shots*math.sin(angle/2)**2)           # Calculate the break points
        limit_array.append(limits)                         # Form the array

    return limit_array          # Return the limits array

def hex_decoder(current_bit_result, shots):
    hex_possible_array = init_hex_numbers()
    output_hex = hex_possible_array[0]
    less_than_array = hex_generate_limits(shots)
    length_lta = len(less_than_array)
    for x in range(length_lta):
        if current_bit_result > less_than_array[x]:  # If the bits to test is greater than the break array
            output_hex = hex_possible_array[x + 1]  # Save the output bits for later
            # print("OB: ", output_bits);
    return output_hex          # Return the total bits

# less_than_array = [20, 225, 600, 1250, 1875, 2725, 3600, 4500, 5500, 6400, 7275, 8125, 8750, 9400, 9775, 9980]
                    # [24, 215, 590, 1134, 1828, 2643, 3548, 4509, 5490, 6451, 7356, 8171, 8865, 9409, 9784, 9975]

# The current amount of 1's, the number of shots, and the number of traditional bits
def decoder(current_bit_result, shots, num_bits):
    bit_possible_array = init_generate_bits(num_bits)  # Call the generate all the possible configurations function
    output_bits = bit_possible_array[0]                # If no if below, use '0000' or '00' or whatever amount of '0's
    less_than_array = generate_limits(num_bits, shots)  # Generate the limits given the num_bits and the shots
    # print(less_than_array)
    length_lta = len(less_than_array)
    for x in range(length_lta):
        # print("X: ", x)
        if current_bit_result > less_than_array[length_lta - 1]:
            output_bits = bit_possible_array[length_lta]
            break
        if current_bit_result > less_than_array[x]:  # If the bits to test is greater than the break array
            # print(x, current_bit_result, less_than_array[x])
            output_bits = bit_possible_array[x + 1]  # Save the output bits for later
            # print("OB: ", output_bits);
    return output_bits          # Return the total bits


# print(generate_lookup(4))
# print(init_generate_bits(4))
# print(generate_lookup(2))
# print(decoder(500, 1000, 2))
# print(generate_limits(2, 1000))
