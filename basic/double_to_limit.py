def double_until_limit_recursive(number, limit):
    #base case: number is greater than limit
    if number > limit:
        return
    #process
    print(number)
    #recursive step: (number*2, limit)
    double_until_limit_recursive(number * 2, limit)

print("Recursive:")
double_until_limit_recursive(2, 40)

def double_until_limit_iterative(number, limit):
    while number < limit:
        print(number)
        number *= 2

print("Iterative:")
double_until_limit_iterative(2, 40)