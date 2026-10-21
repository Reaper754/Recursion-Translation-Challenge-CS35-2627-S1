def print_even_recursive(number):
    #base case: number less than or equal to zero
    if number <= 0:
        return
    #process
    print(number)
    #recursive function: number minus two
    print_even_recursive(number - 2)

print("Recursive:")
print_even_recursive(10)

def print_even_iterative(number):
    while number > 0:
        print(number)
        number -= 2

print("Iterative:")
print_even_iterative(10)