# A Qubit decoder for multiple Qubits in superposition
# Typical output is of the form:

# 'init_bit_find(4,0)' ->
# ['0001', '0011', '0101', '0111', '1001', '1011', '1101', '1111']

# 'init_bit_find(3,1)' ->
# ['010', '011', '110', '111']

# 'init_bit_find(2,1)' ->
# ['10', '11']

# Initialize the variables used in the loop
which_one_to_target = 0
array_of_possibilities = []

def init_bit_find(num_of_qubits, target):
    global which_one_to_target  # Replaces the local variable by a global
    global array_of_possibilities
    array_of_possibilities = []
    which_one_to_target = target
    recur_find('', num_of_qubits - 1)  # Decrement by 1 because Qubits are indexed from 1 not 0
    return array_of_possibilities

# Takes in the previous array and the number left in the recurences
def recur_find(previous_bit_array, num_to_recur):
    for x in ['0', '1']:        # Loop over the two possible values
        # As long as there are still some positionsleft
        if num_to_recur > 0:
            if which_one_to_target == num_to_recur:  # If it is on the target, means the target should equal one
                new_bit_array = previous_bit_array + '1'
                recur_find(new_bit_array, num_to_recur - 1)
                break
            else:
                new_bit_array = previous_bit_array + x  # Else add in the x from the for loop
                recur_find(new_bit_array, num_to_recur - 1)
        else:
            if which_one_to_target == 0:  # If the target is the last, the last position is one
                array_of_possibilities.append(previous_bit_array + '1')
                break
            else:
                array_of_possibilities.append(previous_bit_array + x)  # Else call the final step and append

