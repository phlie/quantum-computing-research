# Initialize the variables used in the loop
bit_find_array = ''
array_of_possibilities = []
number_of_recurs = 3
which_one_to_target = 3

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

recur_find('', number_of_recurs)
print(array_of_possibilities)
