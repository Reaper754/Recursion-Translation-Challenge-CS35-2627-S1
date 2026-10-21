def repeat_message_iterative(message, times):
    #base case: times greater than zero
    while times > 0:
        #process
        print(message)
        #recursive step: times minus equals 1
        times -= 1

print("iterative")
repeat_message_iterative("Hello World!", 3)

def repeat_message_recursive(message, times):
    if times > 0:
        return
    print(message)
    repeat_message_recursive(message, times - 1)

print("recursive")
repeat_message_recursive("Hello World!", 3)