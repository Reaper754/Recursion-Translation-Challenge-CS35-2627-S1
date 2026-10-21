def repeat_message_iterative(message, times):
    while times > 0:
        print(message)
        times -= 1

def repeat_message_recursive(message, times):
    #base case: times less than or equal to zero
    if times <= 0:
        return
    #process
    print(message)
    #recursive step: times minus 1
    repeat_message_recursive(message, times - 1)

message_question = "What would you like to say?\n"
times_question = "How many times do you want the message to be said?\n"

while True:
    print("Type exit to quit")
    message_input = input(message_question).strip().title()
    if message_input.lower() == "exit":
        break
    elif message_input.isdigit():
        print("Invalid Message")
    while True:
        times_input = input(times_question)
        if times_input.isdigit() == False:
            print("Invalid Number")
        else:
            print("Recursive:")
            repeat_message_recursive(message_input, int(times_input))
            print("Iterative:")
            repeat_message_iterative(message_input, int(times_input))
            break