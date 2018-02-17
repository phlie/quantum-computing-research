my_file = open("data/first_test_of_fredkin_gate.txt", "r")


output = my_file.readlines()

my_file.close()
output_without_newline = []
for y in output:
    output_without_newline.append(y.replace("\n", ""))

total_array = []
    # output = list(output)
for x in output_without_newline:
    save = x.replace("[", "")
    save = save.replace("]", "")
    save = save.split(', ')
    temp_array = []
    for place in save:
        temp_array.append(int(place))
    total_array.append(temp_array)

print(total_array)
