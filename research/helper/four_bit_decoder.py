# This helper function decodes a 4 bits stored into a single Q.
# The decoder is manually inputed to guess what range the values
# Of a certain input will take
def decoder(current_bit_result, shots):
    if current_bit_result < 20 * shots / 10000 :
        output_bits = "0000"  # Save the output bits for later
    elif current_bit_result < 225 * shots / 10000:
        output_bits = "0001"
    elif current_bit_result < 600 * shots / 10000:
        output_bits = "0010"
    elif current_bit_result < 1250 * shots / 10000:
        output_bits = "0011"
    elif current_bit_result < 1875 * shots / 10000:
        output_bits = "0100"
    elif current_bit_result < 2725 * shots / 10000:
        output_bits = "0101"
    elif current_bit_result < 3600 * shots / 10000:
        output_bits = "0110"
    elif current_bit_result < 4500 * shots / 10000:
        output_bits = "0111"
    elif current_bit_result < 5500 * shots / 10000:
        output_bits = "1000"
    elif current_bit_result < 6400 * shots / 10000:
        output_bits = "1001"
    elif current_bit_result < 7275 * shots / 10000:
        output_bits = "1010"
    elif current_bit_result < 8125 * shots / 10000:
        output_bits = "1011"
    elif current_bit_result < 8750 * shots / 10000:
        output_bits = "1100"
    elif current_bit_result < 9400 * shots / 10000:
        output_bits = "1101"
    elif current_bit_result < 9775 * shots / 10000:
        output_bits = "1110"
    else:
        output_bits = "1111"

    return output_bits
