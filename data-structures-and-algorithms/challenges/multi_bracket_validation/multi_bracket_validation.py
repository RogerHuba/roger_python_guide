from data_structures.stacks_and_queues.stacks_and_queues import Stack

def multi_bracket_validation(input: str) -> bool:
    """Check if the passed string has matching pairs of brackets

    Args:
        input (str): String to be checked

    Returns:
        bool: Whether or not the brackets match
    """
    
    br_stack = Stack()
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    
    for char in input:
        # Add opening bracket to the stack
        if char in brackets.values():
            br_stack.push(char)
            
        # Check if closing bracket matches the most recent opening
        elif char in brackets.keys():
            
            try:
                if not brackets[char] == br_stack.pop():
                    return False
            except AttributeError as err:
                print(err)
                return False
    
    return br_stack.is_empty()