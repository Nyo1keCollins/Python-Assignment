# Function to repeatedly ask for input until 'exit' is typed
def input_until_exit():
    while True:
        user_input = input("Enter a word (type 'exit' to stop): ")
        if user_input.lower() == "exit":
            break
        print(user_input)

# Uncomment the line below to test this function in an interactive session
# input_until_exit()
