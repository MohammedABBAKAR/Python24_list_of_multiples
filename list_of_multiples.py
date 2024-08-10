# List of Multiples

# Create a function that takes two numbers 
# as arguments (num, length) and returns a list 
# of multiples of num until the list length reaches length.
# Examples

# list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]

# list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]

# ///////////////////////////////////////////////



# ???????????????????????????????????????????????
def list_of_multiples (num,num2):
    list_of =[]
    test = 0
    for i in range(num2):
        i = num * 2
        test += i
        list_of.append(test)
    return list_of
print(list_of_multiples (7,5))

# ///////////////////////////////////////////////


def list_of_multiples(num, length):
    list_of = []
    for i in range(1, length + 1):
        list_of.append(num * i)
    return list_of

# Example usage
print(list_of_multiples(7, 5))  # Output: [7, 14, 21, 28, 35]

# ///////////////////////////////////////////////

def list_of_multiples(num, length):
    return [num * i for i in range(1, length + 1)]

# Examples
print(list_of_multiples(7, 5))   # Output: [7, 14, 21, 28, 35]
print(list_of_multiples(12, 10)) # Output: [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
print(list_of_multiples(17, 6))  # Output: [17, 34, 51, 68, 85, 102]


# ///////////////////////////////////////////////