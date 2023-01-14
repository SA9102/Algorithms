# A program that takes in a sequence of brackets and determines whether or not the sequence is valid.

# Accepted characters: ()[]{} -> normal, square and curly brackets

# The sequence of brackets is said to be valid if the string contains PAIRS of brackets that are of
# the same type and are in the correct order.

# NOTES:
# - This algorithm uses a stack data structure.
# - All whitespaces, including those in between words, are removed.

# EXAMPLES OF VALID SEQUENCES:
# - {{}()}
# - [((){{}})]
# - {()[[]]({})}

# EXAMPLES OF INVALID SEQUENCES:
# - )({})
# - {[[)()}
# - {(})


from DataStructures import Stack

def get_opening_bracket(bracket):
    '''Find the corresponding opening bracket from the given closing bracket'''

    matching = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    return matching[bracket]

def is_opening_bracket(bracket):
    '''Checks if the given bracket is an opening bracket'''

    return bracket in '([{'

def check_sequence(brackets):
    '''Checks to see if the bracket sequence is valid'''

    # Create a stack
    brackets_stack = Stack()

    for bracket in brackets:
        if is_opening_bracket(bracket):
            # Push the opening bracket onto the stack
            brackets_stack.push(bracket)
        # If 'bracket' is a closing bracket
        else:
            # If the closing bracket is of the same type as the opening bracket at the top of the stack
            if get_opening_bracket(bracket) == brackets_stack.peek():
                brackets_stack.pop()
            else:
                return 'Invalid bracket sequence'

        # After the loop, we still need to check if the list is empty or not.
        # If the list is not empty, it would mean that there is at least one opening bracket which hasn't been 'closed', in
        # which case would indicate invalid bracket sequence.
    return 'Valid!\n' if brackets_stack.is_empty() else 'Invalid bracket sequence\n'


# Continuously ask the user to enter a bracket sequence
while True:
    brackets_str = input('Enter a sequence of brackets to check its validity (q to quit): ')

    # Remove all whitespaces
    brackets_str = ''.join(brackets_str.split(' '))

    if brackets_str == 'q':
        break

    # Block of code that checks if the string ONLY contains the acceptable characters.
    legal_chars = '()[]{}'
    illegal_char_flag = False
    for i in brackets_str:
        if i not in legal_chars:
            illegal_char_flag = True
            break
        
    if illegal_char_flag:
        print('\n[INVALID INPUT]\nPlease only enter a sequence of brackets.\nAccepted characters: ()[]{}\n')
    else:
        print(check_sequence(brackets_str))
