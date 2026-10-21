def print_characters_recursive(text, position):
    #base case: position equals end of text
    if position == len(text):
        return
    #process
    print(text[position])
    #recursive step: position plus 1
    print_characters_recursive(text, position + 1)

print("Recursive:")
print_characters_recursive("robot", 0)

def print_characters_iterative(text):
    for letters in text:
        print(letters)

print("Iterative:")
print_characters_iterative("robot")