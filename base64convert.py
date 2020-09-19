from base_sets import base64_dict

def tobinary(s):
	encoded_output = ''
	for i in s:
		bits = bin(ord(i))[2:]
		bits = '00000000'[len(bits):] + bits
		encoded_output = encoded_output+bits

	return encoded_output


def to_6bit_binary(s):
	binary_string = ''
	base64_decode_dict = dict((v,k) for k,v in base64_dict.items())
	for i in s:
		byte = base64_decode_dict[i]
		binary_string = binary_string + byte

	return binary_string


def base64_encode(input_string):
	n = 6
	encoded_output = ''
	binary_input = tobinary(input_string)
	list_of_bytes = [binary_input[i:i+n] for i in range(0, len(binary_input), n)]

	if len(binary_input) % n != 0:
		list_of_bytes[-1] = list_of_bytes[-1].ljust(n,'0')

	for i in list_of_bytes:
		encoded_output = encoded_output+base64_dict[i]

	if len(list_of_bytes) % 4 != 0:
		num_missing_bytes = len(list_of_bytes) % 4
		num_needed_pads = 4 - num_missing_bytes
		encoded_output = encoded_output+(base64_dict['padder']*num_needed_pads)

	return encoded_output


def base64_decode(input_string):
	n = 6
	string_binary = to_6bit_binary(input_string)

	list_6bit_bytes = [string_binary[i:i+n] for i in range(0, len(string_binary), n)]
	list_6bit_bytes = [i for i in list_6bit_bytes if i != 'padder']

	joined_string_bytes = ''.join(list_6bit_bytes)

	list_8bit_bytes = [joined_string_bytes[i:i+8] for i in range(0, len(joined_string_bytes), 8)]
	list_8bit_bytes = [i for i in list_8bit_bytes if len(i) == 8]

	decoded_ouput = ("".join([chr(int(binary, 2)) for binary in list_8bit_bytes]))
	
	return decoded_ouput