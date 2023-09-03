
# Reverse the result string at the end
def reverse_string(s):
    str = ""
    for i in s:
        str = i + str
    return str

# Converts the number to binary
def convert_to_binary(number):
    binary_repr_padded = format(number, '08b')
    return binary_repr_padded

# Creates the 1 for the twos method
def generate_zeros(length):
   return '0' * (length - 1) + '1'

# Flip the numbers in the binary string
def reverse_binary(s):
    result = ""
    for char in s:
        if char == '0':
            result += '1'
        elif char == '1':
            result += '0'
    return result


# Uses 2 functions to improve the readability
def handle_input(s):
    a = convert_to_binary(s)
    return str(reverse_binary(a))


# Helping variables
result = ""
nasa = 0


x = int(input("Enter a number: "))
x = handle_input(x)
y = generate_zeros(len(x))



# The last nasa will handled correctly because the for loop will end at index 0
for i in range(len(x)-1, -1, -1):
    current_x = int(x[i])
    current_y = int(y[i])
    if nasa != 0:
        current_x += nasa
        nasa -= 1
    if current_x + current_y >= 2:
        result += "0"
        nasa += 1
    elif current_x + current_y == 1:
        result += "1"
    elif current_x + current_y == 0:
        result += "0"

print("Binary > " + reverse_string(result))
    
        