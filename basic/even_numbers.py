def print_even_recursive(number):
    #base case: number less than or equal to zero
    if number <= 0:
        return
    #process
    print(number)
    #recursive function: number minus two
    print_even_recursive(number - 2)

print("recursive")
print_even_recursive(10)

def print_even_iterative(number):
    while True:
        if number <= 0:
            break
        else:
            print(number)
            number -= 2

print("iterative")
print_even_iterative(10)