import sys


def validate_input():
    """
        This function checks if the number of arguments is correct
        If there is an argument, it returns the argument as text
        If there is no argument, it asks the user to input a text
        If the text is empty, it returns a space (Carriage return)
        Else it returns the text with a space at the end (Carriage return)

        Returns:
            text: the text to count
    """
    try:
        assert (len(sys.argv)) <= 2, "more than one argument is provided"
    except AssertionError as msg:
        print("AssertionError:", msg)
        exit()

    if (len(sys.argv)) < 2:
        text = None
        try:
            while text is None:
                text = input("What is the text to count?\n")
        except EOFError:
            return ""

        if len(text) == 0:
            return " "
        return text + " "
    return sys.argv[1]


def main():
    """
        Validates the input first
        Increment counters for each type of character
        Prints the results
    """
    input_string = validate_input()
    upper_sum = 0
    lower_sum = 0
    punctuation_sum = 0
    digit_sum = 0
    space_sum = 0

    for char in input_string:
        if char.isupper():
            upper_sum += 1
        elif char.islower():
            lower_sum += 1
        elif char in {'!', '"', '#', '$', '%', '&', "'", '(',
                      ')', '*', '+', ',', '-', '.', '/', ':',
                      ';', '<', '=', '>', '?', '@', '[', '\\',
                      ']', '^', '_', '`', '{', '|', '}', '~'}:
            punctuation_sum += 1
        elif char.isdigit():
            digit_sum += 1
        elif char.isspace():
            space_sum += 1
    print(f"{upper_sum} upper letters")
    print(f"{lower_sum} lower letters")
    print(f"{punctuation_sum} punctuation marks")
    print(f"{space_sum} spaces")
    print(f"{digit_sum} digits")


if __name__ == "__main__":
    main()
