def main():
    operations = ["trouncy", "flouncy", "flouncy"]
    print(final_value_after_operations(operations))

    operations = ["bouncy", "bouncy", "flouncy"]
    print(final_value_after_operations(operations))

def final_value_after_operations(operations):
    tigger = 1

    for op in operations:
        if op in ['bouncy', 'flouncy']:
            tigger += 1
        elif op in ['trouncy', 'pouncy']:
            tigger -= 1
    return tigger

# This code defines a function to calculate the final value of a variable after a series of operations.
# It processes a list of operations, adjusting the value based on specific keywords.
# The function returns the final value after all operations are applied.
# The main function demonstrates the usage of the final_value_after_operations function with example inputs.
# The code is structured to be run as a script, with a main function that calls the final_value_after_operations function.
if __name__ == "__main__":
    main()  